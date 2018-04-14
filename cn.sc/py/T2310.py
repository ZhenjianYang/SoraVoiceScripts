from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2310   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        '克拉姆',                               # 9
        '波利',                                 # 10
        '玛丽',                                 # 11
        '达尼艾尔',                             # 12
        '卢西亚',                               # 13
        '扎古',                                 # 14
        '阿梅莉娅',                             # 15
        '索雷诺',                               # 16
        '塞尔吉村长',                           # 17
        '目标用照相机',                         # 18
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
        'ED6_DT07/CH02590 ._CH',             # 00
        'ED6_DT07/CH02500 ._CH',             # 01
        'ED6_DT07/CH02630 ._CH',             # 02
        'ED6_DT07/CH02640 ._CH',             # 03
        'ED6_DT07/CH01070 ._CH',             # 04
        'ED6_DT07/CH01460 ._CH',             # 05
        'ED6_DT07/CH01050 ._CH',             # 06
        'ED6_DT07/CH01040 ._CH',             # 07
        'ED6_DT07/CH01000 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02590P._CP',             # 00
        'ED6_DT07/CH02500P._CP',             # 01
        'ED6_DT07/CH02630P._CP',             # 02
        'ED6_DT07/CH02640P._CP',             # 03
        'ED6_DT07/CH01070P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
        'ED6_DT07/CH01050P._CP',             # 06
        'ED6_DT07/CH01040P._CP',             # 07
        'ED6_DT07/CH01000P._CP',             # 08
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4440,
        Z                   = 0,
        Y                   = 5030,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -130,
        Z                   = 0,
        Y                   = 8460,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -32750,
        Z                   = 0,
        Y                   = 3570,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -28110,
        Z                   = 0,
        Y                   = 7510,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_232",          # 00, 0
        "Function_1_2AD",          # 01, 1
        "Function_2_2BD",          # 02, 2
        "Function_3_43A",          # 03, 3
        "Function_4_1430",         # 04, 4
        "Function_5_1916",         # 05, 5
        "Function_6_1B6B",         # 06, 6
        "Function_7_20E4",         # 07, 7
        "Function_8_2D17",         # 08, 8
    )


    def Function_0_232(): pass

    label("Function_0_232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_25E")
    OP_8C(0xE, 0, 0)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0x10, -30060, 0, 3800, 270)
    Jump("loc_299")

    label("loc_25E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_268")
    Jump("loc_299")

    label("loc_268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_283")
    SetChrPos(0x10, -27680, 0, 40800, 270)
    Jump("loc_299")

    label("loc_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_28D")
    Jump("loc_299")

    label("loc_28D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_299")
    SetChrFlags(0x10, 0x80)

    label("loc_299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2AC")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_2AC")

    Return()

    # Function_0_232 end

    def Function_1_2AD(): pass

    label("Function_1_2AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_2BC")
    OP_71(0x0, 0x4)
    OP_82(0x82, 0x0)

    label("loc_2BC")

    Return()

    # Function_1_2AD end

    def Function_2_2BD(): pass

    label("Function_2_2BD")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E2")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_424")

    label("loc_2E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FB")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_424")

    label("loc_2FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_314")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_424")

    label("loc_314")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_424")

    label("loc_32D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_346")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_424")

    label("loc_346")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35F")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_424")

    label("loc_35F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_378")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_424")

    label("loc_378")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_391")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_424")

    label("loc_391")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AA")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_424")

    label("loc_3AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C3")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_424")

    label("loc_3C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DC")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_424")

    label("loc_3DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F5")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_424")

    label("loc_3F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_424")

    label("loc_40E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_424")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_424")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_439")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_424")

    label("loc_439")

    Return()

    # Function_2_2BD end

    def Function_3_43A(): pass

    label("Function_3_43A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_73A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 5)), scpexpr(EXPR_END)), "loc_51C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4A9")

    ChrTalk(    #0
        0xFE,
        (
            "灯塔看守弗科特爷爷\x01",
            "最近好像都没看见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "爷爷也一把年纪了，\x01",
            "偶尔去看看他吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_519")

    label("loc_4A9")

    OP_A2(0x0)

    ChrTalk(    #2
        0xFE,
        (
            "这么说来，灯塔看守\x01",
            "弗科特爷爷还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "最近\x01",
            "好像都没看见啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "他也一把年纪了，\x01",
            "偶尔去看看他吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_519")

    Jump("loc_737")

    label("loc_51C")

    TurnDirection(0xFE, 0x101, 0)
    OP_A2(0x122D)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0xFE,
        (
            "哦，还以为是谁呢，\x01",
            "是那时的游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "去过孤儿院了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#1000F嗯，看过了。\x02\x03",

            "变得和原来一模一样\x01",
            "真是吃了一惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "嘿嘿，是吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "帮过忙的我们\x01",
            "也很得意呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "孩子们的笑容也回来了，\x01",
            "感觉总算解决了一件大事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "不过…\x01",
            "发生什么事件了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_685")

    ChrTalk(    #12
        0x106,
        (
            "#050F啊啊，是有点。\x02\x03",

            "姑且算是解决了，\x01",
            "可以放心啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BD")

    label("loc_685")


    ChrTalk(    #13
        0x103,
        (
            "#020F嗯嗯，是啊。\x02\x03",

            "姑且算是解决了，\x01",
            "可以放心了哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BD")

    TurnDirection(0xFE, 0xF7, 400)

    ChrTalk(    #14
        0xFE,
        (
            "呼，那就好。\x01",
            "平安无事最重要了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #15
        0xFE,
        (
            "那么再见，游击士们。\x01",
            "今后也要继续加油啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#1006F嗯，回头见。\x02",
    )

    CloseMessageWindow()

    label("loc_737")

    Jump("loc_142C")

    label("loc_73A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_A7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 5)), scpexpr(EXPR_END)), "loc_847")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7C0")

    ChrTalk(    #17
        0xFE,
        (
            "下任市长一定要\x01",
            "选个心灵纯净的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "不过上次大家\x01",
            "也一定都是这么想着投票的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "唉，政治真复杂。\x02",
    )

    CloseMessageWindow()
    Jump("loc_844")

    label("loc_7C0")

    OP_A2(0x0)

    ChrTalk(    #20
        0xFE,
        (
            "那个恶德市长被捕之后\x01",
            "已经过了相当长的时间\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "可以的话下任市长\x01",
            "选个心灵纯净的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "上次大家也都是这么想着\x01",
            "投票的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_844")

    Jump("loc_A78")

    label("loc_847")

    TurnDirection(0xFE, 0x101, 0)
    OP_A2(0x122D)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0xFE,
        (
            "哦，还以为是谁呢，\x01",
            "是那时的游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "看过孤儿院了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1000F嗯，看过了。\x02\x03",

            "变得和原来一模一样\x01",
            "真是吃了一惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "嘿嘿，是吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "帮过忙的我们\x01",
            "也很得意呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "孩子们的笑容也回来了，\x01",
            "感觉总算解决了一件大事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "不过…\x01",
            "发生什么事件了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9BA")

    ChrTalk(    #30
        0x106,
        (
            "#050F不，只是有些事\x01",
            "以防万一要调查一下。\x02\x03",

            "不是事件，放心吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FE")

    label("loc_9BA")


    ChrTalk(    #31
        0x103,
        (
            "#020F是有些事要调查，\x01",
            "不过事件性比较低。\x02\x03",

            "不用担心，没问题的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FE")

    TurnDirection(0xFE, 0xF7, 400)

    ChrTalk(    #32
        0xFE,
        (
            "呼，那就好。\x01",
            "平安无事最重要了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "那么再见，游击士们。\x01",
            "今后也要继续加油啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #34
        0x101,
        "#1006F嗯，回头见。\x02",
    )

    CloseMessageWindow()

    label("loc_A78")

    Jump("loc_142C")

    label("loc_A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_D8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 5)), scpexpr(EXPR_END)), "loc_B58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AFC")

    ChrTalk(    #35
        0xFE,
        (
            "我叔叔奥维德\x01",
            "是处理食材的商人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "总是到处转悠，\x01",
            "很少回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "那样的生活\x01",
            "对于我来说太困难了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B55")

    label("loc_AFC")

    OP_A2(0x0)

    ChrTalk(    #38
        0xFE,
        (
            "平安无事虽好，\x01",
            "但我也得早点找工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "虽然想在本地工作，\x01",
            "但很难找到好的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B55")

    Jump("loc_D89")

    label("loc_B58")

    TurnDirection(0xFE, 0x101, 0)
    OP_A2(0x122D)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #40
        0xFE,
        (
            "哦，还以为是谁呢，\x01",
            "是那时的游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "看过孤儿院了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1000F啊，看过了。\x02\x03",

            "变得和原来一模一样\x01",
            "真是吃了一惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "嘿嘿，是吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "帮过忙的我们\x01",
            "也很得意呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "孩子们的笑容也回来了，\x01",
            "感觉总算解决了一件大事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "不过…\x01",
            "发生什么事件了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_CCB")

    ChrTalk(    #47
        0x106,
        (
            "#050F不，只是有些事\x01",
            "以防万一要调查一下。\x02\x03",

            "不是事件，放心吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D0F")

    label("loc_CCB")


    ChrTalk(    #48
        0x103,
        (
            "#020F是有些事要调查，\x01",
            "不过事件性比较低。\x02\x03",

            "不用担心，没问题的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0F")

    TurnDirection(0xFE, 0xF7, 400)

    ChrTalk(    #49
        0xFE,
        (
            "呼，那就好。\x01",
            "平安无事最重要了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #50
        0xFE,
        (
            "那么再见，游击士们。\x01",
            "今后也要继续加油啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#1006F嗯，回头见。\x02",
    )

    CloseMessageWindow()

    label("loc_D89")

    Jump("loc_142C")

    label("loc_D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 6)), scpexpr(EXPR_END)), "loc_11B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 5)), scpexpr(EXPR_END)), "loc_DE5")

    ChrTalk(    #52
        0xFE,
        (
            "主日学校在村子南边的\x01",
            "风车小屋上呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "应该快结束了\x01",
            "去看看如何？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B3")

    label("loc_DE5")

    OP_A2(0x122D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_FD9")
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #54
        0xFE,
        (
            "哦，还以为是谁呢，\x01",
            "是那时的游击士们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "看过孤儿院了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x106,
        (
            "#051F啊啊，刚刚\x01",
            "从那边过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1000F变得和以前一样\x01",
            "真是吃了一惊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #58
        0xFE,
        "嘿嘿，是吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "帮过忙的我们\x01",
            "也很得意呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "孩子们的笑容也回来了，\x01",
            "这下总算解决一件大事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1015F啊，孩子们\x01",
            "来上主日学校了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "啊啊，在村子南边的\x01",
            "风车小屋上呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "应该快结束了\x01",
            "去看看如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x106,
        (
            "#050F南边的风车小屋啊……\x01",
            "好，去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#1006F那么，回头见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "哦，今后\x01",
            "要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B3")

    label("loc_FD9")

    TurnDirection(0xFE, 0x101, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0xFE,
        (
            "哦，还以为是谁呢，\x01",
            "是那时的游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "看过孤儿院了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1000F嗯，刚好\x01",
            "从那边过来。\x02\x03",

            "完全恢复了原样\x01",
            "真是吃了一惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "嘿嘿，是吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "帮过忙的我们\x01",
            "也很得意呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "孩子们的笑容也回来了，\x01",
            "这下总算解决一件大事了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1015F啊，孩子们\x01",
            "来上主日学校了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "啊啊，在村子南边的\x01",
            "风车小屋上呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "应该快结束了\x01",
            "去看看如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x103,
        (
            "#020F南边的风车小屋啊。\x01",
            "马上去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#1006F那么，回头见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "哦，今后\x01",
            "要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B3")

    Jump("loc_142C")

    label("loc_11B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_142C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 5)), scpexpr(EXPR_END)), "loc_120D")

    ChrTalk(    #79
        0xFE,
        (
            "承蒙你们游击士\x01",
            "诸多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "有空再来哦。\x01",
            "我随时都热烈欢迎。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142C")

    label("loc_120D")

    TurnDirection(0xFE, 0x101, 0)
    OP_A2(0x122D)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0xFE,
        (
            "哦，还以为是谁呢，\x01",
            "是那时的游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "看过孤儿院了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#1000F啊，正打算去。\x02\x03",

            "正好有些事\x01",
            "要调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "难道…\x01",
            "是什么事件吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_130A")

    ChrTalk(    #85
        0x106,
        (
            "#050F不，只是有些事\x01",
            "以防万一要调查一下。\x02\x03",

            "不是事件，放心吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_134A")

    label("loc_130A")


    ChrTalk(    #86
        0x103,
        (
            "#020F是要去调查，\x01",
            "不过事件性比较低。\x02\x03",

            "不用担心，没问题的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_134A")

    TurnDirection(0xFE, 0xF7, 400)

    ChrTalk(    #87
        0xFE,
        (
            "呼，是吗。\x01",
            "不是事件就好。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #88
        0xFE,
        (
            "不着急的话\x01",
            "稍微在村子里休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "你们的话\x01",
            "我随时都热烈欢迎哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1006F嗯，谢谢。\x02\x03",

            "#1015F嗯……不过现在\x01",
            "还是要去孤儿院才行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "哦，这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "那么，再来哦。\x02",
    )

    CloseMessageWindow()

    label("loc_142C")

    TalkEnd(0xFE)
    Return()

    # Function_3_43A end

    def Function_4_1430(): pass

    label("Function_4_1430")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1512")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14BF")

    ChrTalk(    #93
        0xFE,
        (
            "用暖炉做料理\x01",
            "真是好久没试过了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "现在正和珂蕾妲婆婆\x01",
            "学习简单的烹饪法呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "老人的智囊\x01",
            "这时候真是靠得住。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_150F")

    label("loc_14BF")


    ChrTalk(    #96
        0xFE,
        (
            "现在正和珂蕾妲婆婆\x01",
            "学习简单的烹饪法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "用暖炉做料理\x01",
            "真是好久没试过了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_150F")

    Jump("loc_1912")

    label("loc_1512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_160F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15BE")

    ChrTalk(    #98
        0xFE,
        (
            "警备艇被迫降落，\x01",
            "导力器停止还真是不妙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "慎重起见，弟弟扎古\x01",
            "去看灯塔的情况了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "那里只有灯塔看守弗科特老人\x01",
            "一个人在，实在是令人不放心。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_160C")

    label("loc_15BE")


    ChrTalk(    #101
        0xFE,
        (
            "慎重起见，弟弟扎古\x01",
            "去看灯塔的情况了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "这种时候那孩子\x01",
            "还真是可靠呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_160C")

    Jump("loc_1912")

    label("loc_160F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_16E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_167C")

    ChrTalk(    #103
        0xFE,
        (
            "弟弟好像想做\x01",
            "对本地有所贡献的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "如果能找到那种工作，\x01",
            "那孩子应该能耐心去做吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16E4")

    label("loc_167C")

    OP_A2(0x1)

    ChrTalk(    #105
        0xFE,
        (
            "弟弟好像想做\x01",
            "对本地有所贡献的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "孤儿院重建的时候\x01",
            "也亲自去帮忙，\x01",
            "这份心意我也很赞同呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E4")

    Jump("loc_1912")

    label("loc_16E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_17E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1755")

    ChrTalk(    #107
        0xFE,
        (
            "弟弟似乎对这次的市长选举\x01",
            "很关心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "我想知道的\x01",
            "不是卢安的未来\x01",
            "而是扎古你的未来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17DE")

    label("loc_1755")

    OP_A2(0x1)

    ChrTalk(    #109
        0xFE,
        (
            "弟弟似乎对这次的市长选举\x01",
            "很关心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "我想知道的\x01",
            "不是卢安的未来\x01",
            "而是扎古你的未来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "投票给谁都无所谓，\x01",
            "早点去找工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17DE")

    Jump("loc_1912")

    label("loc_17E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_18AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1834")

    ChrTalk(    #112
        0xFE,
        (
            "叔叔怎么\x01",
            "那么鲁莽呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "弟弟扎古\x01",
            "也有点像他，真令人担心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A7")

    label("loc_1834")

    OP_A2(0x1)

    ChrTalk(    #114
        0xFE,
        (
            "做食材商人的\x01",
            "奥维德叔叔\x01",
            "难得回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "却又说要去\x01",
            "找新食材了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "好不容易留下他，\x01",
            "怎么这样鲁莽呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18A7")

    Jump("loc_1912")

    label("loc_18AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1912")

    ChrTalk(    #117
        0xFE,
        (
            "孤儿院的孩子们\x01",
            "似乎也完全恢复精神了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "在主日学校上课的日子，\x01",
            "笑声乘着风\x01",
            "在这里回响呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1912")

    TalkEnd(0xFE)
    Return()

    # Function_4_1430 end

    def Function_5_1916(): pass

    label("Function_5_1916")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_19EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_197A")

    ChrTalk(    #119
        0xFE,
        (
            "旅游业的推进，\x01",
            "还是海运业……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "父亲说的对，\x01",
            "这可不能用普通的方法解决。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19EB")

    label("loc_197A")

    OP_A2(0x2)

    ChrTalk(    #121
        0xFE,
        (
            "旅游业的推进，\x01",
            "还是海运业的维持……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "实际的行政\x01",
            "可没有黑白分明这么简单。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        "……嗯，这是父亲说的。\x02",
    )

    CloseMessageWindow()

    label("loc_19EB")

    Jump("loc_1B67")

    label("loc_19EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1AC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A4D")

    ChrTalk(    #124
        0xFE,
        (
            "选举也得在玛诺利亚\x01",
            "准备投票所才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "市长选举之前\x01",
            "需要做许多准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC5")

    label("loc_1A4D")

    OP_A2(0x2)

    ChrTalk(    #126
        0xFE,
        (
            "父亲也为了选举的准备\x01",
            "忙个不停的样子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "玛诺利亚也要\x01",
            "准备投票所才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "作为村长\x01",
            "也需要做许多准备哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC5")

    Jump("loc_1B67")

    label("loc_1AC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_1B1C")

    ChrTalk(    #129
        0xFE,
        (
            "看来主日学校\x01",
            "好像结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "刚才还那么热闹，\x01",
            "现在就完全静下来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B67")

    label("loc_1B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1B67")

    ChrTalk(    #131
        0xFE,
        (
            "孤儿院的孩子们\x01",
            "似乎很精神呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "重建工程那么努力\x01",
            "也值得了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B67")

    TalkEnd(0xFE)
    Return()

    # Function_5_1916 end

    def Function_6_1B6B(): pass

    label("Function_6_1B6B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1C98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C3F")

    ChrTalk(    #133
        0xFE,
        (
            "玛诺利亚村自然资源丰富，\x01",
            "收集柴火也很自由。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "不行的话野鸟、鱼、山菜\x01",
            "都能拿来当食物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "可是，像王都一样的都市\x01",
            "就没办法这样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "如果这状况长久持续，恐怕\x01",
            "都市会陷入危机吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1C95")

    label("loc_1C3F")


    ChrTalk(    #137
        0xFE,
        (
            "如果这状况长久持续，恐怕\x01",
            "都市会陷入危机吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "大城市可是相当\x01",
            "依靠导力器的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C95")

    Jump("loc_20E0")

    label("loc_1C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1DD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D6F")

    ChrTalk(    #139
        0xFE,
        (
            "风车小屋里食品和燃料\x01",
            "都有少量的储备……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "如果只想有那些储备就可以的话，\x01",
            "那很快就会开始匮乏的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "为了向卢安市请求支持，\x01",
            "让儿子索雷诺去了城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "如果能和新市长先生\x01",
            "谈妥就好了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1DCD")

    label("loc_1D6F")


    ChrTalk(    #143
        0xFE,
        (
            "风车小屋里那种程度的储备\x01",
            "很快就会用完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "因此时间紧迫，\x01",
            "就让儿子立即去请求支持了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DCD")

    Jump("loc_20E0")

    label("loc_1DD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1EBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1E45")

    ChrTalk(    #145
        0xFE,
        (
            "贵族的前市长被逮捕，\x01",
            "平民出身的候选人在竞争其继任。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "此次的市长选举\x01",
            "真像是时代变化的象征。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB8")

    label("loc_1E45")

    OP_A2(0x3)

    ChrTalk(    #147
        0xFE,
        (
            "诺曼氏和波尔多斯氏\x01",
            "都是平民出身，\x01",
            "两人都是出色的人物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "以前要说选举\x01",
            "都是从贵族中选，\x01",
            "这时代真是变了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB8")

    Jump("loc_20E0")

    label("loc_1EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1F8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1F16")

    ChrTalk(    #149
        0xFE,
        (
            "上次选举时\x01",
            "这里是投票所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "许多人相信戴尔蒙家\x01",
            "的家名而投了票……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F87")

    label("loc_1F16")

    OP_A2(0x3)

    ChrTalk(    #151
        0xFE,
        (
            "上次选举时\x01",
            "这里曾经是投票所……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "……唔，怎么看都很狭窄啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "大概还是只有拜托\x01",
            "白之木莲亭合作了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F87")

    Jump("loc_20E0")

    label("loc_1F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_1FF5")

    ChrTalk(    #154
        0xFE,
        (
            "孤儿院开始重建工程时，\x01",
            "村里的年轻人好像\x01",
            "也都去帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "真希望他们能一直\x01",
            "保持这种心情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E0")

    label("loc_1FF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_20E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_205A")

    ChrTalk(    #156
        0xFE,
        (
            "前市长引起的事件\x01",
            "对玛诺利亚来说也是重伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "发生大事件之后\x01",
            "游客也都不来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E0")

    label("loc_205A")

    OP_A2(0x3)

    ChrTalk(    #158
        0xFE,
        (
            "哎呀，旅行的人吗？\x01",
            "欢迎来到玛诺利亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "烧掉的孤儿院也被重建，\x01",
            "恢复到平常的生活了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "之后就只等\x01",
            "后任的市长被选出来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20E0")

    TalkEnd(0xFE)
    Return()

    # Function_6_1B6B end

    def Function_7_20E4(): pass

    label("Function_7_20E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20F5")
    Call(0, 8)

    label("loc_20F5")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    AddParty(0x8, 0xF8, 0xFF)
    OP_31(0x8, 0x0, 0x27)
    OP_31(0x8, 0xFE, 0x0)
    OP_41(0x8, 0xE6, 0xFF)
    OP_41(0x8, 0xFF, 0xFF)
    OP_41(0x8, 0x120, 0xFF)
    OP_41(0x8, 0x273, 0x0)
    OP_41(0x8, 0x25B, 0x1)
    OP_41(0x8, 0x258, 0x2)
    OP_41(0x8, 0x265, 0x3)
    OP_41(0x8, 0x262, 0x4)
    OP_35(0x8, 0x8C)
    OP_35(0x8, 0x0)
    OP_BB(0x8, 0x6, 0x10E)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0xF7, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x101, -30000, 0, 34900, 0)
    SetChrPos(0xF7, -30000, 0, 34900, 0)
    SetChrPos(0x109, -30000, 0, 42500, 180)
    SetChrPos(0x8, -30000, 0, 40000, 0)
    SetChrPos(0x9, -28640, 0, 40440, 315)
    SetChrPos(0xA, -30970, 0, 40340, 0)
    SetChrPos(0xB, -31570, 0, 41240, 45)
    SetChrPos(0xC, -27690, 0, 41900, 315)
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x109, 0x0)
    OP_6C(45000, 0)
    OP_6B(3010, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #161
        0x109,
        (
            "#1065F『不必同情他啦。\x01",
            "  真是的，蒂雅大人太善良了』\x02\x03",

            "#1067F老实说，加斯顿公爵\x01",
            "会就这样默默地退出，\x01",
            "佩德罗无论如何也没有想到。\x02\x03",

            "#1063F还有那个诡异的蒙面人偶师，\x01",
            "哈雷库因的动向也很令人在意。\x02\x03",

            "虽然彼此似乎相识，\x01",
            "但师父卡普利闪烁其词，\x01",
            "完全没向自己说明些什么。\x02\x03",

            "#1065F不管怎么样，\x01",
            "最近必定还会有一场动乱。\x01",
            "佩德罗下定决心要改造苍骑士。\x02\x03",

            "#1060F『真是的，佩德罗大人。』\x02\x03",

            "稍显愠怒的语调\x01",
            "让佩德罗回过神来。\x02\x03",

            "#1061F『茶要凉了哦？』\x02\x03",

            "她那双照映着蓝天的清爽眼眸\x01",
            "就好像在说『没问题』一样，\x01",
            "闪耀着恶作剧般的光辉。\x02\x03",

            "#1062F感到些许害羞的佩德罗，\x01",
            "端起微温的红茶润了润喉咙。\x02\x03",

            "#1071F……人偶骑士·完。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_24A0():
        OP_95(0x8, 0x0, 0x0, 0x0, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_24A0)

    def lambda_24BE():
        OP_95(0xA, 0x0, 0x0, 0x0, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_24BE)
    Sleep(50)

    def lambda_24E1():
        OP_95(0xB, 0x0, 0x0, 0x0, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_24E1)

    def lambda_24FF():
        OP_95(0xC, 0x0, 0x0, 0x0, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_24FF)
    Sleep(50)

    def lambda_2522():
        OP_95(0x9, 0x0, 0x0, 0x0, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2522)
    OP_62(0x8, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_62(0x9, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_62(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xC, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)

    ChrTalk(    #162
        0x8,
        (
            "#774F咦咦～！\x01",
            "这就完了吗～！？\x02\x03",

            "跟哈雷库因的\x01",
            "的决斗怎么办啊！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(    #163
        0xA,
        (
            "#6P白痴啊，克拉姆真是的。\x01",
            "在这里结束不是正好吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xA,
        (
            "#6P佩德罗和蒂雅公主\x01",
            "总有一天会结婚，然后过着幸福的生活。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xA,
        "#6P啊～太浪漫了㈱\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xA, 400)

    ChrTalk(    #166
        0xC,
        "嗯嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xC,
        (
            "的确要两人结婚的\x01",
            "大团圆结局才行呢㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xB,
        (
            "我觉得\x01",
            "好想喝老师的茶啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x9,
        "#2P卡普利师父好帅哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x109,
        (
            "#1068F呼呼……\x02\x03",

            "把『人偶骑士』\x01",
            "全２２卷一口气念完还真是辛苦啊。\x02\x03",

            "#1062F好了，这样行了吧。\x01",
            "今天的授课结束啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x8,
        "#772F呵～呵～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x109, 400)

    ChrTalk(    #172
        0xA,
        "#6P凯文老师，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x109,
        "#1066F呼，真是被打败了……\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #174
        0x109,
        (
            "#1062F啊～那边的。\x02\x03",

            "授课结束了，\x01",
            "可以进来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        (
            "#5P啊哈哈……\x01",
            "注意到了吗。\x02\x03",

            "嗯，打扰了。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_2844():
        OP_6D(-29990, 0, 40480, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2844)

    def lambda_285C():
        OP_67(0, 6620, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_285C)

    def lambda_2874():
        TurnDirection(0x8, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2874)

    def lambda_2882():
        TurnDirection(0x9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2882)

    def lambda_2890():
        TurnDirection(0xA, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2890)

    def lambda_289E():
        TurnDirection(0xB, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_289E)

    def lambda_28AC():
        TurnDirection(0xC, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_28AC)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF7, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x8)

    def lambda_28D5():
        OP_8F(0x101, 0xFFFF8ABC, 0x0, 0x9470, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28D5)

    def lambda_28F0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_28F0)
    Sleep(500)
    ClearChrFlags(0xF7, 0x8)

    def lambda_290C():
        OP_8F(0xF7, 0xFFFF8742, 0x0, 0x8F70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_290C)

    def lambda_2927():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_2927)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #176
        0x109,
        "#1064F#5P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x8,
        "#774F#5P#3S啊啊啊啊啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xA,
        "#5P#3S艾丝蒂尔！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        (
            "#1018F#6P大家，好久不见呢！\x02\x03",

            "还好吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A5F():
        OP_92(0x8, 0x101, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2A5F)
    Sleep(50)

    def lambda_2A79():
        OP_8E(0x9, 0xFFFF8D3C, 0x0, 0x94A2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2A79)
    Sleep(50)

    def lambda_2A99():
        OP_8E(0xA, 0xFFFF86FC, 0x0, 0x947A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2A99)
    Sleep(50)

    def lambda_2AB9():
        OP_8E(0xB, 0xFFFF8710, 0x0, 0x97EA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2AB9)
    Sleep(50)

    def lambda_2AD9():
        OP_8E(0xC, 0xFFFF8DF0, 0x0, 0x990C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2AD9)
    Sleep(50)

    def lambda_2AF9():
        OP_8E(0x109, 0xFFFF8A44, 0x0, 0xA136, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2AF9)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0x101, 0)
    TurnDirection(0xA, 0x101, 0)
    TurnDirection(0xB, 0x101, 0)

    ChrTalk(    #180
        0x8,
        (
            "#771F#5P怎么啦！\x01",
            "是来玩的吗～！？\x02",
        )
    )

    WaitChrThread(0xC, 0x1)
    TurnDirection(0xC, 0x101, 0)
    CloseMessageWindow()

    ChrTalk(    #181
        0xA,
        (
            "#6P呜哇！\x01",
            "真的是好久不见了～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xB,
        (
            "#5P艾丝蒂尔姐姐。\x01",
            "一起玩一起玩～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x9,
        (
            "#2P来得正好～\x01",
            "欢迎欢迎～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        (
            "#1016F#6P啊哈哈……\x01",
            "大家还是这么精神呢。\x02\x03",

            "#1017F啊。\x01",
            "凯文先生也好久不见呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x109,
        (
            "#1061F#5P哦哦，艾丝蒂尔。\x01",
            "还记得我吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#1006F#6P那当然了。\x02\x03",

            "#1016F不过，你真的\x01",
            "这副打扮来当神父啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x109,
        (
            "#1068F#5P这话是什么意思嘛。\x02\x03",

            "#1062F不过，没想到\x01",
            "能在这种地方重逢啊。\x02\x03",

            "#1061F难不成这是\x01",
            "命运的重逢也说不定啊㈱\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2412   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_20E4 end

    def Function_8_2D17(): pass

    label("Function_8_2D17")

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
        (0, "loc_2D91"),
        (1, "loc_2D97"),
        (SWITCH_DEFAULT, "loc_2D9D"),
    )


    label("loc_2D91")

    OP_A2(0x1200)
    Jump("loc_2D9D")

    label("loc_2D97")

    OP_A2(0x1201)
    Jump("loc_2D9D")

    label("loc_2D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2DAB")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_2DAF")

    label("loc_2DAB")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_2DAF")

    Return()

    # Function_8_2D17 end

    SaveToFile()

Try(main)
