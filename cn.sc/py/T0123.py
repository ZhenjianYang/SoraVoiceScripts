from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0123   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0123.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0123   ._SN',
            'ED6_DT21/T0123_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '爱娜',                                 # 9
        '雪拉扎德',                             # 10
        '阿加特',                               # 11
        '奥利维尔',                             # 12
        '科洛丝',                               # 13
        '提妲',                                 # 14
        '金',                                   # 15
        '克劳斯市长',                           # 16
        '里农',                                 # 17
        '布露姆老奶奶',                         # 18
        '基蒂',                                 # 19
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
        'ED6_DT07/CH02560 ._CH',             # 00
        'ED6_DT07/CH00020 ._CH',             # 01
        'ED6_DT07/CH00050 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00040 ._CH',             # 04
        'ED6_DT07/CH00060 ._CH',             # 05
        'ED6_DT07/CH00070 ._CH',             # 06
        'ED6_DT07/CH00023 ._CH',             # 07
        'ED6_DT07/CH00053 ._CH',             # 08
        'ED6_DT07/CH00033 ._CH',             # 09
        'ED6_DT07/CH00073 ._CH',             # 0A
        'ED6_DT07/CH02350 ._CH',             # 0B
        'ED6_DT07/CH01040 ._CH',             # 0C
        'ED6_DT07/CH01010 ._CH',             # 0D
        'ED6_DT07/CH01770 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH02560P._CP',             # 00
        'ED6_DT07/CH00020P._CP',             # 01
        'ED6_DT07/CH00050P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00040P._CP',             # 04
        'ED6_DT07/CH00060P._CP',             # 05
        'ED6_DT07/CH00070P._CP',             # 06
        'ED6_DT07/CH00023P._CP',             # 07
        'ED6_DT07/CH00053P._CP',             # 08
        'ED6_DT07/CH00033P._CP',             # 09
        'ED6_DT07/CH00073P._CP',             # 0A
        'ED6_DT07/CH02350P._CP',             # 0B
        'ED6_DT07/CH01040P._CP',             # 0C
        'ED6_DT07/CH01010P._CP',             # 0D
        'ED6_DT07/CH01770P._CP',             # 0E
    )

    DeclNpc(
        X                   = 750,
        Z                   = 0,
        Y                   = 118600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3800,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 47500,
        Z                   = 0,
        Y                   = -1110,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 46300,
        Z                   = 0,
        Y                   = -1110,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    DeclActor(
        TriggerX            = 1271,
        TriggerZ            = 0,
        TriggerY            = 116402,
        TriggerRange        = 800,
        ActorX              = 750,
        ActorZ              = 1500,
        ActorY              = 118600,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3810,
        TriggerZ            = 0,
        TriggerY            = 1080,
        TriggerRange        = 800,
        ActorX              = 3800,
        ActorZ              = 1500,
        ActorY              = 2000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4900,
        TriggerZ            = 0,
        TriggerY            = 112600,
        TriggerRange        = 1400,
        ActorX              = 4900,
        ActorZ              = 2000,
        ActorY              = 112600,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2EE",          # 00, 0
        "Function_1_2EF",          # 01, 1
        "Function_2_3D6",          # 02, 2
        "Function_3_553",          # 03, 3
        "Function_4_651",          # 04, 4
        "Function_5_656",          # 05, 5
        "Function_6_8EF",          # 06, 6
        "Function_7_D78",          # 07, 7
        "Function_8_EB6",          # 08, 8
        "Function_9_FEC",          # 09, 9
        "Function_10_11D5",        # 0A, 10
        "Function_11_1414",        # 0B, 11
        "Function_12_150C",        # 0C, 12
        "Function_13_173D",        # 0D, 13
        "Function_14_1902",        # 0E, 14
        "Function_15_1A0F",        # 0F, 15
        "Function_16_2D41",        # 10, 16
        "Function_17_2E73",        # 11, 17
        "Function_18_2EC4",        # 12, 18
        "Function_19_2F4E",        # 13, 19
    )


    def Function_0_2EE(): pass

    label("Function_0_2EE")

    Return()

    # Function_0_2EE end

    def Function_1_2EF(): pass

    label("Function_1_2EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_335")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 8)
    SetChrPos(0xA, -790, 200, 69820, 360)

    label("loc_335")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_362")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 9)
    SetChrPos(0xB, 1060, 200, 69820, 360)

    label("loc_362")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_385")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -1940, 0, 74490, 360)

    label("loc_385")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A8")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -4290, 0, 73800, 360)

    label("loc_3A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3D5")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 10)
    SetChrPos(0xE, 140, 200, 71510, 180)

    label("loc_3D5")

    Return()

    # Function_1_2EF end

    def Function_2_3D6(): pass

    label("Function_2_3D6")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FB")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_53D")

    label("loc_3FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_414")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_53D")

    label("loc_414")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42D")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_53D")

    label("loc_42D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_446")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_53D")

    label("loc_446")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45F")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_53D")

    label("loc_45F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_478")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_53D")

    label("loc_478")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_491")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_53D")

    label("loc_491")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AA")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_53D")

    label("loc_4AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C3")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_53D")

    label("loc_4C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DC")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_53D")

    label("loc_4DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F5")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_53D")

    label("loc_4F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50E")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_53D")

    label("loc_50E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_527")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_53D")

    label("loc_527")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53D")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_53D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_552")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_53D")

    label("loc_552")

    Return()

    # Function_2_3D6 end

    def Function_3_553(): pass

    label("Function_3_553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_572")
    Call(0, 15)
    Jump("loc_650")

    label("loc_572")

    TalkBegin(0x8)
    Call(6, 5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63B")
    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x3)"), scpexpr(EXPR_END)), "loc_5E1")

    ChrTalk(    #0
        0x8,
        (
            "#740F辛苦了。\x01",
            "看来顺利达成目的了呢。\x02\x03",

            "完成了什么任务的话\x01",
            "再来报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_632")

    label("loc_5E1")


    ChrTalk(    #1
        0x8,
        (
            "#740F哎呀，现在\x01",
            "好像没有可以报告的工作吧。\x02\x03",

            "完成了什么任务的话\x01",
            "再来报告吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_632")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_63B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_64C")
    TalkEnd(0x8)
    Return()

    label("loc_64C")

    Call(0, 5)

    label("loc_650")

    Return()

    # Function_3_553 end

    def Function_4_651(): pass

    label("Function_4_651")

    Call(0, 6)
    Return()

    # Function_4_651 end

    def Function_5_656(): pass

    label("Function_5_656")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_807")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C9")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "报告\x01",          # 1
            "呼叫同伴\x01",      # 2
            "离开\x01",          # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jump("loc_6CD")

    label("loc_6C9")

    Call(6, 5)

    label("loc_6CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F6")
    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_747")
    OP_28(0xC3, 0x4, 0x20)
    OP_A9(0x3)

    ChrTalk(    #2
        0x8,
        (
            "#740F辛苦了。\x01",
            "看来顺利达成目的了呢。\x02\x03",

            "完成了什么任务的话\x01",
            "再来报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7ED")

    label("loc_747")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x3)"), scpexpr(EXPR_END)), "loc_79C")

    ChrTalk(    #3
        0x8,
        (
            "#740F辛苦了。\x01",
            "看来顺利达成目的了呢。\x02\x03",

            "完成了什么任务的话\x01",
            "再来报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7ED")

    label("loc_79C")


    ChrTalk(    #4
        0x8,
        (
            "#740F哎呀，现在\x01",
            "好像没有可以报告的工作吧。\x02\x03",

            "完成了什么任务的话\x01",
            "再来报告吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7ED")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_7F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_807")
    TalkEnd(0x8)
    Return()

    label("loc_807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_826")
    Call(0, 15)
    Jump("loc_8EE")

    label("loc_826")

    OP_A2(0x1884)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_878")

    ChrTalk(    #5
        0x8,
        (
            "#740F那么，昏睡事件的调查\x01",
            "麻烦你们了。\x02\x03",

            "请你们\x01",
            "小心谨慎的进行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EB")

    label("loc_878")


    ChrTalk(    #6
        0x8,
        (
            "#740F听说你们在克劳斯市长的\x01",
            "委托下开始调查昏睡事件了？\x02\x03",

            "我们已经正式\x01",
            "受到委托了。\x02\x03",

            "那么调查就\x01",
            "麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_8EB")

    TalkEnd(0x8)

    label("loc_8EE")

    Return()

    # Function_5_656 end

    def Function_6_8EF(): pass

    label("Function_6_8EF")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 5)), scpexpr(EXPR_END)), "loc_924")
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_913")
    OP_A9(0x2)
    TalkEnd(0x10)
    Return()

    label("loc_913")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_924")
    TalkEnd(0x10)
    Return()

    label("loc_924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_D74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 5)), scpexpr(EXPR_END)), "loc_B50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_9CB")

    ChrTalk(    #7
        0x10,
        (
            "我老妈带回来的那位小姐，\x01",
            "说要在店里帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "这、这一定是……\x01",
            "为了让我结婚设计的阴谋啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "啊，真郁闷……\x01",
            "我该怎么拒绝呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE1")

    label("loc_9CB")


    ChrTalk(    #10
        0x10,
        "哟，这么晚，辛苦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "游击士真不容易啊，\x01",
            "现在对我个人来说是个大危机……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "我老妈带回来的那个小姐，\x01",
            "说要在店里帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "本来这是一件好事，\x01",
            "不过一和我老妈扯上关系……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "这、这一定是……\x01",
            "这是为了让我结婚设计的阴谋啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "啊，真郁闷……\x01",
            "可我还不想结婚啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_AE1")

    Jump("loc_B4D")

    label("loc_AE4")


    ChrTalk(    #16
        0x10,
        (
            "如果装备不足的话，\x01",
            "请随时过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "今晚还没\x01",
            "那么快打烊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "那么，艾丝蒂尔你们\x01",
            "工作也要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4D")

    Jump("loc_D74")

    label("loc_B50")

    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x10, 0x101, 0)
    Sleep(400)

    ChrTalk(    #19
        0x10,
        (
            "哦！\x01",
            "艾丝蒂尔，终于来了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1008F里农先生……\x01",
            "嘿嘿，好久不见。\x02\x03",

            "这么晚才来跟你打招呼，真对不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        "哪里哪里，没关系啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "不过你回来的\x01",
            "可真不是时候啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "莫非你们现在\x01",
            "还在巡逻什么的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1015F啊，嗯……\x01",
            "算是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x103,
        (
            "#020F嗯，为了以防万一，\x01",
            "协会也提高了警惕。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x103, 400)

    ChrTalk(    #26
        0x10,
        "呼，真不容易。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "不过这样一来\x01",
            "就给我们这些居民壮胆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "如果装备不足的话\x01",
            "请随时过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "今晚还没\x01",
            "那么快打烊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x103,
        "#525F谢谢，真是太好了㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1006F嗯……\x01",
            "那么，里农先生。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #32
        0x10,
        "嗯，你们加油工作吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1885)
    OP_A2(0x2)

    label("loc_D74")

    TalkEnd(0x10)
    Return()

    # Function_6_8EF end

    def Function_7_D78(): pass

    label("Function_7_D78")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_EB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_DE4")

    ChrTalk(    #33
        0xFE,
        (
            "基蒂小姐从明天起\x01",
            "要在店里帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "里农的表情虽然很复杂，\x01",
            "不过我可没说过什么。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB2")

    label("loc_DE4")


    ChrTalk(    #35
        0xFE,
        (
            "这是基蒂小姐自己\x01",
            "强烈要求的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "她从明天起就要在我家的\x01",
            "店里帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "可是我家的里农\x01",
            "表情却很复杂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "他好像以为\x01",
            "这是我安排的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "可能因为我去给他找过新娘，\x01",
            "那孩子的警惕性一下子升高了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_EB2")

    TalkEnd(0x11)
    Return()

    # Function_7_D78 end

    def Function_8_EB6(): pass

    label("Function_8_EB6")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_FE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_F20")

    ChrTalk(    #40
        0xFE,
        (
            "在我好说歹说下，\x01",
            "终于能在这店里帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "既然受了别人的关照，\x01",
            "就得有所回报。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE8")

    label("loc_F20")


    ChrTalk(    #42
        0xFE,
        (
            "在我不断拜托之下\x01",
            "终于能在这店里帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "受了别人的关照，\x01",
            "就得有所回报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "……不过老太太的儿子\x01",
            "好像有点不高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "像我这种不明来历的人，\x01",
            "突然来到店里，\x01",
            "果然还是令人比较在意吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_FE8")

    TalkEnd(0x12)
    Return()

    # Function_8_EB6 end

    def Function_9_FEC(): pass

    label("Function_9_FEC")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_107C")
    Jump("loc_10BE")

    label("loc_107C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1098")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10BE")

    label("loc_1098")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10B4")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10BE")

    label("loc_10B4")

    OP_51(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10BE")

    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)

    ChrTalk(    #46
        0xA,
        "#050F哟，调查还顺利吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_115D"),
        (1, "loc_118A"),
        (SWITCH_DEFAULT, "loc_11CC"),
    )


    label("loc_115D")


    ChrTalk(    #47
        0xA,
        (
            "#051F哦，知道了。\x01",
            "要调整队伍吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 14)
    Jump("loc_11CC")

    label("loc_118A")


    ChrTalk(    #48
        0xA,
        (
            "#052F怎么，不调整了吗？\x02\x03",

            "#050F需要我的重剑时\x01",
            "尽管开口吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CC")

    label("loc_11CC")

    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)
    Return()

    # Function_9_FEC end

    def Function_10_11D5(): pass

    label("Function_10_11D5")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1265")
    Jump("loc_12A7")

    label("loc_1265")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1281")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12A7")

    label("loc_1281")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_129D")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12A7")

    label("loc_129D")

    OP_51(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12A7")

    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(    #49
        0xB,
        (
            "#034F真是的……\x01",
            "真是个麻烦的夜晚。\x02\x03",

            "#030F如果你们希望的话，\x01",
            "我来唱一曲给你们散散心如何？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1387"),
        (1, "loc_13C8"),
        (SWITCH_DEFAULT, "loc_140B"),
    )


    label("loc_1387")


    ChrTalk(    #50
        0xB,
        (
            "#030F呵，原来如此。\x02\x03",

            "看来是需要\x01",
            "我这个天才的力量啊。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 14)
    Jump("loc_140B")

    label("loc_13C8")


    ChrTalk(    #51
        0xB,
        (
            "#030F哎呀，不要我了吗？\x02\x03",

            "呵呵，那么我就在这里\x01",
            "静候佳音了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_140B")

    label("loc_140B")

    SetChrSubChip(0xB, 0)
    TalkEnd(0xB)
    Return()

    # Function_10_11D5 end

    def Function_11_1414(): pass

    label("Function_11_1414")

    TalkBegin(0xC)

    ChrTalk(    #52
        0xC,
        (
            "#043F啊，各位……\x02\x03",

            "有什么我\x01",
            "可以帮忙的吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_14A4"),
        (1, "loc_14CD"),
        (SWITCH_DEFAULT, "loc_1508"),
    )


    label("loc_14A4")


    ChrTalk(    #53
        0xC,
        (
            "#042F明白了。\x01",
            "要调整队伍吧？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 14)
    Jump("loc_1508")

    label("loc_14CD")


    ChrTalk(    #54
        0xC,
        (
            "#049F外面雾很浓……\x02\x03",

            "希望不要增添更多的\x01",
            "受害者……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1508")

    label("loc_1508")

    TalkEnd(0xC)
    Return()

    # Function_11_1414 end

    def Function_12_150C(): pass

    label("Function_12_150C")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_154D")

    ChrTalk(    #55
        0xD,
        (
            "#560F啊，阿加特哥哥。\x02\x03",

            "那个，有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C0")

    label("loc_154D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_158D")

    ChrTalk(    #56
        0x107,
        (
            "#060F啊，姐姐，是你们啊。\x01",
            "怎么了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C0")

    label("loc_158D")


    ChrTalk(    #57
        0x107,
        (
            "#060F啊，姐姐，是你们啊。\x02\x03",

            "那个，有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C0")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_161D"),
        (1, "loc_168C"),
        (SWITCH_DEFAULT, "loc_1739"),
    )


    label("loc_161D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_165F")

    ChrTalk(    #58
        0x107,
        (
            "#060F啊，嗯，明白了。\x01",
            "要调整队伍吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1685")

    label("loc_165F")


    ChrTalk(    #59
        0x107,
        (
            "#560F啊，明白了。\x01",
            "要调整队伍吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1685")

    Call(0, 14)
    Jump("loc_1739")

    label("loc_168C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16ED")

    ChrTalk(    #60
        0x107,
        (
            "#064F咦，又不要了吗……？\x02\x03",

            "#060F我就在这里等，\x01",
            "有什么事就来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1736")

    label("loc_16ED")


    ChrTalk(    #61
        0x107,
        (
            "#064F咦，又不要了吗……？\x02\x03",

            "#060F我会在这里等的，\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1736")

    Jump("loc_1739")

    label("loc_1739")

    TalkEnd(0xD)
    Return()

    # Function_12_150C end

    def Function_13_173D(): pass

    label("Function_13_173D")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17CD")
    Jump("loc_180F")

    label("loc_17CD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_17E9")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_180F")

    label("loc_17E9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1805")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_180F")

    label("loc_1805")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_180F")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(    #62
        0xE,
        "#072F哟，状态怎么样？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_18AC"),
        (1, "loc_18CA"),
        (SWITCH_DEFAULT, "loc_18F9"),
    )


    label("loc_18AC")


    ChrTalk(    #63
        0xE,
        "#072F要更换队员？\x02",
    )

    CloseMessageWindow()
    Call(0, 14)
    Jump("loc_18F9")

    label("loc_18CA")


    ChrTalk(    #64
        0xE,
        (
            "#072F我在这里等，\x01",
            "需要的时候就说一声。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18F9")

    label("loc_18F9")

    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Return()

    # Function_13_173D end

    def Function_14_1902(): pass

    label("Function_14_1902")

    OP_C9(0x1, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_196D")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 8)
    SetChrPos(0xA, -790, 200, 69820, 360)

    label("loc_196D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_199A")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 9)
    SetChrPos(0xB, 1060, 200, 69820, 360)

    label("loc_199A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19BD")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -1940, 0, 74490, 360)

    label("loc_19BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19E0")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -4290, 0, 73800, 360)

    label("loc_19E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A0D")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 10)
    SetChrPos(0xE, 140, 200, 71510, 180)

    label("loc_1A0D")

    OP_0D()
    Return()

    # Function_14_1902 end

    def Function_15_1A0F(): pass

    label("Function_15_1A0F")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A33")
    Call(0, 18)
    FadeToBright(0, 0)
    Call(0, 19)

    label("loc_1A33")

    Fade(1000)
    OP_6D(370, 0, 117930, 0)
    OP_67(0, 6810, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 640, 0, 116600, 0)
    SetChrPos(0x103, 1600, 0, 116600, 0)
    SetChrPos(0xF8, 1800, 0, 115320, 0)
    SetChrPos(0xF9, 840, 0, 115320, 0)
    OP_8C(0x8, 180, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6D")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇从教会出来之后没跟爱娜说话】\x01",        # 0
            "【◇从教会出来之后已经跟爱娜说话】\x01",      # 1
            "【◇不变更】\x01",                            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B61"),
        (1, "loc_1B67"),
        (SWITCH_DEFAULT, "loc_1B6D"),
    )


    label("loc_1B61")

    OP_A3(0x1884)
    Jump("loc_1B6D")

    label("loc_1B67")

    OP_A2(0x1884)
    Jump("loc_1B6D")

    label("loc_1B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BCA")

    ChrTalk(    #65
        0x8,
        (
            "#742F听说你们在克劳斯市长的\x01",
            "委托下开始调查昏睡事件了？\x02\x03",

            "怎么样？调查得如何？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C03")

    label("loc_1BCA")


    ChrTalk(    #66
        0x8,
        (
            "#742F事件的调查，辛苦你们了。\x02\x03",

            "怎么样？调查得如何？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C03")


    ChrTalk(    #67
        0x101,
        (
            "#1025F#6P啊，嗯。\x02\x03",

            "从昏睡者的家人那里\x01",
            "大致了解过情况了……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【继续调查】\x01",        # 0
            "【向爱娜报告】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE6")

    ChrTalk(    #68
        0x8,
        (
            "#742F明白了。\x02\x03",

            "等情况都了解完后\x01",
            "就回协会了报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1884)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Jump("loc_2D40")

    label("loc_1CE6")


    ChrTalk(    #69
        0x8,
        (
            "#742F明白了。\x02\x03",

            "那么，把大家叫来\x01",
            "对信息进行一遍整理吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    Call(0, 16)
    OP_4A(0x8, 255)
    OP_6D(140, 0, 117080, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 510, 0, 116600, 0)
    SetChrPos(0x103, 1570, 0, 116600, 0)
    SetChrPos(0x105, -230, 0, 115790, 0)
    SetChrPos(0x104, 2320, 0, 115270, 0)
    SetChrPos(0x107, 1070, 0, 115580, 0)
    SetChrPos(0x108, 250, 0, 114280, 0)
    SetChrPos(0x106, 1500, 0, 114310, 0)
    OP_8C(0x8, 180, 0)
    OP_1D(0x73)
    Sleep(500)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #70
        0x8,
        (
            "#744F……原来如此。\x01",
            "你们调查到不少情况了呢。\x02\x03",

            "#742F尤其是昏睡者的\x01",
            "相关人员对事件描述很有意思。\x02\x03",

            "总之在所有的描述中\x01",
            "有一个地方是完全相符的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#1004F#6P啊，那是指……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #72
        "\x18\x07\x05４份描述的共同点是？\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【昏睡的时刻】\x01",        # 0
            "【是否有目击者】\x01",      # 1
            "【听见的声音】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F70"),
        (1, "loc_20BB"),
        (2, "loc_2135"),
        (SWITCH_DEFAULT, "loc_2224"),
    )


    label("loc_1F70")

    TurnDirection(0x103, 0x101, 400)
    Sleep(500)

    ChrTalk(    #73
        0x103,
        (
            "#524F不……\x01",
            "这方面各自都有微妙的差别。\x02\x03",

            "玲达小姐是在５点前被\x01",
            "在准备饭菜的夫人发现的，\x01",
            "所以实际昏睡应该在４点半前后。\x02\x03",

            "另一方面，拉欧爷爷\x01",
            "是在５点半左右昏睡的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #74
        0x101,
        (
            "#1015F#5P这样啊……\x01",
            "有一个小时的差距啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x103,
        (
            "#026F４个人的案子共同拥有的特点……\x02\x03",

            "#022F那就是昏睡时\x01",
            "都没有目击者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#1004F#5P啊……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2224")

    label("loc_20BB")

    OP_2B(0x90, 0x3)
    TurnDirection(0x103, 0x101, 400)
    Sleep(500)

    ChrTalk(    #77
        0x103,
        (
            "#026F嗯，确实是这样。\x02\x03",

            "#022F４个人的案子共同拥有的特点……\x02\x03",

            "就是昏睡的瞬间\x01",
            "都没有目击者。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_2224")

    label("loc_2135")

    OP_2B(0x90, 0x1)
    TurnDirection(0x103, 0x101, 400)
    Sleep(500)

    ChrTalk(    #78
        0x103,
        (
            "#524F……铃声啊。\x02\x03",

            "确实很令人在意，\x01",
            "不过在托露塔夫人和鲁克的案子里\x01",
            "都没有提到铃声。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #79
        0x101,
        "#1015F#5P哦，对……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x103,
        (
            "#026F４个人的案子共同拥有的特点……\x02\x03",

            "#022F那就是昏睡时\x01",
            "都没有目击者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        "#1004F#5P啊……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2224")

    label("loc_2224")


    ChrTalk(    #82
        0x106,
        (
            "#051F#6P哟，原来如此。\x02\x03",

            "就好像是算准时机\x01",
            "一样地睡着了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 90, 400)
    Sleep(500)

    ChrTalk(    #83
        0x105,
        (
            "#043F#5P如果是这样的话，\x01",
            "这场雾的背后似乎就隐藏着什么了。\x02\x03",

            "视野这么差，\x01",
            "目击者就会减少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x104,
        (
            "#035F#6P悄悄地出现在雾中，\x01",
            "会吞噬牺牲者灵魂的恶魔……\x02\x03",

            "#030F这种妖艳的印象\x01",
            "浮现在我的眼前。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x107,
        "#065F#6P啊啊啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        "#1007F#5P唔，鸡皮疙瘩也起来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        (
            "#744F经你这么一说……\x02\x03",

            "#740F好像就有了能确定恶魔印象\x01",
            "的有力描述了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x103,
        (
            "#026F嗯……\x01",
            "『铃声』和『黑衣女人』。\x02\x03",

            "#022F这些看来都和\x01",
            "昏睡事件有关。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#1015F#5P先不说铃声，\x01",
            "看到黑衣女人的\x01",
            "应该是伊莉莎吧。\x02\x03",

            "有没有是偶然的可能性呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x103,
        (
            "#027F不……这不可能。\x02\x03",

            "如果你仔细想想那个女人\x01",
            "出现的地方发生了什么的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        "#1004F#5P啊……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #92
        "\x18\x07\x05在黑衣女人出现的地方发生了什么？\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【托露塔昏睡了】\x01",        # 0
            "【拉欧爷爷昏睡了】\x01",      # 1
            "【鲁克昏睡了】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_257C"),
        (1, "loc_25F4"),
        (2, "loc_2662"),
        (SWITCH_DEFAULT, "loc_26B8"),
    )


    label("loc_257C")


    ChrTalk(    #93
        0x103,
        (
            "#026F托露塔夫人是倒在\x01",
            "酒馆二楼的阳台上的。\x02\x03",

            "既然黑衣女子\x01",
            "是出现在钟楼上的……\x02\x03",

            "#022F帕特是在那里\x01",
            "发现鲁克的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B8")

    label("loc_25F4")


    ChrTalk(    #94
        0x103,
        (
            "#026F拉欧爷爷是倒在\x01",
            "自家门口的。\x02\x03",

            "既然黑衣女子\x01",
            "是出现在钟楼上的……\x02\x03",

            "#022F帕特是在那里\x01",
            "发现鲁克的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B8")

    label("loc_2662")

    OP_2B(0x90, 0x3)

    ChrTalk(    #95
        0x103,
        (
            "#026F对，黑衣女子\x01",
            "是出现在钟楼上的……\x02\x03",

            "#022F帕特是在那里\x01",
            "发现鲁克的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B8")

    label("loc_26B8")


    ChrTalk(    #96
        0x101,
        (
            "#1020F#5P确、确实……\x01",
            "不可能是偶然。\x02\x03",

            "那么那个\x01",
            "黑衣女人果然……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x108,
        (
            "#074F嗯，没错。\x02\x03",

            "#072F看来又有新的\x01",
            "『执行者』出现了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x106,
        "#057F#6P哼……果然是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x105,
        (
            "#047F#5P原因不明的雾和昏睡\x01",
            "是这次的『不可能的现象』。\x02\x03",

            "#042F那么铃声\x01",
            "就是『暗示』了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "#744F现在总算能\x01",
            "确定敌人的身份了。\x02\x03",

            "#742F我接下来要联络\x01",
            "各地支部和王国军……\x02\x03",

            "你们有什么打算？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 0, 400)

    def lambda_2824():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2824)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #101
        0x103,
        (
            "#522F#6P是啊……\x02\x03",

            "这样下去不知何时\x01",
            "又会有其他市民遭到袭击。\x02\x03",

            "#022F我们应该彻夜巡逻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#1006F#6P嗯，我也赞成。\x02\x03",

            "换班进行的话\x01",
            "也能稍微得到一点休息。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x108, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(50)
    OP_63(0x108)

    ChrTalk(    #103
        0x108,
        "#070F啊，没这个必要。\x02",
    )

    CloseMessageWindow()

    def lambda_2929():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2929)
    Sleep(50)

    def lambda_293C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_293C)
    Sleep(50)

    def lambda_294F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_294F)
    Sleep(50)

    def lambda_2962():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2962)
    Sleep(400)

    ChrTalk(    #104
        0x101,
        "#1004F#5P啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x106,
        (
            "#051F#6P晚上的巡逻就\x01",
            "交给我们这些男人吧。\x02\x03",

            "你们就一起\x01",
            "在家好好休息吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1026F#5P但，但是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #107
        0x103,
        (
            "#524F是啊，艾丝蒂尔\x01",
            "今天也累了吧。\x02\x03",

            "你带公主还有\x01",
            "提妲去家里吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #108
        0x101,
        (
            "#1026F#5P啊……\x02\x03",

            "#1007F……嗯，好的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x106,
        (
            "#555F#6P我说，雪拉扎德，\x01",
            "你怎么说得事不关己一样啊。\x02\x03",

            "我都说了巡逻交给\x01",
            "我们这些男人了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x103, 180, 400)

    def lambda_2AF0():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AF0)

    ChrTalk(    #110
        0x103,
        "#023F#2P……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x108,
        (
            "#070F你和艾丝蒂尔\x01",
            "在调查上已经很努力了。\x02\x03",

            "也可以说是换班吧，\x01",
            "今晚你们就好好休息吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x103,
        (
            "#024F#2P你、你等等……\x02\x03",

            "对Ｂ级游击士\x01",
            "没必要有这方面的担心！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x104,
        (
            "#030F#6P雪拉，\x01",
            "这个你就听他的吧。\x02\x03",

            "虽然你装出一副没事的样子，\x01",
            "不过疲劳完全浮现在脸上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x103,
        "#522F#2P……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x104,
        (
            "#031F#6P在必要的时候休息，\x01",
            "不也是游击士的工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x103,
        (
            "#522F#2P…………………………\x02\x03",

            "#025F……没错。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(500)

    ChrTalk(    #117
        0x101,
        "#1026F#5P雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x103,
        (
            "#524F#2P金先生、阿加特，\x02\x03",

            "夜间的巡逻……\x01",
            "就麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x108,
        "#071F嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x106,
        (
            "#051F#6P明天则需要你\x01",
            "努力工作了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearParty()
    AddParty(0x0, 0xF6, 0xFF)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T0101   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_2D40")

    Return()

    # Function_15_1A0F end

    def Function_16_2D41(): pass

    label("Function_16_2D41")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D7A")
    AddParty(0x3, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2DB3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D9B")
    AddParty(0x4, 0xFA, 0xFF)
    Jump("loc_2D9F")

    label("loc_2D9B")

    AddParty(0x4, 0xFB, 0xFF)

    label("loc_2D9F")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2DB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E00")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DD4")
    AddParty(0x7, 0xFA, 0xFF)
    Jump("loc_2DEC")

    label("loc_2DD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DE8")
    AddParty(0x7, 0xFB, 0xFF)
    Jump("loc_2DEC")

    label("loc_2DE8")

    AddParty(0x7, 0xFC, 0xFF)

    label("loc_2DEC")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E4D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E21")
    AddParty(0x5, 0xFA, 0xFF)
    Jump("loc_2E39")

    label("loc_2E21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E35")
    AddParty(0x5, 0xFB, 0xFF)
    Jump("loc_2E39")

    label("loc_2E35")

    AddParty(0x5, 0xFC, 0xFF)

    label("loc_2E39")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E72")
    AddParty(0x6, 0xFC, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E72")

    Return()

    # Function_16_2D41 end

    def Function_17_2E73(): pass

    label("Function_17_2E73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2E83")
    RemoveParty(0x3, 0xFF)

    label("loc_2E83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2E93")
    RemoveParty(0x4, 0xFF)

    label("loc_2E93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2EA3")
    RemoveParty(0x6, 0xFF)

    label("loc_2EA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2EB3")
    RemoveParty(0x7, 0xFF)

    label("loc_2EB3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2EC3")
    RemoveParty(0x5, 0xFF)

    label("loc_2EC3")

    Return()

    # Function_17_2E73 end

    def Function_18_2EC4(): pass

    label("Function_18_2EC4")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_2F41"),
        (1, "loc_2F47"),
        (SWITCH_DEFAULT, "loc_2F4D"),
    )


    label("loc_2F41")

    OP_A2(0x1200)
    Jump("loc_2F4D")

    label("loc_2F47")

    OP_A2(0x1201)
    Jump("loc_2F4D")

    label("loc_2F4D")

    Return()

    # Function_18_2EC4 end

    def Function_19_2F4E(): pass

    label("Function_19_2F4E")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_19_2F4E end

    SaveToFile()

Try(main)
