from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 调试地图

    CreateScenaFile(
        FileName            = 'T0001_2 ._SN',
        MapName             = 'map',
        Location            = 'T0001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '',                                     # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 1,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 2,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_1DF",          # 01, 1
        "Function_2_2A3",          # 02, 2
        "Function_3_39B",          # 03, 3
        "Function_4_4BB",          # 04, 4
        "Function_5_622",          # 05, 5
        "Function_6_854",          # 06, 6
        "Function_7_A03",          # 07, 7
        "Function_8_B6E",          # 08, 8
        "Function_9_BFE",          # 09, 9
        "Function_10_EF8",         # 0A, 10
        "Function_11_12EC",        # 0B, 11
        "Function_12_12ED",        # 0C, 12
        "Function_13_138B",        # 0D, 13
        "Function_14_1484",        # 0E, 14
        "Function_15_1569",        # 0F, 15
        "Function_16_1641",        # 10, 16
        "Function_17_164F",        # 11, 17
        "Function_18_1727",        # 12, 18
        "Function_19_17FF",        # 13, 19
        "Function_20_18D7",        # 14, 20
        "Function_21_19AF",        # 15, 21
        "Function_22_1A87",        # 16, 22
        "Function_23_1B5F",        # 17, 23
        "Function_24_1C37",        # 18, 24
        "Function_25_1D0F",        # 19, 25
        "Function_26_1DE7",        # 1A, 26
        "Function_27_1DE8",        # 1B, 27
        "Function_28_1EC0",        # 1C, 28
        "Function_29_1EC1",        # 1D, 29
        "Function_30_1F99",        # 1E, 30
        "Function_31_20EC",        # 1F, 31
        "Function_32_227D",        # 20, 32
        "Function_33_2355",        # 21, 33
        "Function_34_2356",        # 22, 34
        "Function_35_2445",        # 23, 35
        "Function_36_255A",        # 24, 36
        "Function_37_2615",        # 25, 37
        "Function_38_2748",        # 26, 38
        "Function_39_2820",        # 27, 39
        "Function_40_2989",        # 28, 40
        "Function_41_2A61",        # 29, 41
        "Function_42_2B39",        # 2A, 42
        "Function_43_2C36",        # 2B, 43
        "Function_44_2D78",        # 2C, 44
        "Function_45_2E50",        # 2D, 45
        "Function_46_2F9C",        # 2E, 46
        "Function_47_3105",        # 2F, 47
        "Function_48_31DD",        # 30, 48
        "Function_49_32B5",        # 31, 49
        "Function_50_338D",        # 32, 50
        "Function_51_3465",        # 33, 51
        "Function_52_353D",        # 34, 52
        "Function_53_3615",        # 35, 53
        "Function_54_3815",        # 36, 54
        "Function_55_3A09",        # 37, 55
        "Function_56_3AB1",        # 38, 56
        "Function_57_3BC0",        # 39, 57
        "Function_58_3BC1",        # 3A, 58
        "Function_59_3DEE",        # 3B, 59
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D1")

    Menu(
        1,
        10,
        100,
        1,
        (
            "测试\x01",          # 0
            "跳跳猫\x01",        # 1
            "盔甲巨蟹\x01",      # 2
            "跳跳猫3\x01",       # 3
            "人型Boss\x01",      # 4
            "大型Boss\x01",      # 5
            "其他Boss\x01",      # 6
            "自动战斗\x01",      # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_12D"),
        (1, "loc_13D"),
        (2, "loc_14D"),
        (3, "loc_15D"),
        (4, "loc_16D"),
        (5, "loc_174"),
        (6, "loc_17B"),
        (7, "loc_182"),
        (SWITCH_DEFAULT, "loc_189"),
    )


    label("loc_12D")

    Battle(0x466, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18C")

    label("loc_13D")

    Battle(0x7D4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18C")

    label("loc_14D")

    Battle(0x7D5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18C")

    label("loc_15D")

    Battle(0x7D7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18C")

    label("loc_16D")

    Call(2, 53)
    Jump("loc_18C")

    label("loc_174")

    Call(2, 54)
    Jump("loc_18C")

    label("loc_17B")

    Call(2, 55)
    Jump("loc_18C")

    label("loc_182")

    Call(2, 56)
    Jump("loc_18C")

    label("loc_189")

    Jump("loc_18C")

    label("loc_18C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1A3"),
        (SWITCH_DEFAULT, "loc_1CE"),
    )


    label("loc_1A3")

    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    Jump("loc_1CE")

    label("loc_1CE")

    Jump("Function_0_AA")

    label("loc_1D1")

    OP_5F(0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_AA end

    def Function_1_1DF(): pass

    label("Function_1_1DF")


    AnonymousTalk(    #0
        "\x06请选择\x02",
    )


    label("loc_1E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_293")

    Menu(
        1,
        10,
        100,
        1,
        (
            "测试\x01",          # 0
            "洛连特\x01",        # 1
            "柏斯\x01",          # 2
            "卢安\x01",          # 3
            "蔡斯\x01",          # 4
            "格兰赛尔\x01",      # 5
            "其他\x01",          # 6
            "取消\x01",          # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_255"),
        (1, "loc_25C"),
        (2, "loc_263"),
        (3, "loc_26A"),
        (4, "loc_271"),
        (5, "loc_278"),
        (6, "loc_27F"),
        (SWITCH_DEFAULT, "loc_286"),
    )


    label("loc_255")

    Call(2, 2)
    Jump("loc_290")

    label("loc_25C")

    Call(2, 3)
    Jump("loc_290")

    label("loc_263")

    Call(2, 4)
    Jump("loc_290")

    label("loc_26A")

    Call(2, 5)
    Jump("loc_290")

    label("loc_271")

    Call(2, 6)
    Jump("loc_290")

    label("loc_278")

    Call(2, 7)
    Jump("loc_290")

    label("loc_27F")

    Call(2, 8)
    Jump("loc_290")

    label("loc_286")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_290")

    Jump("loc_1E9")

    label("loc_293")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_1DF end

    def Function_2_2A3(): pass

    label("Function_2_2A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38B")

    Menu(
        2,
        10,
        100,
        1,
        (
            "地图１ BTTEST01\x01",      # 0
            "地图２ BTTEST02\x01",      # 1
            "地图３ BTTEST03\x01",      # 2
            "地图４ BTTEST04\x01",      # 3
            "地图５ BTTEST05\x01",      # 4
            "取消\x01",                 # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_32E"),
        (1, "loc_33E"),
        (2, "loc_34E"),
        (3, "loc_35E"),
        (4, "loc_36E"),
        (SWITCH_DEFAULT, "loc_37E"),
    )


    label("loc_32E")

    Battle(0x7DA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_388")

    label("loc_33E")

    Battle(0x7DB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_388")

    label("loc_34E")

    Battle(0x7DC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_388")

    label("loc_35E")

    Battle(0x7DD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_388")

    label("loc_36E")

    Battle(0x7DE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_388")

    label("loc_37E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_388")

    Jump("Function_2_2A3")

    label("loc_38B")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_2A3 end

    def Function_3_39B(): pass

    label("Function_3_39B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AD")

    AnonymousTalk(    #1
        "\x06请选择\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BC0700（里）翡翠之塔战斗地图\x01",                    # 0
            "BC0701（里）翡翠之塔战斗地图（塔顶Boss战）\x01",      # 1
            "BT0400 帕赛尔农场（雾）\x01",                         # 2
            "BC0403 翡翠之塔战斗地图\x01",                         # 3
            "取消\x01",                                            # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_454"),
        (1, "loc_464"),
        (2, "loc_474"),
        (3, "loc_490"),
        (SWITCH_DEFAULT, "loc_4A0"),
    )


    label("loc_454")

    Battle(0x3EE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_4AA")

    label("loc_464")

    Battle(0x456, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_4AA")

    label("loc_474")

    OP_C4(0x0, 0x4)
    Battle(0x799, 0x0, 0x0, 0x0, 0xFF)
    OP_C4(0x1, 0x4)
    Jump("loc_4AA")

    label("loc_490")

    Battle(0x31, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_4AA")

    label("loc_4A0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4AA")

    Jump("Function_3_39B")

    label("loc_4AD")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_39B end

    def Function_4_4BB(): pass

    label("Function_4_4BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_614")

    AnonymousTalk(    #2
        "\x06请选择\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BC1601　古龙的住处战斗地图\x01",                        # 0
            "BC1603　古龙的住处战斗地图（Boss战\x01",                # 1
            "BC1700　（里）琥珀之塔战斗地图\x01",                    # 2
            "BC1701　（里）琥珀之塔战斗地图（塔顶boss战）\x01",      # 3
            "BC1203　（表）琥珀之塔战斗地图（塔顶boss战）\x01",      # 4
            "取消\x01",                                              # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5B7"),
        (1, "loc_5C7"),
        (2, "loc_5D7"),
        (3, "loc_5E7"),
        (4, "loc_5F7"),
        (SWITCH_DEFAULT, "loc_607"),
    )


    label("loc_5B7")

    Battle(0x3C7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_611")

    label("loc_5C7")

    Battle(0x44F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_611")

    label("loc_5D7")

    Battle(0x3F4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_611")

    label("loc_5E7")

    Battle(0x457, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_611")

    label("loc_5F7")

    Battle(0x93, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_611")

    label("loc_607")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_611")

    Jump("Function_4_4BB")

    label("loc_614")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_4BB end

    def Function_5_622(): pass

    label("Function_5_622")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_846")

    AnonymousTalk(    #3
        "\x06请选择\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BC2300　（里）绀碧之塔战斗地图\x01",                    # 0
            "BC2301　（里）绀碧之塔战斗地图（塔顶boss战）\x01",      # 1
            "BC2400　王立学院旧校舍地下\x01",                        # 2
            "BC2401　王立学院旧校舍地下Boss\x01",                    # 3
            "BC2500　王立学院校园\x01",                              # 4
            "BC2510　王立学院走廊\x01",                              # 5
            "BC2511　王立学院男子宿舍\x01",                          # 6
            "BC2512　王立学院女子宿舍\x01",                          # 7
            "BT2611　王立学院旧校舍内部（白天）\x01",                # 8
            "BC2102　绀碧之塔战斗地图\x01",                          # 9
            "取消\x01",                                              # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_799"),
        (1, "loc_7A9"),
        (2, "loc_7B9"),
        (3, "loc_7C9"),
        (4, "loc_7D9"),
        (5, "loc_7E9"),
        (6, "loc_7F9"),
        (7, "loc_809"),
        (8, "loc_819"),
        (9, "loc_829"),
        (SWITCH_DEFAULT, "loc_839"),
    )


    label("loc_799")

    Battle(0x407, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_843")

    label("loc_7A9")

    Battle(0x454, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_843")

    label("loc_7B9")

    Battle(0x398, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_843")

    label("loc_7C9")

    Battle(0x44C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_843")

    label("loc_7D9")

    Battle(0xF3C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_843")

    label("loc_7E9")

    Battle(0x79C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_843")

    label("loc_7F9")

    Battle(0x79D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_843")

    label("loc_809")

    Battle(0x79F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_843")

    label("loc_819")

    Battle(0xF40, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_843")

    label("loc_829")

    Battle(0x1BD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_843")

    label("loc_839")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_843")

    Jump("Function_5_622")

    label("loc_846")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_622 end

    def Function_6_854(): pass

    label("Function_6_854")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F5")

    AnonymousTalk(    #4
        "\x06请选择\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BC3600　（里）红莲之塔战斗地图\x01",                    # 0
            "BC3601　（里）红莲之塔战斗地图（塔顶boss战）\x01",      # 1
            "BC3400　温泉源流战斗地图\x01",                          # 2
            "BC3401　温泉源流战斗地图（Boss战）\x01",                # 3
            "BT0600　亚宁堡城墙（格鲁纳门）\x01",                    # 4
            "BC3101　雷斯顿要塞中庭\x01",                            # 5
            "BC3503　红莲之塔战斗地图\x01",                          # 6
            "取消\x01",                                              # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_978"),
        (1, "loc_988"),
        (2, "loc_998"),
        (3, "loc_9A8"),
        (4, "loc_9B8"),
        (5, "loc_9C8"),
        (6, "loc_9D8"),
        (SWITCH_DEFAULT, "loc_9E8"),
    )


    label("loc_978")

    Battle(0x412, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_9F2")

    label("loc_988")

    Battle(0x455, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_9F2")

    label("loc_998")

    Battle(0x3B0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_9F2")

    label("loc_9A8")

    Battle(0x3AF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_9F2")

    label("loc_9B8")

    Battle(0x45A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_9F2")

    label("loc_9C8")

    Battle(0xC80, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_9F2")

    label("loc_9D8")

    Battle(0x1F5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_9F2")

    label("loc_9E8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9F2")

    Jump("Function_6_854")

    label("loc_9F5")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_854 end

    def Function_7_A03(): pass

    label("Function_7_A03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B60")

    AnonymousTalk(    #5
        "\x06请选择\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "BT4403　王都格兰赛尔外部（码头）战斗地图（Boss）\x01",        # 0
            "BT4404　王都格兰赛尔外部（码头）战斗地图（小怪）\x01",        # 1
            "BT4405　王都格兰赛尔外部（码头）战斗地图（仓库内）\x01",      # 2
            "BT4100　王都街区\x01",                                        # 3
            "BT4200　城门前（桥）\x01",                                    # 4
            "取消\x01",                                                    # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B03"),
        (1, "loc_B13"),
        (2, "loc_B23"),
        (3, "loc_B33"),
        (4, "loc_B43"),
        (SWITCH_DEFAULT, "loc_B53"),
    )


    label("loc_B03")

    Battle(0x45E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_B5D")

    label("loc_B13")

    Battle(0x45D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_B5D")

    label("loc_B23")

    Battle(0x45C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_B5D")

    label("loc_B33")

    Battle(0x79E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_B5D")

    label("loc_B43")

    Battle(0x550, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_B5D")

    label("loc_B53")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B5D")

    Jump("Function_7_A03")

    label("loc_B60")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_A03 end

    def Function_8_B6E(): pass

    label("Function_8_B6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF0")

    AnonymousTalk(    #6
        "\x06请选择\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "卢·洛克尔，研究所，古罗力亚斯\x01",      # 0
            "中枢塔，辉之环\x01",                      # 1
            "取消\x01",                                # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BD5"),
        (1, "loc_BDC"),
        (SWITCH_DEFAULT, "loc_BE3"),
    )


    label("loc_BD5")

    Call(2, 9)
    Jump("loc_BED")

    label("loc_BDC")

    Call(2, 10)
    Jump("loc_BED")

    label("loc_BE3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BED")

    Jump("Function_8_B6E")

    label("loc_BF0")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_B6E end

    def Function_9_BFE(): pass

    label("Function_9_BFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EEA")

    AnonymousTalk(    #7
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        80,
        1,
        (
            "BT5110　卢·洛克尔宿舍\x01",                                  # 0
            "BC5500　卢·洛克尔训练场战斗地图（训练场１）\x01",            # 1
            "BC5501　卢·洛克尔训练场战斗地图（训练场１Boss战）\x01",      # 2
            "BC5502　卢·洛克尔训练场战斗地图（训练场２）\x01",            # 3
            "BC5503　卢·洛克尔训练场战斗地图（训练场２Boss战）\x01",      # 4
            "BC5504　卢·洛克尔训练场战斗地图（训练场３）\x01",            # 5
            "BC5505　卢·洛克尔训练场战斗地图（训练场３Boss战）\x01",      # 6
            "BC5610　研究所·房间战斗地图\x01",                            # 7
            "BC5611　研究所·通路战斗地图\x01",                            # 8
            "BC5400　古罗力亚斯通路\x01",                                  # 9
            "BC5408　古罗力亚斯甲板\x01",                                  # 10
            "BC5406　古罗力亚斯机库（Boss）\x01",                          # 11
            "取消\x01",                                                    # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E1D"),
        (1, "loc_E2D"),
        (2, "loc_E3D"),
        (3, "loc_E4D"),
        (4, "loc_E5D"),
        (5, "loc_E6D"),
        (6, "loc_E7D"),
        (7, "loc_E8D"),
        (8, "loc_E9D"),
        (9, "loc_EAD"),
        (10, "loc_EBD"),
        (11, "loc_ECD"),
        (SWITCH_DEFAULT, "loc_EDD"),
    )


    label("loc_E1D")

    Battle(0x397, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_EE7")

    label("loc_E2D")

    Battle(0x387, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_EE7")

    label("loc_E3D")

    Battle(0x393, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_EE7")

    label("loc_E4D")

    Battle(0x389, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_EE7")

    label("loc_E5D")

    Battle(0x394, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_EE7")

    label("loc_E6D")

    Battle(0x38D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_EE7")

    label("loc_E7D")

    Battle(0x395, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_EE7")

    label("loc_E8D")

    Battle(0x41A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_EE7")

    label("loc_E9D")

    Battle(0x41C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_EE7")

    label("loc_EAD")

    Battle(0x427, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_EE7")

    label("loc_EBD")

    Battle(0x428, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_EE7")

    label("loc_ECD")

    Battle(0x429, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_EE7")

    label("loc_EDD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EE7")

    Jump("Function_9_BFE")

    label("loc_EEA")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_9_BFE end

    def Function_10_EF8(): pass

    label("Function_10_EF8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12DE")

    AnonymousTalk(    #8
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        80,
        1,
        (
            "BC5800　辉之环居住区外侧（事件）\x01",                              # 0
            "BC5702　辉之环工场区古罗力亚斯前（事件）\x01",                      # 1
            "BC5200　辉之环地下道战斗地图 公园区～居住区\x01",                   # 2
            "BC5201　辉之环地下道战斗地图 居住区～工场区\x01",                   # 3
            "BC5202　辉之环地下道战斗地图 工场区～中枢塔\x01",                   # 4
            "BC5203　辉之环地下道战斗地图 中枢塔～公园区\x01",                   # 5
            "BC5300　中枢塔内部战斗地图\x01",                                    # 6
            "BC5301　中枢塔内部中Boss战斗地图１\x01",                            # 7
            "BC5302　中枢塔内部中Boss战斗地图２\x01",                            # 8
            "BC5303　中枢塔内部顶上战斗地图 莱维\x01",                           # 9
            "BC5304　中枢塔内部高速升降梯战斗地图 德尔基昂\x01",                 # 10
            "BC5305　中枢塔内部Boss战斗地图１（通常空间）怀斯曼\x01",            # 11
            "BC5306　中枢塔内部Boss战斗地图２（异空间）本Boss第二形态\x01",      # 12
            "BC5100　中枢塔前通路\x01",                                          # 13
            "BC5801　辉之环居住区外侧\x01",                                      # 14
            "BC5700　辉之环工场区古罗力亚斯前\x01",                              # 15
            "取消\x01",                                                          # 16
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11D1"),
        (1, "loc_11E1"),
        (2, "loc_11F1"),
        (3, "loc_1201"),
        (4, "loc_1211"),
        (5, "loc_1221"),
        (6, "loc_1231"),
        (7, "loc_1241"),
        (8, "loc_1251"),
        (9, "loc_1261"),
        (10, "loc_1271"),
        (11, "loc_1281"),
        (12, "loc_1291"),
        (13, "loc_12A1"),
        (14, "loc_12B1"),
        (15, "loc_12C1"),
        (SWITCH_DEFAULT, "loc_12D1"),
    )


    label("loc_11D1")

    Battle(0x50B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12DB")

    label("loc_11E1")

    Battle(0x518, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12DB")

    label("loc_11F1")

    Battle(0x43A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12DB")

    label("loc_1201")

    Battle(0x440, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12DB")

    label("loc_1211")

    Battle(0x449, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12DB")

    label("loc_1221")

    Battle(0x43D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12DB")

    label("loc_1231")

    Battle(0x508, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12DB")

    label("loc_1241")

    Battle(0x509, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12DB")

    label("loc_1251")

    Battle(0x50A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12DB")

    label("loc_1261")

    Battle(0x458, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12DB")

    label("loc_1271")

    Battle(0x450, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12DB")

    label("loc_1281")

    Battle(0x459, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12DB")

    label("loc_1291")

    Battle(0x452, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12DB")

    label("loc_12A1")

    Battle(0x525, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12DB")

    label("loc_12B1")

    Battle(0x50E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12DB")

    label("loc_12C1")

    Battle(0x514, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12DB")

    label("loc_12D1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12DB")

    Jump("Function_10_EF8")

    label("loc_12DE")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_EF8 end

    def Function_11_12EC(): pass

    label("Function_11_12EC")

    Return()

    # Function_11_12EC end

    def Function_12_12ED(): pass

    label("Function_12_12ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_137D")

    AnonymousTalk(    #9
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0100_01\x01",      # 0
            "C0100_02\x01",      # 1
            "C0100_03\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1340"),
        (1, "loc_1350"),
        (2, "loc_1360"),
        (SWITCH_DEFAULT, "loc_1370"),
    )


    label("loc_1340")

    Battle(0x56, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_137A")

    label("loc_1350")

    Battle(0x57, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_137A")

    label("loc_1360")

    Battle(0x58, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_137A")

    label("loc_1370")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_137A")

    Jump("Function_12_12ED")

    label("loc_137D")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_12ED end

    def Function_13_138B(): pass

    label("Function_13_138B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1476")

    AnonymousTalk(    #10
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0100_01\x01",          # 0
            "C0100_02\x01",          # 1
            "C0100_03\x01",          # 2
            "C0100_20\x01",          # 3
            "C0100_11\x01",          # 4
            "BTL_EVENT001\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1409"),
        (1, "loc_1419"),
        (2, "loc_1429"),
        (3, "loc_1439"),
        (4, "loc_1449"),
        (5, "loc_1459"),
        (SWITCH_DEFAULT, "loc_1469"),
    )


    label("loc_1409")

    Battle(0x3E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1473")

    label("loc_1419")

    Battle(0x3F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1473")

    label("loc_1429")

    Battle(0x40, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1473")

    label("loc_1439")

    Battle(0x51, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1473")

    label("loc_1449")

    Battle(0x48, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1473")

    label("loc_1459")

    Battle(0x76D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1473")

    label("loc_1469")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1473")

    Jump("Function_13_138B")

    label("loc_1476")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_138B end

    def Function_14_1484(): pass

    label("Function_14_1484")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_155B")

    AnonymousTalk(    #11
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0400_01\x01",          # 0
            "C0400_02\x01",          # 1
            "C0400_07\x01",          # 2
            "C0400_13\x01",          # 3
            "C0400_10\x01",          # 4
            "BTL_EVENT002\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_14FE"),
        (1, "loc_150E"),
        (2, "loc_151E"),
        (3, "loc_152E"),
        (4, "loc_153E"),
        (SWITCH_DEFAULT, "loc_154E"),
    )


    label("loc_14FE")

    Battle(0x31, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1558")

    label("loc_150E")

    Battle(0x32, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1558")

    label("loc_151E")

    Battle(0x37, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1558")

    label("loc_152E")

    Battle(0x3D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1558")

    label("loc_153E")

    Battle(0x3A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1558")

    label("loc_154E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1558")

    Jump("Function_14_1484")

    label("loc_155B")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_1484 end

    def Function_15_1569(): pass

    label("Function_15_1569")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1633")

    AnonymousTalk(    #12
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R0100_02\x01",      # 0
            "R0100_05\x01",      # 1
            "R0100_09\x01",      # 2
            "R0100_11\x01",      # 3
            "R0100_14\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_15D6"),
        (1, "loc_15E6"),
        (2, "loc_15F6"),
        (3, "loc_1606"),
        (4, "loc_1616"),
        (SWITCH_DEFAULT, "loc_1626"),
    )


    label("loc_15D6")

    Battle(0x15, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1630")

    label("loc_15E6")

    Battle(0x18, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1630")

    label("loc_15F6")

    Battle(0x1C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1630")

    label("loc_1606")

    Battle(0x1E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1630")

    label("loc_1616")

    Battle(0x21, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1630")

    label("loc_1626")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1630")

    Jump("Function_15_1569")

    label("loc_1633")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_15_1569 end

    def Function_16_1641(): pass

    label("Function_16_1641")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_16_1641 end

    def Function_17_164F(): pass

    label("Function_17_164F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1719")

    AnonymousTalk(    #13
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R0300_02\x01",      # 0
            "R0300_06\x01",      # 1
            "R0300_09\x01",      # 2
            "R0300_12\x01",      # 3
            "R0300_17\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16BC"),
        (1, "loc_16CC"),
        (2, "loc_16DC"),
        (3, "loc_16EC"),
        (4, "loc_16FC"),
        (SWITCH_DEFAULT, "loc_170C"),
    )


    label("loc_16BC")

    Battle(0x65, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1716")

    label("loc_16CC")

    Battle(0x69, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1716")

    label("loc_16DC")

    Battle(0x6C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1716")

    label("loc_16EC")

    Battle(0x6F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1716")

    label("loc_16FC")

    Battle(0x74, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1716")

    label("loc_170C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1716")

    Jump("Function_17_164F")

    label("loc_1719")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_164F end

    def Function_18_1727(): pass

    label("Function_18_1727")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17F1")

    AnonymousTalk(    #14
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0500_01\x01",      # 0
            "C0500_02\x01",      # 1
            "C0500_03\x01",      # 2
            "C0500_04\x01",      # 3
            "C0500_07\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1794"),
        (1, "loc_17A4"),
        (2, "loc_17B4"),
        (3, "loc_17C4"),
        (4, "loc_17D4"),
        (SWITCH_DEFAULT, "loc_17E4"),
    )


    label("loc_1794")

    Battle(0x2A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_17EE")

    label("loc_17A4")

    Battle(0x2B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_17EE")

    label("loc_17B4")

    Battle(0x2C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_17EE")

    label("loc_17C4")

    Battle(0x2D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_17EE")

    label("loc_17D4")

    Battle(0x30, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_17EE")

    label("loc_17E4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17EE")

    Jump("Function_18_1727")

    label("loc_17F1")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_18_1727 end

    def Function_19_17FF(): pass

    label("Function_19_17FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18C9")

    AnonymousTalk(    #15
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1300_01\x01",      # 0
            "C1300_02\x01",      # 1
            "C1300_03\x01",      # 2
            "C1300_04\x01",      # 3
            "C1300_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_186C"),
        (1, "loc_187C"),
        (2, "loc_188C"),
        (3, "loc_189C"),
        (4, "loc_18AC"),
        (SWITCH_DEFAULT, "loc_18BC"),
    )


    label("loc_186C")

    Battle(0xA1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18C6")

    label("loc_187C")

    Battle(0xA2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18C6")

    label("loc_188C")

    Battle(0xA3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18C6")

    label("loc_189C")

    Battle(0xA4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18C6")

    label("loc_18AC")

    Battle(0xA5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18C6")

    label("loc_18BC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18C6")

    Jump("Function_19_17FF")

    label("loc_18C9")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_19_17FF end

    def Function_20_18D7(): pass

    label("Function_20_18D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19A1")

    AnonymousTalk(    #16
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1400_01\x01",      # 0
            "C1400_02\x01",      # 1
            "C1400_03\x01",      # 2
            "C1400_04\x01",      # 3
            "C1400_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1944"),
        (1, "loc_1954"),
        (2, "loc_1964"),
        (3, "loc_1974"),
        (4, "loc_1984"),
        (SWITCH_DEFAULT, "loc_1994"),
    )


    label("loc_1944")

    Battle(0xB5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_199E")

    label("loc_1954")

    Battle(0xB6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_199E")

    label("loc_1964")

    Battle(0xB7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_199E")

    label("loc_1974")

    Battle(0xB8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_199E")

    label("loc_1984")

    Battle(0xB9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_199E")

    label("loc_1994")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_199E")

    Jump("Function_20_18D7")

    label("loc_19A1")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_20_18D7 end

    def Function_21_19AF(): pass

    label("Function_21_19AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A79")

    AnonymousTalk(    #17
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1500_01\x01",      # 0
            "C1500_02\x01",      # 1
            "C1500_03\x01",      # 2
            "C1500_04\x01",      # 3
            "C1500_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A1C"),
        (1, "loc_1A2C"),
        (2, "loc_1A3C"),
        (3, "loc_1A4C"),
        (4, "loc_1A5C"),
        (SWITCH_DEFAULT, "loc_1A6C"),
    )


    label("loc_1A1C")

    Battle(0xC9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1A76")

    label("loc_1A2C")

    Battle(0xCA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1A76")

    label("loc_1A3C")

    Battle(0xCB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1A76")

    label("loc_1A4C")

    Battle(0xCC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1A76")

    label("loc_1A5C")

    Battle(0xCD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1A76")

    label("loc_1A6C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A76")

    Jump("Function_21_19AF")

    label("loc_1A79")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_21_19AF end

    def Function_22_1A87(): pass

    label("Function_22_1A87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B51")

    AnonymousTalk(    #18
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1100_01\x01",      # 0
            "R1100_02\x01",      # 1
            "R1100_20\x01",      # 2
            "R1100_04\x01",      # 3
            "R1100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1AF4"),
        (1, "loc_1B04"),
        (2, "loc_1B14"),
        (3, "loc_1B24"),
        (4, "loc_1B34"),
        (SWITCH_DEFAULT, "loc_1B44"),
    )


    label("loc_1AF4")

    Battle(0xDD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1B4E")

    label("loc_1B04")

    Battle(0xDE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1B4E")

    label("loc_1B14")

    Battle(0xF0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1B4E")

    label("loc_1B24")

    Battle(0xE0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1B4E")

    label("loc_1B34")

    Battle(0xE1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1B4E")

    label("loc_1B44")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B4E")

    Jump("Function_22_1A87")

    label("loc_1B51")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_22_1A87 end

    def Function_23_1B5F(): pass

    label("Function_23_1B5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C29")

    AnonymousTalk(    #19
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1200_01\x01",      # 0
            "R1200_02\x01",      # 1
            "R1200_03\x01",      # 2
            "R1200_04\x01",      # 3
            "R1200_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BCC"),
        (1, "loc_1BDC"),
        (2, "loc_1BEC"),
        (3, "loc_1BFC"),
        (4, "loc_1C0C"),
        (SWITCH_DEFAULT, "loc_1C1C"),
    )


    label("loc_1BCC")

    Battle(0xF1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C26")

    label("loc_1BDC")

    Battle(0xF2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C26")

    label("loc_1BEC")

    Battle(0xF3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C26")

    label("loc_1BFC")

    Battle(0xF4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C26")

    label("loc_1C0C")

    Battle(0xF5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C26")

    label("loc_1C1C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C26")

    Jump("Function_23_1B5F")

    label("loc_1C29")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_23_1B5F end

    def Function_24_1C37(): pass

    label("Function_24_1C37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D01")

    AnonymousTalk(    #20
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1300_01\x01",      # 0
            "R1300_02\x01",      # 1
            "R1300_03\x01",      # 2
            "R1300_04\x01",      # 3
            "R1300_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1CA4"),
        (1, "loc_1CB4"),
        (2, "loc_1CC4"),
        (3, "loc_1CD4"),
        (4, "loc_1CE4"),
        (SWITCH_DEFAULT, "loc_1CF4"),
    )


    label("loc_1CA4")

    Battle(0x105, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1CFE")

    label("loc_1CB4")

    Battle(0x106, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1CFE")

    label("loc_1CC4")

    Battle(0x107, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1CFE")

    label("loc_1CD4")

    Battle(0x108, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1CFE")

    label("loc_1CE4")

    Battle(0x109, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1CFE")

    label("loc_1CF4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CFE")

    Jump("Function_24_1C37")

    label("loc_1D01")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_24_1C37 end

    def Function_25_1D0F(): pass

    label("Function_25_1D0F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DD9")

    AnonymousTalk(    #21
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1400_01\x01",      # 0
            "R1400_02\x01",      # 1
            "R1400_03\x01",      # 2
            "R1400_04\x01",      # 3
            "R1400_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D7C"),
        (1, "loc_1D8C"),
        (2, "loc_1D9C"),
        (3, "loc_1DAC"),
        (4, "loc_1DBC"),
        (SWITCH_DEFAULT, "loc_1DCC"),
    )


    label("loc_1D7C")

    Battle(0x119, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DD6")

    label("loc_1D8C")

    Battle(0x11A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DD6")

    label("loc_1D9C")

    Battle(0x11B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DD6")

    label("loc_1DAC")

    Battle(0x11C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DD6")

    label("loc_1DBC")

    Battle(0x11D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DD6")

    label("loc_1DCC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DD6")

    Jump("Function_25_1D0F")

    label("loc_1DD9")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_25_1D0F end

    def Function_26_1DE7(): pass

    label("Function_26_1DE7")

    Return()

    # Function_26_1DE7 end

    def Function_27_1DE8(): pass

    label("Function_27_1DE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EB2")

    AnonymousTalk(    #22
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1100_01\x01",      # 0
            "C1100_02\x01",      # 1
            "C1100_03\x01",      # 2
            "C1100_04\x01",      # 3
            "C1100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E55"),
        (1, "loc_1E65"),
        (2, "loc_1E75"),
        (3, "loc_1E85"),
        (4, "loc_1E95"),
        (SWITCH_DEFAULT, "loc_1EA5"),
    )


    label("loc_1E55")

    Battle(0x141, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1EAF")

    label("loc_1E65")

    Battle(0x142, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1EAF")

    label("loc_1E75")

    Battle(0x143, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1EAF")

    label("loc_1E85")

    Battle(0x144, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1EAF")

    label("loc_1E95")

    Battle(0x145, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1EAF")

    label("loc_1EA5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EAF")

    Jump("Function_27_1DE8")

    label("loc_1EB2")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_27_1DE8 end

    def Function_28_1EC0(): pass

    label("Function_28_1EC0")

    Return()

    # Function_28_1EC0 end

    def Function_29_1EC1(): pass

    label("Function_29_1EC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F8B")

    AnonymousTalk(    #23
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2100_01\x01",      # 0
            "R2100_02\x01",      # 1
            "R2100_03\x01",      # 2
            "R2100_04\x01",      # 3
            "R2100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F2E"),
        (1, "loc_1F3E"),
        (2, "loc_1F4E"),
        (3, "loc_1F5E"),
        (4, "loc_1F6E"),
        (SWITCH_DEFAULT, "loc_1F7E"),
    )


    label("loc_1F2E")

    Battle(0x169, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F88")

    label("loc_1F3E")

    Battle(0x16A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F88")

    label("loc_1F4E")

    Battle(0x16B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F88")

    label("loc_1F5E")

    Battle(0x16C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F88")

    label("loc_1F6E")

    Battle(0x16D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F88")

    label("loc_1F7E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F88")

    Jump("Function_29_1EC1")

    label("loc_1F8B")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_29_1EC1 end

    def Function_30_1F99(): pass

    label("Function_30_1F99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20DE")

    AnonymousTalk(    #24
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2200_01主场景\x01",              # 0
            "R2200_02\x01",                    # 1
            "R2201_01沙滩\x01",                # 2
            "R2201_02\x01",                    # 3
            "R2202_01主场景（黄昏）\x01",      # 4
            "R2202_02\x01",                    # 5
            "R2203_01沙滩（黄昏）\x01",        # 6
            "R2203_02\x01",                    # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2051"),
        (1, "loc_2061"),
        (2, "loc_2071"),
        (3, "loc_2081"),
        (4, "loc_2091"),
        (5, "loc_20A1"),
        (6, "loc_20B1"),
        (7, "loc_20C1"),
        (SWITCH_DEFAULT, "loc_20D1"),
    )


    label("loc_2051")

    Battle(0x17D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20DB")

    label("loc_2061")

    Battle(0x17E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20DB")

    label("loc_2071")

    Battle(0x187, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20DB")

    label("loc_2081")

    Battle(0x188, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20DB")

    label("loc_2091")

    Battle(0x321, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20DB")

    label("loc_20A1")

    Battle(0x322, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20DB")

    label("loc_20B1")

    Battle(0x32B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20DB")

    label("loc_20C1")

    Battle(0x32C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20DB")

    label("loc_20D1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20DB")

    Jump("Function_30_1F99")

    label("loc_20DE")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_30_1F99 end

    def Function_31_20EC(): pass

    label("Function_31_20EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_226F")

    AnonymousTalk(    #25
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2300_01\x01",              # 0
            "R2300_02\x01",              # 1
            "R2300_03\x01",              # 2
            "R2300_04\x01",              # 3
            "R2300_05\x01",              # 4
            "R2301_01（黄昏）\x01",      # 5
            "R2301_02（黄昏）\x01",      # 6
            "R2301_03（黄昏）\x01",      # 7
            "R2301_04（黄昏）\x01",      # 8
            "R2301_05（黄昏）\x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_21C2"),
        (1, "loc_21D2"),
        (2, "loc_21E2"),
        (3, "loc_21F2"),
        (4, "loc_2202"),
        (5, "loc_2212"),
        (6, "loc_2222"),
        (7, "loc_2232"),
        (8, "loc_2242"),
        (9, "loc_2252"),
        (SWITCH_DEFAULT, "loc_2262"),
    )


    label("loc_21C2")

    Battle(0x191, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_226C")

    label("loc_21D2")

    Battle(0x192, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_226C")

    label("loc_21E2")

    Battle(0x193, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_226C")

    label("loc_21F2")

    Battle(0x194, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_226C")

    label("loc_2202")

    Battle(0x195, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_226C")

    label("loc_2212")

    Battle(0x335, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_226C")

    label("loc_2222")

    Battle(0x336, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_226C")

    label("loc_2232")

    Battle(0x337, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_226C")

    label("loc_2242")

    Battle(0x338, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_226C")

    label("loc_2252")

    Battle(0x339, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_226C")

    label("loc_2262")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_226C")

    Jump("Function_31_20EC")

    label("loc_226F")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_31_20EC end

    def Function_32_227D(): pass

    label("Function_32_227D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2347")

    AnonymousTalk(    #26
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2400_01\x01",      # 0
            "R2400_02\x01",      # 1
            "R2400_03\x01",      # 2
            "R2400_04\x01",      # 3
            "R2400_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_22EA"),
        (1, "loc_22FA"),
        (2, "loc_230A"),
        (3, "loc_231A"),
        (4, "loc_232A"),
        (SWITCH_DEFAULT, "loc_233A"),
    )


    label("loc_22EA")

    Battle(0x1A5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2344")

    label("loc_22FA")

    Battle(0x1A6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2344")

    label("loc_230A")

    Battle(0x1A7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2344")

    label("loc_231A")

    Battle(0x1A8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2344")

    label("loc_232A")

    Battle(0x1A9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2344")

    label("loc_233A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2344")

    Jump("Function_32_227D")

    label("loc_2347")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_32_227D end

    def Function_33_2355(): pass

    label("Function_33_2355")

    Return()

    # Function_33_2355 end

    def Function_34_2356(): pass

    label("Function_34_2356")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2437")

    AnonymousTalk(    #27
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "BTL_EVENT011（迪恩）\x01",          # 0
            "BTL_EVENT012（雷斯）\x01",          # 1
            "BTL_EVENT013（洛克）\x01",          # 2
            "BTL_EVENT014（黑衣男子）\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23EA"),
        (1, "loc_23FA"),
        (2, "loc_240A"),
        (3, "loc_241A"),
        (SWITCH_DEFAULT, "loc_242A"),
    )


    label("loc_23EA")

    Battle(0x777, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2434")

    label("loc_23FA")

    Battle(0x778, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2434")

    label("loc_240A")

    Battle(0x779, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2434")

    label("loc_241A")

    Battle(0x77A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2434")

    label("loc_242A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2434")

    Jump("Function_34_2356")

    label("loc_2437")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_34_2356 end

    def Function_35_2445(): pass

    label("Function_35_2445")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_254C")

    AnonymousTalk(    #28
        "\x06请选择\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "卡鲁迪亚隧道\x01",          # 0
            "卡鲁迪亚钟乳洞\x01",        # 1
            "红莲之塔\x01",              # 2
            "托兰特平原道\x01",          # 3
            "利塔街道\x01",              # 4
            "佐达特军用道\x01",          # 5
            "雷斯顿水上要塞\x01",        # 6
            "红莲之塔（事件）\x01",      # 7
            "取消\x01",                  # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24FE"),
        (1, "loc_2505"),
        (2, "loc_250C"),
        (3, "loc_2513"),
        (4, "loc_251A"),
        (5, "loc_2521"),
        (6, "loc_2528"),
        (7, "loc_252F"),
        (SWITCH_DEFAULT, "loc_253F"),
    )


    label("loc_24FE")

    Call(2, 36)
    Jump("loc_2549")

    label("loc_2505")

    Call(2, 37)
    Jump("loc_2549")

    label("loc_250C")

    Call(2, 38)
    Jump("loc_2549")

    label("loc_2513")

    Call(2, 39)
    Jump("loc_2549")

    label("loc_251A")

    Call(2, 40)
    Jump("loc_2549")

    label("loc_2521")

    Call(2, 41)
    Jump("loc_2549")

    label("loc_2528")

    Call(2, 42)
    Jump("loc_2549")

    label("loc_252F")

    Battle(0x788, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2549")

    label("loc_253F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2549")

    Jump("Function_35_2445")

    label("loc_254C")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_35_2445 end

    def Function_36_255A(): pass

    label("Function_36_255A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2607")

    AnonymousTalk(    #29
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3400_01\x01",      # 0
            "R3400_02\x01",      # 1
            "R3400_03\x01",      # 2
            "R3400_04\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_25BA"),
        (1, "loc_25CA"),
        (2, "loc_25DA"),
        (3, "loc_25EA"),
        (SWITCH_DEFAULT, "loc_25FA"),
    )


    label("loc_25BA")

    Battle(0x1CD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2604")

    label("loc_25CA")

    Battle(0x1CE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2604")

    label("loc_25DA")

    Battle(0x1CF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2604")

    label("loc_25EA")

    Battle(0x1D0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2604")

    label("loc_25FA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2604")

    Jump("Function_36_255A")

    label("loc_2607")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_36_255A end

    def Function_37_2615(): pass

    label("Function_37_2615")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_273A")

    AnonymousTalk(    #30
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C3300_01\x01",          # 0
            "C3300_02\x01",          # 1
            "C3300_03\x01",          # 2
            "C3300_04\x01",          # 3
            "C3300_05\x01",          # 4
            "C3300_06\x01",          # 5
            "C3300_07\x01",          # 6
            "BTL_EVENT020\x01",      # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_26AD"),
        (1, "loc_26BD"),
        (2, "loc_26CD"),
        (3, "loc_26DD"),
        (4, "loc_26ED"),
        (5, "loc_26FD"),
        (6, "loc_270D"),
        (7, "loc_271D"),
        (SWITCH_DEFAULT, "loc_272D"),
    )


    label("loc_26AD")

    Battle(0x1E1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2737")

    label("loc_26BD")

    Battle(0x1E2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2737")

    label("loc_26CD")

    Battle(0x1E3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2737")

    label("loc_26DD")

    Battle(0x1E4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2737")

    label("loc_26ED")

    Battle(0x1E5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2737")

    label("loc_26FD")

    Battle(0x1E6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2737")

    label("loc_270D")

    Battle(0x1E7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2737")

    label("loc_271D")

    Battle(0x780, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2737")

    label("loc_272D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2737")

    Jump("Function_37_2615")

    label("loc_273A")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_37_2615 end

    def Function_38_2748(): pass

    label("Function_38_2748")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2812")

    AnonymousTalk(    #31
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C3511_01\x01",      # 0
            "C3511_02\x01",      # 1
            "C3511_03\x01",      # 2
            "C3511_04\x01",      # 3
            "C3511_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_27B5"),
        (1, "loc_27C5"),
        (2, "loc_27D5"),
        (3, "loc_27E5"),
        (4, "loc_27F5"),
        (SWITCH_DEFAULT, "loc_2805"),
    )


    label("loc_27B5")

    Battle(0x1F5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_280F")

    label("loc_27C5")

    Battle(0x1F6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_280F")

    label("loc_27D5")

    Battle(0x1F7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_280F")

    label("loc_27E5")

    Battle(0x1F8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_280F")

    label("loc_27F5")

    Battle(0x1F9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_280F")

    label("loc_2805")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_280F")

    Jump("Function_38_2748")

    label("loc_2812")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_38_2748 end

    def Function_39_2820(): pass

    label("Function_39_2820")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_297B")

    AnonymousTalk(    #32
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3100_01\x01",      # 0
            "R3100_02\x01",      # 1
            "R3100_03\x01",      # 2
            "R3100_04\x01",      # 3
            "R3101_05\x01",      # 4
            "R3101_01\x01",      # 5
            "R3101_02\x01",      # 6
            "R3101_03\x01",      # 7
            "R3101_04\x01",      # 8
            "R3101_05\x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_28CE"),
        (1, "loc_28DE"),
        (2, "loc_28EE"),
        (3, "loc_28FE"),
        (4, "loc_290E"),
        (5, "loc_291E"),
        (6, "loc_292E"),
        (7, "loc_293E"),
        (8, "loc_294E"),
        (9, "loc_295E"),
        (SWITCH_DEFAULT, "loc_296E"),
    )


    label("loc_28CE")

    Battle(0x209, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2978")

    label("loc_28DE")

    Battle(0x20A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2978")

    label("loc_28EE")

    Battle(0x20B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2978")

    label("loc_28FE")

    Battle(0x20C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2978")

    label("loc_290E")

    Battle(0x20D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2978")

    label("loc_291E")

    Battle(0x349, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2978")

    label("loc_292E")

    Battle(0x34A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2978")

    label("loc_293E")

    Battle(0x34B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2978")

    label("loc_294E")

    Battle(0x34C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2978")

    label("loc_295E")

    Battle(0x34D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2978")

    label("loc_296E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2978")

    Jump("Function_39_2820")

    label("loc_297B")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_39_2820 end

    def Function_40_2989(): pass

    label("Function_40_2989")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A53")

    AnonymousTalk(    #33
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3200_01\x01",      # 0
            "R3200_02\x01",      # 1
            "R3200_03\x01",      # 2
            "R3200_04\x01",      # 3
            "R3200_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_29F6"),
        (1, "loc_2A06"),
        (2, "loc_2A16"),
        (3, "loc_2A26"),
        (4, "loc_2A36"),
        (SWITCH_DEFAULT, "loc_2A46"),
    )


    label("loc_29F6")

    Battle(0x21D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A50")

    label("loc_2A06")

    Battle(0x21E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A50")

    label("loc_2A16")

    Battle(0x21F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A50")

    label("loc_2A26")

    Battle(0x220, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A50")

    label("loc_2A36")

    Battle(0x221, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A50")

    label("loc_2A46")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A50")

    Jump("Function_40_2989")

    label("loc_2A53")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_40_2989 end

    def Function_41_2A61(): pass

    label("Function_41_2A61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B2B")

    AnonymousTalk(    #34
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3300_01\x01",      # 0
            "R3300_02\x01",      # 1
            "R3300_03\x01",      # 2
            "R3300_04\x01",      # 3
            "R3300_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2ACE"),
        (1, "loc_2ADE"),
        (2, "loc_2AEE"),
        (3, "loc_2AFE"),
        (4, "loc_2B0E"),
        (SWITCH_DEFAULT, "loc_2B1E"),
    )


    label("loc_2ACE")

    Battle(0x231, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B28")

    label("loc_2ADE")

    Battle(0x232, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B28")

    label("loc_2AEE")

    Battle(0x233, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B28")

    label("loc_2AFE")

    Battle(0x234, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B28")

    label("loc_2B0E")

    Battle(0x235, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B28")

    label("loc_2B1E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B28")

    Jump("Function_41_2A61")

    label("loc_2B2B")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_41_2A61 end

    def Function_42_2B39(): pass

    label("Function_42_2B39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C28")

    AnonymousTalk(    #35
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C3107_01\x01",              # 0
            "C3107_02\x01",              # 1
            "C3107_10\x01",              # 2
            "C3107_11\x01",              # 3
            "C3107_12\x01",              # 4
            "C3107_14特务兵Ｃ\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2BBB"),
        (1, "loc_2BCB"),
        (2, "loc_2BDB"),
        (3, "loc_2BEB"),
        (4, "loc_2BFB"),
        (5, "loc_2C0B"),
        (SWITCH_DEFAULT, "loc_2C1B"),
    )


    label("loc_2BBB")

    Battle(0x245, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C25")

    label("loc_2BCB")

    Battle(0x246, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C25")

    label("loc_2BDB")

    Battle(0x24E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C25")

    label("loc_2BEB")

    Battle(0x24F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C25")

    label("loc_2BFB")

    Battle(0x250, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C25")

    label("loc_2C0B")

    Battle(0x252, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C25")

    label("loc_2C1B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C25")

    Jump("Function_42_2B39")

    label("loc_2C28")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_42_2B39 end

    def Function_43_2C36(): pass

    label("Function_43_2C36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D6A")

    AnonymousTalk(    #36
        "\x06请选择\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "艾尔贝周游道\x01",                            # 0
            "下水道\x01",                                  # 1
            "封印区域\x01",                                # 2
            "庭园大道\x01",                                # 3
            "艾尔贝离宫外部  中庭，回廊（夜晚）\x01",      # 4
            "艾尔贝离宫外部  内部（夜晚）\x01",            # 5
            "格兰赛尔城内部，中庭，女王宫内\x01",          # 6
            "格兰赛尔城内部，空中庭园\x01",                # 7
            "取消\x01",                                    # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D25"),
        (1, "loc_2D2C"),
        (2, "loc_2D33"),
        (3, "loc_2D3A"),
        (4, "loc_2D41"),
        (5, "loc_2D48"),
        (6, "loc_2D4F"),
        (7, "loc_2D56"),
        (SWITCH_DEFAULT, "loc_2D5D"),
    )


    label("loc_2D25")

    Call(2, 44)
    Jump("loc_2D67")

    label("loc_2D2C")

    Call(2, 45)
    Jump("loc_2D67")

    label("loc_2D33")

    Call(2, 46)
    Jump("loc_2D67")

    label("loc_2D3A")

    Call(2, 47)
    Jump("loc_2D67")

    label("loc_2D41")

    Call(2, 48)
    Jump("loc_2D67")

    label("loc_2D48")

    Call(2, 49)
    Jump("loc_2D67")

    label("loc_2D4F")

    Call(2, 50)
    Jump("loc_2D67")

    label("loc_2D56")

    Call(2, 51)
    Jump("loc_2D67")

    label("loc_2D5D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D67")

    Jump("Function_43_2C36")

    label("loc_2D6A")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_43_2C36 end

    def Function_44_2D78(): pass

    label("Function_44_2D78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E42")

    AnonymousTalk(    #37
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C4100_01\x01",      # 0
            "C4100_02\x01",      # 1
            "C4100_03\x01",      # 2
            "C4100_04\x01",      # 3
            "C4100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2DE5"),
        (1, "loc_2DF5"),
        (2, "loc_2E05"),
        (3, "loc_2E15"),
        (4, "loc_2E25"),
        (SWITCH_DEFAULT, "loc_2E35"),
    )


    label("loc_2DE5")

    Battle(0x259, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2E3F")

    label("loc_2DF5")

    Battle(0x25A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2E3F")

    label("loc_2E05")

    Battle(0x25B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2E3F")

    label("loc_2E15")

    Battle(0x25C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2E3F")

    label("loc_2E25")

    Battle(0x25D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2E3F")

    label("loc_2E35")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E3F")

    Jump("Function_44_2D78")

    label("loc_2E42")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_44_2D78 end

    def Function_45_2E50(): pass

    label("Function_45_2E50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F8E")

    AnonymousTalk(    #38
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C4200_01\x01",      # 0
            "C4200_02\x01",      # 1
            "C4200_03\x01",      # 2
            "C4200_04\x01",      # 3
            "C4200_05\x01",      # 4
            "C4200_06\x01",      # 5
            "C4200_07\x01",      # 6
            "C4200_08\x01",      # 7
            "C4200_09\x01",      # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2EF1"),
        (1, "loc_2F01"),
        (2, "loc_2F11"),
        (3, "loc_2F21"),
        (4, "loc_2F31"),
        (5, "loc_2F41"),
        (6, "loc_2F51"),
        (7, "loc_2F61"),
        (8, "loc_2F71"),
        (SWITCH_DEFAULT, "loc_2F81"),
    )


    label("loc_2EF1")

    Battle(0x26D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F8B")

    label("loc_2F01")

    Battle(0x26E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F8B")

    label("loc_2F11")

    Battle(0x26F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F8B")

    label("loc_2F21")

    Battle(0x270, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F8B")

    label("loc_2F31")

    Battle(0x271, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F8B")

    label("loc_2F41")

    Battle(0x272, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F8B")

    label("loc_2F51")

    Battle(0x273, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F8B")

    label("loc_2F61")

    Battle(0x274, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F8B")

    label("loc_2F71")

    Battle(0x275, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F8B")

    label("loc_2F81")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F8B")

    Jump("Function_45_2E50")

    label("loc_2F8E")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_45_2E50 end

    def Function_46_2F9C(): pass

    label("Function_46_2F9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30F7")

    AnonymousTalk(    #39
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C4300_01\x01",      # 0
            "C4300_02\x01",      # 1
            "C4300_03\x01",      # 2
            "C4300_04\x01",      # 3
            "C4300_05\x01",      # 4
            "C4300_06\x01",      # 5
            "C4300_07\x01",      # 6
            "C4300_08\x01",      # 7
            "C4300_09\x01",      # 8
            "C4300_10\x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_304A"),
        (1, "loc_305A"),
        (2, "loc_306A"),
        (3, "loc_307A"),
        (4, "loc_308A"),
        (5, "loc_309A"),
        (6, "loc_30AA"),
        (7, "loc_30BA"),
        (8, "loc_30CA"),
        (9, "loc_30DA"),
        (SWITCH_DEFAULT, "loc_30EA"),
    )


    label("loc_304A")

    Battle(0x281, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30F4")

    label("loc_305A")

    Battle(0x282, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30F4")

    label("loc_306A")

    Battle(0x283, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30F4")

    label("loc_307A")

    Battle(0x284, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30F4")

    label("loc_308A")

    Battle(0x285, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30F4")

    label("loc_309A")

    Battle(0x286, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30F4")

    label("loc_30AA")

    Battle(0x287, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30F4")

    label("loc_30BA")

    Battle(0x288, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30F4")

    label("loc_30CA")

    Battle(0x289, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30F4")

    label("loc_30DA")

    Battle(0x28A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30F4")

    label("loc_30EA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30F4")

    Jump("Function_46_2F9C")

    label("loc_30F7")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_46_2F9C end

    def Function_47_3105(): pass

    label("Function_47_3105")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31CF")

    AnonymousTalk(    #40
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R4100_01\x01",      # 0
            "R4100_02\x01",      # 1
            "R4100_03\x01",      # 2
            "R4100_04\x01",      # 3
            "R4100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3172"),
        (1, "loc_3182"),
        (2, "loc_3192"),
        (3, "loc_31A2"),
        (4, "loc_31B2"),
        (SWITCH_DEFAULT, "loc_31C2"),
    )


    label("loc_3172")

    Battle(0x295, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_31CC")

    label("loc_3182")

    Battle(0x296, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_31CC")

    label("loc_3192")

    Battle(0x297, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_31CC")

    label("loc_31A2")

    Battle(0x298, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_31CC")

    label("loc_31B2")

    Battle(0x299, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_31CC")

    label("loc_31C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31CC")

    Jump("Function_47_3105")

    label("loc_31CF")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_47_3105 end

    def Function_48_31DD(): pass

    label("Function_48_31DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32A7")

    AnonymousTalk(    #41
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4301_01\x01",      # 0
            "T4301_02\x01",      # 1
            "T4301_03\x01",      # 2
            "T4301_04\x01",      # 3
            "T4301_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_324A"),
        (1, "loc_325A"),
        (2, "loc_326A"),
        (3, "loc_327A"),
        (4, "loc_328A"),
        (SWITCH_DEFAULT, "loc_329A"),
    )


    label("loc_324A")

    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_32A4")

    label("loc_325A")

    Battle(0x2BE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_32A4")

    label("loc_326A")

    Battle(0x2BF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_32A4")

    label("loc_327A")

    Battle(0x2C0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_32A4")

    label("loc_328A")

    Battle(0x2C1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_32A4")

    label("loc_329A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32A4")

    Jump("Function_48_31DD")

    label("loc_32A7")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_48_31DD end

    def Function_49_32B5(): pass

    label("Function_49_32B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_337F")

    AnonymousTalk(    #42
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4310_01\x01",      # 0
            "T4310_02\x01",      # 1
            "T4310_03\x01",      # 2
            "T4310_04\x01",      # 3
            "T4310_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3322"),
        (1, "loc_3332"),
        (2, "loc_3342"),
        (3, "loc_3352"),
        (4, "loc_3362"),
        (SWITCH_DEFAULT, "loc_3372"),
    )


    label("loc_3322")

    Battle(0x2D1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_337C")

    label("loc_3332")

    Battle(0x2D2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_337C")

    label("loc_3342")

    Battle(0x2D3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_337C")

    label("loc_3352")

    Battle(0x2D4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_337C")

    label("loc_3362")

    Battle(0x2D5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_337C")

    label("loc_3372")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_337C")

    Jump("Function_49_32B5")

    label("loc_337F")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_49_32B5 end

    def Function_50_338D(): pass

    label("Function_50_338D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3457")

    AnonymousTalk(    #43
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4210_01\x01",      # 0
            "T4210_02\x01",      # 1
            "T4210_03\x01",      # 2
            "T4210_04\x01",      # 3
            "T4210_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_33FA"),
        (1, "loc_340A"),
        (2, "loc_341A"),
        (3, "loc_342A"),
        (4, "loc_343A"),
        (SWITCH_DEFAULT, "loc_344A"),
    )


    label("loc_33FA")

    Battle(0x2E5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3454")

    label("loc_340A")

    Battle(0x2E6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3454")

    label("loc_341A")

    Battle(0x2E7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3454")

    label("loc_342A")

    Battle(0x2E8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3454")

    label("loc_343A")

    Battle(0x2E9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3454")

    label("loc_344A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3454")

    Jump("Function_50_338D")

    label("loc_3457")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_50_338D end

    def Function_51_3465(): pass

    label("Function_51_3465")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_352F")

    AnonymousTalk(    #44
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4201_01\x01",      # 0
            "T4201_02\x01",      # 1
            "T4201_03\x01",      # 2
            "T4201_04\x01",      # 3
            "T4201_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_34D2"),
        (1, "loc_34E2"),
        (2, "loc_34F2"),
        (3, "loc_3502"),
        (4, "loc_3512"),
        (SWITCH_DEFAULT, "loc_3522"),
    )


    label("loc_34D2")

    Battle(0x2F9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_352C")

    label("loc_34E2")

    Battle(0x2FA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_352C")

    label("loc_34F2")

    Battle(0x2FB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_352C")

    label("loc_3502")

    Battle(0x2FC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_352C")

    label("loc_3512")

    Battle(0x2FD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_352C")

    label("loc_3522")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_352C")

    Jump("Function_51_3465")

    label("loc_352F")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_51_3465 end

    def Function_52_353D(): pass

    label("Function_52_353D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3607")

    AnonymousTalk(    #45
        "\x06请选择\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R4100_21\x01",      # 0
            "R4100_22\x01",      # 1
            "R4100_23\x01",      # 2
            "R4100_24\x01",      # 3
            "R4100_25\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_35AA"),
        (1, "loc_35BA"),
        (2, "loc_35CA"),
        (3, "loc_35DA"),
        (4, "loc_35EA"),
        (SWITCH_DEFAULT, "loc_35FA"),
    )


    label("loc_35AA")

    Battle(0x2A9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3604")

    label("loc_35BA")

    Battle(0x2AA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3604")

    label("loc_35CA")

    Battle(0x2AB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3604")

    label("loc_35DA")

    Battle(0x2AC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3604")

    label("loc_35EA")

    Battle(0x2AD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3604")

    label("loc_35FA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3604")

    Jump("Function_52_353D")

    label("loc_3607")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_52_353D end

    def Function_53_3615(): pass

    label("Function_53_3615")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_361F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3807")

    AnonymousTalk(    #46
        "\x06请选择\x02",
    )


    Menu(
        2,
        10,
        100,
        1,
        (
            "布卢布兰\x01",          # 0
            "瓦鲁特\x01",            # 1
            "露茜奥拉\x01",          # 2
            "玲\x01",                # 3
            "莱维\x01",              # 4
            "怀斯曼\x01",            # 5
            "猎兵克鲁茨\x01",        # 6
            "猎兵卡露娜\x01",        # 7
            "猎兵库拉茨\x01",        # 8
            "洗脑库拉茨\x01",        # 9
            "洗脑卡露娜\x01",        # 10
            "洗脑亚妮拉丝\x01",      # 11
            "猎兵基尔巴特\x01",      # 12
            "穆拉\x01",              # 13
            "希德\x01",              # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_370A"),
        (1, "loc_371A"),
        (2, "loc_372A"),
        (3, "loc_373A"),
        (4, "loc_374A"),
        (5, "loc_375A"),
        (6, "loc_376A"),
        (7, "loc_377A"),
        (8, "loc_378A"),
        (9, "loc_379A"),
        (10, "loc_37AA"),
        (11, "loc_37BA"),
        (12, "loc_37CA"),
        (13, "loc_37DA"),
        (14, "loc_37EA"),
        (SWITCH_DEFAULT, "loc_37FA"),
    )


    label("loc_370A")

    Battle(0x802, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3804")

    label("loc_371A")

    Battle(0x803, 0x30000D, 0x0, 0x0, 0xFF)
    Jump("loc_3804")

    label("loc_372A")

    Battle(0x804, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3804")

    label("loc_373A")

    Battle(0x805, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3804")

    label("loc_374A")

    Battle(0x806, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3804")

    label("loc_375A")

    Battle(0x807, 0x30000C, 0x0, 0x0, 0xFF)
    Jump("loc_3804")

    label("loc_376A")

    Battle(0x395, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3804")

    label("loc_377A")

    Battle(0x394, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3804")

    label("loc_378A")

    Battle(0x397, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3804")

    label("loc_379A")

    Battle(0x41E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3804")

    label("loc_37AA")

    Battle(0x41F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3804")

    label("loc_37BA")

    Battle(0x420, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3804")

    label("loc_37CA")

    Battle(0x42A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3804")

    label("loc_37DA")

    Battle(0xA8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3804")

    label("loc_37EA")

    Battle(0xC82, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3804")

    label("loc_37FA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3804")

    Jump("loc_361F")

    label("loc_3807")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_53_3615 end

    def Function_54_3815(): pass

    label("Function_54_3815")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_381F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39FB")

    AnonymousTalk(    #47
        "\x06请选择\x02",
    )


    Menu(
        2,
        10,
        100,
        1,
        (
            "前篇最终Boss\x01",                      # 0
            "风暴袭击者\x01",                        # 1
            "幻想乐曲·德尔基昂\x01",                # 2
            "雷格纳特\x01",                          # 3
            "奥尔杰尤\x01",                          # 4
            "帕蒂尔·玛蒂尔\x01",                    # 5
            "帕蒂尔·玛蒂尔（玲附着）\x01",          # 6
            "天使·怀斯曼第一形态\x01",              # 7
            "天使·怀斯曼第二形态\x01",              # 8
            "天使·怀斯曼不能取胜\x01",              # 9
            "天使·怀斯曼第二形态（效果）\x01",      # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3938"),
        (1, "loc_3948"),
        (2, "loc_3958"),
        (3, "loc_3968"),
        (4, "loc_3978"),
        (5, "loc_3988"),
        (6, "loc_3998"),
        (7, "loc_39A8"),
        (8, "loc_39B8"),
        (9, "loc_39C8"),
        (10, "loc_39DE"),
        (SWITCH_DEFAULT, "loc_39EE"),
    )


    label("loc_3938")

    Battle(0x7D3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_39F8")

    label("loc_3948")

    Battle(0x44C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_39F8")

    label("loc_3958")

    Battle(0x450, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_39F8")

    label("loc_3968")

    Battle(0x44F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_39F8")

    label("loc_3978")

    Battle(0x44E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_39F8")

    label("loc_3988")

    Battle(0x463, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_39F8")

    label("loc_3998")

    Battle(0x453, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_39F8")

    label("loc_39A8")

    Battle(0x451, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_39F8")

    label("loc_39B8")

    Battle(0x452, 0x300017, 0x0, 0x0, 0xFF)
    Jump("loc_39F8")

    label("loc_39C8")

    OP_A2(0x2298)
    Battle(0x465, 0x300014, 0x0, 0x0, 0xFF)
    OP_A3(0x2298)
    Jump("loc_39F8")

    label("loc_39DE")

    Battle(0x7D8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_39F8")

    label("loc_39EE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39F8")

    Jump("loc_381F")

    label("loc_39FB")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_54_3815 end

    def Function_55_3A09(): pass

    label("Function_55_3A09")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AA3")

    AnonymousTalk(    #48
        "\x06请选择\x02",
    )


    Menu(
        2,
        10,
        100,
        1,
        (
            "螃蟹老大\x01",      # 0
            "企鹅老大\x01",      # 1
            "猿羊老大\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3A66"),
        (1, "loc_3A76"),
        (2, "loc_3A86"),
        (SWITCH_DEFAULT, "loc_3A96"),
    )


    label("loc_3A66")

    Battle(0x59, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AA0")

    label("loc_3A76")

    Battle(0x1EA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AA0")

    label("loc_3A86")

    Battle(0x1EB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AA0")

    label("loc_3A96")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3AA0")

    Jump("loc_3A13")

    label("loc_3AA3")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_55_3A09 end

    def Function_56_3AB1(): pass

    label("Function_56_3AB1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3ABB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BB2")

    AnonymousTalk(    #49
        "\x06请选择\x02",
    )


    Menu(
        2,
        10,
        100,
        1,
        (
            "８章，露茜奥拉～玲\x01",            # 0
            "８章，布卢布兰\x01",                # 1
            "９章，约修亚ＶＳ艾丝蒂尔\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3B2E"),
        (1, "loc_3B7C"),
        (2, "loc_3B95"),
        (SWITCH_DEFAULT, "loc_3BA5"),
    )


    label("loc_3B2E")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x2710, 0x30000F, 0x0, 0x0, 0xFF)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x2711, 0x300010, 0x0, 0x0, 0xFF)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x2712, 0x300011, 0x0, 0x0, 0xFF)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BAF")

    label("loc_3B7C")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x2713, 0x300012, 0x0, 0x0, 0xFF)
    Jump("loc_3BAF")

    label("loc_3B95")

    Battle(0x2714, 0x300013, 0x0, 0x0, 0xFF)
    Jump("loc_3BAF")

    label("loc_3BA5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BAF")

    Jump("loc_3ABB")

    label("loc_3BB2")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_56_3AB1 end

    def Function_57_3BC0(): pass

    label("Function_57_3BC0")

    Return()

    # Function_57_3BC0 end

    def Function_58_3BC1(): pass

    label("Function_58_3BC1")

    OP_31(0x0, 0x0, 0x55)
    OP_31(0x1, 0x0, 0x55)
    OP_31(0x2, 0x0, 0x55)
    OP_31(0x3, 0x0, 0x55)
    OP_31(0x6, 0x0, 0x55)
    OP_31(0x4, 0x0, 0x55)
    OP_31(0x5, 0x0, 0x55)
    OP_31(0x7, 0x0, 0x55)
    OP_31(0x0, 0x5, 0x64)
    OP_31(0x1, 0x5, 0x64)
    OP_31(0x2, 0x5, 0x64)
    OP_31(0x3, 0x5, 0x64)
    OP_31(0x6, 0x5, 0x64)
    OP_31(0x4, 0x5, 0x64)
    OP_31(0x5, 0x5, 0x64)
    OP_31(0x7, 0x5, 0x64)
    OP_31(0x8, 0x5, 0x64)
    OP_31(0x9, 0x5, 0x64)
    OP_31(0xA, 0x5, 0x64)
    OP_31(0xB, 0x5, 0x64)
    OP_31(0xC, 0x5, 0x64)
    OP_31(0xD, 0x5, 0x64)
    OP_37(0x0, 0xFF)
    OP_37(0x1, 0xFF)
    OP_37(0x2, 0xFF)
    OP_37(0x3, 0xFF)
    OP_37(0x6, 0xFF)
    OP_37(0x4, 0xFF)
    OP_37(0x5, 0xFF)
    OP_37(0x7, 0xFF)
    OP_37(0x8, 0xFF)
    OP_37(0x9, 0xFF)
    OP_37(0xA, 0xFF)
    OP_37(0xB, 0xFF)
    OP_37(0xC, 0xFF)
    OP_37(0xD, 0xFF)
    OP_3E(0x202, 99)
    OP_3E(0x1F7, 99)
    OP_3E(0x1FB, 99)
    OP_3E(0x1FC, 99)
    OP_3E(0x1FD, 10)
    OP_3E(0x204, 8)
    OP_3E(0x1FF, 99)
    OP_3E(0x1FF, 99)
    OP_34(0x1, 0x3C)
    OP_34(0x1, 0x3E)
    OP_34(0x1, 0x41)
    OP_34(0x1, 0x3F)
    OP_34(0x1, 0x5F)
    OP_34(0x1, 0x60)
    OP_34(0x1, 0x69)
    OP_34(0x1, 0x6A)
    OP_34(0x0, 0x1E)
    OP_34(0x0, 0x1F)
    OP_34(0x0, 0x20)
    OP_34(0x0, 0x23)
    OP_34(0x0, 0x25)
    OP_34(0x0, 0x6E)
    OP_34(0x0, 0x6F)
    OP_34(0x0, 0x70)
    OP_34(0x0, 0x76)
    OP_34(0x0, 0x77)
    OP_34(0x0, 0x78)
    OP_34(0x2, 0x32)
    OP_34(0x2, 0x33)
    OP_34(0x2, 0x34)
    OP_34(0x2, 0x36)
    OP_34(0x2, 0x37)
    OP_34(0x3, 0x64)
    OP_34(0x3, 0x69)
    OP_34(0x3, 0x69)
    OP_34(0x3, 0x4B)
    OP_34(0x3, 0x4C)
    OP_34(0x4, 0x6E)
    OP_34(0x4, 0x6F)
    OP_34(0x4, 0x70)
    OP_34(0x4, 0x72)
    OP_34(0x4, 0x73)
    OP_34(0x4, 0x76)
    OP_34(0x4, 0x77)
    OP_34(0x4, 0x78)
    OP_34(0x5, 0x1E)
    OP_34(0x5, 0x1F)
    OP_34(0x5, 0x20)
    OP_34(0x6, 0x56)
    OP_34(0x6, 0x57)
    OP_34(0x6, 0x58)
    OP_34(0x6, 0x6E)
    OP_34(0x6, 0x6F)
    OP_34(0x6, 0x76)
    OP_34(0x7, 0xB)
    OP_34(0x7, 0xD)
    OP_34(0x7, 0x10)
    OP_34(0x7, 0x4B)
    OP_34(0x7, 0x4C)
    OP_35(0x0, 0x0)
    OP_35(0x1, 0x0)
    OP_35(0x2, 0x0)
    OP_35(0x3, 0x0)
    OP_35(0x4, 0x0)
    OP_35(0x5, 0x0)
    OP_35(0x6, 0x0)
    OP_35(0x7, 0x0)
    OP_35(0x8, 0x0)
    OP_35(0xA, 0x0)
    OP_41(0x0, 0x15, 0xFF)
    OP_41(0x0, 0x108, 0xFF)
    OP_41(0x0, 0x109, 0xFF)
    OP_41(0x1, 0x2B, 0xFF)
    OP_41(0x1, 0x108, 0xFF)
    OP_41(0x1, 0x129, 0xFF)
    OP_41(0x2, 0x4C, 0xFF)
    OP_41(0x2, 0x108, 0xFF)
    OP_41(0x2, 0x129, 0xFF)
    OP_41(0x3, 0x6B, 0xFF)
    OP_41(0x3, 0x108, 0xFF)
    OP_41(0x3, 0x129, 0xFF)
    OP_41(0x4, 0x88, 0xFF)
    OP_41(0x4, 0x108, 0xFF)
    OP_41(0x4, 0x129, 0xFF)
    OP_41(0x5, 0xA6, 0xFF)
    OP_41(0x5, 0x108, 0xFF)
    OP_41(0x5, 0x129, 0xFF)
    OP_41(0x6, 0xC3, 0xFF)
    OP_41(0x6, 0x108, 0xFF)
    OP_41(0x6, 0x129, 0xFF)
    OP_41(0x7, 0xE0, 0xFF)
    OP_41(0x7, 0x108, 0xFF)
    OP_41(0x7, 0x129, 0xFF)
    Return()

    # Function_58_3BC1 end

    def Function_59_3DEE(): pass

    label("Function_59_3DEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4079")

    AnonymousTalk(    #50
        "\x06请选择\x02",
    )


    Menu(
        1,
        10,
        100,
        1,
        (
            "迷你游戏00俄罗斯轮盘\x01",      # 0
            "迷你游戏01游戏机\x01",          # 1
            "迷你游戏02 21点\x01",           # 2
            "迷你游戏03钓鱼\x01",            # 3
            "迷你游戏04纸牌\x01",            # 4
            "迷你游戏05\x01",                # 5
        )
    )

    MenuEnd(0x0)
    OP_5F(0xFF)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3E96"),
        (1, "loc_3ECF"),
        (2, "loc_3F08"),
        (3, "loc_3F41"),
        (4, "loc_3FFA"),
        (5, "loc_4033"),
        (SWITCH_DEFAULT, "loc_406C"),
    )


    label("loc_3E96")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_406C")

    label("loc_3ECF")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0xC, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_406C")

    label("loc_3F08")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0xD, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_406C")

    label("loc_3F41")

    OP_3E(0x24E, 10)
    OP_3E(0x24F, 10)
    OP_3E(0x250, 10)
    OP_3E(0x251, 10)
    OP_3E(0x252, 10)
    OP_3E(0x253, 10)
    OP_3E(0x254, 10)
    OP_3E(0x3D4, 10)
    OP_3E(0x3D5, 10)
    OP_3E(0x3D6, 10)
    OP_3E(0x3D7, 10)
    OP_3E(0x3D8, 10)
    OP_3E(0x3D9, 10)
    OP_3E(0x3DA, 10)
    OP_3E(0x3DB, 10)
    OP_3E(0x3DC, 10)
    OP_3E(0x3DD, 10)
    OP_3E(0x3DE, 10)
    OP_3E(0x3DF, 10)
    OP_3E(0x3E0, 10)
    OP_3E(0x3E1, 10)
    OP_3E(0x3E2, 10)
    OP_3E(0x3E3, 10)

    AnonymousTalk(    #51
        (
            "因为移动到布莱特家，\x01",
            "请寻找后面池子的钓鱼点\x01",
            "开始钓鱼。\x02",
        )
    )

    CloseMessageWindow()
    NewScene("ED6_DT21/T0300   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_406C")

    label("loc_3FFA")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0xF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_406C")

    label("loc_4033")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_406C")

    label("loc_406C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("Function_59_3DEE")

    label("loc_4079")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_59_3DEE end

    SaveToFile()

Try(main)
