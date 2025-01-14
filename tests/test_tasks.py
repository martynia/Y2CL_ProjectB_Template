"""Test Tasks
Laura Hollister
Septemvber 2023
    """
from types import FunctionType, MethodType, NoneType
from inspect import signature
import pytest
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle



class TestTask2():

    def test_module_exists(self, balls_mod):
        pass

    def test_ball_class_exists(self, balls_mod):
        assert "Ball" in vars(balls_mod)

    def test_init_args(self, balls_mod):
        assert {"pos", "vel", "radius", "mass"}.issubset(signature(balls_mod.Ball).parameters.keys())

    def test_construction(self, default_ball, custom_ball):
        pass

    def test_pos_method_exists(self, balls_mod):
        assert isinstance(balls_mod.Ball.pos, (FunctionType, property))

    def test_vel_method_exists(self, balls_mod):
        assert isinstance(balls_mod.Ball.vel, (FunctionType, property))

    def test_set_vel_method_exists(self, balls_mod):
        if isinstance(balls_mod.Ball.vel, property):
            assert isinstance(balls_mod.Ball.vel.fset, FunctionType)
        else:
            assert isinstance(balls_mod.Ball.set_vel, FunctionType)

    def test_mass_method_exists(self, balls_mod):
        assert isinstance(balls_mod.Ball.mass, (FunctionType, property))

    def test_radius_method_exists(self, balls_mod):
        assert isinstance(balls_mod.Ball.radius, (FunctionType, property))

    def test_move_method_exists(self, balls_mod):
        assert isinstance(balls_mod.Ball.move, FunctionType)

    def test_pos_returns_array(self, default_ball, custom_ball):
        default_pos = default_ball.pos
        if isinstance(default_pos, MethodType):
            default_pos = default_pos()
        assert isinstance(default_pos, np.ndarray), "Default constructed Ball.pos does not return a numpy array"

        custom_pos = custom_ball.pos
        if isinstance(custom_pos, MethodType):
            custom_pos = custom_pos()
        assert isinstance(custom_pos, np.ndarray), "Custom constructed Ball.pos does not return a numpy array"

    def test_pos_correct(self, default_ball, custom_ball):
        default_pos = default_ball.pos
        if isinstance(default_pos, MethodType):
            default_pos = default_pos()
        assert np.allclose(default_pos, [0., 0.])

        custom_pos = custom_ball.pos
        if isinstance(custom_pos, MethodType):
            custom_pos = custom_pos()
        assert np.allclose(custom_pos, [1., 2.])

    def test_vel_returns_array(self, default_ball, custom_ball):
        default_vel = default_ball.vel
        if isinstance(default_vel, MethodType):
            default_vel = default_vel()
        assert isinstance(default_vel, np.ndarray), "Default constructed Ball.vel does not return a numpy array"

        custom_vel = custom_ball.vel
        if isinstance(custom_vel, MethodType):
            custom_vel = custom_vel()
        assert isinstance(custom_vel, np.ndarray), "Custom constructed Ball.vel does not return a numpy array"

    def test_vel_correct(self, default_ball, custom_ball):
        default_vel = default_ball.vel
        if isinstance(default_vel, MethodType):
            default_vel = default_vel()
        assert np.allclose(default_vel, [1., 0.])

        custom_vel = custom_ball.vel
        if isinstance(custom_vel, MethodType):
            custom_vel = custom_vel()
        assert np.allclose(custom_vel, [3., 4.])

    def test_set_vel_sets_array(self, default_ball):
        if isinstance(default_ball.vel, MethodType):
            default_ball.set_vel([8, 9])
            assert isinstance(default_ball.vel(), np.ndarray)
        else:
            default_ball.vel = [8, 9]
            assert isinstance(default_ball.vel, np.ndarray)

    def test_set_vel_correct(self, default_ball):
        if isinstance(default_ball.vel, MethodType):
            default_ball.set_vel([8, 9])
            assert np.allclose(default_ball.vel(), [8., 9.])
        else:
            default_ball.vel = [8, 9]
            assert np.allclose(default_ball.vel, [8., 9.])




## advanced check raise exception, check setting as well

#     def test_pos_input(self, balls_mod):
#         with pytest.raises(Exception):
#             ball = balls_mod.Ball(pos=[1, 2, 3])
#         with pytest.raises(Exception):
#             ball = balls_mod.Ball(pos=[1])
#         with pytest.raises(Exception):
#             ball = balls_mod.Ball(pos=4)
## check thats it's a float64 as well

