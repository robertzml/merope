from app import biz


def test_week():
    week_save = biz.week_save.equipment_week_save('0110368200103008',
                                                  '2020-09-12')
    print("week save prev {0}, curr {1}".format(week_save.prev_time,
                                                week_save.curr_time))
    assert 1
