class bird:
    def flight(self):
        print("birds can fly")

class sparrow(bird):
    def flight(self):
        print("sparrow can fly")

obj_spr=sparrow()
obj_spr.flight()