#     def test_vel_input(self, ball_mod):
#         with pytest.raises(Exception):
#             ball = ball_mod.Ball(vel=[1, 2, 3])
#         with pytest.raises(Exception):
#             ball = ball_mod.Ball(vel=[1])
#         with pytest.raises(Exception):
#             ball = ball_mod.Ball(vel=4)

    def test_mass_type(self, default_ball, custom_ball):
        default_mass = default_ball.mass
        if isinstance(default_mass, MethodType):
            default_mass = default_mass()
        assert isinstance(default_mass, float)

        custom_mass = custom_ball.mass
        if isinstance(custom_mass, MethodType):
            custom_mass = custom_mass()
        assert isinstance(custom_mass, float)

    def test_mass_correct(self, default_ball, custom_ball):
        default_mass = default_ball.mass
        if isinstance(default_mass, MethodType):
            default_mass = default_mass()
        assert default_mass == 1.

        custom_mass = custom_ball.mass
        if isinstance(custom_mass, MethodType):
            custom_mass = custom_mass()
        assert custom_mass == 6.

    def test_radius_type(self, default_ball, custom_ball):
        default_radius = default_ball.radius
        if isinstance(default_radius, MethodType):
            default_radius = default_radius()
        assert isinstance(default_radius, float)

        custom_radius = custom_ball.radius
        if isinstance(custom_radius, MethodType):
            custom_radius = custom_radius()
        assert isinstance(custom_radius, float)

    def test_radius_correct(self, default_ball, custom_ball):
        default_radius = default_ball.radius
        if isinstance(default_radius, MethodType):
            default_radius = default_radius()
        assert default_radius == 1.

        custom_radius = custom_ball.radius
        if isinstance(custom_radius, MethodType):
            custom_radius = custom_radius()
        assert custom_radius == 5.

    def test_move_correct(self, default_ball):
        default_ball.move(3)
        pos = default_ball.pos
        if isinstance(pos, MethodType):
            pos = pos()
        assert np.allclose(pos, [3, 0])

    ## advanced
    # def move_correct(self, default_ball):
    #     with pytest.raises(Exception):
    #         default_ball.move(-0.4)

# class TestTask2():
#     def test_default_con_rad_type(self, default_con):
#         assert isinstance(default_con.radius, MethodType)
    
#     def test_default_rad_type(self, default_con):
#         assert isinstance(default_con.radius(), float)
    
#     def test_default_con_rad(self, default_con):
#         assert default_con.radius() == 10.
        
#     def test_repr(self, con_class):
#         assert hasattr(con_class, '__repr__')

class TestTask3():

    def test_patch_exists(self, balls_mod):
        assert isinstance(balls_mod.Ball.patch, (FunctionType, property))

    def test_patch_type(self, default_ball, custom_ball):
        default_patch = default_ball.patch
        if isinstance(default_patch, MethodType):
            default_patch = default_patch()
        assert isinstance(default_patch, Circle)

        custom_patch = custom_ball.patch
        if isinstance(custom_patch, MethodType):
            custom_patch = custom_patch()
        assert isinstance(custom_patch, Circle)

    def test_patch_correct(self, default_ball, custom_ball):
        default_patch = default_ball.patch
        if isinstance(default_patch, MethodType):
            default_patch = default_patch()
        assert np.allclose(default_patch.center, [0., 0])
        assert np.isclose(default_patch.radius, 1.)

        custom_patch = custom_ball.patch
        if isinstance(custom_patch, MethodType):
            custom_patch = custom_patch()
        assert np.allclose(custom_patch.center, [1., 2])
        assert np.isclose(custom_patch.radius, 5.)

    def test_patch_moves(self, default_ball, custom_ball):
        default_ball.move(3)
        default_patch = default_ball.patch
        if isinstance(default_patch, MethodType):
            default_patch = default_patch()
        assert np.allclose(default_patch.center, [3., 0])

        custom_ball.move(4)
        custom_patch = custom_ball.patch
        if isinstance(custom_patch, MethodType):
            custom_patch = custom_patch()
        assert np.allclose(custom_patch.center, [13., 18])


class TestTask4():

    def test_ttc_exists(self, balls_mod):
        assert isinstance(balls_mod.Ball.time_to_collision, FunctionType)

    def test_ttc_return_type(self, balls_mod, default_ball):
        ball1 = balls_mod.Ball(pos=[5, 0], vel=[-1, 0])
        assert isinstance(default_ball.time_to_collision(ball1), float)

        ball2 = balls_mod.Ball(pos=[5, 0], vel=[1, 0])
        assert isinstance(default_ball.time_to_collision(ball2), NoneType)

    def test_ttc_correct(self, balls_mod, default_ball):
        ball1 = balls_mod.Ball(pos=[5, 0], vel=[-1, 0])
        assert np.isclose(default_ball.time_to_collision(ball1), 1.5)

        ball2 = balls_mod.Ball(pos=[5, 1], vel=[-1, 0])
        assert np.isclose(default_ball.time_to_collision(ball2), 1.6339745962155614)

        ball1 = balls_mod.Ball(pos=[1, 1], vel=[1., 0])
        ball2 = balls_mod.Ball(pos=[5., 4.], vel=[0, -0.75])
        assert np.isclose(ball1.time_to_collision(ball2), 2.4)

    def test_ttc_parallel(self, balls_mod):
        ball1 = balls_mod.Ball(pos=[0.1, 0], vel=[0., 2.])
        ball2 = balls_mod.Ball(pos=[0., 1.], vel=[0., 2.])
        assert ball1.time_to_collision(ball2) is None

    def test_ttc_going_away(self, balls_mod):
        ball1 = balls_mod.Ball(pos=[2, 0], vel=[1, 0])
        ball2 = balls_mod.Ball(pos=[-3, 0], vel=[-1, 0])
        assert ball1.time_to_collision(ball2) is None   
               
    # def test_time_to_collision_con(self, ball_mod, default_con):
    #     ball1 = ball_mod.Ball(pos=[1., -1.], vel=[0., 2.])
    #     assert np.isclose(ball1.time_to_collision(default_con), 5.42468273)


