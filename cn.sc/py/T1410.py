from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1410   ._SN',
        MapName             = 'Bose',
        Location            = 'T1410.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        '王国军士兵',                           # 9
        '王国军士兵',                           # 10
        '摩尔根将军',                           # 11
        '诺朗',                                 # 12
        '艾蕾米亚',                             # 13
        '阿尔宾',                               # 14
        '蔡尔德',                               # 15
        '马尔科',                               # 16
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
        'ED6_DT07/CH01300 ._CH',             # 00
        'ED6_DT07/CH02083 ._CH',             # 01
        'ED6_DT07/CH01270 ._CH',             # 02
        'ED6_DT07/CH01150 ._CH',             # 03
        'ED6_DT07/CH01040 ._CH',             # 04
        'ED6_DT07/CH01140 ._CH',             # 05
        'ED6_DT07/CH01100 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH01300P._CP',             # 00
        'ED6_DT07/CH02083P._CP',             # 01
        'ED6_DT07/CH01270P._CP',             # 02
        'ED6_DT07/CH01150P._CP',             # 03
        'ED6_DT07/CH01040P._CP',             # 04
        'ED6_DT07/CH01140P._CP',             # 05
        'ED6_DT07/CH01100P._CP',             # 06
    )

    DeclNpc(
        X                   = 104300,
        Z                   = 0,
        Y                   = 107600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 201700,
        Z                   = 0,
        Y                   = 109600,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 209550,
        Z                   = 200,
        Y                   = 11820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 18100,
        Z                   = 0,
        Y                   = 16400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 15350,
        Z                   = 0,
        Y                   = 15480,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 20700,
        Z                   = 0,
        Y                   = 13230,
        Direction           = 191,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 23470,
        Z                   = 0,
        Y                   = 12150,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 23470,
        Z                   = 0,
        Y                   = 12150,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )


    DeclActor(
        TriggerX            = 17690,
        TriggerZ            = 0,
        TriggerY            = 14350,
        TriggerRange        = 800,
        ActorX              = 18100,
        ActorZ              = 1500,
        ActorY              = 16400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 207600,
        TriggerZ            = 0,
        TriggerY            = 11880,
        TriggerRange        = 800,
        ActorX              = 209550,
        ActorZ              = 1500,
        ActorY              = 11820,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 123890,
        TriggerZ            = 0,
        TriggerY            = 11990,
        TriggerRange        = 800,
        ActorX              = 123890,
        ActorZ              = 800,
        ActorY              = 11990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_24E",          # 00, 0
        "Function_1_29E",          # 01, 1
        "Function_2_303",          # 02, 2
        "Function_3_480",          # 03, 3
        "Function_4_4A4",          # 04, 4
        "Function_5_4A9",          # 05, 5
        "Function_6_FA4",          # 06, 6
        "Function_7_1370",         # 07, 7
        "Function_8_1583",         # 08, 8
        "Function_9_1588",         # 09, 9
        "Function_10_1BE0",        # 0A, 10
        "Function_11_1EE5",        # 0B, 11
        "Function_12_2180",        # 0C, 12
        "Function_13_243E",        # 0D, 13
        "Function_14_2692",        # 0E, 14
    )


    def Function_0_24E(): pass

    label("Function_0_24E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_26C")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_29D")

    label("loc_26C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_276")
    Jump("loc_29D")

    label("loc_276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_296")
    SetChrFlags(0xA, 0x80)
    SetChrPos(0x9, 206990, -20, 101510, 45)
    Jump("loc_29D")

    label("loc_296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_29D")

    label("loc_29D")

    Return()

    # Function_0_24E end

    def Function_1_29E(): pass

    label("Function_1_29E")

    OP_72(0x3, 0x10)
    OP_72(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2B2")
    Jump("loc_2D1")

    label("loc_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2BC")
    Jump("loc_2D1")

    label("loc_2BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2CA")
    OP_64(0x1, 0x1)
    Jump("loc_2D1")

    label("loc_2CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2D1")

    label("loc_2D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_302")
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_79(0x5, 0x2)
    OP_79(0x6, 0x2)
    OP_79(0x7, 0x2)
    OP_79(0x8, 0x2)
    OP_7B()

    label("loc_302")

    Return()

    # Function_1_29E end

    def Function_2_303(): pass

    label("Function_2_303")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_328")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_46A")

    label("loc_328")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_341")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_46A")

    label("loc_341")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_46A")

    label("loc_35A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_373")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_46A")

    label("loc_373")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_46A")

    label("loc_38C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A5")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_46A")

    label("loc_3A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BE")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_46A")

    label("loc_3BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D7")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_46A")

    label("loc_3D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F0")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_46A")

    label("loc_3F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_409")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_46A")

    label("loc_409")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_422")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_46A")

    label("loc_422")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_46A")

    label("loc_43B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_454")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_46A")

    label("loc_454")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_46A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_46A")

    label("loc_47F")

    Return()

    # Function_2_303 end

    def Function_3_480(): pass

    label("Function_3_480")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A3")
    OP_8D(0xFE, 20000, 13500, 21500, 11750, 1500)
    Jump("Function_3_480")

    label("loc_4A3")

    Return()

    # Function_3_480 end

    def Function_4_4A4(): pass

    label("Function_4_4A4")

    Call(0, 5)
    Return()

    # Function_4_4A4 end

    def Function_5_4A9(): pass

    label("Function_5_4A9")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_539")
    Jump("loc_57B")

    label("loc_539")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_555")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57B")

    label("loc_555")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_571")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57B")

    label("loc_571")

    OP_51(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_57B")

    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_874")

    ChrTalk(    #0
        0xA,
        (
            "#160F嗯，是你们呀……\x02\x03",

            "『塔』被压制住了，辛苦你们了……还有，\x01",
            "本来应该慰劳你们的。\x02\x03",

            "#166F但是现在这个形势下\x01",
            "我连说些客套话的工夫都没有。\x02\x03",

            "有机会的话再招待你们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        "#1015F哎呀，真是可惜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        (
            "#1043F的确和以前相比\x01",
            "状况已经改变了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D0")

    ChrTalk(    #3
        0x106,
        "#053F而且还是往坏的方向……\x02",
    )

    CloseMessageWindow()
    Jump("loc_731")

    label("loc_6D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_702")

    ChrTalk(    #4
        0x103,
        "#026F而且还是往坏的方向……\x02",
    )

    CloseMessageWindow()
    Jump("loc_731")

    label("loc_702")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_731")

    ChrTalk(    #5
        0x108,
        "#072F而且还是往坏的方向……\x02",
    )

    CloseMessageWindow()

    label("loc_731")


    ChrTalk(    #6
        0xA,
        (
            "#160F由于那个发生器的作用，\x01",
            "据点间的通信恢复了……\x02\x03",

            "果然这个导力停止现象\x01",
            "是在王国全境内发生的。\x02\x03",

            "我想你们已经见到了，\x01",
            "现在这个关所也处于危险状态中。\x02\x03",

            "总之不能让敌人乘虚而入，\x01",
            "这就是尽了军人的本分。\x02\x03",

            "我也期待你们游击士的工作\x01",
            "能有更好的表现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1006F嗯！加油呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        "#1042F为了不负您的期待，我们会努力的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    OP_A2(0x2097)
    Jump("loc_B0C")

    label("loc_874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_AA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_8EC")

    ChrTalk(    #9
        0xA,
        (
            "#160F总之不能让敌人乘虚而入，\x01",
            "这就是尽了军人的本分。\x02\x03",

            "你们游击士的工作也是，\x01",
            "希望能有更好的表现。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA2")

    label("loc_8EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A19")

    ChrTalk(    #10
        0xA,
        (
            "#160F继续整顿防备，\x01",
            "不能使用导力兵器真糟糕。\x02\x03",

            "如果敌人来进攻的话，\x01",
            "只能靠白兵战死守大门了。\x02\x03",

            "#163F不过，敌人也是一样。\x01",
            "胜算都是五五成。\x02\x03",

            "我想精于算计的帝国，\x01",
            "不会做出这样危险的决定……\x02\x03",

            "#160F不过，希望这至少\x01",
            "不是我们单方面的想法。\x02\x03",

            "要经常做好最坏的心理准备，\x01",
            "保卫国家是国民的职责。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_AA2")

    label("loc_A19")


    ChrTalk(    #11
        0xA,
        (
            "#166F敌人也一样不能使用导力兵器……\x02\x03",

            "这样的话，除了白兵战\x01",
            "之外就没有其它的战斗手段了。\x02\x03",

            "像这样的消耗战\x01",
            "我认为帝国不会来硬碰硬的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA2")

    Jump("loc_B0C")

    label("loc_AA5")


    ChrTalk(    #12
        0xA,
        (
            "#160F总之不能让敌人乘虚而入，\x01",
            "这就是尽了军人的本分。\x02\x03",

            "你们游击士的工作也是，\x01",
            "希望能有更好的表现。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0C")

    Jump("loc_F9B")

    label("loc_B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_C11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x349, 7)), scpexpr(EXPR_END)), "loc_B5B")

    ChrTalk(    #13
        0xA,
        (
            "#163F…………………………………\x02\x03",

            "请帮我们弄清这事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C0E")

    label("loc_B5B")


    ChrTalk(    #14
        0xA,
        (
            "#160F嗯，是你们呀。\x01",
            "捕获作战辛苦你们了。\x02\x03",

            "#166F有什么要问的吗，\x01",
            "看你的脸我就明白了……\x02\x03",

            "#163F…………………………………\x02\x03",

            "……关于这件事\x01",
            "我也说不好。\x02\x03",

            "请帮我们弄清这事……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A4F)

    label("loc_C0E")

    Jump("loc_F9B")

    label("loc_C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_F9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x349, 6)), scpexpr(EXPR_END)), "loc_C79")

    ChrTalk(    #15
        0xA,
        (
            "#160F我们会协助协会\x01",
            "也是因为互相信赖。\x02\x03",

            "有什么事件发生的话\x01",
            "希望你们马上联络军方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9B")

    label("loc_C79")


    ChrTalk(    #16
        0xA,
        (
            "#160F什么，我还以为是谁呢，\x01",
            "这不是卡西乌斯的女儿嘛。\x02\x03",

            "在王都辛苦你了。\x02\x03",

            "听说结社在洛连特也发动\x01",
            "了骚乱……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1003F嗯，虽然很糟糕，\x01",
            "不过总算解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x106,
        (
            "#053F啊，真是经历了\x01",
            "非常大的灾难呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xA,
        (
            "#163F嗯，是这样呀。\x02\x03",

            "果然是结社的人，\x01",
            "好像都是些很难对付的家伙呀。\x02\x03",

            "看来今后提高警戒\x01",
            "是很有必要的。\x02\x03",

            "#160F真巧，是你们呀……\x02\x03",

            "你们现在在这个地方\x01",
            "进行工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1011F啊，嗯，是这样呀。\x02\x03",

            "在帮助柏斯支部\x01",
            "消灭通缉魔兽呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xA,
        (
            "#165F原来如此……\x01",
            "剿灭魔兽真是多呀。\x02\x03",

            "#160F不过，有什么事件发生的话\x01",
            "希望你们马上联络军方。\x02\x03",

            "我们会协助协会\x01",
            "也是因为互相信赖。\x02\x03",

            "特别是最近，因为\x01",
            "出现邪恶组织的关系呀。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F20")

    ChrTalk(    #22
        0x103,
        (
            "#027F如果有什么事的话\x01",
            "通过支部联络我们吧。\x02\x03",

            "这样就没问题了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F62")

    label("loc_F20")


    ChrTalk(    #23
        0x106,
        (
            "#050F如果有什么事的话\x01",
            "通过支部联络我们吧。\x02\x03",

            "这样就没问题了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F62")


    ChrTalk(    #24
        0xA,
        (
            "#160F嗯，就这样吧。\x02\x03",

            "但请务必……\x01",
            "不要太逞强呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A4E)

    label("loc_F9B")

    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)
    Return()

    # Function_5_4A9 end

    def Function_6_FA4(): pass

    label("Function_6_FA4")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1098")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104B")

    ChrTalk(    #25
        0xFE,
        (
            "现在这时候\x01",
            "帝国军似乎没什么行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "但相反来说\x01",
            "却更让人更紧张了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "看，不是有句话说\x01",
            "暴风雨前的宁静吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "和那个一样的感觉吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1095")

    label("loc_104B")


    ChrTalk(    #29
        0xFE,
        (
            "现在这时候\x01",
            "帝国军似乎没什么行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "但相反来说\x01",
            "却更让人更紧张了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1095")

    Jump("loc_136C")

    label("loc_1098")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1128")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FC")

    ChrTalk(    #31
        0xFE,
        (
            "现在几乎所有的士兵\x01",
            "都有出勤命令了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "无论怎样现在可是王国最大危机呀。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1125")

    label("loc_10FC")


    ChrTalk(    #33
        0xFE,
        (
            "现在几乎所有的士兵\x01",
            "都有出勤命令了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1125")

    Jump("loc_136C")

    label("loc_1128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_11F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_117F")

    ChrTalk(    #34
        0xFE,
        (
            "看来这里也要\x01",
            "重新进行通常勤务了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "唉，真想再\x01",
            "稍微喘口气呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F3")

    label("loc_117F")


    ChrTalk(    #36
        0xFE,
        (
            "看来这里也要\x01",
            "重新进行通常勤务了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "因为旁边就是帝国，\x01",
            "不能掉以轻心的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "唉，真想再\x01",
            "稍微喘口气呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_11F3")

    Jump("loc_136C")

    label("loc_11F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_129E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1242")

    ChrTalk(    #39
        0xFE,
        (
            "但我们也为许会\x01",
            "出动进行龙的搜索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "真是不安呀……\x02",
    )

    CloseMessageWindow()
    Jump("loc_129B")

    label("loc_1242")


    ChrTalk(    #41
        0xFE,
        (
            "关所也被\x01",
            "命令待命了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "但我们也为许会\x01",
            "出动进行龙的搜索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "真是不安呀……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_129B")

    Jump("loc_136C")

    label("loc_129E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_136C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_12FB")

    ChrTalk(    #44
        0xFE,
        (
            "这段时期洛连特\x01",
            "的浓雾真厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "感觉人简直就像\x01",
            "在牛奶中游泳一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136C")

    label("loc_12FB")


    ChrTalk(    #46
        0xFE,
        (
            "这段时期我作为增援被派遣\x01",
            "洛连特地区来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "哎呀，好大的雾啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "感觉人简直就像\x01",
            "在牛奶中游泳一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_136C")

    TalkEnd(0x8)
    Return()

    # Function_6_FA4 end

    def Function_7_1370(): pass

    label("Function_7_1370")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1441")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_13C9")

    ChrTalk(    #49
        0xFE,
        (
            "这次帝国那边\x01",
            "什么反应也没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "难道是互不侵犯条约的效果吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_143E")

    label("loc_13C9")


    ChrTalk(    #51
        0xFE,
        (
            "这次帝国那边\x01",
            "什么反应也没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "过去就算有点人员调动\x01",
            "他们就会赶过来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "这是互不侵犯条约的效果吗？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_143E")

    Jump("loc_157F")

    label("loc_1441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1522")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_14B7")

    ChrTalk(    #54
        0xFE,
        "龙好像逃进峡谷里了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "从那边的山岳地带翻过去\x01",
            "就是帝国的国境了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "是个很难出手的地方。\x02",
    )

    CloseMessageWindow()
    Jump("loc_151F")

    label("loc_14B7")


    ChrTalk(    #57
        0xFE,
        "龙好像逃进峡谷里了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "那边的山岳地带就算是\x01",
            "飞行舰队也很难出手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "将军大人要怎么办呢……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_151F")

    Jump("loc_157F")

    label("loc_1522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_157F")

    ChrTalk(    #60
        0xFE,
        (
            "虽然缔结了互不侵犯条约，\x01",
            "但警戒还是那么严密。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "应该不会让\x01",
            "帝国看到空隙了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157F")

    TalkEnd(0x9)
    Return()

    # Function_7_1370 end

    def Function_8_1583(): pass

    label("Function_8_1583")

    Call(0, 9)
    Return()

    # Function_8_1583 end

    def Function_9_1588(): pass

    label("Function_9_1588")

    TalkBegin(0xB)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "休息\x01",        # 2
            "离开\x01",        # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F7")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x54)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_15F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1610")
    OP_0D()
    OP_A9(0x55)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_1610")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_162A")
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_162A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1711")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B6")

    ChrTalk(    #62
        0xB,
        (
            "士兵们都在发抖呢，\x01",
            "帝国真的会来吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xB,
        (
            "已经有了互不侵犯条约，\x01",
            "我想应该不可能吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xB,
        (
            "士兵们有点\x01",
            "神经过敏罢了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_170E")

    label("loc_16B6")


    ChrTalk(    #65
        0xB,
        (
            "士兵们都在发抖呢，\x01",
            "帝国真的会来吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xB,
        (
            "已经有了互不侵犯条约，\x01",
            "我想应该不可能吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_170E")

    Jump("loc_1BDC")

    label("loc_1711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_17F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179E")

    ChrTalk(    #67
        0xB,
        "哟，欢迎来到关所的酒吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        (
            "虽然看上去是戒严状态，\x01",
            "但还是来一杯吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xB,
        (
            "放心吧，不会这么简单\x01",
            "就发生武装冲突的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_17F0")

    label("loc_179E")


    ChrTalk(    #70
        0xB,
        (
            "虽然看上去是戒严状态，\x01",
            "但还是来一杯吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xB,
        (
            "不会这么简单\x01",
            "就发生武装冲突的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F0")

    Jump("loc_1BDC")

    label("loc_17F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 0)), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_18B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_186E")

    ChrTalk(    #72
        0xB,
        (
            "龙的事件解决了，\x01",
            "现在也能放松一下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xB,
        (
            "接下来，现在\x01",
            "开始准备晚饭了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18B0")

    label("loc_186E")


    ChrTalk(    #74
        0xB,
        "哟，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xB,
        (
            "龙的事件解决了，\x01",
            "现在也能放松一下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_18B0")

    Jump("loc_19C6")

    label("loc_18B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_196C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1916")

    ChrTalk(    #76
        0xB,
        (
            "因为龙的事件，\x01",
            "这里处于戒严状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xB,
        (
            "士兵们也准备出动了，\x01",
            "好像都在待命呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1969")

    label("loc_1916")


    ChrTalk(    #78
        0xB,
        (
            "因为龙的事件，\x01",
            "这里处于戒严状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xB,
        (
            "哎呀哎呀，这里最近\x01",
            "一直都很和平呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1969")

    Jump("loc_19C6")

    label("loc_196C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_19C6")

    ChrTalk(    #80
        0xB,
        "哟，欢迎来到关所的酒吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xB,
        (
            "虽然拿不出象样的东西，\x01",
            "但至少还是能填饱肚子的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C6")

    Jump("loc_1A17")

    label("loc_19C9")


    ChrTalk(    #82
        0xB,
        (
            "看样子还真是次\x01",
            "厉害的旅行呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xB,
        (
            "那就来一杯，\x01",
            "我还想听听你们的故事呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A17")

    Jump("loc_1BDC")

    label("loc_1A1A")


    ChrTalk(    #84
        0xB,
        "哟，欢迎来到关所的酒吧。\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xB, 0x104, 400)
    Sleep(400)

    ChrTalk(    #85
        0xB,
        "哎呀，是你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x104,
        (
            "#031F呵，好久不见了。\x02\x03",

            "自从那时入境利贝尔王国时\x01",
            "碰过面到现在一直都没见呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #87
        0xB,
        (
            "喔，你果然是\x01",
            "那个帝国旅行者呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xB,
        "那么旅行怎么样呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x104,
        (
            "#030F啊啊，真是\x01",
            "超乎想象的愉快呀。\x02\x03",

            "#035F只能用一场大冒险\x01",
            "来形容的这次旅行呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xB,
        "哎呀，那还真不错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xB,
        (
            "那就来一杯，\x01",
            "我还想听听旅行中的故事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x104,
        (
            "#031F呵，等到时候\x01",
            "我会找你喝一杯的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A50)
    OP_A2(0x2)

    label("loc_1BDC")

    TalkEnd(0xB)
    Return()

    # Function_9_1588 end

    def Function_10_1BE0(): pass

    label("Function_10_1BE0")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1C3D")

    ChrTalk(    #93
        0xFE,
        (
            "为什么王国全境\x01",
            "的导力器都停止了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "我想老板一定会认为\x01",
            "是导力器坏了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE1")

    label("loc_1C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1D24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD4")

    ChrTalk(    #95
        0xFE,
        (
            "这个关所经常会发生骚乱，\x01",
            "不过这次有些特别。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "我从士兵们的脸上也\x01",
            "感觉到了平日没有的紧张。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "希望什么也没发生就好了……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1D21")

    label("loc_1CD4")


    ChrTalk(    #98
        0xFE,
        (
            "这个关所经常会发生骚乱，\x01",
            "不过这次有些特别。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "什么也没发生就好了……\x02",
    )

    CloseMessageWindow()

    label("loc_1D21")

    Jump("loc_1EE1")

    label("loc_1D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1D70")

    ChrTalk(    #100
        0xFE,
        (
            "终于这个关所也\x01",
            "恢复平静了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "这下晚上\x01",
            "终于能睡个好觉了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE1")

    label("loc_1D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1DCA")

    ChrTalk(    #102
        0xFE,
        (
            "龙的捕获作战\x01",
            "真是拖了好长时间呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "看了士兵们的表情\x01",
            "心里就会感到不安。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE1")

    label("loc_1DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1EE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1E52")

    ChrTalk(    #104
        0xFE,
        (
            "登山家虽然很有气魄，\x01",
            "但总觉得土土的呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "在这点上，理查德上校\x01",
            "相当的出色。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "呀啊，为什么要\x01",
            "发动政变呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE1")

    label("loc_1E52")


    ChrTalk(    #107
        0xFE,
        (
            "那边的客人们\x01",
            "好像要去登山。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "嗯，那些登山家\x01",
            "的确很有男子气概……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "我，对那些汗臭\x01",
            "非常头痛呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "我还是喜欢\x01",
            "更加潇洒的男性。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1EE1")

    TalkEnd(0xC)
    Return()

    # Function_10_1BE0 end

    def Function_11_1EE5(): pass

    label("Function_11_1EE5")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1F9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1F44")

    ChrTalk(    #111
        0xFE,
        (
            "漫长的等待有了价值，\x01",
            "登山许可终于下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "好了，准备出发登山吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F97")

    label("loc_1F44")


    ChrTalk(    #113
        0xFE,
        (
            "等待终于有了价值，\x01",
            "登山许可下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "跟蔡尔德说的一样，\x01",
            "耐心等就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1F97")

    Jump("loc_217C")

    label("loc_1F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2095")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1FF7")

    ChrTalk(    #115
        0xFE,
        (
            "不管军队怎么说，\x01",
            "登山是不能中止的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "干脆不管警告，\x01",
            "现在就出发吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2092")

    label("loc_1FF7")


    ChrTalk(    #117
        0xFE,
        (
            "王国军发来劝告，\x01",
            "要我们中止登山。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "都准备了好几个月了，\x01",
            "简直是开玩笑嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "都走到这了，\x01",
            "竟然不能上山……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "干脆不管警告，\x01",
            "马上就出发吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2092")

    Jump("loc_217C")

    label("loc_2095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_217C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_20F4")

    ChrTalk(    #121
        0xFE,
        (
            "我们可是山的孩子。\x01",
            "准备登上国境的山脉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "现在为了准备\x01",
            "留在这个关所。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_217C")

    label("loc_20F4")


    ChrTalk(    #123
        0xFE,
        (
            "我们可是山的孩子。\x01",
            "准备登上国境的山脉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "迷雾峡谷的西面\x01",
            "还有很多未被踏足的山脉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "对我们来说\x01",
            "实在是很块有魅力的地区呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_217C")

    TalkEnd(0xD)
    Return()

    # Function_11_1EE5 end

    def Function_12_2180(): pass

    label("Function_12_2180")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2279")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_21E2")

    ChrTalk(    #126
        0xFE,
        (
            "路线必须\x01",
            "严格地进行确认。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "不管怎样这次挑战的\x01",
            "是前人未踏足过的山呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2276")

    label("loc_21E2")


    ChrTalk(    #128
        0xFE,
        (
            "嗯，根据今天的风向\x01",
            "可以暂时不用担心雾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "但是，路线必须\x01",
            "严格地进行确认。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "不管怎样挑战的可是未踏足过的山峰。\x01",
            "一定要尽可能的慎重。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2276")

    Jump("loc_243A")

    label("loc_2279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2382")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_22D8")

    ChrTalk(    #131
        0xFE,
        (
            "耐心等待的话\x01",
            "也许会有好结果的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "我的伙伴阿尔宾，应该\x01",
            "变得再耐心点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_237F")

    label("loc_22D8")


    ChrTalk(    #133
        0xFE,
        (
            "因为军队的劝告，我们\x01",
            "只能在这里等待……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "这种时候，\x01",
            "就是考验忍耐力的时候呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "总之就算着急也没用，\x01",
            "只有慢慢等了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "耐心等待的话\x01",
            "也许会有好结果的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_237F")

    Jump("loc_243A")

    label("loc_2382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_243A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_23E3")

    ChrTalk(    #137
        0xFE,
        (
            "迷雾峡谷周围环境…\x01",
            "特别是天气很容易变化。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "我们必须慎重地\x01",
            "看清楚变化。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_243A")

    label("loc_23E3")


    ChrTalk(    #139
        0xFE,
        (
            "食物的分配，\x01",
            "装备的检查都完成了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "之后就等进山了，\x01",
            "只剩等一个好时机了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_243A")

    TalkEnd(0xE)
    Return()

    # Function_12_2180 end

    def Function_13_243E(): pass

    label("Function_13_243E")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_252D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24E1")

    ChrTalk(    #141
        0xFE,
        (
            "我虽是帝国人，\x01",
            "但帝国真的会行动吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "既然和利贝尔王国\x01",
            "刚刚缔结了互不侵犯条约……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "突然像这样背信的行动\x01",
            "也是祖国不想有的吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_252A")

    label("loc_24E1")


    ChrTalk(    #144
        0xFE,
        "但帝国真的会行动吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "和利贝尔王国刚刚才\x01",
            "缔结了互不侵犯条约……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_252A")

    Jump("loc_268E")

    label("loc_252D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_268E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2611")

    ChrTalk(    #146
        0xFE,
        (
            "因定期船停航，只能\x01",
            "从陆路回帝国了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "遇到这样的情况\x01",
            "真是做梦也没想到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "我身为帝国商人的一员\x01",
            "祝愿祖国的繁荣……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "不过，那应该能通过\x01",
            "和平的方式达成的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "两国间的关系紧张\x01",
            "实在是可惜呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_268E")

    label("loc_2611")


    ChrTalk(    #151
        0xFE,
        (
            "我身为帝国商人的一员\x01",
            "祈祷祖国的繁荣……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "不过，那应该能通过\x01",
            "和平的方式达成的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "两国间的关系紧张\x01",
            "实在是可惜呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_268E")

    TalkEnd(0xF)
    Return()

    # Function_13_243E end

    def Function_14_2692(): pass

    label("Function_14_2692")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #154
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_14_2692 end

    SaveToFile()

Try(main)
