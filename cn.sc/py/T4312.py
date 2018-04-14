from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4312   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4312.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '@FileName',                            # 8
        '管家雷蒙德',                           # 9
        '希德中校',                             # 10
        '贝尔克副队长',                         # 11
        '西莫鲁',                               # 12
        '王国军士兵',                           # 13
        '妮娜',                                 # 14
        '王国军士兵',                           # 15
        '王国军士兵',                           # 16
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
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01570 ._CH',             # 00
        'ED6_DT27/CH03590 ._CH',             # 01
        'ED6_DT07/CH01600 ._CH',             # 02
        'ED6_DT07/CH01350 ._CH',             # 03
        'ED6_DT07/CH01640 ._CH',             # 04
        'ED6_DT07/CH01770 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01570P._CP',             # 00
        'ED6_DT27/CH03590P._CP',             # 01
        'ED6_DT07/CH01600P._CP',             # 02
        'ED6_DT07/CH01350P._CP',             # 03
        'ED6_DT07/CH01640P._CP',             # 04
        'ED6_DT07/CH01770P._CP',             # 05
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -9300,
        Z                   = 0,
        Y                   = 400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 15260,
        Z                   = 0,
        Y                   = -1160,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 7340,
        Z                   = 0,
        Y                   = 58660,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -49260,
        Z                   = 0,
        Y                   = 20160,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -53120,
        Z                   = 0,
        Y                   = 20160,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 250,
        TriggerY            = 70040,
        TriggerRange        = 500,
        ActorX              = 0,
        ActorZ              = 1250,
        ActorY              = 70040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1FE",          # 00, 0
        "Function_1_30D",          # 01, 1
        "Function_2_319",          # 02, 2
        "Function_3_496",          # 03, 3
        "Function_4_543",          # 04, 4
        "Function_5_BCC",          # 05, 5
        "Function_6_CB0",          # 06, 6
        "Function_7_F38",          # 07, 7
        "Function_8_109D",         # 08, 8
        "Function_9_1152",         # 09, 9
        "Function_10_1260",        # 0A, 10
        "Function_11_15A8",        # 0B, 11
        "Function_12_237B",        # 0C, 12
        "Function_13_23AE",        # 0D, 13
        "Function_14_23F6",        # 0E, 14
        "Function_15_243E",        # 0F, 15
        "Function_16_2486",        # 10, 16
        "Function_17_24CE",        # 11, 17
        "Function_18_269C",        # 12, 18
        "Function_19_3298",        # 13, 19
        "Function_20_3331",        # 14, 20
    )


    def Function_0_1FE(): pass

    label("Function_0_1FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_219")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_216")
    ClearChrFlags(0xC, 0x80)

    label("loc_216")

    Jump("loc_2D2")

    label("loc_219")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_254")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 900, 0, 66800, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_2D2")

    label("loc_254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_299")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 900, 0, 66800, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -840, 0, 66800, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_2D2")

    label("loc_299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2B2")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_2D2")

    label("loc_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 2)), scpexpr(EXPR_END)), "loc_2C6")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_2D2")

    label("loc_2C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 4)), scpexpr(EXPR_END)), "loc_2D2")
    ClearChrFlags(0xD, 0x80)

    label("loc_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2E8")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 18)
    Jump("loc_30C")

    label("loc_2E8")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2F4"),
        (SWITCH_DEFAULT, "loc_30C"),
    )


    label("loc_2F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_309")
    SetMapFlags(0x10000000)
    Event(0, 11)

    label("loc_309")

    Jump("loc_30C")

    label("loc_30C")

    Return()

    # Function_0_1FE end

    def Function_1_30D(): pass

    label("Function_1_30D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_318")
    OP_64(0x0, 0x1)

    label("loc_318")

    Return()

    # Function_1_30D end

    def Function_2_319(): pass

    label("Function_2_319")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33E")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_480")

    label("loc_33E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_357")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_480")

    label("loc_357")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_370")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_480")

    label("loc_370")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_389")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_480")

    label("loc_389")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A2")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_480")

    label("loc_3A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BB")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_480")

    label("loc_3BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D4")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_480")

    label("loc_3D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ED")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_480")

    label("loc_3ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_406")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_480")

    label("loc_406")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41F")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_480")

    label("loc_41F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_438")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_480")

    label("loc_438")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_451")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_480")

    label("loc_451")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46A")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_480")

    label("loc_46A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_480")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_480")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_495")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_480")

    label("loc_495")

    Return()

    # Function_2_319 end

    def Function_3_496(): pass

    label("Function_3_496")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_542")
    OP_8E(0xFE, 0x3B9C, 0x0, 0xFFFFFB78, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFC464, 0x0, 0xFFFFFB78, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFBEEC, 0x0, 0xFFFFF664, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFBEEC, 0x0, 0xFFFFF0EC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFC464, 0x0, 0xFFFFEC14, 0x7D0, 0x0)
    OP_8E(0xFE, 0x3B9C, 0x0, 0xFFFFEC14, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4114, 0x0, 0xFFFFF0EC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4114, 0x0, 0xFFFFF664, 0x7D0, 0x0)
    Jump("Function_3_496")

    label("loc_542")

    Return()

    # Function_3_496 end

    def Function_4_543(): pass

    label("Function_4_543")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_840")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CB, 7)), scpexpr(EXPR_END)), "loc_5AC")

    ChrTalk(    #0
        0x9,
        (
            "#701F签字仪式的警备\x01",
            "一定会完成好的。\x02\x03",

            "如果去柏斯地区\x01",
            "一定要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83D")

    label("loc_5AC")


    ChrTalk(    #1
        0x9,
        (
            "#701F呀，是艾丝蒂尔你们啊。\x02\x03",

            "此次事件的解决要\x01",
            "多谢你们的协助了。\x02\x03",

            "也让我向你们道谢吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1000F哪里，我们才是\x01",
            "若没有尤莉亚小姐前来\x01",
            "真不知道会变成怎样……\x02\x03",

            "希德中校把尤莉亚小姐\x01",
            "叫来的对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "#701F哈哈，是啊……\x02\x03",

            "#703F不过，一切都是有你们\x01",
            "配合才能成功的。\x02\x03",

            "#701F希望今后军方和协会\x01",
            "也能多多协作。\x02\x03",

            "特别是在对付『结社』方面，对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1000F是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "#701F艾丝蒂尔你们\x01",
            "现在就要离开王都吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1000F嗯，预定接下来要去\x01",
            "特务兵出现的柏斯地区。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        (
            "#703F果然，是这样啊……\x02\x03",

            "#700F摩尔根将军似乎也在柏斯\x01",
            "开始了大规模的搜索。\x02\x03",

            "你们也要\x01",
            "多加小心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1000F谢谢，希德中校\x01",
            "也要在签字仪式的警备上加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        (
            "#701F啊啊，谢谢。\x01",
            "一定会完成好的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x165F)

    label("loc_83D")

    Jump("loc_BC8")

    label("loc_840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_B3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CC, 0)), scpexpr(EXPR_END)), "loc_8CD")

    ChrTalk(    #10
        0x9,
        (
            "#703F话说回来没想到情报部\x01",
            "居然潜藏在柏斯地区。\x02\x03",

            "#700F能够逃过那个摩尔根将军的搜索，\x01",
            "潜伏起来真不知是不是该佩服一下……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B39")

    label("loc_8CD")


    ChrTalk(    #11
        0x9,
        (
            "#703F话说回来没想到情报部\x01",
            "居然潜藏在柏斯地区。\x02\x03",

            "#700F能够逃过那个摩尔根将军的搜索，\x01",
            "潜伏起来真不知是不是该佩服一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x12F,
        (
            "#264F……那个情报部的\x01",
            "很擅长躲猫猫吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x12F, 400)

    ChrTalk(    #13
        0x9,
        (
            "#701F因为他们是为了能在各种\x01",
            "状况下都能收集情报\x01",
            "而接受过特殊训练的部队嘛。\x02\x03",

            "#700F潜伏在敌阵中的\x01",
            "野外生存技术应该也很擅长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x12F,
        (
            "#265F那么，就让玲和特务兵\x01",
            "用躲猫猫来决一胜负！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        "#702F躲、躲猫猫？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12F, 400)

    ChrTalk(    #16
        0x101,
        "#1016F这、这实在有点勉强呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0x101, 400)

    ChrTalk(    #17
        0x12F,
        (
            "#264F哎呀，为什么？\x02\x03",

            "#263F要是躲猫猫\x01",
            "玲有自信绝对不会输的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1015F这个倒确实\x01",
            "很可能是玲会赢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        (
            "#701F哈哈，虽然对不起小姑娘\x01",
            "但那些人可不会陪你玩啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x12F,
        (
            "#267F是吗？\x01",
            "真不好玩……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1660)

    label("loc_B39")

    Jump("loc_BC8")

    label("loc_B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_BC8")

    ChrTalk(    #21
        0x9,
        (
            "#700F潜伏起来的情报部\x01",
            "余党在这个时期现身……\x02\x03",

            "问题就是这个事件\x01",
            "是否和签字仪式有关了……\x02\x03",

            "#703F无论如何，都需要\x01",
            "再进一步的材料。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC8")

    TalkEnd(0x9)
    Return()

    # Function_4_543 end

    def Function_5_BCC(): pass

    label("Function_5_BCC")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_C60")

    ChrTalk(    #22
        0xFE,
        (
            "发现情报部的\x01",
            "据说是２人组合的游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "要是协会的王都支部，\x01",
            "说不定会有新的信息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "你们赶快\x01",
            "返回格兰赛尔就好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAC")

    label("loc_C60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_CAC")

    ChrTalk(    #25
        0xFE,
        (
            "现场虽说在柏斯，\x01",
            "可能会要求支援哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "必须保持紧张才行啊……\x02",
    )

    CloseMessageWindow()

    label("loc_CAC")

    TalkEnd(0xA)
    Return()

    # Function_5_BCC end

    def Function_6_CB0(): pass

    label("Function_6_CB0")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_E5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CB, 6)), scpexpr(EXPR_END)), "loc_CF7")

    ChrTalk(    #27
        0xFE,
        (
            "无论如何……这孩子\x01",
            "就拜托大家了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E58")

    label("loc_CF7")

    TurnDirection(0xFE, 0x12F, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)

    ChrTalk(    #28
        0xFE,
        "哎呀，那孩子是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "终于～出来啦～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x12F,
        (
            "#261F哈哈哈，女佣姐姐\x01",
            "躲猫猫真好玩。\x02\x03",

            "#260F玲现在\x01",
            "要去协会了。\x02\x03",

            "在那里等爸爸和妈妈\x01",
            "来接我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "哎……哎呀，是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "……想玩躲猫猫了，\x01",
            "就再来这里哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "我会拜托雷蒙德先生的,\x01",
            "你想玩多久就陪你多久。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x12F,
        (
            "#261F真的？\x01",
            "谢谢，大姐姐。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x165E)

    label("loc_E58")

    Jump("loc_F34")

    label("loc_E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 2)), scpexpr(EXPR_END)), "loc_F34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_EC2")

    ChrTalk(    #36
        0xFE,
        (
            "那孩子真是的，\x01",
            "把大人耍着玩～……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "要是出来了要打屁股一百下\x01",
            "作为惩罚，哼哼！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F34")

    label("loc_EC2")


    ChrTalk(    #38
        0xFE,
        (
            "嗯～似乎没有\x01",
            "藏在这附近呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "那孩子真是的，\x01",
            "把大人耍着玩～……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "难不成已经被雷蒙德先生\x01",
            "发现了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_F34")

    TalkEnd(0xB)
    Return()

    # Function_6_CB0 end

    def Function_7_F38(): pass

    label("Function_7_F38")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_F8E")

    ChrTalk(    #41
        0xFE,
        (
            "一直收不到\x01",
            "情报真是不安啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "希望导力器\x01",
            "早日能够使用。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F8E")

    Jump("loc_1099")

    label("loc_F91")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1099")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_101B")

    ChrTalk(    #43
        0xFE,
        (
            "发生事件那天柏斯\x01",
            "似乎连空贼都出现了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "空贼就是那次武术大会\x01",
            "赢了不少场的家伙们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "希望别出大事……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1099")

    label("loc_101B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1099")

    ChrTalk(    #46
        0xFE,
        (
            "今天早上，去艾尔贝周游道\x01",
            "扫荡了一下魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "嗯，就是在警备正式化之前\x01",
            "类似演习一样吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "作为热身\x01",
            "应该正好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1099")

    TalkEnd(0xC)
    Return()

    # Function_7_F38 end

    def Function_8_109D(): pass

    label("Function_8_109D")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_114E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_10F8")

    ChrTalk(    #49
        0xFE,
        (
            "希德中校的话，\x01",
            "在这个房间里呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "要去见他的话，\x01",
            "请进吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_114E")

    label("loc_10F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1135")

    ChrTalk(    #51
        0xFE,
        (
            "据说要采取第２种警戒体制，\x01",
            "到底发生了什么事？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_114E")

    label("loc_1135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_114E")

    ChrTalk(    #52
        0xFE,
        "工作辛苦了！\x02",
    )

    CloseMessageWindow()

    label("loc_114E")

    TalkEnd(0xE)
    Return()

    # Function_8_109D end

    def Function_9_1152(): pass

    label("Function_9_1152")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_125C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_11B4")

    ChrTalk(    #53
        0xFE,
        (
            "哟，你们和亲卫队配合\x01",
            "逮捕了特务兵是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "今天找希德中校有事吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_125C")

    label("loc_11B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_121A")

    ChrTalk(    #55
        0xFE,
        "第２种警戒体制……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "果然是有妨碍\x01",
            "签字仪式的家伙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "好像听到\x01",
            "情报部什么的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125C")

    label("loc_121A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_125C")

    ChrTalk(    #58
        0xFE,
        (
            "副队长神色大变，\x01",
            "冲进了房间……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "到底出什么事了？\x02",
    )

    CloseMessageWindow()

    label("loc_125C")

    TalkEnd(0xF)
    Return()

    # Function_9_1152 end

    def Function_10_1260(): pass

    label("Function_10_1260")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_12FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_12B5")

    ChrTalk(    #60
        0xFE,
        (
            "……嗯～\x01",
            "擦的还不够啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "必须更加用力的磨！\x02",
    )

    CloseMessageWindow()
    Jump("loc_12F8")

    label("loc_12B5")


    ChrTalk(    #62
        0xFE,
        (
            "露露露啦⊙\x01",
            "露露露啦～⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "擦得亮晶晶～⊙\x01",
            "心情够舒畅～⊙\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_12F8")

    Jump("loc_15A4")

    label("loc_12FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 4)), scpexpr(EXPR_END)), "loc_15A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_135A")

    ChrTalk(    #64
        0xFE,
        (
            "这里是举行互不侵犯条约签字仪式\x01",
            "的纹章之间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "所以自然鼓起劲\x01",
            "打扫了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15A4")

    label("loc_135A")


    ChrTalk(    #66
        0xFE,
        (
            "这里是举行互不侵犯条约签字仪式\x01",
            "的纹章之间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1011F哦～是这样啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "是的，当天帝国\x01",
            "和共和国的大使不用说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "我利贝尔王国的代表\x01",
            "也都在这里集合。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1015F记得政变的时候来过，\x01",
            "不过都没空好好看。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14EB")

    ChrTalk(    #71
        0x105,
        (
            "#048F呵呵，真怀念啊。\x02\x03",

            "在这里被抓住的我们\x01",
            "多亏了大家帮助。\x02\x03",

            "在那个时候的房间里举行\x01",
            "签字仪式真是感慨良深啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1001F嗯嗯⊙\x02\x03",

            "#1006F不过看起来\x01",
            "真是格调高贵的房间啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_151A")

    label("loc_14EB")


    ChrTalk(    #73
        0x101,
        (
            "#1006F这样重新来看\x01",
            "真是格调高贵的房间啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_151A")


    ChrTalk(    #74
        0xFE,
        "是的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "所以自然鼓起劲\x01",
            "打扫了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#1016F啊哈哈，虽然我不擅长打扫,\x01",
            "但很明白这种心情。\x02\x03",

            "#1001F那么，加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "是，谢谢！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_15A4")

    TalkEnd(0xD)
    Return()

    # Function_10_1260 end

    def Function_11_15A8(): pass

    label("Function_11_15A8")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15BF")
    Call(0, 19)
    Call(0, 20)

    label("loc_15BF")

    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 0, 0, -1790, 90)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_67(0, 5220, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(37000, 0)
    OP_6E(280, 0)
    OP_69(0x8, 0x0)
    FadeToBright(2000, 0)
    OP_43(0x8, 0x1, 0x0, 0xC)
    OP_0D()

    ChrTalk(    #78
        0x8,
        "唉，不行了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "游击士就要来了,\x01",
            "跑去哪里了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 0, 0, -9300, 0)

    ChrTalk(    #80
        0x101,
        "#1P请问～\x02",
    )

    CloseMessageWindow()
    OP_44(0x8, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x8, 180, 400)

    ChrTalk(    #81
        0x8,
        (
            "啊，是是。\x01",
            "怎么了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16C6():
        OP_6D(630, 0, -3120, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_16C6)
    OP_43(0x101, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0xE)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0xF)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x10)
    WaitChrThread(0xF7, 0x1)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1796")

    ChrTalk(    #82
        0x8,
        (
            "#5P咦！？\x01",
            "你们不是……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x108, 0x1)

    ChrTalk(    #83
        0x108,
        "#070F哟，好久不见啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1016F嘿嘿，你好。\x01",
            "看来记着呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17D7")

    label("loc_1796")


    ChrTalk(    #85
        0x8,
        (
            "#5P咦！？\x01",
            "记得你是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1016F嘿嘿，你好。\x01",
            "看来记着呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1940")

    ChrTalk(    #87
        0x8,
        "#5P哈哈，怎么可能忘记嘛！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        (
            "#5P怎么说都是把艾尔贝离宫\x01",
            "解放了的恩人嘛……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 400)

    ChrTalk(    #89
        0x8,
        "#5P咦，你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x105,
        "#542F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        (
            "#5P呀，哈哈……\x01",
            "没那回事啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        "#5P一定是其他很像的人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x105,
        (
            "#048F呵呵，难不成是\x01",
            "错认为你的恋人了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        "#5P没、没有的事！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    Sleep(500)

    ChrTalk(    #95
        0x8,
        (
            "#5P嗯，那么你们\x01",
            "是接受委托的游击士吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B7")

    label("loc_1940")


    ChrTalk(    #96
        0x8,
        "#5P哈哈，怎么可能忘记嘛！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        (
            "#5P怎么说都是把艾尔贝离宫\x01",
            "解放了的恩人嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        (
            "#5P那么你们\x01",
            "是接受委托的游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B7")


    ChrTalk(    #99
        0x101,
        (
            "#1011F嗯，是没错……\x02\x03",

            "到底怎么了？\x01",
            "似乎有什么难处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "#5P那是……\x01",
            "那个迷路的孩子的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x8,
        (
            "#5P突然说『玩躲猫猫吧』,\x01",
            "然后就不见了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        "#5P我正在拼命找她呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#1016F哎呀呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "#5P马、马上就会找到的,\x01",
            "你们在谈话室等等哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        "#5P知道地点吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#1015F那倒是记得……\x02\x03",

            "看来你似乎陷入苦战了呢,\x01",
            "要我们也帮忙找吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x8,
        "#5P咦……这好吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B6E")

    ChrTalk(    #108
        0x106,
        (
            "#051F嗯，这也算是\x01",
            "上了贼船了吧。\x02\x03",

            "说一下那小鬼的名字和特征吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC1")

    label("loc_1B6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BC1")

    ChrTalk(    #109
        0x103,
        (
            "#021F呵呵……\x01",
            "打铁就要趁热。\x02\x03",

            "#020F说一下那孩子的名字和特征吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC1")


    ChrTalk(    #110
        0x8,
        "#5P帮、帮大忙了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "#5P穿着轻飘飘的白裙子,\x01",
            "头上扎着黑色的丝带\x01",
            "１０岁左右的女孩子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x8,
        "#5P就是不知道叫什么名字。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#1004F不知道名字？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x8,
        (
            "#5P我怎么问她都说是『秘·密』\x01",
            "就是不告诉我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        (
            "#5P以为她是和家人一起来的,\x01",
            "可也找不到类似的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        (
            "#5P实在是发愁\x01",
            "就向协会求助了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#1016F是、是这样啊。\x02\x03",

            "#1000F不过爱玩躲猫猫\x01",
            "应该是挺精神的女孩子吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        "#5P嗯～说精神……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x8,
        (
            "#5P倒是有点小大人样\x01",
            "但又阴晴无常的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x8,
        (
            "#5P把大人耍着玩\x01",
            "还觉得很开心。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DD3")

    ChrTalk(    #121
        0x104,
        (
            "#035F哦哦……\x01",
            "喜欢恶作剧的小猫型啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E45")

    label("loc_1DD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E10")

    ChrTalk(    #122
        0x103,
        (
            "#027F就是那种喜欢恶作剧的\x01",
            "小猫类型吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E45")

    label("loc_1E10")


    ChrTalk(    #123
        0x101,
        (
            "#1015F嗯～就是所谓的\x01",
            "喜欢恶作剧的小猫那种感觉？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E45")


    ChrTalk(    #124
        0x8,
        "#5P对，就是这种感觉！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x8,
        (
            "#5P唉～真是的,\x01",
            "到底跑哪里去了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x8,
        (
            "#5P大概，没出这栋\x01",
            "建筑物吧……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F20")

    ChrTalk(    #127
        0x104,
        (
            "#030F这么说，包括中庭在内的\x01",
            "所有房间就是搜索对象吗。\x02\x03",

            "#031F呼，说不定很适合\x01",
            "给小猫咪躲猫猫呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FF8")

    label("loc_1F20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F88")

    ChrTalk(    #128
        0x108,
        (
            "#070F这么说，包括中庭在内的\x01",
            "所有房间就是搜索对象吧。\x02\x03",

            "确实很适合\x01",
            "躲猫猫也不一定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FF8")

    label("loc_1F88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FF8")

    ChrTalk(    #129
        0x105,
        (
            "#040F这么说，包括中庭在内的\x01",
            "所有房间就是搜索对象吧。\x02\x03",

            "#041F呵呵，确实很适合\x01",
            "躲猫猫也不一定。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF8")


    ChrTalk(    #130
        0x8,
        (
            "#5P我暂时回谈话室\x01",
            "等那个孩子吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        "#5P找到了希望能带来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#1006F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)

    def lambda_205E():
        OP_6D(-1400, 0, -3120, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_205E)

    def lambda_2076():

        label("loc_2076")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2076")

    QueueWorkItem2(0x101, 1, lambda_2076)

    def lambda_2087():

        label("loc_2087")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2087")

    QueueWorkItem2(0xF7, 1, lambda_2087)

    def lambda_2098():

        label("loc_2098")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2098")

    QueueWorkItem2(0xF8, 1, lambda_2098)

    def lambda_20A9():

        label("loc_20A9")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_20A9")

    QueueWorkItem2(0xF9, 1, lambda_20A9)
    OP_8E(0x8, 0xFFFFDCB0, 0x0, 0xFFFFFACE, 0xBB8, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    WaitChrThread(0x101, 0x3)
    Sleep(500)

    def lambda_20ED():
        OP_6D(-260, 0, -4800, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_20ED)

    def lambda_2105():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2105)
    Sleep(50)

    def lambda_2118():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2118)
    Sleep(50)

    def lambda_212B():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_212B)
    Sleep(50)

    def lambda_213E():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_213E)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #133
        0x101,
        (
            "#1006F#5P好了～来寻找\x01",
            "逃跑的小猫咪吧。\x02\x03",

            "说是穿着白色甩袖\x01",
            "配有黑色丝带的礼服吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21F9")

    ChrTalk(    #134
        0x107,
        (
            "#061F呵呵……\x01",
            "似乎很快就能找到了。\x02\x03",

            "是怎样的孩子呢，真令人期待啊⊙\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_224D")

    label("loc_21F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_224D")

    ChrTalk(    #135
        0x105,
        (
            "#041F呵呵，似乎是很快\x01",
            "就能找到的外表呢。\x02\x03",

            "真想看看是怎样的孩子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_224D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_228C")

    ChrTalk(    #136
        0x106,
        (
            "#051F总之还是在\x01",
            "建筑物里搜索一遍看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C8")

    label("loc_228C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22C8")

    ChrTalk(    #137
        0x103,
        (
            "#020F总之还是在\x01",
            "建筑物里搜索一遍看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C8")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(430, 0, -4710, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 430, 0, -4710, 0)
    SetChrPos(0x1, 430, 0, -4710, 0)
    SetChrPos(0x2, 430, 0, -4710, 0)
    SetChrPos(0x3, 430, 0, -4710, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x160D)
    OP_28(0x89, 0x1, 0x2)
    OP_28(0x89, 0x1, 0x4)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_11_15A8 end

    def Function_12_237B(): pass

    label("Function_12_237B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23AD")
    OP_8C(0xFE, 0, 300)
    OP_8C(0xFE, 270, 300)
    Sleep(1000)
    OP_8C(0xFE, 0, 300)
    OP_8C(0xFE, 90, 300)
    Sleep(1000)
    Jump("Function_12_237B")

    label("loc_23AD")

    Return()

    # Function_12_237B end

    def Function_13_23AE(): pass

    label("Function_13_23AE")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, 0, -11240, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_23D5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_23D5)
    OP_8E(0xFE, 0x1AE, 0x0, 0xFFFFED9A, 0x9C4, 0x0)
    Return()

    # Function_13_23AE end

    def Function_14_23F6(): pass

    label("Function_14_23F6")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, 0, -11240, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_241D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_241D)
    OP_8E(0xFE, 0xFFFFFD6C, 0x0, 0xFFFFED68, 0x9C4, 0x0)
    Return()

    # Function_14_23F6 end

    def Function_15_243E(): pass

    label("Function_15_243E")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, 0, -11240, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2465():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2465)
    OP_8F(0xFE, 0xFFFFF984, 0x0, 0xFFFFEA3E, 0x9C4, 0x0)
    Return()

    # Function_15_243E end

    def Function_16_2486(): pass

    label("Function_16_2486")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, 0, -11240, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_24AD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_24AD)
    OP_8F(0xFE, 0x438, 0x0, 0xFFFFEAB6, 0x9C4, 0x0)
    Return()

    # Function_16_2486 end

    def Function_17_24CE(): pass

    label("Function_17_24CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2635")
    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #138
        "\x07\x05放着精致的讲台。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #139
        "\x07\x05看看里面似乎没有任何人藏着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #140
        0x101,
        (
            "#1019F唔……\x01",
            "本来以为猜对了的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2595")

    ChrTalk(    #141
        0x105,
        (
            "#048F呼呼，挺厉害的\x01",
            "小猫咪嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2627")

    label("loc_2595")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25D2")

    ChrTalk(    #142
        0x108,
        (
            "#071F哈哈，看来没那么简单\x01",
            "抓到尾巴呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2627")

    label("loc_25D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2601")

    ChrTalk(    #143
        0x106,
        (
            "#051F嘿……\x01",
            "挺厉害的嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2627")

    label("loc_2601")


    ChrTalk(    #144
        0x103,
        (
            "#027F呵呵……\x01",
            "挺厉害的小猫咪嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2627")

    EventEnd(0x1)
    OP_A2(0x1610)
    OP_28(0x89, 0x1, 0x20)
    Jump("loc_269B")

    label("loc_2635")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #145
        "\x07\x05放着精致的讲台。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #146
        "\x07\x05看看里面似乎没有任何人藏着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_269B")

    Return()

    # Function_17_24CE end

    def Function_18_269C(): pass

    label("Function_18_269C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26AF")
    Call(0, 19)

    label("loc_26AF")

    RemoveParty(0x5, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x9, 0xFF)
    AddParty(0x0, 0xF6, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_26CA")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_26CE")

    label("loc_26CA")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_26CE")

    OP_4A(0x9, 255)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, -930, 0, 66950, 90)
    SetChrPos(0xF7, -1030, 0, 65950, 90)
    SetChrPos(0x9, 1000, 0, 66810, 270)
    SetChrFlags(0xD, 0x80)
    OP_6D(1460, 0, 74990, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)

    def lambda_2797():
        OP_6D(720, 0, 67490, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2797)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #147
        0x9,
        (
            "#702F原来如此……\x01",
            "这真是充实的报告书啊。\x02\x03",

            "#701F真是帮大忙了。\x01",
            "竟然调查得这么细致。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        (
            "#1015F#6P嗯、嗯……\x02\x03",

            "这犯人最后不能确定,\x01",
            "说实话，是有点遗憾……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x9,
        (
            "#701F作为调查报告已经充分过头了。\x02\x03",

            "在这个阶段能找到恐吓犯\x01",
            "我们也没想过。\x02\x03",

            "要说起来，对今后的警备\x01",
            "是必要的参考。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2914")

    ChrTalk(    #150
        0x106,
        (
            "#051F这么说我们就安心了。\x02\x03",

            "那么，王国军方面\x01",
            "有什么进展吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2954")

    label("loc_2914")


    ChrTalk(    #151
        0x103,
        (
            "#020F这么说我们就安心了。\x02\x03",

            "那么，王国军方面\x01",
            "有什么进展吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2954")


    ChrTalk(    #152
        0x9,
        (
            "#701F嗯，昨天警备体制的\x01",
            "第一阶段完成了吧。\x02\x03",

            "此后，条约签字仪式结束之前\x01",
            "这个艾尔贝离宫将成为警备本部。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        (
            "#1006F#6P所以士兵们\x01",
            "聚集了不少呢。\x02\x03",

            "这么说来，周游道上\x01",
            "也几乎没有魔兽了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x9,
        (
            "#701F今天早晨，刚刚实施过\x01",
            "大规模的扫荡作战。\x02\x03",

            "条约签字仪式之前\x01",
            "应该会定期执行。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2A9D")

    ChrTalk(    #155
        0x106,
        (
            "#053F平时就这么做的话\x01",
            "也帮了我们的大忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ACD")

    label("loc_2A9D")


    ChrTalk(    #156
        0x103,
        (
            "#027F平时就这么做的话\x01",
            "也帮了协会的大忙了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ACD")


    ChrTalk(    #157
        0x9,
        (
            "#701F哈哈……\x01",
            "这话说得真刺耳啊。\x02\x03",

            "#702F对了，关于昨天说的\x01",
            "女孩子的父母……\x02\x03",

            "通知发到了各地的关所\x01",
            "但至今还没收到信息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        (
            "#1015F#6P这样啊……\x01",
            "只有耐心等待了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x9,
        (
            "#701F我们如果收到情报，\x01",
            "也会马上告知协会。\x02\x03",

            "总之，恐吓信的调查\x01",
            "做到这份上就足够了。\x02\x03",

            "稍后会把报酬\x01",
            "汇给协会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        (
            "#1006F#6P嗯，拜托了。\x02\x03",

            "#1015F不过……\x01",
            "今后打算怎样做？\x02\x03",

            "我们，也这样留在王都\x01",
            "帮忙警戒好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x9,
        (
            "#700F如果留在王都\x01",
            "能帮忙就再好不过了。\x02\x03",

            "#703F只是你们也很忙\x01",
            "我们也能理解。\x02\x03",

            "不会强人所难的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        (
            "#1015F#6P嗯……\x02\x03",

            "#1006F还有玲的事没解决，\x01",
            "和艾南哥哥商量看看？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2D18")

    ChrTalk(    #163
        0x106,
        "#051F啊啊，就这么试试吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D37")

    label("loc_2D18")


    ChrTalk(    #164
        0x103,
        "#020F啊啊，就这么试试吧。\x02",
    )

    CloseMessageWindow()

    label("loc_2D37")

    OP_4A(0xA, 255)
    SetChrPos(0xA, 970, 0, 58600, 0)
    ClearChrFlags(0xA, 0x80)

    NpcTalk(    #165
        0xA,
        "男人的声音",
        "#1P……打扰了！\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2D93():
        OP_6D(850, 0, 67000, 1000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2D93)

    def lambda_2DAB():
        OP_8E(0xFE, 0x406, 0x0, 0xFF8C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2DAB)

    def lambda_2DC6():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2DC6)
    Sleep(50)

    def lambda_2DD9():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2DD9)
    Sleep(50)

    def lambda_2DEC():

        label("loc_2DEC")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_2DEC")

    QueueWorkItem2(0x101, 2, lambda_2DEC)

    def lambda_2DFD():

        label("loc_2DFD")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_2DFD")

    QueueWorkItem2(0xF7, 2, lambda_2DFD)

    def lambda_2E0E():

        label("loc_2E0E")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_2E0E")

    QueueWorkItem2(0x9, 1, lambda_2E0E)
    WaitChrThread(0xA, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0xF7, 0x2)
    OP_44(0x9, 0x1)
    OP_8C(0x101, 90, 0)

    ChrTalk(    #166
        0x9,
        "#702F怎么，出什么事了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xA,
        "那个……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 315, 400)
    Sleep(500)
    OP_8C(0xA, 0, 400)
    Sleep(500)

    ChrTalk(    #168
        0x9,
        "#701F没问题，他们是来帮忙的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xA,
        "是，那么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xA,
        (
            "刚才从雷斯顿要塞\x01",
            "发来了导力通信联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xA,
        (
            "似乎是柏斯地区\x01",
            "出现了情报部的余党。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #172
        0x101,
        "#1020F咦咦咦！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2F86")

    ChrTalk(    #173
        0x106,
        "#052F说什么！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F9B")

    label("loc_2F86")


    ChrTalk(    #174
        0x103,
        "#023F说什么！？\x02",
    )

    CloseMessageWindow()

    label("loc_2F9B")


    ChrTalk(    #175
        0x9,
        "#700F唔，详细说说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xA,
        (
            "那个，最初时发现的\x01",
            "好像是协会的游击士……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xA,
        (
            "确切的现场状况\x01",
            "至今未能掌握。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xA,
        (
            "总之从司令部\x01",
            "发来了全王国军部队进入\x01",
            "第２种警戒体制的指示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x9,
        "#703F是吗，明白了。\x02",
    )

    CloseMessageWindow()

    def lambda_3065():
        OP_6D(720, 0, 67490, 1000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3065)
    TurnDirection(0x9, 0x101, 400)
    WaitChrThread(0x9, 0x2)

    ChrTalk(    #180
        0x9,
        (
            "#700F……看来我们彼此\x01",
            "都要开始忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_30F9")

    ChrTalk(    #181
        0x106,
        "#053F啊啊，是啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 0, 400)

    ChrTalk(    #182
        0x106,
        (
            "#050F艾丝蒂尔。\x01",
            "赶快回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_313B")

    label("loc_30F9")


    ChrTalk(    #183
        0x103,
        "#020F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 0, 400)

    ChrTalk(    #184
        0x103,
        (
            "#022F艾丝蒂尔。\x01",
            "立即返回协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_313B")

    OP_8C(0x101, 180, 400)

    ChrTalk(    #185
        0x101,
        "#1002F#5P嗯……！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    OP_8C(0xF7, 90, 400)

    ChrTalk(    #186
        0x101,
        (
            "#1006F#6P希德中校。\x01",
            "警备的工作，要加油哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x9,
        "#701F啊啊，你们也要加油。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(10, 0, 61900, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x9, 900, 0, 66800, 270)
    SetChrPos(0xA, -840, 0, 66800, 90)
    SetChrPos(0x101, 10, 0, 61900, 180)
    SetChrPos(0xF7, 10, 0, 61900, 180)
    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    OP_A2(0x162A)
    OP_28(0x8B, 0x1, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3263")
    OP_28(0x8A, 0x1, 0x20)
    Jump("loc_3270")

    label("loc_3263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3270")
    OP_28(0x8A, 0x1, 0x10)

    label("loc_3270")

    OP_28(0x8A, 0x1, 0x40)
    OP_28(0x8A, 0x1, 0x80)
    OP_28(0x8A, 0x1, 0x100)
    OP_28(0xC4, 0x4, 0x40)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_18_269C end

    def Function_19_3298(): pass

    label("Function_19_3298")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3312"),
        (1, "loc_3318"),
        (SWITCH_DEFAULT, "loc_331E"),
    )


    label("loc_3312")

    OP_A2(0x1200)
    Jump("loc_331E")

    label("loc_3318")

    OP_A2(0x1201)
    Jump("loc_331E")

    label("loc_331E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_332C")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_3330")

    label("loc_332C")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_3330")

    Return()

    # Function_19_3298 end

    def Function_20_3331(): pass

    label("Function_20_3331")

    ClearMapFlags(0x1)
    OP_6D(-3960, 0, -27940, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3374")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_3392")

    label("loc_3374")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_3392")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_20_3331 end

    SaveToFile()

Try(main)