class TestTask5():

    def test_collide_exists(self, balls_mod):
        assert isinstance(balls_mod.Ball.collide, FunctionType)

    def test_collide_correct_1D(self, balls_mod, default_ball):
        ball = balls_mod.Ball(pos=[5.,0], vel=[-1, 0.])
        default_ball.collide(ball)

        default_vel = default_ball.vel
        if isinstance(default_vel, MethodType):
            default_vel = default_vel()

        ball_vel = ball.vel
        if isinstance(ball_vel, MethodType):
            ball_vel = ball_vel()

        assert np.allclose(ball_vel, [1,0.])
        assert np.allclose(default_vel, [-1, 0.]) 

    def test_collide_correct_2D(self, balls_mod):
        ball1 = balls_mod.Ball(pos=[1, 1.], vel=[1, 0])
        ball2 = balls_mod.Ball(pos=[5, 4], vel=[0., -0.75])
        ball1.collide(ball2)

        ball1_vel = ball1.vel
        if isinstance(ball1_vel, MethodType):
            ball1_vel = ball1_vel()

        ball2_vel = ball2.vel
        if isinstance(ball2_vel, MethodType):
            ball2_vel = ball2_vel()

        assert np.allclose(ball1_vel, [0, -0.75])
        assert np.allclose(ball2_vel, [1, 0.])

    # def test_collide_functionality_2(self, ball_mod, default_con):
    #     ball1 = ball_mod.Ball(pos=[1., -1.], vel=[0.,2.])
    #     time = ball1.time_to_collision(default_con)
    #     ball1.move(time)
    #     ball1.collide(default_con)

    #     assert np.allclose(ball1.pos() ,[1., 9.84936546])
    #     assert np.allclose(default_con.pos(),[0., 0.])
    #     assert np.allclose(ball1.vel(),[-0.4019739 , -1.95918784])
    #     assert np.allclose(default_con.vel() ,[0., 0.])
        
class TestTask6:

    def test_container_exists(self, balls_mod):
        assert "Container" in vars(balls_mod)

    def test_container_args(self, balls_mod):
        assert {"radius", "mass"}.issubset(signature(balls_mod.Container).parameters.keys())

    def test_container_construction(self, balls_mod, default_container):
        balls_mod.Container(radius=11.)
        balls_mod.Container(radius=12., mass=10000000.)

    def test_ttc_exists(self, container_class):
        assert isinstance(container_class.time_to_collision, FunctionType)

    def test_ttc_return_type(self, default_container, default_ball):
        assert isinstance(default_container.time_to_collision(default_ball), float)

    def test_ttc_correct(self, balls_mod, default_container, default_ball):
        assert np.isclose(default_container.time_to_collision(default_ball), 9.)

        ball = balls_mod.Ball(pos=[3, 5.], vel=[-1, 1.])
        assert np.isclose(default_container.time_to_collision(ball), 3.9497474683058327)

    def test_collide_exists(self, container_class):
        assert isinstance(container_class.collide, FunctionType)

    @pytest.mark.skip
    def test_collide_correct(self):  ##FIXME
        pass  # are we insisting on container not having infinite mass?

    # advanced, test inheritance of these methods

    def test_volume_exists(self, container_class):
        assert isinstance(container_class.volume, (FunctionType, property))

    def test_volume_correct(self, container_class):
        cont1 = container_class()
        vol1 = cont1.volume
        if isinstance(vol1, MethodType):
            vol1 = vol1()
        assert np.isclose(vol1, 100*np.pi)

        cont2 = container_class(radius=5.)
        vol2 = cont2.volume
        if isinstance(vol2, MethodType):
            vol2 = vol2()
        assert np.isclose(vol2, 25*np.pi)

    def test_sa_exists(self, container_class):
        assert isinstance(container_class.surface_area, (FunctionType, property))

    def test_sa_correct(self, container_class):
        cont1 = container_class()
        sa1 = cont1.surface_area
        if isinstance(sa1, MethodType):
            sa1 = sa1()
        assert np.isclose(sa1, 20*np.pi)

        cont2 = container_class(radius=5.)
        sa2 = cont2.surface_area
        if isinstance(sa2, MethodType):
            sa2 = sa2()
        assert np.isclose(sa2, 10*np.pi)    

    def test_dp_tot_exists(self, container_class):
        assert isinstance(container_class.dp_tot, (FunctionType, property))

    @pytest.mark.skip
    def test_dp_tot_correct(self): ##FIXME
        # need to check if assuming infinite mass for container
        pass

class TestTask7:

    def test_simulations_exits(self, simulation_mod):
        pass
