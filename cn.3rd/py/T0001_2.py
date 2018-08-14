from ED63RDScenarioHelper import *

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
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 2,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_30C",          # 01, 1
        "Function_2_460",          # 02, 2
        "Function_3_559",          # 03, 3
        "Function_4_5E6",          # 04, 4
        "Function_5_670",          # 05, 5
        "Function_6_7CB",          # 06, 6
        "Function_7_88C",          # 07, 7
        "Function_8_AC8",          # 08, 8
        "Function_9_B57",          # 09, 9
        "Function_10_103C",        # 0A, 10
        "Function_11_15A8",        # 0B, 11
        "Function_12_1739",        # 0C, 12
        "Function_13_189B",        # 0D, 13
        "Function_14_1B0E",        # 0E, 14
        "Function_15_1B0F",        # 0F, 15
        "Function_16_1B10",        # 10, 16
        "Function_17_1B11",        # 11, 17
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FE")

    Menu(
        1,
        10,
        100,
        1,
        (
            "测试\x01",                        # 0
            "跳跳猫\x01",                      # 1
            "盔甲巨蟹\x01",                    # 2
            "跳跳猫3\x01",                     # 3
            "人型Boss\x01",                    # 4
            "大型Boss\x01",                    # 5
            "其他Boss\x01",                    # 6
            "选择魔兽后进行战斗\x01",          # 7
            "用选择了的魔兽进行战斗\x01",      # 8
            "DEMO用①\x01",                    # 9
            "DEMO用②\x01",                    # 10
            "DEMO用③\x01",                    # 11
            "自动战斗\x01",                    # 12
        )
    )

    Jump("loc_19A")

    label("loc_19A")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1DA"),
        (1, "loc_1EA"),
        (2, "loc_1FA"),
        (3, "loc_20A"),
        (4, "loc_21A"),
        (5, "loc_221"),
        (6, "loc_228"),
        (7, "loc_22F"),
        (8, "loc_266"),
        (9, "loc_276"),
        (10, "loc_286"),
        (11, "loc_296"),
        (12, "loc_2A6"),
        (SWITCH_DEFAULT, "loc_2B6"),
    )


    label("loc_1DA")

    Battle(0x397, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B9")

    label("loc_1EA")

    Battle(0x7D4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B9")

    label("loc_1FA")

    Battle(0x7D5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B9")

    label("loc_20A")

    Battle(0x7D7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B9")

    label("loc_21A")

    Call(2, 12)
    Jump("loc_2B9")

    label("loc_221")

    Call(2, 13)
    Jump("loc_2B9")

    label("loc_228")

    Call(2, 14)
    Jump("loc_2B9")

    label("loc_22F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_C0(0x21, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_263")
    Battle(0x7D1, 0x0, 0x0, 0x0, 0xFF)

    label("loc_263")

    Jump("loc_2B9")

    label("loc_266")

    Battle(0x7D1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B9")

    label("loc_276")

    Battle(0x7DA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B9")

    label("loc_286")

    Battle(0x7DB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B9")

    label("loc_296")

    Battle(0x7DC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B9")

    label("loc_2A6")

    Battle(0x2710, 0x30000B, 0x0, 0x0, 0xFF)
    Jump("loc_2B9")

    label("loc_2B6")

    Jump("loc_2B9")

    label("loc_2B9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2D0"),
        (SWITCH_DEFAULT, "loc_2FB"),
    )


    label("loc_2D0")

    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    Jump("loc_2FB")

    label("loc_2FB")

    Jump("Function_0_AA")

    label("loc_2FE")

    OP_5F(0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_AA end

    def Function_1_30C(): pass

    label("Function_1_30C")


    AnonymousTalk(    #0
        "\x06请选择\x02",
    )

    Jump("loc_321")

    label("loc_321")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_450")

    Menu(
        1,
        10,
        100,
        1,
        (
            "测试\x01",            # 0
            "洛连特\x01",          # 1
            "柏斯\x01",            # 2
            "卢安\x01",            # 3
            "蔡斯\x01",            # 4
            "格兰赛尔\x01",        # 5
            "后篇追加\x01",        # 6
            "外传追加①\x01",      # 7
            "外传追加②\x01",      # 8
            "外传追加③\x01",      # 9
            "取消\x01",            # 10
        )
    )

    Jump("loc_3C9")

    label("loc_3C9")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3FD"),
        (1, "loc_404"),
        (2, "loc_40B"),
        (3, "loc_412"),
        (4, "loc_419"),
        (5, "loc_420"),
        (6, "loc_427"),
        (7, "loc_42E"),
        (8, "loc_435"),
        (9, "loc_43C"),
        (SWITCH_DEFAULT, "loc_443"),
    )


    label("loc_3FD")

    Call(2, 2)
    Jump("loc_44D")

    label("loc_404")

    Call(2, 3)
    Jump("loc_44D")

    label("loc_40B")

    Call(2, 4)
    Jump("loc_44D")

    label("loc_412")

    Call(2, 5)
    Jump("loc_44D")

    label("loc_419")

    Call(2, 6)
    Jump("loc_44D")

    label("loc_420")

    Call(2, 7)
    Jump("loc_44D")

    label("loc_427")

    Call(2, 8)
    Jump("loc_44D")

    label("loc_42E")

    Call(2, 9)
    Jump("loc_44D")

    label("loc_435")

    Call(2, 10)
    Jump("loc_44D")

    label("loc_43C")

    Call(2, 11)
    Jump("loc_44D")

    label("loc_443")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44D")

    Jump("loc_321")

    label("loc_450")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_30C end

    def Function_2_460(): pass

    label("Function_2_460")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_549")

    Menu(
        2,
        10,
        100,
        1,
        (
            "地图1 BTTEST01\x01",      # 0
            "地图2 BTTEST02\x01",      # 1
            "地图3 BTTEST03\x01",      # 2
            "地图4 BTTEST04\x01",      # 3
            "地图5 BTTEST05\x01",      # 4
            "取消\x01",                # 5
        )
    )

    Jump("loc_4CC")

    label("loc_4CC")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4EC"),
        (1, "loc_4FC"),
        (2, "loc_50C"),
        (3, "loc_51C"),
        (4, "loc_52C"),
        (SWITCH_DEFAULT, "loc_53C"),
    )


    label("loc_4EC")

    Battle(0x82B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_546")

    label("loc_4FC")

    Battle(0x82C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_546")

    label("loc_50C")

    Battle(0x82D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_546")

    label("loc_51C")

    Battle(0x82E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_546")

    label("loc_52C")

    Battle(0x82F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_546")

    label("loc_53C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_546")

    Jump("Function_2_460")

    label("loc_549")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_460 end

    def Function_3_559(): pass

    label("Function_3_559")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D8")

    AnonymousTalk(    #1
        "\x06请选择\x02",
    )

    Jump("loc_57B")

    label("loc_57B")


    Menu(
        2,
        10,
        80,
        1,
        (
            "BC0300 神秘森林\x01",      # 0
            "取消\x01",                 # 1
        )
    )

    Jump("loc_59F")

    label("loc_59F")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5AF"),
        (SWITCH_DEFAULT, "loc_5CB"),
    )


    label("loc_5AF")

    OP_C4(0x0, 0x4)
    Battle(0x834, 0x0, 0x0, 0x0, 0xFF)
    OP_C4(0x1, 0x4)
    Jump("loc_5D5")

    label("loc_5CB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D5")

    Jump("Function_3_559")

    label("loc_5D8")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_559 end

    def Function_4_5E6(): pass

    label("Function_4_5E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_662")

    AnonymousTalk(    #2
        "\x06请选择\x02",
    )

    Jump("loc_608")

    label("loc_608")


    Menu(
        2,
        10,
        80,
        1,
        (
            "BC1300　空贼基地战斗地图\x01",      # 0
            "取消\x01",                          # 1
        )
    )

    Jump("loc_635")

    label("loc_635")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_645"),
        (SWITCH_DEFAULT, "loc_655"),
    )


    label("loc_645")

    Battle(0x898, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_65F")

    label("loc_655")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_65F")

    Jump("Function_4_5E6")

    label("loc_662")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_5E6 end

    def Function_5_670(): pass

    label("Function_5_670")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BD")

    AnonymousTalk(    #3
        "\x06请选择\x02",
    )

    Jump("loc_692")

    label("loc_692")


    Menu(
        2,
        10,
        80,
        1,
        (
            "BC2401 王立学院旧校舍地下BOSS\x01",          # 0
            "BT2500 王立学院校园战斗地图\x01",            # 1
            "BT2510 王立学院走廊战斗地图\x01",            # 2
            "BT2511 王立学院(男生宿舍)战斗地图\x01",      # 3
            "BT2512 王立学院(女神宿舍)战斗地图\x01",      # 4
            "取消\x01",                                   # 5
        )
    )

    Jump("loc_740")

    label("loc_740")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_760"),
        (1, "loc_770"),
        (2, "loc_780"),
        (3, "loc_790"),
        (4, "loc_7A0"),
        (SWITCH_DEFAULT, "loc_7B0"),
    )


    label("loc_760")

    Battle(0x8FC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_7BA")

    label("loc_770")

    Battle(0x8FD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_7BA")

    label("loc_780")

    Battle(0x8FE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_7BA")

    label("loc_790")

    Battle(0x8FF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_7BA")

    label("loc_7A0")

    Battle(0x900, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_7BA")

    label("loc_7B0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7BA")

    Jump("Function_5_670")

    label("loc_7BD")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_670 end

    def Function_6_7CB(): pass

    label("Function_6_7CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_87E")

    AnonymousTalk(    #4
        "\x06请选择\x02",
    )

    Jump("loc_7ED")

    label("loc_7ED")


    Menu(
        2,
        10,
        80,
        1,
        (
            "BR3400 卡鲁迪亚隧道战斗地图\x01",          # 0
            "BC3300 卡鲁迪亚大钟乳洞战斗地图\x01",      # 1
            "取消\x01",                                 # 2
        )
    )

    Jump("loc_83D")

    label("loc_83D")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_851"),
        (1, "loc_861"),
        (SWITCH_DEFAULT, "loc_871"),
    )


    label("loc_851")

    Battle(0x960, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_87B")

    label("loc_861")

    Battle(0x961, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_87B")

    label("loc_871")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_87B")

    Jump("Function_6_7CB")

    label("loc_87E")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_7CB end

    def Function_7_88C(): pass

    label("Function_7_88C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ABA")

    AnonymousTalk(    #5
        "\x06请选择\x02",
    )

    Jump("loc_8AE")

    label("loc_8AE")


    Menu(
        2,
        10,
        80,
        1,
        (
            "BT4100 王都街区战斗地图（＊顶点颜色修正为傍晚）\x01",                    # 0
            "BT4404 格兰赛尔（码头通路）战斗地图　（＊顶点颜色修正为傍晚）\x01",      # 1
            "BT4105 格兰赛尔竞技场战斗地图(傍晚)\x01",                                # 2
            "BT4210 格兰赛尔城内部战斗地图\x01",                                      # 3
            "BC4100 艾尔贝周游道战斗地图\x01",                                        # 4
            "BC4303 封印区域（BOSS部屋理查德战·BOSS第1形态使用）\x01",               # 5
            "BT4138 帝国大使馆内部战斗地图\x01",                                      # 6
            "BT4139 共和国大使馆内部战斗地图\x01",                                    # 7
            "取消\x01",                                                               # 8
        )
    )

    Jump("loc_A01")

    label("loc_A01")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A2D"),
        (1, "loc_A3D"),
        (2, "loc_A4D"),
        (3, "loc_A5D"),
        (4, "loc_A6D"),
        (5, "loc_A7D"),
        (6, "loc_A8D"),
        (7, "loc_A9D"),
        (SWITCH_DEFAULT, "loc_AAD"),
    )


    label("loc_A2D")

    Battle(0x9C4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_AB7")

    label("loc_A3D")

    Battle(0x9C5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_AB7")

    label("loc_A4D")

    Battle(0x9C6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_AB7")

    label("loc_A5D")

    Battle(0x9C7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_AB7")

    label("loc_A6D")

    Battle(0x9C8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_AB7")

    label("loc_A7D")

    Battle(0x9C9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_AB7")

    label("loc_A8D")

    Battle(0x9CA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_AB7")

    label("loc_A9D")

    Battle(0x9CB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_AB7")

    label("loc_AAD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AB7")

    Jump("Function_7_88C")

    label("loc_ABA")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_88C end

    def Function_8_AC8(): pass

    label("Function_8_AC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B49")

    AnonymousTalk(    #6
        "\x06请选择\x02",
    )

    Jump("loc_AEA")

    label("loc_AEA")


    Menu(
        2,
        10,
        80,
        1,
        (
            "BC5303 中枢塔内部頂上战斗地图\x01",      # 0
            "取消\x01",                               # 1
        )
    )

    Jump("loc_B1C")

    label("loc_B1C")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B2C"),
        (SWITCH_DEFAULT, "loc_B3C"),
    )


    label("loc_B2C")

    Battle(0xA28, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_B46")

    label("loc_B3C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B46")

    Jump("Function_8_AC8")

    label("loc_B49")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_AC8 end

    def Function_9_B57(): pass

    label("Function_9_B57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_102E")

    AnonymousTalk(    #7
        "\x06请选择\x02",
    )

    Jump("loc_B79")

    label("loc_B79")


    Menu(
        2,
        10,
        80,
        1,
        (
            "BE0310 第１星层 王家专用飞船（埃尔赛尤）内部\x01",      # 0
            "BM7000 第１星层 翡翠 (喽啰战用）\x01",                  # 1
            "BM7001 第１星层 翡翠 (地区BOSS战用）\x01",              # 2
            "BU4138 第２星层 帝国大使馆内部\x01",                    # 3
            "BU4403 第２星层 码头仓库内部(傍晚)\x01",                # 4
            "BU4166 第２星层 格兰竞技场（竞技场夜）\x01",            # 5
            "BU4250 第２星层 格兰赛尔城内部（大厅夜）\x01",          # 6
            "BU4204 第２星层 格兰赛尔城内部（空中庭院夜）\x01",      # 7
            "BM7100 第３星层 金之道（喽啰战用）\x01",                # 8
            "BM7101 第３星层 金之道（BOSS战用）\x01",                # 9
            "BM7102 第３星层 银之道（喽啰战用）\x01",                # 10
            "BM7103 第３星层 银之道（BOSS战用）\x01",                # 11
            "BM5500 第４星层 巴斯塔尔水道（喽啰战用）\x01",          # 12
            "BM5501 第４星层 巴斯塔尔水道（BOSS战用）\x01",          # 13
            "BM5502 第４星层 圣科洛瓦森林（喽啰战用）\x01",          # 14
            "BM5503 第４星层 圣科洛瓦森林（BOSS战用）\x01",          # 15
            "BU5102 第４星层 宿舍前（亚斯塔提战用）\x01",            # 16
            "BM7200 第５星层 光之迷宫（喽啰战用）\x01",              # 17
            "BM7201 第５星层 影之迷宫（喽啰战用）\x01",              # 18
            "BM7202 第５星层 光之迷宫（BOSS战用）\x01",              # 19
            "取消\x01",                                              # 20
        )
    )

    Jump("loc_E85")

    label("loc_E85")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EE1"),
        (1, "loc_EF1"),
        (2, "loc_F01"),
        (3, "loc_F11"),
        (4, "loc_F21"),
        (5, "loc_F31"),
        (6, "loc_F41"),
        (7, "loc_F51"),
        (8, "loc_F61"),
        (9, "loc_F71"),
        (10, "loc_F81"),
        (11, "loc_F91"),
        (12, "loc_FA1"),
        (13, "loc_FB1"),
        (14, "loc_FC1"),
        (15, "loc_FD1"),
        (16, "loc_FE1"),
        (17, "loc_FF1"),
        (18, "loc_1001"),
        (19, "loc_1011"),
        (SWITCH_DEFAULT, "loc_1021"),
    )


    label("loc_EE1")

    Battle(0xA8C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_EF1")

    Battle(0xA8D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_F01")

    Battle(0xA8E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_F11")

    Battle(0xA8F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_F21")

    Battle(0xA90, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_F31")

    Battle(0xA91, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_F41")

    Battle(0xA92, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_F51")

    Battle(0xA93, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_F61")

    Battle(0xA94, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_F71")

    Battle(0xA95, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_F81")

    Battle(0xA96, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_F91")

    Battle(0xA97, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_FA1")

    Battle(0xA98, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_FB1")

    Battle(0xA99, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_FC1")

    Battle(0xA9A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_FD1")

    Battle(0xA9B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_FE1")

    Battle(0xA9C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_FF1")

    Battle(0xA9C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_1001")

    Battle(0xA9D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_1011")

    Battle(0xA9E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_102B")

    label("loc_1021")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_102B")

    Jump("Function_9_B57")

    label("loc_102E")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_9_B57 end

    def Function_10_103C(): pass

    label("Function_10_103C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_159A")

    AnonymousTalk(    #8
        "\x06请选择\x02",
    )

    Jump("loc_105E")

    label("loc_105E")


    Menu(
        2,
        10,
        80,
        1,
        (
            "BM4120 第６星层 艾尔贝周游道（喽啰战用）\x01",            # 0
            "BM3200 第６星层 雷斯顿要塞内部（司令室喽啰战）\x01",      # 1
            "BM3201 第６星层 雷斯顿要塞内部（兵舎喽啰战）\x01",        # 2
            "BM3202 第６星层 雷斯顿要塞内部（中BOSS1）\x01",           # 3
            "BM3203 第６星层 雷斯顿要塞内部（中BOSS1）\x01",           # 4
            "BM3204 第６星层 雷斯顿要塞内部（中BOSS1）\x01",           # 5
            "BM5400 第６星层 古罗力亚斯(黑) 通路\x01",                 # 6
            "BM5401 第６星层 古罗力亚斯(黑) 圣堂\x01",                 # 7
            "BM5406 第６星层 古罗力亚斯(黑) 飞机库\x01",               # 8
            "BM5408 第６星层 古罗力亚斯(黑) 甲板\x01",                 # 9
            "BM5415 第６星层 异次元圆形舞台\x01",                      # 10
            "BU2501 第６星层 通往学院旧校舍的路\x01",                  # 11
            "BM5600 第６星层 研究所屋顶\x01",                          # 12
            "BM7300 第７星层 炼狱（喽啰战用）\x01",                    # 13
            "BM7301 第７星层 炼狱（BOSS战用）\x01",                    # 14
            "BM7302 第７星层（深渊）（喽啰战用）\x01",                 # 15
            "BM7303 第７星层（深渊）（中BOSS战用）\x01",               # 16
            "BM7304 第７星层（深渊）（最深部BOSS战用）\x01",           # 17
            "BM7400 第８星层 幻影之城中枢（喽啰战用）\x01",            # 18
            "BM7401 第８星层 幻影之城中枢（中BOSS战用）\x01",          # 19
            "BM7402 第８星层 幻影之城中枢（雷那莫吉战用）\x01",        # 20
            "BM7403 第８星层 幻影之城中枢（最后BOSS战用 ）\x01",       # 21
            "取消\x01",                                                # 22
        )
    )

    Jump("loc_13C9")

    label("loc_13C9")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_142D"),
        (1, "loc_143D"),
        (2, "loc_144D"),
        (3, "loc_145D"),
        (4, "loc_146D"),
        (5, "loc_147D"),
        (6, "loc_148D"),
        (7, "loc_149D"),
        (8, "loc_14AD"),
        (9, "loc_14BD"),
        (10, "loc_14CD"),
        (11, "loc_14DD"),
        (12, "loc_14ED"),
        (13, "loc_14FD"),
        (14, "loc_150D"),
        (15, "loc_151D"),
        (16, "loc_152D"),
        (17, "loc_153D"),
        (18, "loc_154D"),
        (19, "loc_155D"),
        (20, "loc_156D"),
        (21, "loc_157D"),
        (SWITCH_DEFAULT, "loc_158D"),
    )


    label("loc_142D")

    Battle(0xABE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_143D")

    Battle(0xABF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_144D")

    Battle(0xAC0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_145D")

    Battle(0xAC1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_146D")

    Battle(0xAC2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_147D")

    Battle(0xAC3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_148D")

    Battle(0xAC4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_149D")

    Battle(0xAC5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_14AD")

    Battle(0xAC6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_14BD")

    Battle(0xAC7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_14CD")

    Battle(0xAC8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_14DD")

    Battle(0xAC9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_14ED")

    Battle(0xACA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_14FD")

    Battle(0xAD2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_150D")

    Battle(0xAD3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_151D")

    Battle(0xAD4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_152D")

    Battle(0xAD5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_153D")

    Battle(0xAD6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_154D")

    Battle(0xAD7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_155D")

    Battle(0xAD8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_156D")

    Battle(0xAD9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_157D")

    Battle(0xADA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1597")

    label("loc_158D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1597")

    Jump("Function_10_103C")

    label("loc_159A")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_103C end

    def Function_11_15A8(): pass

    label("Function_11_15A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_172B")

    AnonymousTalk(    #9
        "\x06请选择\x02",
    )

    Jump("loc_15CA")

    label("loc_15CA")


    Menu(
        2,
        10,
        80,
        1,
        (
            "BP9000 章节房屋·月\x01",                  # 0
            "BP9001 章节房屋·星\x01",                  # 1
            "BP9002 章节房屋·太阳\x01",                # 2
            "BE1110 露西塔尼亚号　走廊\x01",            # 3
            "BE1111 露西塔尼亚号　踢撞娃澳侔\x01",      # 4
            "BE1100 露西塔尼亚号　外部\x01",            # 5
            "BE0820 荒野(天空地图)\x01",                # 6
            "取消\x01",                                 # 7
        )
    )

    Jump("loc_1686")

    label("loc_1686")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16AE"),
        (1, "loc_16BE"),
        (2, "loc_16CE"),
        (3, "loc_16DE"),
        (4, "loc_16EE"),
        (5, "loc_16FE"),
        (6, "loc_170E"),
        (SWITCH_DEFAULT, "loc_171E"),
    )


    label("loc_16AE")

    Battle(0xADC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1728")

    label("loc_16BE")

    Battle(0xADD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1728")

    label("loc_16CE")

    Battle(0xADE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1728")

    label("loc_16DE")

    Battle(0xADF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1728")

    label("loc_16EE")

    Battle(0xAE0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1728")

    label("loc_16FE")

    Battle(0xAE1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1728")

    label("loc_170E")

    Battle(0xAE2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1728")

    label("loc_171E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1728")

    Jump("Function_11_15A8")

    label("loc_172B")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_15A8 end

    def Function_12_1739(): pass

    label("Function_12_1739")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1743")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_188D")

    AnonymousTalk(    #10
        "\x06请选择\x02",
    )

    Jump("loc_1765")

    label("loc_1765")


    Menu(
        2,
        10,
        100,
        1,
        (
            "布卢布兰\x01",      # 0
            "瓦鲁特\x01",        # 1
            "露茜奥拉\x01",      # 2
            "怀斯曼\x01",        # 3
            "卡西乌斯\x01",      # 4
            "雾香\x01",          # 5
            "菲利普\x01",        # 6
        )
    )

    Jump("loc_17E8")

    label("loc_17E8")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1810"),
        (1, "loc_1820"),
        (2, "loc_1830"),
        (3, "loc_1840"),
        (4, "loc_1850"),
        (5, "loc_1860"),
        (6, "loc_1870"),
        (SWITCH_DEFAULT, "loc_1880"),
    )


    label("loc_1810")

    Battle(0x802, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_188A")

    label("loc_1820")

    Battle(0x803, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_188A")

    label("loc_1830")

    Battle(0x804, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_188A")

    label("loc_1840")

    Battle(0x807, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_188A")

    label("loc_1850")

    Battle(0x808, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_188A")

    label("loc_1860")

    Battle(0x809, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_188A")

    label("loc_1870")

    Battle(0x80A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_188A")

    label("loc_1880")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_188A")

    Jump("loc_1743")

    label("loc_188D")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_1739 end

    def Function_13_189B(): pass

    label("Function_13_189B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B00")

    AnonymousTalk(    #11
        "\x06请选择\x02",
    )

    Jump("loc_18C7")

    label("loc_18C7")


    Menu(
        2,
        10,
        100,
        1,
        (
            "幻想乐曲Ⅱ骑兵之王\x01",                # 0
            "风暴袭击者\x01",                        # 1
            "幻想乐曲·德尔基昂\x01",                # 2
            "雷格纳特\x01",                          # 3
            "奥尔杰尤\x01",                          # 4
            "外传洛斯托尔姆\x01",                    # 5
            "外传亚斯塔提\x01",                      # 6
            "外传最终BOSS\x01",                      # 7
            "外传最后BOSS（登场及荬胜?）\x01",       # 8
            "最后BOSS战队伍设置(魔法以外)\x01",      # 9
        )
    )

    Jump("loc_198D")

    label("loc_198D")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_19C1"),
        (1, "loc_19D1"),
        (2, "loc_19E1"),
        (3, "loc_19F1"),
        (4, "loc_1A01"),
        (5, "loc_1A11"),
        (6, "loc_1A21"),
        (7, "loc_1A31"),
        (8, "loc_1A41"),
        (9, "loc_1A56"),
        (SWITCH_DEFAULT, "loc_1AF3"),
    )


    label("loc_19C1")

    Battle(0x335, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFD")

    label("loc_19D1")

    Battle(0xE11, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFD")

    label("loc_19E1")

    Battle(0xE15, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFD")

    label("loc_19F1")

    Battle(0x336, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFD")

    label("loc_1A01")

    Battle(0xE13, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFD")

    label("loc_1A11")

    Battle(0xF9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFD")

    label("loc_1A21")

    Battle(0x1A6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFD")

    label("loc_1A31")

    Battle(0xE16, 0x300001, 0x0, 0x0, 0xFF)
    Jump("loc_1AFD")

    label("loc_1A41")

    Battle(0xE16, 0x0, 0x0, 0x0, 0xFF)
    Sleep(1000)
    Jump("loc_1AFD")

    label("loc_1A56")

    OP_DC(0x1, 0x0, 0x8)
    OP_DC(0x1, 0x0, 0xE)
    OP_DC(0x1, 0x0, 0x5)
    OP_DC(0x1, 0x0, 0x4)
    OP_DC(0x0, 0x0)
    OP_31(0x8, 0x0, 0x88)
    OP_31(0xE, 0x0, 0x88)
    OP_31(0x5, 0x0, 0x88)
    OP_31(0x4, 0x0, 0x88)
    OP_35(0x8, 0x0)
    OP_35(0xE, 0x0)
    OP_35(0x5, 0x0)
    OP_35(0x4, 0x0)
    OP_41(0x8, 0x55B, 0xFF)
    OP_41(0x8, 0x618, 0xFF)
    OP_41(0x8, 0x6E, 0xFF)
    OP_41(0xE, 0x5B5, 0xFF)
    OP_41(0xE, 0x618, 0xFF)
    OP_41(0xE, 0x6E, 0xFF)
    OP_41(0x5, 0x4D3, 0xFF)
    OP_41(0x5, 0x618, 0xFF)
    OP_41(0x5, 0x6E, 0xFF)
    OP_41(0x4, 0x4A7, 0xFF)
    OP_41(0x4, 0x618, 0xFF)
    OP_41(0x4, 0x6E, 0xFF)
    OP_37(0x8, 0x7F, 0x3)
    OP_37(0xE, 0x7F, 0x3)
    OP_37(0x5, 0x7F, 0x3)
    OP_37(0x4, 0x7F, 0x3)
    OP_31(0x8, 0x5, 0x96)
    OP_31(0xE, 0x5, 0x96)
    OP_31(0x5, 0x5, 0x96)
    OP_31(0x4, 0x5, 0x96)
    OP_DB(0x2, 0xFF)
    Jump("loc_1AFD")

    label("loc_1AF3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AFD")

    Jump("loc_18A5")

    label("loc_1B00")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_189B end

    def Function_14_1B0E(): pass

    label("Function_14_1B0E")

    Return()

    # Function_14_1B0E end

    def Function_15_1B0F(): pass

    label("Function_15_1B0F")

    Return()

    # Function_15_1B0F end

    def Function_16_1B10(): pass

    label("Function_16_1B10")

    Return()

    # Function_16_1B10 end

    def Function_17_1B11(): pass

    label("Function_17_1B11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_201E")

    AnonymousTalk(    #12
        (
            "\x06这个跳转是Debug用的。\x01",
            "如果需要确认游戏中的迷你游戏，\x01",
            "请从项目『章节』中选择。\x02",
        )
    )


    Menu(
        1,
        10,
        100,
        1,
        (
            "迷你游戏00游乐台\x01",            # 0
            "迷你游戏01游戏机\x01",            # 1
            "迷你游戏02 21点\x01",             # 2
            "迷你游戏03钓鱼\x01",              # 3
            "迷你游戏04纸牌\x01",              # 4
            "迷你游戏05射击\x01",              # 5
            "迷你游戏06捉虫\x01",              # 6
            "迷你游戏07双六\x01",              # 7
            "迷你游戏08问答\x01",              # 8
            "迷你游戏09钓鱼·改\x01",          # 9
            "迷你游戏10扑克·改\x01",          # 10
            "迷你游戏11二十一点·改\x01",      # 11
        )
    )

    MenuEnd(0x0)
    OP_5F(0xFF)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C84"),
        (1, "loc_1CBD"),
        (2, "loc_1CF6"),
        (3, "loc_1D2F"),
        (4, "loc_1DEA"),
        (5, "loc_1E23"),
        (6, "loc_1EE8"),
        (7, "loc_1F21"),
        (8, "loc_1F63"),
        (9, "loc_1F77"),
        (10, "loc_1F9F"),
        (11, "loc_1FD8"),
        (SWITCH_DEFAULT, "loc_2011"),
    )


    label("loc_1C84")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_2011")

    label("loc_1CBD")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0xC, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_2011")

    label("loc_1CF6")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0xD, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_2011")

    label("loc_1D2F")

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

    AnonymousTalk(    #13
        (
            "因为移动到布莱特家，\x01",
            "请寻找后面池子的钓鱼点\x01",
            "开始钓鱼。\x02",
        )
    )

    CloseMessageWindow()
    NewScene("ED6_DT21/T0300   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2011")

    label("loc_1DEA")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0xF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_2011")

    label("loc_1E23")


    Menu(
        1,
        10,
        100,
        1,
        (
            "喽罗战\x01",      # 0
            "BOSS战\x01",      # 1
        )
    )

    Jump("loc_1E46")

    label("loc_1E46")

    MenuEnd(0x0)
    OP_5F(0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E9A")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E3(0x0, 0x1, 1024, 0x0)
    OP_C0(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_1EE5")

    label("loc_1E9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EE5")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E3(0x0, 0x1, 1024, 0x0)
    OP_C0(0x11, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)

    label("loc_1EE5")

    Jump("loc_2011")

    label("loc_1EE8")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_2011")

    label("loc_1F21")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0x19, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    NewScene("ED6_DT21/T0001   ._SN", 0, 0, 0)
    IdleLoop()
    FadeToBright(300, 0)
    Jump("loc_2011")

    label("loc_1F63")

    OP_E3(0x0, 0xA, 0, 0x0)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2011")

    label("loc_1F77")

    OP_D6(0x0)
    OP_E3(0x0, 0xC, 1, 0x0)
    ClearParty()
    AddParty(0x0, 0xEE, 0xFF)
    OP_28(0x1C, 0x4, 0x20)
    OP_28(0x1D, 0x4, 0x20)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2011")

    label("loc_1F9F")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0x1C, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_2011")

    label("loc_1FD8")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_C0(0x1D, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    Jump("loc_2011")

    label("loc_2011")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("Function_17_1B11")

    label("loc_201E")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_1B11 end

    SaveToFile()

Try(main)
