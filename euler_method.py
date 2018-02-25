def euler_method(func, x, tmp_step,  dt):
    next_x = dt*func(x, (tmp_step)*dt) + x
    return next_x
