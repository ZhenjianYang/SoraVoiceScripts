from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 调试地图

    CreateScenaFile(
        FileName            = 'T0001_3 ._SN',
        MapName             = 'map',
        Location            = 'T0001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0001   ._SN',
            'ED6_DT21/T0001_1 ._SN',
            'ED6_DT21/T0001_2 ._SN',
            'ED6_DT21/T0001_3 ._SN',
            'ED6_DT21/T0001_4 ._SN',
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
        "Function_1_113",          # 01, 1
        "Function_2_32E",          # 02, 2
        "Function_3_513",          # 03, 3
        "Function_4_57C",          # 04, 4
        "Function_5_93E",          # 05, 5
        "Function_6_B90",          # 06, 6
        "Function_7_CAA",          # 07, 7
        "Function_8_11DD",         # 08, 8
        "Function_9_1781",         # 09, 9
        "Function_10_1E4B",        # 0A, 10
        "Function_11_2456",        # 0B, 11
        "Function_12_2B4A",        # 0C, 12
        "Function_13_38FC",        # 0D, 13
        "Function_14_3DDA",        # 0E, 14
    )


    def Function_0_AA(): pass

    label("Function_0_AA")


    AnonymousTalk(    #0
        "\x06哪个？\x02",
    )


    label("loc_B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_103")

    Menu(
        1,
        10,
        32,
        1,
        (
            "后篇\x01",      # 0
            "前篇\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E8"),
        (1, "loc_EF"),
        (SWITCH_DEFAULT, "loc_F6"),
    )


    label("loc_E8")

    Call(3, 1)
    Jump("loc_100")

    label("loc_EF")

    Call(3, 2)
    Jump("loc_100")

    label("loc_F6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_100")

    Jump("loc_B4")

    label("loc_103")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_AA end

    def Function_1_113(): pass

    label("Function_1_113")


    AnonymousTalk(    #1
        "\x06哪个？\x02",
    )


    label("loc_11D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31E")

    Menu(
        2,
        10,
        100,
        1,
        (
            "A0020 队伍与专用ＮＰＬ\x01",                                  # 0
            "A0021战斗艾丝蒂尔 约修亚 金 阿加特 奥利维尔\x01",             # 1
            "A0022 战斗雪拉、提妲、科洛丝、科洛丝礼服\x01",                # 2
            "A0023 战斗凯文，亚尼拉丝，乔丝特，克鲁茨\x01",                # 3
            "A0024 战斗尤莉亚，穆拉，基德，凯诺娜\x01",                    # 4
            "A0025 战斗瓦鲁特，玲，露茜奥拉，布卢布兰\x01",                # 5
            "A0026 战斗莱恩哈特，怀斯曼，猎兵约修亚、乌猫蝶\x01",          # 6
            "A0027 战斗猎兵Ａ，猎兵Ｂ，克鲁茨，卡露娜，基尔巴特\x01",      # 7
            "A0039 后篇座位一览\x01",                                      # 8
            "取消\x01",                                                    # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C0"),
        (1, "loc_2C9"),
        (2, "loc_2D2"),
        (3, "loc_2DB"),
        (4, "loc_2E4"),
        (5, "loc_2ED"),
        (6, "loc_2F6"),
        (7, "loc_2FF"),
        (8, "loc_308"),
        (SWITCH_DEFAULT, "loc_311"),
    )


    label("loc_2C0")

    NewScene("ED6_DT21/A0020   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_2C9")

    NewScene("ED6_DT21/A0021   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_2D2")

    NewScene("ED6_DT21/A0022   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_2DB")

    NewScene("ED6_DT21/A0023   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_2E4")

    NewScene("ED6_DT21/A0024   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_2ED")

    NewScene("ED6_DT21/A0025   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_2F6")

    NewScene("ED6_DT21/A0026   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_2FF")

    NewScene("ED6_DT21/A0027   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_308")

    NewScene("ED6_DT21/A0039   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_311")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11D")

    label("loc_31E")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_113 end

    def Function_2_32E(): pass

    label("Function_2_32E")


    AnonymousTalk(    #2
        "\x06哪个？\x02",
    )


    label("loc_338")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_503")

    Menu(
        2,
        10,
        100,
        1,
        (
            "30泛用ＮＰＬ\x01",                                                 # 0
            "31队伍与专用ＮＰＬ\x01",                                           # 1
            "32泛用ＮＰＬ与专用ＮＰＬ２＿ＡＰＬ\x01",                           # 2
            "33PT战斗艾丝蒂尔，约修亚、金、阿加特、奥利维尔\x01",               # 3
            "34PT战斗约修亚、雪拉扎德、提妲、科洛丝\x01",                       # 4
            "35NPC战斗男女游击士、小流氓、空贼们\x01",                          # 5
            "36NPC战斗小流氓团伙、男女游击士２\x01",                            # 6
            "37NPC战斗王国兵士、士官、特务兵、洛伦斯、理查德、凯诺娜\x01",      # 7
            "39座位角色\x01",                                                   # 8
            "取消\x01",                                                         # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4A5"),
        (1, "loc_4AE"),
        (2, "loc_4B7"),
        (3, "loc_4C0"),
        (4, "loc_4C9"),
        (5, "loc_4D2"),
        (6, "loc_4DB"),
        (7, "loc_4E4"),
        (8, "loc_4ED"),
        (SWITCH_DEFAULT, "loc_4F6"),
    )


    label("loc_4A5")

    NewScene("ED6_DT21/T0030   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_4AE")

    NewScene("ED6_DT21/T0031   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_4B7")

    NewScene("ED6_DT21/T0032   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_4C0")

    NewScene("ED6_DT21/T0033   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_4C9")

    NewScene("ED6_DT21/T0034   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_4D2")

    NewScene("ED6_DT21/T0035   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_4DB")

    NewScene("ED6_DT21/T0036   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_4E4")

    NewScene("ED6_DT21/T0037   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_4ED")

    NewScene("ED6_DT21/T0039   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_4F6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_338")

    label("loc_503")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_32E end

    def Function_3_513(): pass

    label("Function_3_513")


    AnonymousTalk(    #3
        "\x06哪个？\x02",
    )


    label("loc_51D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56C")

    Menu(
        1,
        10,
        32,
        1,
        (
            "后篇\x01",      # 0
            "前篇\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_551"),
        (1, "loc_558"),
        (SWITCH_DEFAULT, "loc_55F"),
    )


    label("loc_551")

    Call(3, 5)
    Jump("loc_569")

    label("loc_558")

    Call(3, 4)
    Jump("loc_569")

    label("loc_55F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_569")

    Jump("loc_51D")

    label("loc_56C")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_513 end

    def Function_4_57C(): pass

    label("Function_4_57C")


    AnonymousTalk(    #4
        "\x06哪个？\x02",
    )


    label("loc_586")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_92E")

    Menu(
        2,
        10,
        32,
        1,
        (
            "40魔兽列表（10000-10290）\x01",      # 0
            "41魔兽列表（10300-10590）\x01",      # 1
            "42魔兽列表（10600-10890）\x01",      # 2
            "57魔兽列表（10900-11040）\x01",      # 3
            "60魔兽列表（11050-11190）\x01",      # 4
            "43魔兽动作（10000-10050）\x01",      # 5
            "44魔兽动作（10060-10140）\x01",      # 6
            "45魔兽动作（10150-10210）\x01",      # 7
            "46魔兽动作（10220-10290）\x01",      # 8
            "47魔兽动作（10300-10380）\x01",      # 9
            "48魔兽动作（10390-10450）\x01",      # 10
            "49魔兽动作（10460-10530）\x01",      # 11
            "50魔兽动作（10540-10610）\x01",      # 12
            "51魔兽动作（10620-10690）\x01",      # 13
            "52魔兽动作（10700-10770）\x01",      # 14
            "53魔兽动作（10780-10850）\x01",      # 15
            "54魔兽动作（10860-10900）\x01",      # 16
            "55魔兽动作（10910-10940）\x01",      # 17
            "56魔兽动作（10950-10990）\x01",      # 18
            "58魔兽动作（11000-11060）\x01",      # 19
            "59魔兽动作（11070-11110）\x01",      # 20
            "61魔兽动作（11120-11150）\x01",      # 21
            "62魔兽动作（11160-11190）\x01",      # 22
            "取消\x01",                           # 23
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_85B"),
        (1, "loc_864"),
        (2, "loc_86D"),
        (3, "loc_876"),
        (4, "loc_87F"),
        (5, "loc_888"),
        (6, "loc_891"),
        (7, "loc_89A"),
        (8, "loc_8A3"),
        (9, "loc_8AC"),
        (10, "loc_8B5"),
        (11, "loc_8BE"),
        (12, "loc_8C7"),
        (13, "loc_8D0"),
        (14, "loc_8D9"),
        (15, "loc_8E2"),
        (16, "loc_8EB"),
        (17, "loc_8F4"),
        (18, "loc_8FD"),
        (19, "loc_906"),
        (20, "loc_90F"),
        (21, "loc_918"),
        (SWITCH_DEFAULT, "loc_921"),
    )


    label("loc_85B")

    NewScene("ED6_DT21/T0040   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_864")

    NewScene("ED6_DT21/T0041   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_86D")

    NewScene("ED6_DT21/T0042   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_876")

    NewScene("ED6_DT21/T0057   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_87F")

    NewScene("ED6_DT21/T0060   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_888")

    NewScene("ED6_DT21/T0043   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_891")

    NewScene("ED6_DT21/T0044   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_89A")

    NewScene("ED6_DT21/T0045   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_8A3")

    NewScene("ED6_DT21/T0046   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_8AC")

    NewScene("ED6_DT21/T0047   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_8B5")

    NewScene("ED6_DT21/T0048   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_8BE")

    NewScene("ED6_DT21/T0049   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_8C7")

    NewScene("ED6_DT21/T0050   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_8D0")

    NewScene("ED6_DT21/T0051   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_8D9")

    NewScene("ED6_DT21/T0052   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_8E2")

    NewScene("ED6_DT21/T0053   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_8EB")

    NewScene("ED6_DT21/T0054   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_8F4")

    NewScene("ED6_DT21/T0055   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_8FD")

    NewScene("ED6_DT21/T0056   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_906")

    NewScene("ED6_DT21/T0058   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_90F")

    NewScene("ED6_DT21/T0059   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_918")

    NewScene("ED6_DT21/T0061   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_921")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_586")

    label("loc_92E")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_57C end

    def Function_5_93E(): pass

    label("Function_5_93E")


    AnonymousTalk(    #5
        "\x06哪个？\x02",
    )


    label("loc_948")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B80")

    Menu(
        2,
        10,
        32,
        1,
        (
            "A0000 魔兽列表（12000-12040）\x01",      # 0
            "A0001 魔兽列表（12050-12090）\x01",      # 1
            "A0002 魔兽列表（12100-12140）\x01",      # 2
            "A0003 魔兽列表（12150-12190）\x01",      # 3
            "A0004 魔兽列表（12200-12240）\x01",      # 4
            "A0005 魔兽列表（12250-12290）\x01",      # 5
            "A0006 魔兽列表（12300-12340）\x01",      # 6
            "A0007 魔兽列表（12350-12390）\x01",      # 7
            "A0008 魔兽列表（12400-12440）\x01",      # 8
            "A0009 魔兽列表（12450-12490）\x01",      # 9
            "A0010 魔兽列表（12500-12520）\x01",      # 10
            "A0011 魔兽列表（12530-12540）\x01",      # 11
            "取消\x01",                               # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B07"),
        (1, "loc_B10"),
        (2, "loc_B19"),
        (3, "loc_B22"),
        (4, "loc_B2B"),
        (5, "loc_B34"),
        (6, "loc_B3D"),
        (7, "loc_B46"),
        (8, "loc_B4F"),
        (9, "loc_B58"),
        (10, "loc_B61"),
        (11, "loc_B6A"),
        (SWITCH_DEFAULT, "loc_B73"),
    )


    label("loc_B07")

    NewScene("ED6_DT21/A0000   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B10")

    NewScene("ED6_DT21/A0001   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B19")

    NewScene("ED6_DT21/A0002   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B22")

    NewScene("ED6_DT21/A0003   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B2B")

    NewScene("ED6_DT21/A0004   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B34")

    NewScene("ED6_DT21/A0005   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B3D")

    NewScene("ED6_DT21/A0006   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B46")

    NewScene("ED6_DT21/A0007   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B4F")

    NewScene("ED6_DT21/A0008   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B58")

    NewScene("ED6_DT21/A0009   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B61")

    NewScene("ED6_DT21/A0010   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B6A")

    NewScene("ED6_DT21/A0011   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B73")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_948")

    label("loc_B80")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_93E end

    def Function_6_B90(): pass

    label("Function_6_B90")


    AnonymousTalk(    #6
        "\x06这是地图。请选择。\x02",
    )


    label("loc_BA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9A")

    Menu(
        1,
        10,
        100,
        1,
        (
            "洛连特地区\x01",                            # 0
            "柏斯地区\x01",                              # 1
            "卢安地区\x01",                              # 2
            "蔡斯地区\x01",                              # 3
            "格兰赛尔地区\x01",                          # 4
            "辉之环、训练所、古罗力亚斯内部等\x01",      # 5
            "事件，飞船\x01",                            # 6
            "看动画。\x01",                              # 7
            "取消\x01",                                  # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C55"),
        (1, "loc_C5C"),
        (2, "loc_C63"),
        (3, "loc_C6A"),
        (4, "loc_C71"),
        (5, "loc_C78"),
        (6, "loc_C7F"),
        (7, "loc_C86"),
        (SWITCH_DEFAULT, "loc_C8D"),
    )


    label("loc_C55")

    Call(3, 7)
    Jump("loc_C97")

    label("loc_C5C")

    Call(3, 8)
    Jump("loc_C97")

    label("loc_C63")

    Call(3, 9)
    Jump("loc_C97")

    label("loc_C6A")

    Call(3, 10)
    Jump("loc_C97")

    label("loc_C71")

    Call(3, 11)
    Jump("loc_C97")

    label("loc_C78")

    Call(3, 12)
    Jump("loc_C97")

    label("loc_C7F")

    Call(3, 13)
    Jump("loc_C97")

    label("loc_C86")

    Call(3, 14)
    Jump("loc_C97")

    label("loc_C8D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C97")

    Jump("loc_BA6")

    label("loc_C9A")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_B90 end

    def Function_7_CAA(): pass

    label("Function_7_CAA")


    AnonymousTalk(    #7
        "\x06哪里？\x02",
    )


    label("loc_CB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11CD")

    Menu(
        2,
        10,
        100,
        1,
        (
            "城里\x01",      # 0
            "迷宫\x01",      # 1
            "大道\x01",      # 2
            "夜\x01",        # 3
            "取消\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CFD"),
        (1, "loc_E4C"),
        (2, "loc_10DA"),
        (3, "loc_1179"),
        (SWITCH_DEFAULT, "loc_11C0"),
    )


    label("loc_CFD")


    AnonymousTalk(    #8
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "洛连特\x01",                  # 0
            "市长邸\x01",                  # 1
            "布莱特家\x01",                # 2
            "帕赛尔农场\x01",              # 3
            "帕赛尔农场（夜晚）\x01",      # 4
            "威尔特关所\x01",              # 5
            "飞船坪\x01",                  # 6
            "布莱特家\x01",                # 7
            "格鲁纳门\x01",                # 8
            "洛连特（夜晚）\x01",          # 9
            "市长邸（夜晚）\x01",          # 10
            "飞船坪（夜晚）\x01",          # 11
            "取消\x01",                    # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DD7"),
        (1, "loc_DE0"),
        (2, "loc_DE9"),
        (3, "loc_DF2"),
        (4, "loc_DFB"),
        (5, "loc_E04"),
        (6, "loc_E0D"),
        (7, "loc_E16"),
        (8, "loc_E1F"),
        (9, "loc_E28"),
        (10, "loc_E31"),
        (11, "loc_E3A"),
        (SWITCH_DEFAULT, "loc_E43"),
    )


    label("loc_DD7")

    NewScene("ED6_DT21/T0100   ._SN", 119, 0, 0)
    IdleLoop()

    label("loc_DE0")

    NewScene("ED6_DT21/T0200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_DE9")

    NewScene("ED6_DT21/T0300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_DF2")

    NewScene("ED6_DT21/T0400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_DFB")

    NewScene("ED6_DT21/T0401   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_E04")

    NewScene("ED6_DT21/T0500   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_E0D")

    NewScene("ED6_DT21/T0700   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_E16")

    NewScene("ED6_DT21/T0300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_E1F")

    NewScene("ED6_DT21/T0600   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_E28")

    NewScene("ED6_DT21/T0101   ._SN", 119, 0, 0)
    IdleLoop()

    label("loc_E31")

    NewScene("ED6_DT21/T0201   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_E3A")

    NewScene("ED6_DT21/T0701   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_E43")

    OP_5F(0x3)
    Jump("loc_E49")

    label("loc_E49")

    Jump("loc_11CA")

    label("loc_E4C")


    AnonymousTalk(    #9
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "玛鲁加矿山（前篇）\x01",                                 # 0
            "玛鲁加矿山（后篇８章任务用）\x01",                       # 1
            "神秘森林\x01",                                           # 2
            "神秘森林圈\x01",                                         # 3
            "地下水路\x01",                                           # 4
            "翡翠之塔1F（前半）\x01",                                 # 5
            "翡翠之塔2F（前半）\x01",                                 # 6
            "翡翠之塔3F（前半）\x01",                                 # 7
            "翡翠之塔4F（前半）\x01",                                 # 8
            "翡翠之塔5F（前半）\x01",                                 # 9
            "翡翠之塔1F（后半）\x01",                                 # 10
            "翡翠之塔2F（后半）\x01",                                 # 11
            "翡翠之塔3F（后半）\x01",                                 # 12
            "翡翠之塔4F（后半）\x01",                                 # 13
            "翡翠之塔5F（后半）\x01",                                 # 14
            "翡翠之塔屋顶（后半 异次元背景）\x01",                    # 15
            "翡翠之塔屋顶（后半 异次元背景，埃尔赛尤视点）\x01",      # 16
            "翡翠之塔屋顶（后半 一般背景）\x01",                      # 17
            "取消\x01",                                               # 18
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_102F"),
        (1, "loc_1038"),
        (2, "loc_1041"),
        (3, "loc_104A"),
        (4, "loc_1053"),
        (5, "loc_105C"),
        (6, "loc_1065"),
        (7, "loc_106E"),
        (8, "loc_1077"),
        (9, "loc_1080"),
        (10, "loc_1089"),
        (11, "loc_1092"),
        (12, "loc_109B"),
        (13, "loc_10A4"),
        (14, "loc_10AD"),
        (15, "loc_10B6"),
        (16, "loc_10BF"),
        (17, "loc_10C8"),
        (SWITCH_DEFAULT, "loc_10D1"),
    )


    label("loc_102F")

    NewScene("ED6_DT21/C0100   ._SN", 103, 0, 0)
    IdleLoop()

    label("loc_1038")

    NewScene("ED6_DT21/C0101   ._SN", 103, 0, 0)
    IdleLoop()

    label("loc_1041")

    NewScene("ED6_DT21/C0300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_104A")

    NewScene("ED6_DT21/C0304   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1053")

    NewScene("ED6_DT21/C0500   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_105C")

    NewScene("ED6_DT21/C0411   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1065")

    NewScene("ED6_DT21/C0412   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_106E")

    NewScene("ED6_DT21/C0413   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1077")

    NewScene("ED6_DT21/C0414   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1080")

    NewScene("ED6_DT21/C0415   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1089")

    NewScene("ED6_DT21/C0700   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1092")

    NewScene("ED6_DT21/C0701   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_109B")

    NewScene("ED6_DT21/C0702   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_10A4")

    NewScene("ED6_DT21/C0703   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_10AD")

    NewScene("ED6_DT21/C0704   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_10B6")

    NewScene("ED6_DT21/C0705   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_10BF")

    NewScene("ED6_DT21/C0706   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_10C8")

    NewScene("ED6_DT21/C0707   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_10D1")

    OP_5F(0x3)
    Jump("loc_10D7")

    label("loc_10D7")

    Jump("loc_11CA")

    label("loc_10DA")


    AnonymousTalk(    #10
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "艾利兹街道\x01",            # 0
            "米尔西街道\x01",            # 1
            "玛鲁加山道\x01",            # 2
            "米尔西街道军用艇\x01",      # 3
            "取消\x01",                  # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1140"),
        (1, "loc_114C"),
        (2, "loc_1158"),
        (3, "loc_1164"),
        (SWITCH_DEFAULT, "loc_1170"),
    )


    label("loc_1140")

    NewScene("ED6_DT21/R0100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1176")

    label("loc_114C")

    NewScene("ED6_DT21/R0200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1176")

    label("loc_1158")

    NewScene("ED6_DT21/R0300   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1176")

    label("loc_1164")

    NewScene("ED6_DT21/R0203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1176")

    label("loc_1170")

    OP_5F(0x3)
    Jump("loc_1176")

    label("loc_1176")

    Jump("loc_11CA")

    label("loc_1179")


    AnonymousTalk(    #11
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        "布莱特家·外观\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11AB"),
        (SWITCH_DEFAULT, "loc_11B7"),
    )


    label("loc_11AB")

    NewScene("ED6_DT21/T0311   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_11BD")

    label("loc_11B7")

    OP_5F(0x3)
    Jump("loc_11BD")

    label("loc_11BD")

    Jump("loc_11CA")

    label("loc_11C0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11CA")

    Jump("loc_CB4")

    label("loc_11CD")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_CAA end

    def Function_8_11DD(): pass

    label("Function_8_11DD")


    AnonymousTalk(    #12
        "\x06哪里？\x02",
    )


    label("loc_11E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1771")

    Menu(
        2,
        10,
        100,
        1,
        (
            "城里\x01",      # 0
            "迷宫\x01",      # 1
            "大道\x01",      # 2
            "夜\x01",        # 3
            "取消\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1230"),
        (1, "loc_137D"),
        (2, "loc_15DD"),
        (3, "loc_16B8"),
        (SWITCH_DEFAULT, "loc_1761"),
    )


    label("loc_1230")


    AnonymousTalk(    #13
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "柏斯城，南门\x01",            # 0
            "柏斯城，民房\x01",            # 1
            "古罗尼关所\x01",              # 2
            "古罗尼关所（夜晚）\x01",      # 3
            "柏斯国际空港\x01",            # 4
            "拉文努村\x01",                # 5
            "拉文努村（夜晚）\x01",        # 6
            "哈肯大门\x01",                # 7
            "哈肯大门北部平原\x01",        # 8
            "湖畔旅馆\x01",                # 9
            "柏斯城北，破坏\x01",          # 10
            "取消\x01",                    # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1311"),
        (1, "loc_131A"),
        (2, "loc_1323"),
        (3, "loc_132C"),
        (4, "loc_1335"),
        (5, "loc_133E"),
        (6, "loc_1347"),
        (7, "loc_1350"),
        (8, "loc_1359"),
        (9, "loc_1362"),
        (10, "loc_136B"),
        (SWITCH_DEFAULT, "loc_1374"),
    )


    label("loc_1311")

    NewScene("ED6_DT21/T1100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_131A")

    NewScene("ED6_DT21/T1110   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1323")

    NewScene("ED6_DT21/T1300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_132C")

    NewScene("ED6_DT21/T1301   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1335")

    NewScene("ED6_DT21/T1102   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_133E")

    NewScene("ED6_DT21/T1200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1347")

    NewScene("ED6_DT21/T1211   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1350")

    NewScene("ED6_DT21/T1400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1359")

    NewScene("ED6_DT21/T1402   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1362")

    NewScene("ED6_DT21/T1500   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_136B")

    NewScene("ED6_DT21/T1103   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1374")

    OP_5F(0x3)
    Jump("loc_137A")

    label("loc_137A")

    Jump("loc_176E")

    label("loc_137D")


    AnonymousTalk(    #14
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "迷雾峡谷\x01",                                           # 0
            "拉文努废坑后篇\x01",                                     # 1
            "空贼城寨\x01",                                           # 2
            "古龙的住处\x01",                                         # 3
            "琥珀之塔1F（前半）\x01",                                 # 4
            "琥珀之塔2F（前半）\x01",                                 # 5
            "琥珀之塔3F（前半）\x01",                                 # 6
            "琥珀之塔4F（前半）\x01",                                 # 7
            "琥珀之塔5F（前半）\x01",                                 # 8
            "琥珀之塔1F（后半）\x01",                                 # 9
            "琥珀之塔2F（后半）\x01",                                 # 10
            "琥珀之塔3F（后半）\x01",                                 # 11
            "琥珀之塔4F（后半）\x01",                                 # 12
            "琥珀之塔5F（后半）\x01",                                 # 13
            "琥珀之塔屋顶（后半 异次元背景）\x01",                    # 14
            "琥珀之塔屋顶（后半 异次元背景，埃尔赛尤视点）\x01",      # 15
            "琥珀之塔屋顶（后半 一般背景）\x01",                      # 16
            "取消\x01",                                               # 17
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_153B"),
        (1, "loc_1544"),
        (2, "loc_154D"),
        (3, "loc_1556"),
        (4, "loc_155F"),
        (5, "loc_1568"),
        (6, "loc_1571"),
        (7, "loc_157A"),
        (8, "loc_1583"),
        (9, "loc_158C"),
        (10, "loc_1595"),
        (11, "loc_159E"),
        (12, "loc_15A7"),
        (13, "loc_15B0"),
        (14, "loc_15B9"),
        (15, "loc_15C2"),
        (16, "loc_15CB"),
        (SWITCH_DEFAULT, "loc_15D4"),
    )


    label("loc_153B")

    NewScene("ED6_DT21/C1400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1544")

    NewScene("ED6_DT21/C1102   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_154D")

    NewScene("ED6_DT21/C1300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1556")

    NewScene("ED6_DT21/C1600   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_155F")

    NewScene("ED6_DT21/C1211   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1568")

    NewScene("ED6_DT21/C1212   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1571")

    NewScene("ED6_DT21/C1213   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_157A")

    NewScene("ED6_DT21/C1214   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1583")

    NewScene("ED6_DT21/C1215   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_158C")

    NewScene("ED6_DT21/C1700   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1595")

    NewScene("ED6_DT21/C1701   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_159E")

    NewScene("ED6_DT21/C1702   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_15A7")

    NewScene("ED6_DT21/C1703   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_15B0")

    NewScene("ED6_DT21/C1704   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_15B9")

    NewScene("ED6_DT21/C1705   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_15C2")

    NewScene("ED6_DT21/C1706   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_15CB")

    NewScene("ED6_DT21/C1707   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_15D4")

    OP_5F(0x3)
    Jump("loc_15DA")

    label("loc_15DA")

    Jump("loc_176E")

    label("loc_15DD")


    AnonymousTalk(    #15
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "古罗尼山道\x01",              # 0
            "钢壁之路\x01",                # 1
            "东柏斯街道\x01",              # 2
            "西柏斯街道\x01",              # 3
            "安塞尔新街\x01",              # 4
            "安塞尔新街（夜晚）\x01",      # 5
            "拉文努山道\x01",              # 6
            "取消\x01",                    # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1670"),
        (1, "loc_1679"),
        (2, "loc_1682"),
        (3, "loc_168B"),
        (4, "loc_1694"),
        (5, "loc_169D"),
        (6, "loc_16A6"),
        (SWITCH_DEFAULT, "loc_16AF"),
    )


    label("loc_1670")

    NewScene("ED6_DT21/C1500   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1679")

    NewScene("ED6_DT21/R1300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1682")

    NewScene("ED6_DT21/R1100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_168B")

    NewScene("ED6_DT21/R1200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1694")

    NewScene("ED6_DT21/R1400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_169D")

    NewScene("ED6_DT21/R1403   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_16A6")

    NewScene("ED6_DT21/R1500   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_16AF")

    OP_5F(0x3)
    Jump("loc_16B5")

    label("loc_16B5")

    Jump("loc_176E")

    label("loc_16B8")


    AnonymousTalk(    #16
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "哈肯门\x01",          # 0
            "古罗尼关所\x01",      # 1
            "迷雾峡谷\x01",        # 2
            "西柏斯街道\x01",      # 3
            "拉文努废坑\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_171C"),
        (1, "loc_1728"),
        (2, "loc_1734"),
        (3, "loc_1740"),
        (4, "loc_174C"),
        (SWITCH_DEFAULT, "loc_1758"),
    )


    label("loc_171C")

    NewScene("ED6_DT21/T1401   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_175E")

    label("loc_1728")

    NewScene("ED6_DT21/T1311   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_175E")

    label("loc_1734")

    NewScene("ED6_DT21/C1402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_175E")

    label("loc_1740")

    NewScene("ED6_DT21/R1203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_175E")

    label("loc_174C")

    NewScene("ED6_DT21/C1104   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_175E")

    label("loc_1758")

    OP_5F(0x3)
    Jump("loc_175E")

    label("loc_175E")

    Jump("loc_176E")

    label("loc_1761")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_176E")

    label("loc_176E")

    Jump("loc_11E7")

    label("loc_1771")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_11DD end

    def Function_9_1781(): pass

    label("Function_9_1781")


    AnonymousTalk(    #17
        "\x06哪里？\x02",
    )


    label("loc_178B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E3B")

    Menu(
        2,
        10,
        100,
        1,
        (
            "城里\x01",      # 0
            "迷宫\x01",      # 1
            "大道\x01",      # 2
            "夜\x01",        # 3
            "其他\x01",      # 4
            "取消\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_17DD"),
        (1, "loc_1A38"),
        (2, "loc_1C8C"),
        (3, "loc_1D4B"),
        (4, "loc_1DDB"),
        (SWITCH_DEFAULT, "loc_1E2B"),
    )


    label("loc_17DD")


    AnonymousTalk(    #18
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "卢安城\x01",                          # 0
            "飞船坪\x01",                          # 1
            "市长官邸\x01",                        # 2
            "王立学院 旧校舍\x01",                 # 3
            "王立学院 本馆\x01",                   # 4
            "王立学院 本馆 上课时\x01",            # 5
            "王立学院 本馆 准备上课时\x01",        # 6
            "玛西亚孤儿院\x01",                    # 7
            "玛西亚孤儿院（火灾后）\x01",          # 8
            "玛西亚孤儿院（重建后）\x01",          # 9
            "民房\x01",                            # 10
            "店\x01",                              # 11
            "教会\x01",                            # 12
            "酒馆，娱乐场\x01",                    # 13
            "艾尔·雷登关所\x01",                  # 14
            "玛诺利亚村\x01",                      # 15
            "玛西亚孤儿院内部（火灾中）\x01",      # 16
            "王立学院 （夜晚）旧校舍\x01",         # 17
            "王立学院 （夜晚）本馆\x01",           # 18
            "卢安城（夜晚）\x01",                  # 19
            "取消\x01",                            # 20
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_197B"),
        (1, "loc_1984"),
        (2, "loc_198D"),
        (3, "loc_1996"),
        (4, "loc_199F"),
        (5, "loc_19A8"),
        (6, "loc_19B1"),
        (7, "loc_19BA"),
        (8, "loc_19C3"),
        (9, "loc_19CC"),
        (10, "loc_19D5"),
        (11, "loc_19DE"),
        (12, "loc_19E7"),
        (13, "loc_19F0"),
        (14, "loc_19F9"),
        (15, "loc_1A02"),
        (16, "loc_1A0B"),
        (17, "loc_1A14"),
        (18, "loc_1A1D"),
        (19, "loc_1A26"),
        (SWITCH_DEFAULT, "loc_1A2F"),
    )


    label("loc_197B")

    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1984")

    NewScene("ED6_DT21/T2102   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_198D")

    NewScene("ED6_DT21/T2200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1996")

    NewScene("ED6_DT21/T2600   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_199F")

    NewScene("ED6_DT21/T2510   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19A8")

    NewScene("ED6_DT21/T2520   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19B1")

    NewScene("ED6_DT21/T2530   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19BA")

    NewScene("ED6_DT21/T2400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19C3")

    NewScene("ED6_DT21/T2401   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19CC")

    NewScene("ED6_DT21/T2402   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19D5")

    NewScene("ED6_DT21/T2110   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19DE")

    NewScene("ED6_DT21/T2120   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19E7")

    NewScene("ED6_DT21/T2130   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19F0")

    NewScene("ED6_DT21/T2131   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19F9")

    NewScene("ED6_DT21/T2700   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1A02")

    NewScene("ED6_DT21/T2300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1A0B")

    NewScene("ED6_DT21/T2411   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1A14")

    NewScene("ED6_DT21/T2601   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1A1D")

    NewScene("ED6_DT21/T2810   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1A26")

    NewScene("ED6_DT21/T2105   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1A2F")

    OP_5F(0x3)
    Jump("loc_1A35")

    label("loc_1A35")

    Jump("loc_1E38")

    label("loc_1A38")


    AnonymousTalk(    #19
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "巴伦诺灯塔\x01",                                         # 0
            "巴伦诺灯塔（夜晚）\x01",                                 # 1
            "旧校舍地下遗迹\x01",                                     # 2
            "绀碧之塔1F（前半）\x01",                                 # 3
            "绀碧之塔2F（前半）\x01",                                 # 4
            "绀碧之塔3F（前半）\x01",                                 # 5
            "绀碧之塔4F（前半）\x01",                                 # 6
            "绀碧之塔5F（前半）\x01",                                 # 7
            "绀碧之塔1F（后半）\x01",                                 # 8
            "绀碧之塔2F（后半）\x01",                                 # 9
            "绀碧之塔3F（后半）\x01",                                 # 10
            "绀碧之塔4F（后半）\x01",                                 # 11
            "绀碧之塔5F（后半）\x01",                                 # 12
            "绀碧之塔屋顶（后半 异次元背景）\x01",                    # 13
            "绀碧之塔屋顶（后半 异次元背景，埃尔赛尤视点）\x01",      # 14
            "绀碧之塔屋顶（后半 一般背景）\x01",                      # 15
            "取消\x01",                                               # 16
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BF3"),
        (1, "loc_1BFC"),
        (2, "loc_1C05"),
        (3, "loc_1C0E"),
        (4, "loc_1C17"),
        (5, "loc_1C20"),
        (6, "loc_1C29"),
        (7, "loc_1C32"),
        (8, "loc_1C3B"),
        (9, "loc_1C44"),
        (10, "loc_1C4D"),
        (11, "loc_1C56"),
        (12, "loc_1C5F"),
        (13, "loc_1C68"),
        (14, "loc_1C71"),
        (15, "loc_1C7A"),
        (SWITCH_DEFAULT, "loc_1C83"),
    )


    label("loc_1BF3")

    NewScene("ED6_DT21/C2209   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1BFC")

    NewScene("ED6_DT21/C2200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1C05")

    NewScene("ED6_DT21/C2400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1C0E")

    NewScene("ED6_DT21/C2111   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1C17")

    NewScene("ED6_DT21/C2112   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1C20")

    NewScene("ED6_DT21/C2113   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1C29")

    NewScene("ED6_DT21/C2114   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1C32")

    NewScene("ED6_DT21/C2115   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1C3B")

    NewScene("ED6_DT21/C2300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1C44")

    NewScene("ED6_DT21/C2301   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1C4D")

    NewScene("ED6_DT21/C2302   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1C56")

    NewScene("ED6_DT21/C2303   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1C5F")

    NewScene("ED6_DT21/C2304   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1C68")

    NewScene("ED6_DT21/C2305   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1C71")

    NewScene("ED6_DT21/C2306   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1C7A")

    NewScene("ED6_DT21/C2307   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1C83")

    OP_5F(0x3)
    Jump("loc_1C89")

    label("loc_1C89")

    Jump("loc_1E38")

    label("loc_1C8C")


    AnonymousTalk(    #20
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "古罗尼山道\x01",          # 0
            "玛诺利亚间道\x01",        # 1
            "阿伊纳街道\x01",          # 2
            "梅威海道\x01",            # 3
            "街景林道\x01",            # 4
            "梅威海道军用艇\x01",      # 5
            "取消\x01",                # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D0C"),
        (1, "loc_1D15"),
        (2, "loc_1D1E"),
        (3, "loc_1D27"),
        (4, "loc_1D30"),
        (5, "loc_1D39"),
        (SWITCH_DEFAULT, "loc_1D42"),
    )


    label("loc_1D0C")

    NewScene("ED6_DT21/C1501   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1D15")

    NewScene("ED6_DT21/R2100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1D1E")

    NewScene("ED6_DT21/R2400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1D27")

    NewScene("ED6_DT21/R2200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1D30")

    NewScene("ED6_DT21/R2300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1D39")

    NewScene("ED6_DT21/R2203   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1D42")

    OP_5F(0x3)
    Jump("loc_1D48")

    label("loc_1D48")

    Jump("loc_1E38")

    label("loc_1D4B")


    AnonymousTalk(    #21
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "玛诺利亚\x01",          # 0
            "玛诺利亚海岸\x01",      # 1
            "孤儿院\x01",            # 2
            "阿伊纳街道\x01",        # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1DA2"),
        (1, "loc_1DAE"),
        (2, "loc_1DBA"),
        (3, "loc_1DC6"),
        (SWITCH_DEFAULT, "loc_1DD2"),
    )


    label("loc_1DA2")

    NewScene("ED6_DT21/T2301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1DD8")

    label("loc_1DAE")

    NewScene("ED6_DT21/R2111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1DD8")

    label("loc_1DBA")

    NewScene("ED6_DT21/T2403   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1DD8")

    label("loc_1DC6")

    NewScene("ED6_DT21/R2412   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1DD8")

    label("loc_1DD2")

    OP_5F(0x3)
    Jump("loc_1DD8")

    label("loc_1DD8")

    Jump("loc_1E38")

    label("loc_1DDB")


    AnonymousTalk(    #22
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "海卷\x01",      # 0
            "海\x01",        # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E0A"),
        (1, "loc_1E16"),
        (SWITCH_DEFAULT, "loc_1E22"),
    )


    label("loc_1E0A")

    NewScene("ED6_DT21/T2103   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1E28")

    label("loc_1E16")

    NewScene("ED6_DT21/T2104   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1E28")

    label("loc_1E22")

    OP_5F(0x3)
    Jump("loc_1E28")

    label("loc_1E28")

    Jump("loc_1E38")

    label("loc_1E2B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E38")

    label("loc_1E38")

    Jump("loc_178B")

    label("loc_1E3B")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_9_1781 end

    def Function_10_1E4B(): pass

    label("Function_10_1E4B")


    AnonymousTalk(    #23
        "\x06哪里？\x02",
    )


    label("loc_1E55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2446")

    Menu(
        2,
        10,
        100,
        1,
        (
            "城里\x01",      # 0
            "迷宫\x01",      # 1
            "大道\x01",      # 2
            "夜\x01",        # 3
            "取消\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E9E"),
        (1, "loc_201D"),
        (2, "loc_2325"),
        (3, "loc_23E0"),
        (SWITCH_DEFAULT, "loc_2436"),
    )


    label("loc_1E9E")


    AnonymousTalk(    #24
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "蔡斯城\x01",                    # 0
            "蔡斯民房1～3室内\x01",          # 1
            "中央工房 室内\x01",             # 2
            "沃尔费堡垒\x01",                # 3
            "蔡斯教会\x01",                  # 4
            "武器点\x01",                    # 5
            "拉赛尔工房\x01",                # 6
            "亚尔摩村外部\x01",              # 7
            "亚尔摩村外部（夜晚）\x01",      # 8
            "圣海姆门\x01",                  # 9
            "圣海姆门 地震后\x01",           # 10
            "蔡斯城（夜晚）\x01",            # 11
            "蔡斯城（停电事件）\x01",        # 12
            "取消\x01",                      # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F9F"),
        (1, "loc_1FA8"),
        (2, "loc_1FB1"),
        (3, "loc_1FBA"),
        (4, "loc_1FC3"),
        (5, "loc_1FCC"),
        (6, "loc_1FD5"),
        (7, "loc_1FDE"),
        (8, "loc_1FE7"),
        (9, "loc_1FF0"),
        (10, "loc_1FF9"),
        (11, "loc_2002"),
        (12, "loc_200B"),
        (SWITCH_DEFAULT, "loc_2014"),
    )


    label("loc_1F9F")

    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FA8")

    NewScene("ED6_DT21/T3110   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FB1")

    NewScene("ED6_DT21/T3111   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FBA")

    NewScene("ED6_DT21/T3300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FC3")

    NewScene("ED6_DT21/T3130   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FCC")

    NewScene("ED6_DT21/T3120   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FD5")

    NewScene("ED6_DT21/T3133   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FDE")

    NewScene("ED6_DT21/T3200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FE7")

    NewScene("ED6_DT21/T3201   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FF0")

    NewScene("ED6_DT21/T3400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FF9")

    NewScene("ED6_DT21/T3401   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2002")

    NewScene("ED6_DT21/T3103   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_200B")

    NewScene("ED6_DT21/T3106   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2014")

    OP_5F(0x3)
    Jump("loc_201A")

    label("loc_201A")

    Jump("loc_2443")

    label("loc_201D")


    AnonymousTalk(    #25
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "雷斯顿水上要塞外\x01",                                   # 0
            "雷斯顿水上要塞中\x01",                                   # 1
            "雷斯顿水上要塞外（夜晚）\x01",                           # 2
            "雷斯顿水上要塞（飞船坪无军用艇）\x01",                   # 3
            "卡鲁迪亚钟乳洞\x01",                                     # 4
            "卡鲁迪亚大钟乳洞　Boss房间\x01",                         # 5
            "温泉源流地图入口\x01",                                   # 6
            "温泉源流\x01",                                           # 7
            "红莲之塔1F（前半）\x01",                                 # 8
            "红莲之塔2F（前半）\x01",                                 # 9
            "红莲之塔3F（前半）\x01",                                 # 10
            "红莲之塔4F（前半）\x01",                                 # 11
            "红莲之塔5F（前半）\x01",                                 # 12
            "红莲之塔1F（后半）\x01",                                 # 13
            "红莲之塔2F（后半）\x01",                                 # 14
            "红莲之塔3F（后半）\x01",                                 # 15
            "红莲之塔4F（后半）\x01",                                 # 16
            "红莲之塔5F（后半）\x01",                                 # 17
            "红莲之塔屋顶（后半 异次元背景）\x01",                    # 18
            "红莲之塔屋顶（后半 异次元背景，埃尔赛尤视点）\x01",      # 19
            "红莲之塔屋顶（后半 一般背景）\x01",                      # 20
            "取消\x01",                                               # 21
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_225F"),
        (1, "loc_2268"),
        (2, "loc_2271"),
        (3, "loc_227A"),
        (4, "loc_2283"),
        (5, "loc_228C"),
        (6, "loc_2295"),
        (7, "loc_229E"),
        (8, "loc_22A7"),
        (9, "loc_22B0"),
        (10, "loc_22B9"),
        (11, "loc_22C2"),
        (12, "loc_22CB"),
        (13, "loc_22D4"),
        (14, "loc_22DD"),
        (15, "loc_22E6"),
        (16, "loc_22EF"),
        (17, "loc_22F8"),
        (18, "loc_2301"),
        (19, "loc_230A"),
        (20, "loc_2313"),
        (SWITCH_DEFAULT, "loc_231C"),
    )


    label("loc_225F")

    NewScene("ED6_DT21/C3100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2268")

    NewScene("ED6_DT21/C3110   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2271")

    NewScene("ED6_DT21/C3104   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_227A")

    NewScene("ED6_DT21/C3108   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2283")

    NewScene("ED6_DT21/C3300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_228C")

    NewScene("ED6_DT21/C3303   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2295")

    NewScene("ED6_DT21/C3400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_229E")

    NewScene("ED6_DT21/C3401   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_22A7")

    NewScene("ED6_DT21/C3511   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_22B0")

    NewScene("ED6_DT21/C3512   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_22B9")

    NewScene("ED6_DT21/C3513   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_22C2")

    NewScene("ED6_DT21/C3514   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_22CB")

    NewScene("ED6_DT21/C3515   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_22D4")

    NewScene("ED6_DT21/C3600   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_22DD")

    NewScene("ED6_DT21/C3601   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_22E6")

    NewScene("ED6_DT21/C3602   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_22EF")

    NewScene("ED6_DT21/C3603   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_22F8")

    NewScene("ED6_DT21/C3604   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2301")

    NewScene("ED6_DT21/C3605   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_230A")

    NewScene("ED6_DT21/C3606   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2313")

    NewScene("ED6_DT21/C3607   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_231C")

    OP_5F(0x3)
    Jump("loc_2322")

    label("loc_2322")

    Jump("loc_2443")

    label("loc_2325")


    AnonymousTalk(    #26
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "佐达特军用道\x01",                # 0
            "卡鲁迪亚隧道（suidou）\x01",      # 1
            "托兰特平原道\x01",                # 2
            "利塔街道\x01",                    # 3
            "托兰特平原道军用舰\x01",          # 4
            "取消\x01",                        # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23AA"),
        (1, "loc_23B3"),
        (2, "loc_23BC"),
        (3, "loc_23C5"),
        (4, "loc_23CE"),
        (SWITCH_DEFAULT, "loc_23D7"),
    )


    label("loc_23AA")

    NewScene("ED6_DT21/R3300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_23B3")

    NewScene("ED6_DT21/R3400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_23BC")

    NewScene("ED6_DT21/R3100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_23C5")

    NewScene("ED6_DT21/R3200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_23CE")

    NewScene("ED6_DT21/R3105   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_23D7")

    OP_5F(0x3)
    Jump("loc_23DD")

    label("loc_23DD")

    Jump("loc_2443")

    label("loc_23E0")


    AnonymousTalk(    #27
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "蔡斯\x01",          # 0
            "中央工房\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2415"),
        (1, "loc_2421"),
        (SWITCH_DEFAULT, "loc_242D"),
    )


    label("loc_2415")

    NewScene("ED6_DT21/T3103   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2433")

    label("loc_2421")

    NewScene("ED6_DT21/T3104   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2433")

    label("loc_242D")

    OP_5F(0x3)
    Jump("loc_2433")

    label("loc_2433")

    Jump("loc_2443")

    label("loc_2436")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2443")

    label("loc_2443")

    Jump("loc_1E55")

    label("loc_2446")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_1E4B end

    def Function_11_2456(): pass

    label("Function_11_2456")


    AnonymousTalk(    #28
        "\x06哪里？\x02",
    )


    label("loc_2460")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B3A")

    Menu(
        2,
        10,
        100,
        1,
        (
            "城里\x01",      # 0
            "迷宫\x01",      # 1
            "大道\x01",      # 2
            "夜\x01",        # 3
            "取消\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24A9"),
        (1, "loc_27ED"),
        (2, "loc_28AE"),
        (3, "loc_2929"),
        (SWITCH_DEFAULT, "loc_2B2A"),
    )


    label("loc_24A9")


    AnonymousTalk(    #29
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "----- 格兰赛尔\x01",                  # 0
            "T4200 格兰赛尔城\x01",                # 1
            "T4300 艾尔贝离宫（夜晚）\x01",        # 2
            "T4133 酒店室内（夜晚）\x01",          # 3
            "T4134 大圣堂室内（夜晚）\x01",        # 4
            "T4135 历史资料馆室内\x01",            # 5
            "T4136 竞技场室内\x01",                # 6
            "T4400 码头\x01",                      # 7
            "T4138 帝国大使馆内部 内部\x01",       # 8
            "T4139 共和国大使馆 内部\x01",         # 9
            "T4140 武器屋、工房（夜晚）\x01",      # 10
            "T4141 艾德尔百货店（夜晚）\x01",      # 11
            "T4142 酒廊（夜晚）\x01",              # 12
            "T4143 黑市商店 内部\x01",             # 13
            "取消\x01",                            # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_262E"),
        (1, "loc_276F"),
        (2, "loc_2778"),
        (3, "loc_2781"),
        (4, "loc_278A"),
        (5, "loc_2793"),
        (6, "loc_279C"),
        (7, "loc_27A5"),
        (8, "loc_27AE"),
        (9, "loc_27B7"),
        (10, "loc_27C0"),
        (11, "loc_27C9"),
        (12, "loc_27D2"),
        (13, "loc_27DB"),
        (SWITCH_DEFAULT, "loc_27E4"),
    )


    label("loc_262E")


    AnonymousTalk(    #30
        "\x06哪里？\x02",
    )


    Menu(
        4,
        10,
        100,
        1,
        (
            "T4100 格兰赛尔（南街区）\x01",              # 0
            "T4101 格兰赛尔（东街区）\x01",              # 1
            "T4102 格兰赛尔（西街区）\x01",              # 2
            "T4103 格兰赛尔（北街区）\x01",              # 3
            "T4104 格兰赛尔（竞技场内侧）\x01",          # 4
            "T4105 格兰赛尔（空港）\x01",                # 5
            "T4106 格兰赛尔（空港无埃尔赛尤）\x01",      # 6
            "取消\x01",                                  # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2727"),
        (1, "loc_2730"),
        (2, "loc_2739"),
        (3, "loc_2742"),
        (4, "loc_274B"),
        (5, "loc_2754"),
        (6, "loc_275D"),
        (SWITCH_DEFAULT, "loc_2766"),
    )


    label("loc_2727")

    NewScene("ED6_DT21/T4100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2730")

    NewScene("ED6_DT21/T4101   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2739")

    NewScene("ED6_DT21/T4102   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2742")

    NewScene("ED6_DT21/T4103   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_274B")

    NewScene("ED6_DT21/T4104   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2754")

    NewScene("ED6_DT21/T4105   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_275D")

    NewScene("ED6_DT21/T4106   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2766")

    OP_5F(0x4)
    OP_5F(0x3)
    Jump("loc_27EA")

    label("loc_276F")

    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2778")

    NewScene("ED6_DT21/T4300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2781")

    NewScene("ED6_DT21/T4133   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_278A")

    NewScene("ED6_DT21/T4134   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2793")

    NewScene("ED6_DT21/T4135   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_279C")

    NewScene("ED6_DT21/T4136   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_27A5")

    NewScene("ED6_DT21/T4400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_27AE")

    NewScene("ED6_DT21/T4138   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_27B7")

    NewScene("ED6_DT21/T4139   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_27C0")

    NewScene("ED6_DT21/T4140   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_27C9")

    NewScene("ED6_DT21/T4141   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_27D2")

    NewScene("ED6_DT21/T4142   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_27DB")

    NewScene("ED6_DT21/T4143   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_27E4")

    OP_5F(0x3)
    Jump("loc_27EA")

    label("loc_27EA")

    Jump("loc_2B37")

    label("loc_27ED")


    AnonymousTalk(    #31
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "下水道Ａ\x01",            # 0
            "下水道Ｂ\x01",            # 1
            "下水道Ｃ\x01",            # 2
            "封印区域最上层\x01",      # 3
            "封印区域中层\x01",        # 4
            "封印区域最下层\x01",      # 5
            "取消\x01",                # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_286F"),
        (1, "loc_2878"),
        (2, "loc_2881"),
        (3, "loc_288A"),
        (4, "loc_2893"),
        (5, "loc_289C"),
        (SWITCH_DEFAULT, "loc_28A5"),
    )


    label("loc_286F")

    NewScene("ED6_DT21/C4200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2878")

    NewScene("ED6_DT21/C4202   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2881")

    NewScene("ED6_DT21/C4204   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_288A")

    NewScene("ED6_DT21/C4300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2893")

    NewScene("ED6_DT21/C4301   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_289C")

    NewScene("ED6_DT21/C4302   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_28A5")

    OP_5F(0x3)
    Jump("loc_28AB")

    label("loc_28AB")

    Jump("loc_2B37")

    label("loc_28AE")


    AnonymousTalk(    #32
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "艾尔贝周游道\x01",          # 0
            "庭园大道\x01",              # 1
            "艾尔贝周游道·湖\x01",      # 2
            "取消\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2905"),
        (1, "loc_290E"),
        (2, "loc_2917"),
        (SWITCH_DEFAULT, "loc_2920"),
    )


    label("loc_2905")

    NewScene("ED6_DT21/C4100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_290E")

    NewScene("ED6_DT21/R4100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2917")

    NewScene("ED6_DT21/C4103   ._SN", 101, 0, 0)
    IdleLoop()

    label("loc_2920")

    OP_5F(0x3)
    Jump("loc_2926")

    label("loc_2926")

    Jump("loc_2B37")

    label("loc_2929")


    AnonymousTalk(    #33
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "艾尔贝周游道 C41111\x01",              # 0
            "艾尔贝周游道 C41113\x01",              # 1
            "艾尔贝离宫 入口庭园（白天）\x01",      # 2
            "艾尔贝离宫 中庭，回廊\x01",            # 3
            "艾尔贝离宫 大厅～\x01",                # 4
            "艾尔贝离宫 客房～\x01",                # 5
            "格兰赛尔 南街区\x01",                  # 6
            "格兰赛尔 東街区\x01",                  # 7
            "格兰赛尔 西街区\x01",                  # 8
            "格兰赛尔 北街区\x01",                  # 9
            "格兰赛尔（空港无埃尔赛尤）\x01",       # 10
            "格兰赛尔城\x01",                       # 11
            "格兰赛尔城 室内\x01",                  # 12
            "码头\x01",                             # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A79"),
        (1, "loc_2A85"),
        (2, "loc_2A91"),
        (3, "loc_2A9D"),
        (4, "loc_2AA9"),
        (5, "loc_2AB5"),
        (6, "loc_2AC1"),
        (7, "loc_2ACD"),
        (8, "loc_2AD9"),
        (9, "loc_2AE5"),
        (10, "loc_2AF1"),
        (11, "loc_2AFD"),
        (12, "loc_2B09"),
        (13, "loc_2B15"),
        (SWITCH_DEFAULT, "loc_2B21"),
    )


    label("loc_2A79")

    NewScene("ED6_DT21/C4111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B27")

    label("loc_2A85")

    NewScene("ED6_DT21/C4113   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B27")

    label("loc_2A91")

    NewScene("ED6_DT21/T4302   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B27")

    label("loc_2A9D")

    NewScene("ED6_DT21/T4303   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B27")

    label("loc_2AA9")

    NewScene("ED6_DT21/T4312   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B27")

    label("loc_2AB5")

    NewScene("ED6_DT21/T4313   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B27")

    label("loc_2AC1")

    NewScene("ED6_DT21/T4150   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B27")

    label("loc_2ACD")

    NewScene("ED6_DT21/T4151   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B27")

    label("loc_2AD9")

    NewScene("ED6_DT21/T4152   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B27")

    label("loc_2AE5")

    NewScene("ED6_DT21/T4153   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B27")

    label("loc_2AF1")

    NewScene("ED6_DT21/T4156   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B27")

    label("loc_2AFD")

    NewScene("ED6_DT21/T4203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B27")

    label("loc_2B09")

    NewScene("ED6_DT21/T4250   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B27")

    label("loc_2B15")

    NewScene("ED6_DT21/T4403   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_2B27")

    label("loc_2B21")

    OP_5F(0x3)
    Jump("loc_2B27")

    label("loc_2B27")

    Jump("loc_2B37")

    label("loc_2B2A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B37")

    label("loc_2B37")

    Jump("loc_2460")

    label("loc_2B3A")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_2456 end

    def Function_12_2B4A(): pass

    label("Function_12_2B4A")


    AnonymousTalk(    #34
        "\x06哪里？\x02",
    )


    label("loc_2B54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38EC")

    Menu(
        2,
        10,
        100,
        1,
        (
            "卢·洛克尔\x01",          # 0
            "研究所\x01",              # 1
            "辉之环\x01",              # 2
            "哈梅尔村\x01",            # 3
            "古罗力亚斯内部\x01",      # 4
            "取消\x01",                # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2BC0"),
        (1, "loc_2CB0"),
        (2, "loc_2E27"),
        (3, "loc_3558"),
        (4, "loc_35AD"),
        (SWITCH_DEFAULT, "loc_38DC"),
    )


    label("loc_2BC0")


    AnonymousTalk(    #35
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T5100 训练场外观\x01",                     # 0
            "C5503 训练场１ 巴斯塔尔水道\x01",          # 1
            "C5504 训练场２ 圣科洛瓦森林\x01",          # 2
            "C5508 训练场３ 格林姆瑟尔小要塞\x01",      # 3
            "T5101 训练场外观（夜晚）\x01",             # 4
            "取消\x01",                                 # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C7A"),
        (1, "loc_2C83"),
        (2, "loc_2C8C"),
        (3, "loc_2C95"),
        (4, "loc_2C9E"),
        (SWITCH_DEFAULT, "loc_2CA7"),
    )


    label("loc_2C7A")

    NewScene("ED6_DT21/T5100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2C83")

    NewScene("ED6_DT21/C5503   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2C8C")

    NewScene("ED6_DT21/C5504   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2C95")

    NewScene("ED6_DT21/C5508   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2C9E")

    NewScene("ED6_DT21/T5101   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2CA7")

    OP_5F(0x3)
    Jump("loc_2CAD")

    label("loc_2CAD")

    Jump("loc_38E9")

    label("loc_2CB0")


    AnonymousTalk(    #36
        (
            "\x06哪里？\x01",
            "室内与夜晚地图连接。\x01",
            "侵入事件只在夜晚进行。白天使用事件专用。\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C5600 研究所外观（入口）\x01",          # 0
            "C5601 研究所外观（入口）夜晚\x01",      # 1
            "C5610 研究所内部（１楼）\x01",          # 2
            "C5611 研究所内部（２楼）\x01",          # 3
            "C5612 研究所内部（３楼）\x01",          # 4
            "C5613 研究所内部（４楼）\x01",          # 5
            "C5614 研究所内部升降梯\x01",            # 6
            "取消\x01",                              # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2DDF"),
        (1, "loc_2DE8"),
        (2, "loc_2DF1"),
        (3, "loc_2DFA"),
        (4, "loc_2E03"),
        (5, "loc_2E0C"),
        (6, "loc_2E15"),
        (SWITCH_DEFAULT, "loc_2E1E"),
    )


    label("loc_2DDF")

    NewScene("ED6_DT21/C5600   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2DE8")

    NewScene("ED6_DT21/C5601   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2DF1")

    NewScene("ED6_DT21/C5610   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2DFA")

    NewScene("ED6_DT21/C5611   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2E03")

    NewScene("ED6_DT21/C5612   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2E0C")

    NewScene("ED6_DT21/C5613   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2E15")

    NewScene("ED6_DT21/C5614   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2E1E")

    OP_5F(0x3)
    Jump("loc_2E24")

    label("loc_2E24")

    Jump("loc_38E9")

    label("loc_2E27")


    AnonymousTalk(    #37
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C5100中枢塔前通路\x01",                    # 0
            "C5101中枢塔入口\x01",                      # 1
            "C5700工业区域法克特里亚\x01",              # 2
            "C5800居住区域克雷德尔\x01",                # 3
            "C5900公园区域卡尔玛丽\x01",                # 4
            "-----辉之环内部（地下道、车站）\x01",      # 5
            "-----中央中枢塔内部\x01",                  # 6
            "-----车站\x01",                            # 7
            "取消\x01",                                 # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2F0F"),
        (1, "loc_2F18"),
        (2, "loc_2F21"),
        (3, "loc_2F2A"),
        (4, "loc_2F33"),
        (5, "loc_2F3C"),
        (6, "loc_3166"),
        (7, "loc_3471"),
        (SWITCH_DEFAULT, "loc_354F"),
    )


    label("loc_2F0F")

    NewScene("ED6_DT21/C5100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2F18")

    NewScene("ED6_DT21/C5101   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2F21")

    NewScene("ED6_DT21/C5700   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2F2A")

    NewScene("ED6_DT21/C5800   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2F33")

    NewScene("ED6_DT21/C5900   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2F3C")


    AnonymousTalk(    #38
        "\x06哪里？\x02",
    )


    Menu(
        4,
        10,
        100,
        1,
        (
            "地下道5200（公园～居住区①）\x01",            # 0
            "地下道5201（公园～居住区②）\x01",            # 1
            "地下道5202（居住区域～工业区域①）\x01",      # 2
            "地下道5203（居住区域～工业区域②）\x01",      # 3
            "地下道5204（工业区域～中枢塔①）\x01",        # 4
            "地下道5205（工业区域～中枢塔②）\x01",        # 5
            "地下道5206（中枢塔～公园区域①）\x01",        # 6
            "地下道5207（中枢塔ー～公园区域②）\x01",      # 7
            "C6000 西卡尔玛丽车站\x01",                    # 8
            "C6001 第３５克雷德尔车站\x01",                # 9
            "C6002 第７法克特里亚车站\x01",                # 10
            "C6003 中枢塔车站\x01",                        # 11
            "取消\x01",                                    # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_30EE"),
        (1, "loc_30F7"),
        (2, "loc_3100"),
        (3, "loc_3109"),
        (4, "loc_3112"),
        (5, "loc_311B"),
        (6, "loc_3124"),
        (7, "loc_312D"),
        (8, "loc_3136"),
        (9, "loc_313F"),
        (10, "loc_3148"),
        (11, "loc_3151"),
        (SWITCH_DEFAULT, "loc_315A"),
    )


    label("loc_30EE")

    NewScene("ED6_DT21/C5200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_30F7")

    NewScene("ED6_DT21/C5201   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3100")

    NewScene("ED6_DT21/C5202   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3109")

    NewScene("ED6_DT21/C5203   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3112")

    NewScene("ED6_DT21/C5204   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_311B")

    NewScene("ED6_DT21/C5205   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3124")

    NewScene("ED6_DT21/C5206   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_312D")

    NewScene("ED6_DT21/C5207   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3136")

    NewScene("ED6_DT21/C6000   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_313F")

    NewScene("ED6_DT21/C6001   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3148")

    NewScene("ED6_DT21/C6002   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3151")

    NewScene("ED6_DT21/C6003   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_315A")

    OP_5F(0x4)
    Jump("loc_3160")

    label("loc_3160")

    OP_5F(0x3)
    Jump("loc_3555")

    label("loc_3166")


    AnonymousTalk(    #39
        "\x06中枢塔内部的哪里？\x02",
    )


    Menu(
        4,
        10,
        100,
        1,
        (
            "C5300 中央中枢塔内部0\x01",                       # 0
            "C5301 中央中枢塔内部1\x01",                       # 1
            "C5302 中央中枢塔内部2\x01",                       # 2
            "C5303 中央中枢塔内部3\x01",                       # 3
            "C5304 中央中枢塔内部4\x01",                       # 4
            "C5305 中央中枢塔内部5\x01",                       # 5
            "C5306 中央中枢塔内部6\x01",                       # 6
            "C5307 中央中枢塔内部7\x01",                       # 7
            "C5308 中Boss地图1（布卢布兰）\x01",               # 8
            "C5309 中Boss地图2（瓦鲁特）\x01",                 # 9
            "C5310 中Boss地图3（露茜奥拉）\x01",               # 10
            "C5311 中Boss地图4（玲）\x01",                     # 11
            "C5312 通路出来到Shaft内部\x01",                   # 12
            "C5313 屋顶\x01",                                  # 13
            "C5314 最下部、Boss房间前通路、Boss房间\x01",      # 14
            "C5315 高速升降梯\x01",                            # 15
            "C5316 小升降梯\x01",                              # 16
            "C5317 Boss房间\x01",                              # 17
            "C5318 Boss战斗地图事件专用\x01",                  # 18
            "C5319 Boss房间前通路\x01",                        # 19
            "取消\x01",                                        # 20
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_33B1"),
        (1, "loc_33BA"),
        (2, "loc_33C3"),
        (3, "loc_33CC"),
        (4, "loc_33D5"),
        (5, "loc_33DE"),
        (6, "loc_33E7"),
        (7, "loc_33F0"),
        (8, "loc_33F9"),
        (9, "loc_3402"),
        (10, "loc_340B"),
        (11, "loc_3414"),
        (12, "loc_341D"),
        (13, "loc_3426"),
        (14, "loc_342F"),
        (15, "loc_3438"),
        (16, "loc_3441"),
        (17, "loc_344A"),
        (18, "loc_3453"),
        (19, "loc_345C"),
        (SWITCH_DEFAULT, "loc_3465"),
    )


    label("loc_33B1")

    NewScene("ED6_DT21/C5300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_33BA")

    NewScene("ED6_DT21/C5301   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_33C3")

    NewScene("ED6_DT21/C5302   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_33CC")

    NewScene("ED6_DT21/C5303   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_33D5")

    NewScene("ED6_DT21/C5304   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_33DE")

    NewScene("ED6_DT21/C5305   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_33E7")

    NewScene("ED6_DT21/C5306   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_33F0")

    NewScene("ED6_DT21/C5307   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_33F9")

    NewScene("ED6_DT21/C5308   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3402")

    NewScene("ED6_DT21/C5309   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_340B")

    NewScene("ED6_DT21/C5310   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3414")

    NewScene("ED6_DT21/C5311   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_341D")

    NewScene("ED6_DT21/C5312   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3426")

    NewScene("ED6_DT21/C5313   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_342F")

    NewScene("ED6_DT21/C5314   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3438")

    NewScene("ED6_DT21/C5315   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3441")

    NewScene("ED6_DT21/C5316   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_344A")

    NewScene("ED6_DT21/C5317   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3453")

    NewScene("ED6_DT21/C5318   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_345C")

    NewScene("ED6_DT21/C5319   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3465")

    OP_5F(0x4)
    Jump("loc_346B")

    label("loc_346B")

    OP_5F(0x3)
    Jump("loc_3555")

    label("loc_3471")


    AnonymousTalk(    #40
        "\x06车站的哪里？\x02",
    )


    Menu(
        4,
        10,
        100,
        1,
        (
            "C6000西卡尔玛丽车站\x01",         # 0
            "C6001第35克雷德尔车站\x01",       # 1
            "C6002第7法克特里亚车站\x01",      # 2
            "C6003中枢塔前车站\x01",           # 3
            "C6010单轨铁路移动中\x01",         # 4
            "取消\x01",                        # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3516"),
        (1, "loc_351F"),
        (2, "loc_3528"),
        (3, "loc_3531"),
        (4, "loc_353A"),
        (SWITCH_DEFAULT, "loc_3543"),
    )


    label("loc_3516")

    NewScene("ED6_DT21/C6000   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_351F")

    NewScene("ED6_DT21/C6001   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3528")

    NewScene("ED6_DT21/C6002   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3531")

    NewScene("ED6_DT21/C6003   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_353A")

    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3543")

    OP_5F(0x4)
    Jump("loc_3549")

    label("loc_3549")

    OP_5F(0x3)
    Jump("loc_3555")

    label("loc_354F")

    OP_5F(0x3)
    Jump("loc_3555")

    label("loc_3555")

    Jump("loc_38E9")

    label("loc_3558")


    AnonymousTalk(    #41
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "哈梅尔\x01",      # 0
            "哈梅尔\x01",      # 1
            "取消\x01",        # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3592"),
        (1, "loc_359B"),
        (SWITCH_DEFAULT, "loc_35A4"),
    )


    label("loc_3592")

    NewScene("ED6_DT21/T5200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_359B")

    NewScene("ED6_DT21/T5201   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_35A4")

    OP_5F(0x3)
    Jump("loc_35AA")

    label("loc_35AA")

    Jump("loc_38E9")

    label("loc_35AD")


    AnonymousTalk(    #42
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C5400古罗力亚斯内部（艾丝蒂尔监禁房间）\x01",                  # 0
            "C5401古罗力亚斯内部（怀斯曼的房间）\x01",                      # 1
            "C5402古罗力亚斯内部（甲板方面通路）\x01",                      # 2
            "C5403古罗力亚斯内部（甲板～升降口方向通路）\x01",              # 3
            "C5404古罗力亚斯内部（升降口～机库方面通路）\x01",              # 4
            "C5405古罗力亚斯内部（机库错误）\x01",                          # 5
            "C5406古罗力亚斯内部（机库正确）\x01",                          # 6
            "C5407古罗力亚斯内部（升降梯箱）\x01",                          # 7
            "C5408古罗力亚斯外部（甲板）\x01",                              # 8
            "C5409古罗力亚斯外部（升降口）\x01",                            # 9
            "C5410古罗力亚斯内部（升降口～机库方向通路入口追加）\x01",      # 10
            "C5411古罗力亚斯内部（机库入口）\x01",                          # 11
            "C5412古罗力亚斯内部（机库错误）\x01",                          # 12
            "C5413古罗力亚斯外部 升降口 夜晚\x01",                          # 13
            "C5414古罗力亚斯外部 附窗外装\x01",                             # 14
            "C5415古罗力亚斯内部 后部升降口\x01",                           # 15
            "取消\x01",                                                     # 16
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3843"),
        (1, "loc_384C"),
        (2, "loc_3855"),
        (3, "loc_385E"),
        (4, "loc_3867"),
        (5, "loc_3870"),
        (6, "loc_3879"),
        (7, "loc_3882"),
        (8, "loc_388B"),
        (9, "loc_3894"),
        (10, "loc_389D"),
        (11, "loc_38A6"),
        (12, "loc_38AF"),
        (13, "loc_38B8"),
        (14, "loc_38C1"),
        (15, "loc_38CA"),
        (SWITCH_DEFAULT, "loc_38D3"),
    )


    label("loc_3843")

    NewScene("ED6_DT21/C5400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_384C")

    NewScene("ED6_DT21/C5401   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3855")

    NewScene("ED6_DT21/C5402   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_385E")

    NewScene("ED6_DT21/C5403   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3867")

    NewScene("ED6_DT21/C5404   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3870")

    NewScene("ED6_DT21/C5405   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3879")

    NewScene("ED6_DT21/C5406   ._SN", 102, 0, 0)
    IdleLoop()

    label("loc_3882")

    NewScene("ED6_DT21/C5407   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_388B")

    NewScene("ED6_DT21/C5408   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3894")

    NewScene("ED6_DT21/C5409   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_389D")

    NewScene("ED6_DT21/C5410   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_38A6")

    NewScene("ED6_DT21/C5411   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_38AF")

    NewScene("ED6_DT21/C5412   ._SN", 102, 0, 0)
    IdleLoop()

    label("loc_38B8")

    NewScene("ED6_DT21/C5413   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_38C1")

    NewScene("ED6_DT21/C5414   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_38CA")

    NewScene("ED6_DT21/C5415   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_38D3")

    OP_5F(0x3)
    Jump("loc_38D9")

    label("loc_38D9")

    Jump("loc_38E9")

    label("loc_38DC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_38E9")

    label("loc_38E9")

    Jump("loc_2B54")

    label("loc_38EC")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_2B4A end

    def Function_13_38FC(): pass

    label("Function_13_38FC")


    AnonymousTalk(    #43
        "\x06哪里？\x02",
    )


    label("loc_3906")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DCA")

    Menu(
        2,
        10,
        100,
        1,
        (
            "许多船\x01",                # 0
            "埃尔赛尤\x01",              # 1
            "空中，水上事件用\x01",      # 2
            "取消\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_395A"),
        (1, "loc_3B28"),
        (2, "loc_3C9D"),
        (SWITCH_DEFAULT, "loc_3DBA"),
    )


    label("loc_395A")


    AnonymousTalk(    #44
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "E0000 定期船　林德号\x01",                                 # 0
            "E0001 定期船　赛希莉亚号（绿色）\x01",                     # 1
            "E0002 工房船\x01",                                         # 2
            "E0100 空贼用飞船\x01",                                     # 3
            "E0101 空贼用飞船（夜用）\x01",                             # 4
            "E0111 空贼用飞船内装置\x01",                               # 5
            "E0200 军用扬陆舰\x01",                                     # 6
            "E0400 特务艇\x01",                                         # 7
            "E0600 红色高速飞艇外观（特务艇改变颜色+小改造）\x01",      # 8
            "E0610 红色高速飞艇内部\x01",                               # 9
            "E0700 国际定期船格雷特纳号（定期船蓝色）\x01",             # 10
            "取消\x01",                                                 # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3ABC"),
        (1, "loc_3AC5"),
        (2, "loc_3ACE"),
        (3, "loc_3AD7"),
        (4, "loc_3AE0"),
        (5, "loc_3AE9"),
        (6, "loc_3AF2"),
        (7, "loc_3AFB"),
        (8, "loc_3B04"),
        (9, "loc_3B0D"),
        (10, "loc_3B16"),
        (SWITCH_DEFAULT, "loc_3B1F"),
    )


    label("loc_3ABC")

    NewScene("ED6_DT21/E0000   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3AC5")

    NewScene("ED6_DT21/E0001   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3ACE")

    NewScene("ED6_DT21/E0002   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3AD7")

    NewScene("ED6_DT21/E0100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3AE0")

    NewScene("ED6_DT21/E0101   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3AE9")

    NewScene("ED6_DT21/E0111   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3AF2")

    NewScene("ED6_DT21/E0200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3AFB")

    NewScene("ED6_DT21/E0400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3B04")

    NewScene("ED6_DT21/E0600   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3B0D")

    NewScene("ED6_DT21/E0610   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3B16")

    NewScene("ED6_DT21/E0700   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3B1F")

    OP_5F(0x3)
    Jump("loc_3B25")

    label("loc_3B25")

    Jump("loc_3DC7")

    label("loc_3B28")


    AnonymousTalk(    #45
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "E0300 埃尔赛尤外观测试\x01",                                       # 0
            "E0301 埃尔赛尤外观 云上、全景、（以OPS切换）\x01",                 # 1
            "E0310 埃尔赛尤内部 甲板连络通路·驾驶室连络通路·驾驶室\x01",      # 2
            "E0311 埃尔赛尤内部 连络通路１·作战会议室·休息室\x01",            # 3
            "E0312 埃尔赛尤内部 连络通路２·工房·货舱通路·货舱\x01",          # 4
            "E0313 埃尔赛尤内部 船仓\x01",                                      # 5
            "取消\x01",                                                         # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3C5E"),
        (1, "loc_3C67"),
        (2, "loc_3C70"),
        (3, "loc_3C79"),
        (4, "loc_3C82"),
        (5, "loc_3C8B"),
        (SWITCH_DEFAULT, "loc_3C94"),
    )


    label("loc_3C5E")

    NewScene("ED6_DT21/E0300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3C67")

    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3C70")

    NewScene("ED6_DT21/E0310   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3C79")

    NewScene("ED6_DT21/E0311   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3C82")

    NewScene("ED6_DT21/E0312   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3C8B")

    NewScene("ED6_DT21/E0313   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3C94")

    OP_5F(0x3)
    Jump("loc_3C9A")

    label("loc_3C9A")

    Jump("loc_3DC7")

    label("loc_3C9D")


    AnonymousTalk(    #46
        "\x06哪里？\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "Sky Books Test\x01",                # 0
            "E0800 空中∶龙＋军用飞船\x01",      # 1
            "E0810 空中∶龙＋军用飞船\x01",      # 2
            "E0811 空中∶夜晚\x01",              # 3
            "E0900 水上∶龙＋埃尔赛尤\x01",      # 4
            "E0901 水上∶夜间船\x01",            # 5
            "E1000 心象风景事件专用\x01",        # 6
            "取消\x01",                          # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3D72"),
        (1, "loc_3D7B"),
        (2, "loc_3D84"),
        (3, "loc_3D8D"),
        (4, "loc_3D96"),
        (5, "loc_3D9F"),
        (6, "loc_3DA8"),
        (SWITCH_DEFAULT, "loc_3DB1"),
    )


    label("loc_3D72")

    NewScene("ED6_DT21/E0500   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3D7B")

    NewScene("ED6_DT21/E0800   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3D84")

    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3D8D")

    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3D96")

    NewScene("ED6_DT21/E0900   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3D9F")

    NewScene("ED6_DT21/E0901   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3DA8")

    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3DB1")

    OP_5F(0x3)
    Jump("loc_3DB7")

    label("loc_3DB7")

    Jump("loc_3DC7")

    label("loc_3DBA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3DC7")

    label("loc_3DC7")

    Jump("loc_3906")

    label("loc_3DCA")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_38FC end

    def Function_14_3DDA(): pass

    label("Function_14_3DDA")

    EventBegin(0x0)
    OP_DA()
    OP_56(0x0)
    OP_5F(0x0)
    OP_5F(0x1)

    AnonymousTalk(    #47
        "\x06哪个？\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3DF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FFB")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        10,
        100,
        1,
        (
            "片头\x01",                          # 0
            "古罗力亚斯登场\x01",                # 1
            "辉之环出现，导力停止现象\x01",      # 2
            "古罗力亚斯袭击\x01",                # 3
            "辉之环上空\x01",                    # 4
            "埃尔赛尤击落\x01",                  # 5
            "辉之环崩溃\x01",                    # 6
            "取消\x01",                          # 7
        )
    )

    MenuEnd(0x0)
    OP_5F(0x2)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3EA7")
    Jump("loc_3FFB")

    label("loc_3EA7")

    FadeToDark(2000, 0, -1)
    OP_20(0x3E8)
    OP_0D()
    OP_21()
    OP_C4(0x0, 0x10)
    FadeToBright(10, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3EED"),
        (1, "loc_3F03"),
        (2, "loc_3F19"),
        (3, "loc_3F6C"),
        (4, "loc_3F82"),
        (5, "loc_3F98"),
        (6, "loc_3FAE"),
        (SWITCH_DEFAULT, "loc_3FC4"),
    )


    label("loc_3EED")

    PlayMovie(0x0, "ed6_2_op.avi", 0x7, 0x0)
    Jump("loc_3FC4")

    label("loc_3F03")

    PlayMovie(0x0, "ED6_DT40.dat", 0x1C, 0x1)
    Jump("loc_3FC4")

    label("loc_3F19")

    PlayMovie(0x0, "ED6_DT41.dat", 0x82, 0x1)
    Sleep(1000)
    OP_56(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F56")
    FadeToDark(2000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToBright(1, 0)
    OP_0D()

    label("loc_3F56")

    PlayMovie(0x0, "ED6_DT42.dat", 0x0, 0x1)
    Jump("loc_3FC4")

    label("loc_3F6C")

    PlayMovie(0x0, "ED6_DT43.dat", 0x77, 0x1)
    Jump("loc_3FC4")

    label("loc_3F82")

    PlayMovie(0x0, "ED6_DT44.dat", 0x83, 0x1)
    Jump("loc_3FC4")

    label("loc_3F98")

    PlayMovie(0x0, "ED6_DT45.dat", 0x84, 0x1)
    Jump("loc_3FC4")

    label("loc_3FAE")

    PlayMovie(0x0, "ED6_DT46.dat", 0x85, 0x1)
    Jump("loc_3FC4")

    label("loc_3FC4")

    Sleep(1000)
    OP_56(0x2)
    FadeToDark(2000, 0, -1)
    OP_20(0x7D0)
    OP_21()
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    Sleep(500)
    OP_C4(0x1, 0x10)
    FadeToBright(10, 0)
    OP_0D()
    Jump("loc_3DF9")

    label("loc_3FFB")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_3DDA end

    SaveToFile()

Try(main)
