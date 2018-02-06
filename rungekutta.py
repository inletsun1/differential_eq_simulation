def rungekutta(func, x, tmp_step,  dt):
    k1 = func(x, (tmp_step)*dt)
    k2 = func(x + k1*dt/2, tmp_step*dt)
    k3 = func(x + k2*dt/2, tmp_step*dt)
    k4 = func(x + k3*dt, tmp_step*dt)
    next_x = x + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)
    return next_x
