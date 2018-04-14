from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1121   ._SN',
        MapName             = 'Bose',
        Location            = 'T1121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 1,
        EntryFunctionIndex  = 2,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1121_1 ._SN',
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
        '卢格兰老人',                           # 9
        '梅贝尔市长',                           # 10
        '莉拉',                                 # 11
        '雪拉扎德',                             # 12
        '奥利维尔',                             # 13
        '科洛丝',                               # 14
        '阿加特',                               # 15
        '提妲',                                 # 16
        '金',                                   # 17
        '艾丝蒂尔',                             # 18
        '约修亚',                               # 19
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
        'ED6_DT07/CH02380 ._CH',             # 00
        'ED6_DT07/CH02360 ._CH',             # 01
        'ED6_DT07/CH02370 ._CH',             # 02
        'ED6_DT07/CH00020 ._CH',             # 03
        'ED6_DT07/CH00030 ._CH',             # 04
        'ED6_DT07/CH00040 ._CH',             # 05
        'ED6_DT07/CH00050 ._CH',             # 06
        'ED6_DT07/CH00060 ._CH',             # 07
        'ED6_DT07/CH00070 ._CH',             # 08
        'ED6_DT07/CH00023 ._CH',             # 09
        'ED6_DT07/CH00033 ._CH',             # 0A
        'ED6_DT07/CH00043 ._CH',             # 0B
        'ED6_DT07/CH00063 ._CH',             # 0C
        'ED6_DT07/CH00073 ._CH',             # 0D
        'ED6_DT27/CH03000 ._CH',             # 0E
        'ED6_DT27/CH03010 ._CH',             # 0F
        'ED6_DT07/CH00053 ._CH',             # 10
        'ED6_DT26/CH20311 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT07/CH02380P._CP',             # 00
        'ED6_DT07/CH02360P._CP',             # 01
        'ED6_DT07/CH02370P._CP',             # 02
        'ED6_DT07/CH00020P._CP',             # 03
        'ED6_DT07/CH00030P._CP',             # 04
        'ED6_DT07/CH00040P._CP',             # 05
        'ED6_DT07/CH00050P._CP',             # 06
        'ED6_DT07/CH00060P._CP',             # 07
        'ED6_DT07/CH00070P._CP',             # 08
        'ED6_DT07/CH00023P._CP',             # 09
        'ED6_DT07/CH00033P._CP',             # 0A
        'ED6_DT07/CH00043P._CP',             # 0B
        'ED6_DT07/CH00063P._CP',             # 0C
        'ED6_DT07/CH00073P._CP',             # 0D
        'ED6_DT27/CH03000P._CP',             # 0E
        'ED6_DT27/CH03010P._CP',             # 0F
        'ED6_DT07/CH00053P._CP',             # 10
        'ED6_DT26/CH20311P._CP',             # 11
    )

    DeclNpc(
        X                   = 180,
        Z                   = 0,
        Y                   = 4400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x114,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 130,
        TriggerZ            = 0,
        TriggerY            = 3000,
        TriggerRange        = 600,
        ActorX              = 180,
        ActorZ              = 1500,
        ActorY              = 4400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4470,
        TriggerZ            = 0,
        TriggerY            = -2690,
        TriggerRange        = 1400,
        ActorX              = -4470,
        ActorZ              = 2000,
        ActorY              = -2690,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3520,
        TriggerZ            = 0,
        TriggerY            = -780,
        TriggerRange        = 1400,
        ActorX              = 3520,
        ActorZ              = 2000,
        ActorY              = -780,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25860,
        TriggerZ            = 0,
        TriggerY            = 21810,
        TriggerRange        = 1000,
        ActorX              = 25860,
        ActorZ              = 1000,
        ActorY              = 21810,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_32A",          # 00, 0
        "Function_1_599",          # 01, 1
        "Function_2_5E0",          # 02, 2
        "Function_3_5F6",          # 03, 3
        "Function_4_5FB",          # 04, 4
        "Function_5_16FD",         # 05, 5
        "Function_6_18E7",         # 06, 6
        "Function_7_1B29",         # 07, 7
        "Function_8_1D1A",         # 08, 8
        "Function_9_2079",         # 09, 9
        "Function_10_2269",        # 0A, 10
        "Function_11_244A",        # 0B, 11
        "Function_12_25B0",        # 0C, 12
        "Function_13_27F1",        # 0D, 13
        "Function_14_4054",        # 0E, 14
        "Function_15_4285",        # 0F, 15
        "Function_16_43F3",        # 10, 16
        "Function_17_494A",        # 11, 17
        "Function_18_49CF",        # 12, 18
        "Function_19_4A32",        # 13, 19
        "Function_20_4A6B",        # 14, 20
        "Function_21_4AA4",        # 15, 21
        "Function_22_4AC9",        # 16, 22
        "Function_23_4AEE",        # 17, 23
        "Function_24_5587",        # 18, 24
        "Function_25_5DA8",        # 19, 25
        "Function_26_736D",        # 1A, 26
        "Function_27_78F5",        # 1B, 27
        "Function_28_8556",        # 1C, 28
        "Function_29_85DD",        # 1D, 29
        "Function_30_86DC",        # 1E, 30
    )


    def Function_0_32A(): pass

    label("Function_0_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_340")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 13)
    Jump("loc_3DC")

    label("loc_340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_356")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 16)
    Jump("loc_3DC")

    label("loc_356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_36C")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 23)
    Jump("loc_3DC")

    label("loc_36C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_38B")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 25)
    Jump("loc_3DC")

    label("loc_38B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_3A1")
    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(0, 24)
    Jump("loc_3DC")

    label("loc_3A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_3C0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F5)
    SetMapFlags(0x10000000)
    Event(0, 26)
    Jump("loc_3DC")

    label("loc_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_3DC")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F6)
    SetMapFlags(0x10000000)
    Event(0, 27)

    label("loc_3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_41E")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 9)
    SetChrPos(0xB, 26770, 200, -3440, 270)

    label("loc_41E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_44B")
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 10)
    SetChrPos(0xC, 28510, 200, -3980, 90)

    label("loc_44B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_478")
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x4)
    SetChrChipByIndex(0xD, 11)
    SetChrPos(0xD, 24150, 200, -3440, 90)

    label("loc_478")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4A5")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x4)
    SetChrChipByIndex(0xF, 12)
    SetChrPos(0xF, 25420, 200, -2270, 180)

    label("loc_4A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4D2")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 13)
    SetChrPos(0x10, 30780, 200, -3130, 270)

    label("loc_4D2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_598")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_514")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 9)
    SetChrPos(0xB, 24140, 200, -3410, 90)

    label("loc_514")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_541")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 16)
    SetChrPos(0xE, 26770, 200, -3440, 270)

    label("loc_541")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_56B")
    ClearChrFlags(0xF, 0x80)
    OP_43(0xF, 0x0, 0x0, 0x2)
    SetChrPos(0xF, 34230, 0, -1860, 0)

    label("loc_56B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_598")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 13)
    SetChrPos(0x10, 25420, 200, -2270, 180)

    label("loc_598")

    Return()

    # Function_0_32A end

    def Function_1_599(): pass

    label("Function_1_599")

    OP_B1("T1121_1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B4")
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x1)

    label("loc_5B4")

    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DF")
    OP_65(0x3, 0x1)

    label("loc_5DF")

    Return()

    # Function_1_599 end

    def Function_2_5E0(): pass

    label("Function_2_5E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5E0")

    label("loc_5F5")

    Return()

    # Function_2_5E0 end

    def Function_3_5F6(): pass

    label("Function_3_5F6")

    Call(0, 4)
    Return()

    # Function_3_5F6 end

    def Function_4_5FB(): pass

    label("Function_4_5FB")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64A")

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

    Jump("loc_662")

    label("loc_64A")


    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",      # 0
            "报告\x01",      # 1
            "离开\x01",      # 2
        )
    )


    label("loc_662")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_68F"),
        (1, "loc_1511"),
        (2, "loc_1649"),
        (SWITCH_DEFAULT, "loc_16F9"),
    )


    label("loc_68F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_9B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_711")

    ChrTalk(    #0
        0x8,
        (
            "#632F话说回来\x01",
            "到底是怎么溜进来的？\x02\x03",

            "就算我上了年纪也难以逃得过我的眼睛。\x01",
            "看来，那家伙的确实是个厉害的家伙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AE")

    label("loc_711")


    ChrTalk(    #1
        0x8,
        (
            "#630F噢，怎么了。\x02\x03",

            "感觉有点不寻常，\x01",
            "不知道楼上在吵闹些什么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#1007F嗯，那个，其实是……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "\x07\x05艾丝蒂尔他们向卢格兰爷爷讲述了\x01",
            "布卢布兰偷偷溜进协会三楼这件事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x8, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #4
        0x8,
        (
            "#633F什，什么！！\x02\x03",

            "#632F呼啊……\x01",
            "竟然眼睁睁地看着被人溜进来……\x02\x03",

            "虽说上了年纪，\x01",
            "但也是我卢格兰此生最大的败笔。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B8")

    ChrTalk(    #5
        0x106,
        (
            "#055F喂喂，老爷子。\x02\x03",

            "动肝火对身体不好哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x106, 400)
    Jump("loc_8F8")

    label("loc_8B8")


    ChrTalk(    #6
        0x101,
        (
            "#1016F卢，卢格兰老爷爷……\x02\x03",

            "不，不用\x01",
            "这么自责嘛……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    label("loc_8F8")


    ChrTalk(    #7
        0x8,
        (
            "#632F不行，这不只是面子问题。\x01",
            "不能就此罢休。\x02\x03",

            "如果不追究的话，\x01",
            "协会的权威将荡然无存。\x02\x03",

            "你们就算把这个柏斯翻个底朝天，\x01",
            "也要把那家伙给我抓到！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1002F嗯……知道了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_8C(0x8, 180, 0)

    label("loc_9AE")

    Jump("loc_150E")

    label("loc_9B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_D95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AED")

    ChrTalk(    #9
        0x8,
        (
            "#630F噢，是你们啊。\x01",
            "发生器的设置真是辛苦了。\x02\x03",

            "王都来过联络了，\x01",
            "已经去过那边了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1002F没有，正准备去。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        (
            "#1042F详细的情况不清楚，\x01",
            "不过似乎是属于高度机密的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#634F噢，原来如此。\x01",
            "因为这个才不能使用通信机啊。\x02\x03",

            "#632F也就是说非常重要。\x01",
            "去的时候切记万事小心啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_B32")

    label("loc_AED")


    ChrTalk(    #13
        0x8,
        (
            "#632F王都的要事……\x01",
            "似乎十分紧急啊。\x02\x03",

            "去的时候务必\x01",
            "多加注意啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B32")

    Jump("loc_D92")

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BEB")

    ChrTalk(    #14
        0x8,
        (
            "#630F『零力场发生器』的设置\x01",
            "看来进展的很顺利。\x02\x03",

            "爱娜和嘉恩那边\x01",
            "刚才已经通过通信机向这里发来了报告。\x02\x03",

            "虽然只剩下蔡斯一处了，\x01",
            "但是未到最后绝对不可以松懈啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D42")

    label("loc_BEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C97")

    ChrTalk(    #15
        0x8,
        (
            "#630F『零力场发生器』的设置\x01",
            "看来进展的很顺利。\x02\x03",

            "爱娜和雾香那边\x01",
            "刚才已经通过通信机向这里发来了报告。\x02\x03",

            "虽然只剩下卢安一处，\x01",
            "但是未到最后绝对不可以松懈啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D42")

    label("loc_C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D42")

    ChrTalk(    #16
        0x8,
        (
            "#630F『零力场发生器』的设置\x01",
            "看来进展的很顺利。\x02\x03",

            "嘉恩和雾香那边\x01",
            "刚才已经通过通信机向这里发来了报告。\x02\x03",

            "虽然只剩下洛连特一处，\x01",
            "但是未到最后绝对不可以松懈啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D42")

    OP_A2(0x0)
    Jump("loc_D92")

    label("loc_D48")


    ChrTalk(    #17
        0x8,
        (
            "#630F发生器的设置\x01",
            "只剩下最后一处了。\x02\x03",

            "切记未到最后绝对不可以松懈啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D92")

    Jump("loc_150E")

    label("loc_D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E29")

    ChrTalk(    #18
        0x8,
        (
            "#632F『零力场发生器』的设置\x01",
            "就拜托你们去完成了。\x02\x03",

            "需要到达的目的地是洛连特，卢安，\x01",
            "以及蔡斯的协会。\x02\x03",

            "各位路上务必小心哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_E75")

    label("loc_E29")


    ChrTalk(    #19
        0x8,
        (
            "#632F『零力场发生器』的设置\x01",
            "就拜托你们去完成了。\x02\x03",

            "各位路上务必小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E75")

    Jump("loc_150E")

    label("loc_E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1003")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_EF0")

    ChrTalk(    #20
        0x8,
        (
            "#632F来委托工作的女人除了我们以外\x01",
            "已经没有别人可依靠了。\x02\x03",

            "我想这工作大概不轻松，\x01",
            "尽量想办法找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1000")

    label("loc_EF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F59")

    ChrTalk(    #21
        0x8,
        (
            "#630F川蝉亭就在柏斯以南的\x01",
            "瓦雷利亚湖畔。\x02\x03",

            "从南街区出去，\x01",
            "沿着安塞尔新街一直往南走就到了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1000")

    label("loc_F59")


    ChrTalk(    #22
        0x8,
        (
            "#630F川蝉亭就在柏斯以南的\x01",
            "瓦雷利亚湖畔。\x02\x03",

            "从南街区出去，\x01",
            "沿着安塞尔新街一直往南走就到了。\x02\x03",

            "#631F住宿那边\x01",
            "我已经联系过了。\x02\x03",

            "暂时把烦恼忘记，\x01",
            "悠闲的养精蓄锐吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1000")

    Jump("loc_150E")

    label("loc_1003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_11CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1065")

    ChrTalk(    #23
        0x8,
        (
            "#630F迷雾峡谷的西北部\x01",
            "是个人迹罕至的危险地方。\x02\x03",

            "特别要注意\x01",
            "准备耐寒措施啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C9")

    label("loc_1065")


    ChrTalk(    #24
        0x8,
        (
            "#630F摩尔根将军来联络了。\x02\x03",

            "你们是要\x01",
            "去迷雾峡谷吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1002F嗯，我们已经习惯在\x01",
            "人数不多的情况下行动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x106,
        "#050F啊，这就是所谓的各尽其能吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#634F嗯，既然将军同意了，\x01",
            "那我也不好多说什么。\x02\x03",

            "#630F军队说了会提供帮助的。\x01",
            "尽管放手去干吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x106,
        "#051F噢，正是这么打算的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#1006F责任虽然重大，\x01",
            "但会全力以赴的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        "#631F嗯，等你们的好消息。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_11C9")

    Jump("loc_150E")

    label("loc_11CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_131A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1232")

    ChrTalk(    #31
        0x8,
        (
            "#630F和军队碰头的地点是\x01",
            "国际空港的第一飞船坪。\x02\x03",

            "等一切都准备好，\x01",
            "就可以出发了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1317")

    label("loc_1232")


    ChrTalk(    #32
        0x8,
        (
            "#630F和军队碰头的地点是\x01",
            "国际空港的第一飞船坪。\x02\x03",

            "时间还很充裕，\x01",
            "提前准备好不是更好吗。\x02\x03",

            "超市的商人好像在\x01",
            "酒店里临时营业，\x01",
            "一些琐碎的东西可以在那里买到。\x02\x03",

            "顺便提一下，目的地第一飞船坪在\x01",
            "空港上面的甲板处。\x02\x03",

            "希望不要弄错了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1317")

    Jump("loc_150E")

    label("loc_131A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1370")

    ChrTalk(    #33
        0x8,
        (
            "#632F沿着西柏斯街道走到一个岔口向北\x01",
            "就是拉文努村。\x02\x03",

            "总之赶紧去现场吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_150E")

    label("loc_1370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1386")
    Call(0, 14)
    Jump("loc_150E")

    label("loc_1386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_150E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_140A")

    ChrTalk(    #34
        0x8,
        (
            "#630F等把所有的魔兽都消灭了，\x01",
            "记得要回来这里报告啊。\x02\x03",

            "敌人各个都是十分难缠的魔兽。\x01",
            "出发前务必做好充足的准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_150E")

    label("loc_140A")


    ChrTalk(    #35
        0x8,
        (
            "#630F有三件事要\x01",
            "委托你们。\x02\x03",

            "首先是出没于古罗尼山顶的\x01",
            "『刀刃毒牙』。\x02\x03",

            "然后是出没于琥珀之塔的\x01",
            "『邪骨章鱼』。\x02\x03",

            "最后是出没于迷雾峡谷的\x01",
            "『幽灵碑文』。\x02\x03",

            "把所有的魔兽都消灭之后，\x01",
            "记得要回来这里报告啊。\x02\x03",

            "敌人各个都是十分难缠的魔兽。\x01",
            "出发前务必做好充足的准备。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_150E")

    Jump("loc_16F9")

    label("loc_1511")

    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_158C")
    OP_28(0xC3, 0x4, 0x20)
    OP_A9(0x36)

    ChrTalk(    #36
        0x8,
        (
            "#630F嗯。辛苦了。\x01",
            "看来任务是已经顺利完成了。\x02\x03",

            "完成了什么任务的话\x01",
            "再过来报告就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1644")

    label("loc_158C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x36)"), scpexpr(EXPR_END)), "loc_15EF")

    ChrTalk(    #37
        0x8,
        (
            "#630F嗯。辛苦了。\x01",
            "看来任务是已经顺利完成了。\x02\x03",

            "完成了什么任务的话\x01",
            "再过来报告就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1644")

    label("loc_15EF")


    ChrTalk(    #38
        0x8,
        (
            "#630F嗯。目前好像\x01",
            "没有可以报告的工作呢。\x02\x03",

            "完成了什么任务的话\x01",
            "再过来报告就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1644")

    OP_56(0x0)
    Jump("loc_16F9")

    label("loc_1649")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16F6")

    ChrTalk(    #39
        0x8,
        (
            "#630F嗯。\x01",
            "想要把同伴叫来是吧？\x02\x03",

            "明白了。\x01",
            "我马上就联络他们。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #40
        (
            "\x07\x05联络各支部，\x01",
            "集合了待命人员。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_16F6")

    Jump("loc_16F9")

    label("loc_16F9")

    TalkEnd(0x8)
    Return()

    # Function_4_5FB end

    def Function_5_16FD(): pass

    label("Function_5_16FD")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_178D")
    Jump("loc_17CF")

    label("loc_178D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_17A9")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17CF")

    label("loc_17A9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17C5")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17CF")

    label("loc_17C5")

    OP_51(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17CF")

    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(    #41
        0xB,
        "#020F嗯，怎么了？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
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
        (0, "loc_1864"),
        (SWITCH_DEFAULT, "loc_189D"),
    )


    label("loc_1864")


    ChrTalk(    #42
        0xB,
        "#020F哎呀，要调整队伍吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1896")
    Call(0, 12)
    Jump("loc_189A")

    label("loc_1896")

    Call(0, 11)

    label("loc_189A")

    Jump("loc_18DE")

    label("loc_189D")


    ChrTalk(    #43
        0xB,
        (
            "#020F呵呵，我就在这儿\x01",
            "休息吧。\x02\x03",

            "那么，之后就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18DE")

    label("loc_18DE")

    SetChrSubChip(0xB, 0)
    TalkEnd(0xB)
    Return()

    # Function_5_16FD end

    def Function_6_18E7(): pass

    label("Function_6_18E7")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1977")
    Jump("loc_19B9")

    label("loc_1977")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1993")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19B9")

    label("loc_1993")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19AF")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19B9")

    label("loc_19AF")

    OP_51(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19B9")

    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(    #44
        0xC,
        (
            "#030F呀，诸位。\x01",
            "贵安。\x02\x03",

            "看来好像有什么事……\x01",
            "不过先来一曲怎样？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
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
        (0, "loc_1A7C"),
        (SWITCH_DEFAULT, "loc_1AD0"),
    )


    label("loc_1A7C")


    ChrTalk(    #45
        0xC,
        (
            "#030F呵，原来如此。\x02\x03",

            "看来是需要\x01",
            "我这个天才的力量啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AC9")
    Call(0, 12)
    Jump("loc_1ACD")

    label("loc_1AC9")

    Call(0, 11)

    label("loc_1ACD")

    Jump("loc_1B20")

    label("loc_1AD0")


    ChrTalk(    #46
        0xC,
        (
            "#033F呀，不要我了吗？\x02\x03",

            "#035F嗯，爱上我那动听的声音的话\x01",
            "就尽管来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B20")

    label("loc_1B20")

    SetChrSubChip(0xC, 0)
    TalkEnd(0xC)
    Return()

    # Function_6_18E7 end

    def Function_7_1B29(): pass

    label("Function_7_1B29")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BB9")
    Jump("loc_1BFB")

    label("loc_1BB9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1BD5")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BFB")

    label("loc_1BD5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BF1")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BFB")

    label("loc_1BF1")

    OP_51(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BFB")

    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)

    ChrTalk(    #47
        0xD,
        (
            "#040F各位，辛苦了。\x02\x03",

            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
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
        (0, "loc_1CA0"),
        (SWITCH_DEFAULT, "loc_1CDC"),
    )


    label("loc_1CA0")


    ChrTalk(    #48
        0xD,
        (
            "#040F明白了。\x01",
            "要调整队伍吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CD5")
    Call(0, 12)
    Jump("loc_1CD9")

    label("loc_1CD5")

    Call(0, 11)

    label("loc_1CD9")

    Jump("loc_1D11")

    label("loc_1CDC")


    ChrTalk(    #49
        0xD,
        (
            "#040F那我在这里待命。\x02\x03",

            "如果有事\x01",
            "请尽管开口。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D11")

    label("loc_1D11")

    SetChrSubChip(0xD, 0)
    TalkEnd(0xD)
    Return()

    # Function_7_1B29 end

    def Function_8_1D1A(): pass

    label("Function_8_1D1A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D2C")
    TalkBegin(0xF)
    Jump("loc_1E23")

    label("loc_1D2C")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    OP_51(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DBC")
    Jump("loc_1DFE")

    label("loc_1DBC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1DD8")
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DFE")

    label("loc_1DD8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DF4")
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DFE")

    label("loc_1DF4")

    OP_51(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DFE")

    OP_51(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    label("loc_1E23")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E61")

    ChrTalk(    #50
        0xF,
        (
            "#560F啊，阿加特哥哥。\x02\x03",

            "那个，有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED4")

    label("loc_1E61")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1EA1")

    ChrTalk(    #51
        0xF,
        (
            "#060F啊，姐姐，是你们啊。\x01",
            "怎么了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED4")

    label("loc_1EA1")


    ChrTalk(    #52
        0xF,
        (
            "#060F啊，姐姐，是你们啊。\x02\x03",

            "那个，有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED4")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
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
        (0, "loc_1F2D"),
        (SWITCH_DEFAULT, "loc_1FAF"),
    )


    label("loc_1F2D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F6F")

    ChrTalk(    #53
        0xF,
        (
            "#060F啊，嗯，明白了。\x01",
            "要调整队伍吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F95")

    label("loc_1F6F")


    ChrTalk(    #54
        0xF,
        (
            "#560F啊，明白了。\x01",
            "要调整队伍吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F95")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FA8")
    Call(0, 12)
    Jump("loc_1FAC")

    label("loc_1FA8")

    Call(0, 11)

    label("loc_1FAC")

    Jump("loc_205E")

    label("loc_1FAF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2012")

    ChrTalk(    #55
        0xF,
        (
            "#064F咦，又不要了吗……？\x02\x03",

            "#060F那我就在这里等，\x01",
            "有什么事就来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_205B")

    label("loc_2012")


    ChrTalk(    #56
        0xF,
        (
            "#064F咦，又不要了吗……？\x02\x03",

            "#060F那我就在这里等，\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_205B")

    Jump("loc_205E")

    label("loc_205E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2070")
    TalkEnd(0xF)
    Jump("loc_2078")

    label("loc_2070")

    SetChrSubChip(0xF, 0)
    TalkEnd(0xF)

    label("loc_2078")

    Return()

    # Function_8_1D1A end

    def Function_9_2079(): pass

    label("Function_9_2079")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x10)
    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x10, 0x0, 0)
    OP_51(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2109")
    Jump("loc_214B")

    label("loc_2109")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2125")
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_214B")

    label("loc_2125")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2141")
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_214B")

    label("loc_2141")

    OP_51(0x10, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_214B")

    OP_51(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x10)

    ChrTalk(    #57
        0x10,
        "#070F噢，情况怎么样？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
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
        (0, "loc_21E4"),
        (SWITCH_DEFAULT, "loc_2217"),
    )


    label("loc_21E4")


    ChrTalk(    #58
        0x10,
        "#070F要调整队伍吧？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2210")
    Call(0, 12)
    Jump("loc_2214")

    label("loc_2210")

    Call(0, 11)

    label("loc_2214")

    Jump("loc_2260")

    label("loc_2217")


    ChrTalk(    #59
        0x10,
        (
            "#070F什么，不做调整了吗。\x02\x03",

            "那我在这里等着。\x01",
            "需要的时候就说一声。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2260")

    label("loc_2260")

    SetChrSubChip(0x10, 0)
    TalkEnd(0x10)
    Return()

    # Function_9_2079 end

    def Function_10_2269(): pass

    label("Function_10_2269")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22F9")
    Jump("loc_233B")

    label("loc_22F9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2315")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_233B")

    label("loc_2315")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2331")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_233B")

    label("loc_2331")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_233B")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(    #60
        0xE,
        "#051F喔，怎么了？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
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
        (0, "loc_23D0"),
        (SWITCH_DEFAULT, "loc_23FD"),
    )


    label("loc_23D0")


    ChrTalk(    #61
        0xE,
        (
            "#051F噢，知道了。\x01",
            "要调整队伍吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_2441")

    label("loc_23FD")


    ChrTalk(    #62
        0xE,
        (
            "#052F怎么，不调整了吗？\x02\x03",

            "#050F那需要我的重剑时\x01",
            "尽管开口吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2441")

    label("loc_2441")

    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Return()

    # Function_10_2269 end

    def Function_11_244A(): pass

    label("Function_11_244A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2469")
    OP_C9(0x1, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    Jump("loc_24A6")

    label("loc_2469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2488")
    OP_C9(0x1, 0x4, 0x0, 0x6, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    Jump("loc_24A6")

    label("loc_2488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_24A6")
    OP_C9(0x1, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)

    label("loc_24A6")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_24FA")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 9)
    SetChrPos(0xB, 26770, 200, -3440, 270)

    label("loc_24FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2527")
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 10)
    SetChrPos(0xC, 28510, 200, -3980, 90)

    label("loc_2527")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2554")
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x4)
    SetChrChipByIndex(0xD, 11)
    SetChrPos(0xD, 24150, 200, -3440, 90)

    label("loc_2554")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2581")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x4)
    SetChrChipByIndex(0xF, 12)
    SetChrPos(0xF, 25420, 200, -2270, 180)

    label("loc_2581")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25AE")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 13)
    SetChrPos(0x10, 30780, 200, -3130, 270)

    label("loc_25AE")

    OP_0D()
    Return()

    # Function_11_244A end

    def Function_12_25B0(): pass

    label("Function_12_25B0")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_A3(0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_264D")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 9)
    SetChrPos(0xB, 24140, 200, -3410, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2632")
    OP_41(0x2, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x2)

    label("loc_2632")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_264D")
    OP_41(0x2, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x2)

    label("loc_264D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_26B0")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 16)
    SetChrPos(0xE, 26770, 200, -3440, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2695")
    OP_41(0x5, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x2)

    label("loc_2695")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26B0")
    OP_41(0x5, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x2)

    label("loc_26B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2710")
    ClearChrFlags(0xF, 0x80)
    OP_43(0xF, 0x0, 0x0, 0x2)
    SetChrPos(0xF, 34230, 0, -1860, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26F5")
    OP_41(0x6, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x2)

    label("loc_26F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2710")
    OP_41(0x6, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x2)

    label("loc_2710")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2773")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 13)
    SetChrPos(0x10, 25420, 200, -2270, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2758")
    OP_41(0x7, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x2)

    label("loc_2758")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2773")
    OP_41(0x7, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x2)

    label("loc_2773")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_27F0")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #63
        (
            "\x07\x05※要待命的成员\x01",
            "　装备着『零力场发生器』。\x01",
            "　将其回收加入队伍的携带品。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_27F0")

    Return()

    # Function_12_25B0 end

    def Function_13_27F1(): pass

    label("Function_13_27F1")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2804")
    Call(0, 28)

    label("loc_2804")

    OP_6D(590, 0, 3270, 0)
    OP_67(0, 5580, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -460, 0, 2350, 0)
    SetChrPos(0xE, 610, 0, 2350, 0)
    SetChrPos(0xF, -430, 0, 1300, 0)
    SetChrPos(0xD, -1300, 0, 1150, 0)
    SetChrPos(0xB, 820, 0, 1410, 0)
    SetChrPos(0xC, -1020, 0, 200, 0)
    SetChrPos(0x10, 400, 0, 300, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_4A(0x8, 255)
    SetChrChipByIndex(0xB, 3)
    SetChrChipByIndex(0xC, 4)
    SetChrChipByIndex(0xD, 5)
    SetChrChipByIndex(0xF, 7)
    SetChrChipByIndex(0x10, 8)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #64
        0x8,
        (
            "#631F呀～从洛连特特意赶来，\x01",
            "真的辛苦你们了啊。\x02\x03",

            "#633F而且……\x01",
            "除了『不动』，『银闪』，『重剑』之外，\x01",
            "还有前途无量的游击士新人。\x02\x03",

            "哈哈，怎么说也是相当豪华的阵容啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#1004F前途无量的游击士新人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#631F哈哈，说的就是你啊。\x02\x03",

            "连续破坏『结社』在四个地方所布设的阴谋，\x01",
            "突然出现的游击士新星。\x02\x03",

            "像这样的赞美之言，时常可以听到的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#1019F真，真是的，开玩笑！\x02\x03",

            "#1007F破坏阴谋什么的，\x01",
            "其实我还没有到达那么厉害的程度。\x02\x03",

            "况且那些家伙每次做完实验之后，\x01",
            "都被他们轻松地逃掉……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 315, 400)
    Sleep(500)

    ChrTalk(    #68
        0xB,
        (
            "#021F#2P不过，对于洛连特事件的处理，\x01",
            "你不是干的很出色吗。\x02\x03",

            "#027F我觉得挺值得自豪呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #69
        0x101,
        (
            "#1013F#5P那，那是……\x01",
            "其实应该是连串的巧合……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10,
        (
            "#071F哈哈，害羞了。\x02\x03",

            "关键是只要能够做出\x01",
            "符合别人评价的工作就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#1007F#5P真是的，不要说的那么简单。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #72
        0x101,
        (
            "#1002F先不说这些了……\x01",
            "柏斯的情况怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C2E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2C2E)
    Sleep(10)
    OP_8C(0x10, 0, 400)

    ChrTalk(    #73
        0x8,
        (
            "#630F嗯，到目前还没发生\x01",
            "被认为是与『结社』有关的事件。\x02\x03",

            "自从发生了那起抢夺空贼艇事件之后，\x01",
            "军队的警戒变得严密了。\x02\x03",

            "#634F至于怪事的话……\x01",
            "也就是通缉魔兽的数量在增加之类的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xE,
        "#555F#4P呼……是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1015F总感觉柏斯这里的通缉魔兽\x01",
            "比其他地方要多呢。\x02\x03",

            "以前来的时候也是这样，\x01",
            "难道有什么特别的原因吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "#634F柏斯地区原本就很广阔，\x01",
            "四面都是险要地形。\x02\x03",

            "那些地方经常会有凶暴的魔兽跳出来……\x01",
            "所以魔兽数量多也不奇怪。\x02\x03",

            "#632F话说回来，\x01",
            "本月以来已经收到了十起报告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xB,
        (
            "#023F这可真多啊……\x02\x03",

            "#020F斯丁克最近表现不错吧，\x01",
            "我听说很努力地工作来着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        (
            "#630F嗯，此外克鲁茨他们\x01",
            "前些日子来的时候顺便去\x01",
            "消灭了几只魔兽。\x02\x03",

            "但是又有几只出现了，要是可以的话，\x01",
            "我们柏斯支部也希望你们能够帮下忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10,
        (
            "#074F嗯……\x01",
            "帮帮忙比较好。\x02\x03",

            "#072F凶暴魔兽的数量在继续增加……\x01",
            "这或许与『结社』有关联也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#1006F嗯嗯，置之不理的话会很危险的，\x01",
            "现在还是把剿灭的任务摆在优先的位置吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xE,
        "#552F#4P……………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 400)

    ChrTalk(    #82
        0xF,
        (
            "#064F#6P？？？\x02\x03",

            "阿加特哥哥。\x01",
            "出什么事了？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3008():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3008)
    Sleep(50)

    def lambda_301B():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_301B)
    Sleep(50)

    def lambda_302E():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_302E)
    Sleep(50)

    def lambda_3041():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3041)
    Sleep(50)
    TurnDirection(0x10, 0xE, 400)

    ChrTalk(    #83
        0x101,
        "#1004F啊，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xE,
        "#053F#4P不……没什么。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 400)
    Sleep(500)

    ChrTalk(    #85
        0xE,
        (
            "#051F#5P总之，现在的工作就是\x01",
            "先把已经知道的通缉魔兽全部剿灭。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)
    SetChrPos(0x9, -4500, 0, -9720, 0)
    SetChrPos(0x9, -930, 0, -7000, 0)

    NpcTalk(    #86
        0x9,
        "女性的声音",
        "#5P……失礼了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x10, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrPos(0x9, -500, 0, -7000, 0)
    SetChrPos(0xA, -500, 0, -7000, 0)
    ClearChrFlags(0x9, 0x80)

    def lambda_3209():
        OP_6D(800, 0, 800, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3209)

    def lambda_3221():
        OP_8E(0xFE, 0xFFFFFE16, 0x0, 0xFFFFF93E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3221)

    def lambda_323C():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_323C)

    def lambda_324A():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_324A)

    def lambda_3258():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3258)

    def lambda_3266():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3266)

    def lambda_3274():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3274)

    def lambda_3282():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3282)

    def lambda_3290():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3290)
    Sleep(500)
    ClearChrFlags(0xA, 0x80)

    def lambda_32A8():
        OP_8E(0xFE, 0x14A, 0x0, 0xFFFFF6A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_32A8)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #87
        0x101,
        (
            "#1018F#5P梅贝尔市长……\x01",
            "还有莉拉小姐！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x9,
        (
            "#611F#6P呵呵，你好。\x02\x03",

            "艾丝蒂尔。\x01",
            "终于又见面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        "#621F……好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1008F#5P哇～真是好久不见了。\x02\x03",

            "好像是从诞辰庆典以后就没见过了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        (
            "#611F#6P是啊，是这样。\x02\x03",

            "但在很多地方都能听到\x01",
            "关于艾丝蒂尔的传闻呢。\x02\x03",

            "#610F其余的各位也好久不见了。\x02\x03",

            "科洛丝……\x01",
            "学校已经放假了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xD,
        (
            "#045F#5P不是呢，\x01",
            "其实是不久前刚刚休学。\x02\x03",

            "#048F看来梅贝尔前辈和莉拉小姐最近都过得很不错，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#1004F#5P梅贝尔……前辈？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 90, 400)

    ChrTalk(    #94
        0xD,
        (
            "#542F#6P啊，她是我的前辈啊。\x01",
            "王立学院的高材生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x9,
        (
            "#611F#6P呵呵，这里又不是公众场合，\x01",
            "炫耀炫耀也无所谓。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1016F#5P啊哈哈，是这样啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 180, 400)

    ChrTalk(    #97
        0x9,
        (
            "#610F#6P还有……\x01",
            "阿加特·科洛斯纳。\x02\x03",

            "好久不见呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xE,
        "#552F#5P……是吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #99
        0x101,
        (
            "#1004F#6P咦，市长\x01",
            "认识阿加特？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x9,
        (
            "#610F#6P曾数次委托于他，\x01",
            "受了他不少照顾。\x02\x03",

            "此外１０年前……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xE,
        "#555F#5P喂喂……我说小姐。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #102
        0x9,
        (
            "#615F#6P抱歉……失礼了。\x02\x03",

            "#610F今天我听说\x01",
            "大家都在，\x01",
            "特意过来打声招呼。\x02\x03",

            "听说你在四处追捕\x01",
            "在王国全范围内引起骚乱的国际犯罪组织，\x01",
            "对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#1015F#5P国，国际犯罪组织……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xB,
        (
            "#022F#5P虽然稍微有点出入，\x01",
            "但这么说也没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x9,
        (
            "#612F#6P我们柏斯市的立场是无论如何\x01",
            "也不允许有这样的犯罪组织存在。\x02\x03",

            "所以，请让我们\x01",
            "尽可能地参与协助你们的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#1006F#5P嗯，到那时候就\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xE,
        (
            "#051F#5P哼……\x01",
            "不过，我倒是期待你的表现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x9,
        (
            "#615F#6P那么，我们\x01",
            "就先告辞了。\x02\x03",

            "#611F若是有什么事的话，\x01",
            "请来市长官邸找我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xA,
        "#620F……告辞。（鞠躬）\x02",
    )

    CloseMessageWindow()

    def lambda_3845():
        OP_6D(10, 0, -1540, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3845)
    OP_8C(0x9, 180, 400)

    def lambda_3864():
        OP_8E(0xFE, 0xFFFFFDF8, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3864)
    Sleep(800)
    OP_8C(0xA, 270, 400)
    OP_8C(0xA, 180, 400)

    def lambda_3892():
        OP_8E(0xFE, 0xFFFFFDF8, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3892)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x4)

    def lambda_38B7():
        OP_8E(0xFE, 0xFFFFFDA8, 0x0, 0xFFFFE3EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_38B7)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x80)
    WaitChrThread(0xA, 0x1)
    SetChrFlags(0xA, 0x4)

    def lambda_38F1():
        OP_8E(0xFE, 0xFFFFFDA8, 0x0, 0xFFFFE3EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_38F1)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0xA, 0x80)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    def lambda_392B():
        OP_6D(590, 0, 3270, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_392B)
    Sleep(1000)

    def lambda_3948():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3948)
    Sleep(50)

    def lambda_395B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_395B)
    Sleep(100)

    def lambda_396E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_396E)
    Sleep(50)

    def lambda_3981():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3981)
    Sleep(100)

    def lambda_3994():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3994)
    Sleep(50)

    def lambda_39A7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_39A7)
    Sleep(100)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #110
        0x8,
        (
            "#634F哎呀，阿加特。\x02\x03",

            "#632F我说你啊，\x01",
            "就不能稍微热情点吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xE,
        (
            "#552F#4P抱歉，本性如此。\x02\x03",

            "况且我是个从事国民安全的游击士。\x01",
            "在这一点上就别计较那么多吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(    #112
        0x101,
        (
            "#1015F#6P嗯，的确是啊……\x01",
            "不管对谁，阿加特总是给人一种很傲慢的态度。\x02\x03",

            "尽管这样，但我觉得\x01",
            "阿加特那种专业的工作态度反而让人感到敬畏呢。\x02\x03",

            "话说回来，刚才看市长姐姐望着阿加特的神情，\x01",
            "感觉到他们之间好像有点隔阂。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 400)

    ChrTalk(    #113
        0xF,
        "#063F#6P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xE,
        (
            "#053F#4P啊？是错觉吧。\x02\x03",

            "#050F别琢磨这些了，\x01",
            "我们还是快点剿灭通缉的魔兽吧。\x02\x03",

            "老爷子，一口气告诉我们吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #115
        0x8,
        (
            "#630F嗯……\x01",
            "目前需要剿灭的通缉魔兽有三个。\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x240099, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    OP_8C(0xF, 0, 0)
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("卢格兰老人")

    AnonymousTalk(    #116
        (
            "\x07\x00#634F首先是出没于古罗尼山顶的\x01",
            "『刀刃毒牙』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x24009B, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("卢格兰老人")

    AnonymousTalk(    #117
        (
            "\x07\x00#632F然后是出没于迷雾峡谷的\x01",
            "『幽灵碑文』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x24009A, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("卢格兰老人")

    AnonymousTalk(    #118
        (
            "\x07\x00#634F最后是出没于琥珀之塔的\x01",
            "『邪骨章鱼』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #119
        0x101,
        (
            "#1006F嗯……\x01",
            "已经仔细记下来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xE, 225, 400)
    Sleep(500)

    ChrTalk(    #120
        0xE,
        (
            "#050F#5P好。说到剿灭魔兽，\x01",
            "就是轮到我的『重剑』出场的时候吧。\x02\x03",

            "这次就让我来处理吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3DF9():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DF9)
    Sleep(100)

    def lambda_3E0C():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3E0C)
    Sleep(50)

    def lambda_3E1F():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3E1F)
    Sleep(50)

    def lambda_3E32():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3E32)
    Sleep(100)
    TurnDirection(0x10, 0xE, 400)

    ChrTalk(    #121
        0x101,
        "#1004F#6P啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xB,
        (
            "#027F柏斯地区\x01",
            "就是你的故乡呢。\x02\x03",

            "这次的任务交给你再适合不过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x10,
        "#070F啊，我也没意见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xE,
        "#053F#5P呵，就这么定了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 270, 400)
    Sleep(500)

    ChrTalk(    #125
        0xE,
        (
            "#051F#2P那么，艾丝蒂尔。\x01",
            "赶紧来挑选队员吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        "#1019F#6P呼，看来真的要强行入队呢。\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrName("")

    AnonymousTalk(    #127
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择２名固定成员以外的同行者。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_28(0xB1, 0x4, 0x2)
    OP_28(0xB1, 0x4, 0x4)
    OP_28(0xB1, 0x4, 0x8)
    OP_28(0xB2, 0x4, 0x2)
    OP_28(0xB2, 0x4, 0x4)
    OP_28(0xB2, 0x4, 0x8)
    OP_28(0xB3, 0x4, 0x2)
    OP_28(0xB3, 0x4, 0x4)
    OP_28(0xB3, 0x4, 0x8)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1101   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_13_27F1 end

    def Function_14_4054(): pass

    label("Function_14_4054")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4075")
    Call(0, 29)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_4075")

    Fade(1000)
    OP_6D(310, 0, 3460, 0)
    OP_67(0, 7010, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -710, 0, 2340, 0)
    SetChrPos(0x106, 470, 0, 2350, 0)
    SetChrPos(0xF8, -680, 0, 1160, 0)
    SetChrPos(0xF9, 440, 0, 1140, 0)
    OP_4A(0x8, 255)
    OP_0D()

    ChrTalk(    #128
        0x101,
        "#1018F我回来了，卢格兰爷爷。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x106,
        "#051F#4P通缉魔兽全部消灭了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x8,
        (
            "#631F#5P噢，辛苦了。\x02\x03",

            "#630F那么先把\x01",
            "这次的报酬付给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x93, 0x4, 0x10)
    OP_AF(0x36, 0x93)
    OP_28(0xB1, 0x4, 0x10)
    OP_28(0xB2, 0x4, 0x10)
    OP_28(0xB3, 0x4, 0x10)
    OP_28(0xB1, 0x4, 0x20)
    OP_28(0xB2, 0x4, 0x20)
    OP_28(0xB3, 0x4, 0x20)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #131
        0x8,
        (
            "#630F#5P嗯嗯，\x01",
            "看来确实是把凶猛的魔兽都剿灭了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1007F嗯～～关于魔兽……\x02\x03",

            "#1002F有一件事让我稍微有点在意呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x8,
        "#633F#5P啊？在意的事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x106,
        "#552F#4P啊，其实是──\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x1A12)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_4054 end

    def Function_15_4285(): pass

    label("Function_15_4285")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_42BE")
    AddParty(0x2, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_42BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_430B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42F3")
    AddParty(0x6, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_430B")

    label("loc_42F3")

    AddParty(0x6, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_430B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4380")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4340")
    AddParty(0x3, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4380")

    label("loc_4340")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4368")
    AddParty(0x3, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4380")

    label("loc_4368")

    AddParty(0x3, 0xFC, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_4380")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43CD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43B5")
    AddParty(0x4, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_43CD")

    label("loc_43B5")

    AddParty(0x4, 0xFC, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_43CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43F2")
    AddParty(0x7, 0xFC, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_43F2")

    Return()

    # Function_15_4285 end

    def Function_16_43F3(): pass

    label("Function_16_43F3")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_440B")
    Call(0, 29)
    Sleep(100)

    label("loc_440B")

    OP_6D(310, 0, 3460, 0)
    OP_67(0, 7010, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -710, 0, 2340, 0)
    SetChrPos(0x106, 470, 0, 2350, 0)
    SetChrPos(0xF8, -680, 0, 1160, 0)
    SetChrPos(0xF9, 440, 0, 1140, 0)
    OP_4A(0x8, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #135
        0x8,
        (
            "#632F#5P嗯，魔兽有时会恐慌，\x01",
            "有时又变得更加凶暴吗……\x02\x03",

            "确实是件很奇怪的事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        "#1002F嗯，挺让人害怕的呢。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(400)

    ChrTalk(    #137
        0x101,
        (
            "#1015F对了，阿加特。\x02\x03",

            "你好像说过之前在柏斯地区\x01",
            "也发生过类似的事吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        "#633F#5P喔，有吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x106,
        (
            "#053F#4P啊……算是吧。\x02\x03",

            "#050F那是老爷子来柏斯之前的事了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #140
        0x101,
        (
            "#1004F咦～卢格兰爷爷\x01",
            "以前不住在这里的……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x8,
        (
            "#630F#5P嗯，我是在百日战役结束之后\x01",
            "才来柏斯任职的。\x02\x03",

            "#634F过去利贝尔只在格兰赛尔有\x01",
            "游击士协会……\x02\x03",

            "各地建立起支部那是\x01",
            "战争结束以后的事了。\x02\x03",

            "#630F顺便说一下，直到１０年以前，\x01",
            "我一直都在王都支部担任接待的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        "#1006F咦～是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x106,
        (
            "#552F#4P……在那场『百日战役』即将爆发的时候。\x02\x03",

            "魔兽的样子变得\x01",
            "越来越古怪……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 500)

    ChrTalk(    #144
        0x101,
        "#1004F啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x8,
        "#632F#5P什么……！？\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_20(0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x88, 0x0, 0x64)
    OP_7C(0x0, 0x190, 0x1388, 0x5DC)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47FD")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_483B")

    label("loc_47FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4824")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_483B")

    label("loc_4824")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_483B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4867")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_48A5")

    label("loc_4867")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_488E")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_48A5")

    label("loc_488E")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_48A5")

    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #146
        0x8,
        "#633F#5P什，什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        "#1020F刚，刚才那震动是什么！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 180, 600)
    Sleep(300)

    ChrTalk(    #148
        0x106,
        "#054F#5P外面……快去看看！\x02",
    )

    CloseMessageWindow()
    NewScene("ED6_DT21/T1103   ._SN", 110, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_16_43F3 end

    def Function_17_494A(): pass

    label("Function_17_494A")

    OP_7C(0x32, 0x32, 0x5DC, 0x1F4)
    Sleep(500)
    OP_7C(0x64, 0x64, 0x3E8, 0x1F4)
    Sleep(500)
    OP_7C(0xC8, 0xC8, 0x3E8, 0x1F4)
    Sleep(500)
    OP_7C(0x64, 0x64, 0x1F4, 0x1F4)
    Sleep(500)
    OP_7C(0x32, 0x32, 0xFA, 0x1F4)
    Sleep(500)
    OP_7C(0xA, 0xA, 0x7D, 0x1F4)
    Sleep(500)
    Return()

    # Function_17_494A end

    def Function_18_49CF(): pass

    label("Function_18_49CF")

    OP_22(0x85, 0x1, 0x64)
    Sleep(2000)
    OP_24(0x85, 0x5F)
    Sleep(100)
    OP_24(0x85, 0x5A)
    Sleep(100)
    OP_24(0x85, 0x55)
    Sleep(100)
    OP_24(0x85, 0x50)
    Sleep(100)
    OP_24(0x85, 0x4B)
    Sleep(100)
    OP_24(0x85, 0x46)
    Sleep(100)
    OP_24(0x85, 0x41)
    Sleep(100)
    OP_24(0x85, 0x32)
    Sleep(100)
    OP_24(0x85, 0x37)
    Sleep(100)
    OP_24(0x85, 0x32)
    OP_23(0x85)
    Return()

    # Function_18_49CF end

    def Function_19_4A32(): pass

    label("Function_19_4A32")

    OP_8E(0xFE, 0x6D6, 0x0, 0x5B4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFFD8A, 0x0, 0xFFFFE674, 0x1388, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_19_4A32 end

    def Function_20_4A6B(): pass

    label("Function_20_4A6B")

    OP_8E(0xFE, 0xFFFFF81C, 0x0, 0x5AA, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFFD8A, 0x0, 0xFFFFE674, 0x1388, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_4A6B end

    def Function_21_4AA4(): pass

    label("Function_21_4AA4")

    OP_8E(0xFE, 0xFFFFFD8A, 0x0, 0xFFFFE674, 0x1388, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_21_4AA4 end

    def Function_22_4AC9(): pass

    label("Function_22_4AC9")

    OP_8E(0xFE, 0xFFFFFD8A, 0x0, 0xFFFFE674, 0x1388, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_22_4AC9 end

    def Function_23_4AEE(): pass

    label("Function_23_4AEE")

    EventBegin(0x0)
    OP_6D(160, 0, 3130, 0)
    OP_67(0, 7040, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -600, 0, 2340, 0)
    SetChrPos(0xB, 720, 0, 2340, 0)
    SetChrPos(0xD, -220, 0, 1580, 0)
    SetChrPos(0xF, -1290, 0, 890, 0)
    SetChrPos(0xC, -20, 0, 520, 0)
    SetChrPos(0x10, 1110, 0, 1360, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xB, 3)
    SetChrChipByIndex(0xC, 4)
    SetChrChipByIndex(0xD, 5)
    SetChrChipByIndex(0xF, 7)
    SetChrChipByIndex(0x10, 8)
    OP_4A(0x8, 255)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #149
        0x8,
        (
            "#634F#5P……总之\x01",
            "辛苦各位了。\x02\x03",

            "#632F驻扎在哈肯大门的王国军部队\x01",
            "很快就会赶来的。\x02\x03",

            "柏斯超市的管理和防护\x01",
            "就交给他们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        (
            "#1007F嗯、嗯……\x02\x03",

            "#1003F不过，\x01",
            "没想到敌人中竟然会有那种怪物……\x02\x03",

            "而且那个洛伦斯少尉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xB,
        (
            "#026F#4P执行者ＮＯ．Ⅱ。\x01",
            "『剑帝』莱恩哈特。\x02\x03",

            "#022F也被称为『莱维』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xC,
        (
            "#035F#4P哼……\x01",
            "看来真正的身份终于显露出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xD,
        (
            "#049F#6P在格兰赛尔城相遇的时候，\x01",
            "也没有料到他竟然会是个\x01",
            "做出这么过分的事的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x10,
        "#072F嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xF,
        (
            "#063F#6P那、那个，卢格兰爷爷……\x02\x03",

            "阿加特哥哥\x01",
            "还没有消息吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x8,
        (
            "#634F#5P嗯……很遗憾。\x02\x03",

            "#632F那个鲁莽的阿加特……\x01",
            "到底去搞些什么了啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 1880, 2000, 5270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC3, 0x1, 0x64)
    Sleep(1000)

    ChrTalk(    #157
        0xF,
        "#064F#6P啊……\x02",
    )


    def lambda_4E93():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4E93)
    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        "#1025F#6P难道说……！\x02",
    )

    CloseMessageWindow()

    def lambda_4EBD():

        label("loc_4EBD")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4EBD")

    QueueWorkItem2(0x101, 1, lambda_4EBD)

    def lambda_4ECE():

        label("loc_4ECE")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4ECE")

    QueueWorkItem2(0xD, 1, lambda_4ECE)

    def lambda_4EDF():

        label("loc_4EDF")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4EDF")

    QueueWorkItem2(0xB, 1, lambda_4EDF)

    def lambda_4EF0():

        label("loc_4EF0")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4EF0")

    QueueWorkItem2(0xC, 1, lambda_4EF0)

    def lambda_4F01():

        label("loc_4F01")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4F01")

    QueueWorkItem2(0xF, 1, lambda_4F01)

    def lambda_4F12():

        label("loc_4F12")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4F12")

    QueueWorkItem2(0x10, 1, lambda_4F12)

    def lambda_4F23():
        OP_6D(1160, 0, 4059, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F23)
    OP_8E(0x8, 0x794, 0x0, 0x1252, 0x5DC, 0x0)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x101, 0x2)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 1880, 2000, 5270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_44(0x101, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0x10, 0x1)

    ChrTalk(    #159
        0x8,
        (
            "#632F#6P这里是游击士协会\x01",
            "所属柏斯支部……\x02\x03",

            "#633F噢，是你啊。\x01",
            "到底怎么了……\x02\x03",

            "………………………………\x01",
            "………………………………\x02\x03",

            "#632F……什么！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        "#1026F#6P（怎，怎么回事……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xB,
        "#022F（这气氛……好像出什么大事了……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x8,
        (
            "#634F#6P嗯，明白了。\x01",
            "我这里马上派游击士过去。\x02\x03",

            "#632F嗯、嗯，请打起精神来。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(500)
    TurnDirection(0x8, 0x101, 500)
    Sleep(500)

    ChrTalk(    #163
        0x8,
        (
            "#632F#5P……刚才……拉文努村莱森村长\x01",
            "传达了一些信息。\x02\x03",

            "就在刚刚，\x01",
            "那条龙袭击了拉文努村。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        "#1002F#3S#6P！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xB,
        "#024F#4P什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x8,
        (
            "#634F#5P据说龙把果树园烧毁之后，\x01",
            "很快就离开了。\x02\x03",

            "#632F在那之后，阿加特出现并加入\x01",
            "到了灭火行动中，但是现在他…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        (
            "#1005F#6P知道了！\x01",
            "我们马上去看看吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)
    OP_62(0xF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #168
        0xF,
        (
            "#065F#6P姐，姐姐！\x01",
            "也带我去吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        "#1004F#6P啊……！？\x02",
    )

    CloseMessageWindow()

    def lambda_52A6():
        OP_6D(860, 0, 2860, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_52A6)

    def lambda_52BE():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_52BE)
    Sleep(50)

    def lambda_52D1():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_52D1)
    Sleep(50)

    def lambda_52E4():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_52E4)
    Sleep(50)

    def lambda_52F7():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_52F7)
    Sleep(50)
    TurnDirection(0xC, 0xF, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #170
        0xF,
        (
            "#062F#6P对手假如是在空中飞的龙的话，\x01",
            "我觉得导力炮能派上用场……\x02\x03",

            "再加上……再加上……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        (
            "#1025F#5P……嗯，知道了。\x02\x03",

            "不过……\x01",
            "切记不可以胡来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xF,
        "#560F#6P是！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrName("")

    AnonymousTalk(    #173
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择２名固定成员以外的同行者。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x6, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(200)
    OP_6D(-500, 0, -720, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -500, 0, -720, 180)
    SetChrPos(0x107, -500, 0, -720, 180)
    SetChrPos(0xF8, -500, 0, -720, 180)
    SetChrPos(0xF9, -500, 0, -720, 180)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x8, 180, 0, 4400, 180)
    OP_69(0x0, 0x0)
    OP_4B(0x8, 255)
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x1)
    OP_28(0x7A, 0x4, 0x40)
    OP_28(0x94, 0x4, 0x2)
    OP_28(0x94, 0x4, 0x8)
    OP_28(0x94, 0x1, 0x1)
    OP_28(0xB1, 0x4, 0x10)
    OP_28(0xB1, 0x4, 0x20)
    OP_28(0xB2, 0x4, 0x10)
    OP_28(0xB2, 0x4, 0x20)
    OP_28(0xB3, 0x4, 0x10)
    OP_28(0xB3, 0x4, 0x20)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_23_4AEE end

    def Function_24_5587(): pass

    label("Function_24_5587")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_559E")
    Call(0, 28)
    Call(0, 30)

    label("loc_559E")

    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0xF8, 0x80)
    OP_6D(40, 0, 3020, 0)
    OP_67(0, 7560, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -590, 0, 2340, 0)
    SetChrPos(0xB, 520, 0, 2350, 0)
    SetChrPos(0xD, -1690, 0, 1980, 0)
    SetChrPos(0xC, -980, 0, 1100, 0)
    SetChrPos(0x10, 250, 0, 1100, 0)
    SetChrChipByIndex(0xB, 3)
    SetChrChipByIndex(0xC, 4)
    SetChrChipByIndex(0xD, 5)
    SetChrChipByIndex(0x10, 8)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_4A(0x8, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #174
        0x101,
        (
            "#1017F是吗，\x01",
            "超市的修复工程已经开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xB,
        (
            "#021F#4P明明只过了短短几天，　\x01",
            "准备的可真周到呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x8,
        (
            "#631F嗯，\x01",
            "梅贝尔市长非常的努力啊。\x02\x03",

            "#630F发放给拉文努村的救援物资\x01",
            "也已经运送过去了。\x02\x03",

            "大家虽然心怀不安，\x01",
            "但都在很努力地工作。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 90, 400)
    Sleep(500)

    ChrTalk(    #177
        0xD,
        (
            "#047F#6P已经和王都取得了联系，\x01",
            "就在昨晚，\x01",
            "祖母大人她发表了声明。\x02\x03",

            "#040F声明内容包括迅速对龙采取的对策，\x01",
            "以及向被害地区提供援助的保证。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)

    def lambda_5803():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5803)

    def lambda_5811():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5811)

    def lambda_581F():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_581F)
    Sleep(500)

    ChrTalk(    #178
        0x101,
        "#1001F#5P是吗，不愧是女王陛下！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xC,
        (
            "#035F呵呵，\x01",
            "真希望帝国的大人物们也好好学习王国的处事手法。\x02\x03",

            "毕竟比起安抚民众，\x01",
            "政党的人发挥团体的精神才更为重要。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x10,
        (
            "#075F不过，要这么说的话，\x01",
            "共和国也是如此啊。\x02\x03",

            "相互太过在意权势，\x01",
            "使得工作中难以放开手脚啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xD,
        (
            "#045F#6P呵呵……过奖了，各位。\x01",
            "这或许是小国所特有的优势也说不定。\x02\x03",

            "#048F不管怎样……\x01",
            "我认为我们已经做好了\x01",
            "对付龙的准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        (
            "#1006F#5P那就让我们先\x01",
            "见识见识王国军的实力吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    def lambda_59E8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_59E8)

    def lambda_59F6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_59F6)

    def lambda_5A04():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5A04)

    def lambda_5A12():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5A12)

    ChrTalk(    #183
        0x101,
        (
            "#1015F那个，我们\x01",
            "只要去国际空港就好了是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x8,
        (
            "#631F嗯，没错。\x01",
            "上午10点，在第一飞船坪。\x02\x03",

            "现在是9点左右，\x01",
            "还有一点时间可以去买东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        "#1006F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xB,
        (
            "#023F#4P可是，\x01",
            "柏斯超市还没有恢复营业吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x8,
        (
            "#630F超市的商人\x01",
            "现在在酒店里避难。\x02\x03",

            "不过他们同时好像也在做买卖，\x01",
            "买东西去那里就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xB,
        "#021F#4P呵呵，原来这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x10,
        (
            "#070F在去空港之前，\x01",
            "去那里逛一下，准备一下随身物资也不错啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5BE9")
    AddParty(0x2, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_5BE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5C36")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C1E")
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_5C36")

    label("loc_5C1E")

    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_5C36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5C83")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C6B")
    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_5C83")

    label("loc_5C6B")

    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_5C83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5CA8")
    AddParty(0x7, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_5CA8")

    RemoveParty(0x4, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x7, 0xFF)
    AddParty(0x4, 0xF7, 0xFF)
    AddParty(0x2, 0xF8, 0xFF)
    AddParty(0x3, 0xF9, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_6D(20, 0, -430, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 20, 0, -430, 185)
    SetChrPos(0x1, 20, 0, -430, 185)
    SetChrPos(0x2, 20, 0, -430, 185)
    SetChrPos(0x3, 20, 0, -430, 185)
    SetChrPos(0x4, 20, 0, -430, 185)
    SetChrPos(0x5, 20, 0, -430, 185)
    OP_4B(0x8, 255)
    OP_A2(0x1A1C)
    OP_28(0x95, 0x4, 0x2)
    OP_28(0x95, 0x4, 0x8)
    OP_28(0x95, 0x1, 0x1)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_24_5587 end

    def Function_25_5DA8(): pass

    label("Function_25_5DA8")

    EventBegin(0x0)
    OP_D6(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DBD")
    Call(0, 28)

    label("loc_5DBD")

    OP_4A(0x8, 255)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x0, 510, 0, 1930, 270)
    SetChrPos(0xE, 1260, 0, 2020, 270)
    SetChrPos(0xF, 1140, 0, 1100, 270)
    SetChrPos(0x10, -1350, 0, 2000, 90)
    SetChrPos(0xB, -1080, 0, 940, 90)
    SetChrPos(0x11, 140, 0, 2350, 90)
    SetChrPos(0xD, 80, 0, 1350, 90)
    SetChrPos(0xC, -380, 0, 230, 45)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_6D(110, 0, -2000, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(45000, 0)
    OP_6E(287, 0)

    def lambda_5EB4():
        OP_6D(790, 0, 2790, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5EB4)

    def lambda_5ECC():
        OP_67(0, 6000, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5ECC)
    FadeToBright(1500, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #190
        0x11,
        (
            "#1007F是吗……\x01",
            "有这种事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xB,
        (
            "#022F『剑帝』莱维……\x01",
            "的确是个有胆量的男人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xE,
        (
            "#053F啊，真是的。\x02\x03",

            "#555F就因为这样，\x01",
            "眼睁睁地看着敌人逃走……\x02\x03",

            "抱歉，我没有什么可以为自己辩解的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x8,
        (
            "#634F不，那种场合，\x01",
            "让他走才是正确的选择吧。\x02\x03",

            "至少……\x01",
            "不能在墓地引发骚乱啊。\x02\x03",

            "#632F话说回来……\x01",
            "这个叫『哈梅尔』的名字似乎非同一般，\x01",
            "总觉得让人很在意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x11,
        (
            "#1003F这名字……\x01",
            "之前在女王宫和洛伦斯少尉战斗的时候，\x01",
            "他好像也提到过。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)
    Sleep(300)

    ChrTalk(    #195
        0x11,
        "#1015F#5P科洛丝，你知道些什么吗？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 0, 400)

    def lambda_60D6():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_60D6)
    Sleep(50)

    def lambda_60E9():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_60E9)

    ChrTalk(    #196
        0xD,
        (
            "#043F#4P很遗憾……不知道。\x02\x03",

            "#049F我想祖母大人她大概会\x01",
            "知道点什么吧……\x02\x03",

            "但是，如果问起关于国家之间的问题的话，\x01",
            "或许她什么也不会告诉我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x11,
        (
            "#1007F#5P是吗……\x02\x03",

            "#1015F奥利维尔你呢？\x01",
            "那是埃雷波尼亚帝国的村庄吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xC,
        (
            "#035F嗯……『哈梅尔』啊。\x02\x03",

            "#030F又出现了一个\x01",
            "奇妙的名字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x11,
        "#1004F#5P奇妙？\x02",
    )

    CloseMessageWindow()

    def lambda_6224():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6224)
    Sleep(50)

    def lambda_6237():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6237)
    Sleep(50)

    def lambda_624A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_624A)

    def lambda_6258():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6258)
    Sleep(50)

    def lambda_626B():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_626B)
    Sleep(400)

    ChrTalk(    #200
        0xC,
        (
            "#032F那个哈梅尔\x01",
            "是位于帝国最南端的一座村庄的名字……\x02\x03",

            "但是现在这名字\x01",
            "并没有记载在帝国的地图上。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #201
        0x11,
        "#1020F#5P啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xF,
        (
            "#064F#5P没有记载……\x01",
            "为什么没有记载呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xC,
        (
            "#035F据说在几年前那里发生了山崩，\x01",
            "死了很多人。\x02\x03",

            "现在似乎是一座废弃的村庄。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xF,
        "#063F#5P废弃的村庄……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xE,
        "#552F#5P……原来是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x11,
        (
            "#1020F#5P可，可是，\x01",
            "据说是死了很多人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xC,
        (
            "#032F因为是出动了军队前去救灾，\x01",
            "民众并不清楚详细的情况……\x02\x03",

            "但有一种说法认为，\x01",
            "全村的人几乎都死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x11,
        "#1026F#5P全、全都死了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x10,
        (
            "#074F#5P确实如此，据说是\x01",
            "爆发了一场很严重的山崩，\x01",
            "把整个村子都吞没了。\x02\x03",

            "#072F好像是叫做『山体滑坡』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xB,
        (
            "#025F#5P原来如此，很奇妙的说法。\x02\x03",

            "#522F不过，这为什么\x01",
            "会和利贝尔女王殿下以及将军\x01",
            "有关呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xC,
        (
            "#035F这个嘛……\x01",
            "目前一点头绪也没有呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x8,
        (
            "#634F嗯……\x01",
            "不如就由我出面向帝国的协会\x01",
            "询问一下这些事吧。\x02\x03",

            "#630F好了，关于『哈梅尔』的\x01",
            "话题就先聊到这里……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6667():
        OP_6D(870, 0, 3840, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6667)

    def lambda_667F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_667F)

    def lambda_668D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_668D)
    Sleep(50)

    def lambda_66A0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_66A0)

    def lambda_66AE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_66AE)

    def lambda_66BC():
        OP_8C(0xFE, 5, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_66BC)
    Sleep(50)

    def lambda_66CF():
        OP_8C(0xFE, 5, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_66CF)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #213
        0x8,
        (
            "#630F先把这次的报酬\x01",
            "付给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x94, 0x4, 0x10)
    OP_AF(0x36, 0x94)
    Sleep(100)
    OP_28(0x95, 0x4, 0x10)
    OP_AF(0x36, 0x95)
    Sleep(100)
    OP_28(0x96, 0x4, 0x10)
    OP_28(0x96, 0x4, 0x20)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #214
        0x8,
        (
            "#631F#5P这次龙引起的骚乱，\x01",
            "真的辛苦各位了。\x02\x03",

            "真是充分体现了游击士协会\x01",
            "的本色呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x11,
        "#1008F#6P嘿嘿……是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xE,
        (
            "#552F#4P但是，\x01",
            "『实验』本身还是未能彻底阻止……\x02\x03",

            "所以我们还不能放松。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xB,
        (
            "#022F#6P而且，直到目前为止，\x01",
            "包括王都在内已经有５个地方\x01",
            "进行过『实验』了。\x02\x03",

            "必须立即调查清楚\x01",
            "下一步『结社』会采取怎么的行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x8,
        (
            "#634F#5P怎么说呢……\x02\x03",

            "#630F你们几个，\x01",
            "稍微休息一下如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #219
        0x11,
        "#1004F#6P啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6985")

    ChrTalk(    #220
        0xE,
        (
            "#052F#4P休息？\x01",
            "怎么回事？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69A8")

    label("loc_6985")


    ChrTalk(    #221
        0xB,
        (
            "#023F#6P休息？\x01",
            "是怎么一回事？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69A8")


    ChrTalk(    #222
        0x8,
        (
            "#630F#5P休息就是休息啊。\x02\x03",

            "以卢安地区为起点的连续５起事件，\x01",
            "已经让你们焦头烂额了吧。\x02\x03",

            "不在这时候休息一下的话，\x01",
            "会对身心造成负担哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x11,
        "#1026F#6P可、可是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6ABB")

    ChrTalk(    #224
        0xE,
        (
            "#555F#4P那些家伙若是再惹出些什么事来，\x01",
            "我们就需要出面去应对。\x02\x03",

            "实在是没什么时间\x01",
            "悠哉游哉的休息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B1D")

    label("loc_6ABB")


    ChrTalk(    #225
        0xB,
        (
            "#022F#6P那些人若是再引起事端的话，\x01",
            "就需要我们行动了。\x02\x03",

            "暂时……\x01",
            "我觉得我们没有休息的余地……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B1D")


    ChrTalk(    #226
        0x8,
        (
            "#634F#5P这次因为龙的事件，\x01",
            "王国军的警戒也变得严密了。\x02\x03",

            "因而，可以说\x01",
            "我们也轻松了很多。\x02\x03",

            "#632F再加上……\x01",
            "克鲁茨他们恐怕也有了点头绪。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #227
        0x11,
        "#1005F#6P#4S啊！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6CC1")

    ChrTalk(    #228
        0xB,
        (
            "#024F#6P有点头绪……\x01",
            "是指『噬身之蛇』的基地吗！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CF4")

    label("loc_6CC1")


    ChrTalk(    #229
        0xE,
        (
            "#054F#4P所谓头绪……\x01",
            "『噬身之蛇』的基地吗！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CF4")


    ChrTalk(    #230
        0x8,
        (
            "#634F#5P嗯，几天来\x01",
            "我们这里得到了确切的情报。\x02\x03",

            "#630F假如查清了那帮人的基地在哪里的话，\x01",
            "肯定会一下子忙碌起来的。\x02\x03",

            "所以在空闲的时候，\x01",
            "我希望你们能多多休息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x11,
        "#1015F#6P这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x10,
        (
            "#070F#6P嗯，既然是这样的话，\x01",
            "就应该恭敬不如从命才是。\x02\x03",

            "其实状态的调整也是\x01",
            "游击士的工作啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xB,
        "#027F#6P确实如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xE,
        (
            "#051F#4P这段时间\x01",
            "稍微休息一下也不错吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_21()
    OP_1D(0xB)
    Sleep(500)

    ChrTalk(    #235
        0xC,
        (
            "#031F呵呵，这不是\x01",
            "意见统一了吗。\x02\x03",

            "#030F但是老人家。\x02\x03",

            "其实你一直劝我们休息，\x01",
            "是不是因为有了什么好东西啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x8,
        (
            "#631F#5P呵呵，真敏锐。\x02\x03",

            "#630F其实，我刚刚从梅贝尔市长那里\x01",
            "得到了一样好东西。\x02\x03",

            "当然，这和龙事件所获的报酬是两回事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x11,
        "#1004F#6P市长姐姐送的……好东西？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x8,
        (
            "#631F#5P直截了当地告诉你吧，就是\x01",
            "位于南面湖畔『川蝉亭』的特別餐券。\x02\x03",

            "总之，\x01",
            "你们大家可以在那里免费住宿三天。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x11,
        "#1018F#6P真，真的！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #240
        "\x07\x00得到了\x1F\x19\x04\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x419, 1)
    Sleep(300)

    ChrTalk(    #241
        0xC,
        (
            "#031F呵呵……\x01",
            "不愧是威名远播的柏斯市长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xD,
        (
            "#048F呼呼……\x01",
            "不愧是前辈，她对我们真是既关心又体贴。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 270, 400)

    ChrTalk(    #243
        0xF,
        (
            "#560F#2P那个，这也就是说……\x02\x03",

            "大家可以一起到郊外游玩，\x01",
            "一起外出住宿吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_710D():
        OP_8C(0xB, 90, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_710D)
    Sleep(50)

    def lambda_7120():
        OP_8C(0xD, 90, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7120)
    Sleep(50)

    def lambda_7133():
        OP_8C(0x10, 90, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7133)
    Sleep(50)

    def lambda_7146():
        OP_8C(0xE, 225, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7146)
    Sleep(50)

    def lambda_7159():
        OP_8C(0x11, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7159)
    Sleep(300)

    ChrTalk(    #244
        0xB,
        (
            "#021F#6P呵呵，是啊。\x02\x03",

            "#027F而且是住在瓦雷利亚湖畔\x01",
            "那座景色宜人的旅馆呢。\x02\x03",

            "不仅酒和料理非常美味，\x01",
            "而且还可以乘坐小船游玩哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xF,
        "#061F#2P哇……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x10,
        (
            "#071F#6P嗯……\x01",
            "这可真不错啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xE,
        (
            "#051F#5P嗯，那里的确是个适合\x01",
            "释放心情的好地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x11,
        (
            "#1001F#5P嗯嗯！\x02\x03",

            "#1018F哟哟，既然要休息的话，\x01",
            "不如去尽情舒展一下筋骨吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(    #249
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "  请在固定成员以外挑选３名同行者。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    ClearMapFlags(0x1)
    OP_6D(9230, 0, 20140, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0xFF, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    OP_A2(0x1C01)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T1101   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_25_5DA8 end

    def Function_26_736D(): pass

    label("Function_26_736D")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_4A(0x8, 255)
    OP_4A(0xF, 255)
    SetChrPos(0x11, -490, 0, 2350, 0)
    SetChrPos(0x12, 520, 0, 2350, 0)
    SetChrPos(0xB, -1340, 0, 950, 0)
    SetChrPos(0xE, -400, 0, 860, 0)
    SetChrPos(0xF, 950, 0, 1650, 0)
    SetChrPos(0x10, 550, 0, 390, 0)
    SetChrChipByIndex(0xB, 3)
    SetChrChipByIndex(0xE, 6)
    SetChrChipByIndex(0xF, 7)
    SetChrChipByIndex(0x10, 8)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_6D(1110, 0, 3380, 0)
    OP_67(0, 6670, -10000, 0)
    OP_6B(2230, 0)
    OP_6C(45000, 0)
    OP_6E(328, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #250
        0x8,
        (
            "#634F唔唔……\x01",
            "竟然在四轮之塔发生这种事……\x02\x03",

            "#632F真是辛苦了。\x02\x03",

            "不管怎么样，\x01",
            "先付给你们报酬吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x9A, 0x4, 0x10)
    OP_AF(0x36, 0x9A)
    Sleep(100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #251
        0x8,
        (
            "#634F……但是，\x01",
            "事态变得一发不可收拾了啊。\x02\x03",

            "#632F没想到导力器无法使用\x01",
            "的事件竟然会在全国范围内\x01",
            "引起如此大的混乱……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x11,
        (
            "#1007F#6P嗯……\x02\x03",

            "#1003F平日大家受了导力器多少恩惠，\x01",
            "现在总算是知道了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x12,
        (
            "#1043F是啊……\x02\x03",

            "#1035F通信、交通、国防、生产线……\x01",
            "国家机能如同瘫痪了一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xB,
        (
            "#025F#6P对市民来说，\x01",
            "最担心的是照明和取暖吧。\x02\x03",

            "#022F对了，\x01",
            "昨天夜里…城里是不是非常混乱？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x8,
        (
            "#632F嗯……\x02\x03",

            "市民涌向了协会、工房、市长官邸，\x01",
            "场面别提多混乱了。\x02\x03",

            "可就算问我发生了什么事，\x01",
            "我也回答不出来啊。\x02\x03",

            "#634F所以啊，昨晚睡眠严重不足呢。唉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x11,
        "#1015F#6P是吗……辛苦爷爷你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xE,
        (
            "#555F浮游都市的事还没处理完，\x01",
            "状况就变得如此的糟糕了啊。\x02\x03",

            "难道说王国会陷入新一轮危机中吗……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x10,
        (
            "#074F但利贝尔的治安很好，\x01",
            "不用担心会发生暴动……\x02\x03",

            "#072F不过长期持续这种状态的话，\x01",
            "也不大好说会怎么样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x8,
        (
            "#634F嗯……\x01",
            "所以要尽早采取措施才行。\x02\x03",

            "#630F──那，你们几个。\x02\x03",

            "拉赛尔博士告诉你们的\x01",
            "起死回生的策略到底是什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x11,
        (
            "#1025F#6P呼呼呼……\x01",
            "没有起死回生那么夸张啦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x12,
        (
            "#1040F拉赛尔博士给我们提供了\x01",
            "最新发明的实验品。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/E0311   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_26_736D end

    def Function_27_78F5(): pass

    label("Function_27_78F5")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_4A(0x8, 255)
    OP_4A(0xF, 255)
    SetChrPos(0x11, -490, 0, 2350, 0)
    SetChrPos(0x12, 520, 0, 2350, 0)
    SetChrPos(0xB, -1340, 0, 950, 0)
    SetChrPos(0xE, -400, 0, 860, 0)
    SetChrPos(0xF, 950, 0, 1650, 0)
    SetChrPos(0x10, 550, 0, 390, 0)
    SetChrChipByIndex(0xB, 3)
    SetChrChipByIndex(0xE, 6)
    SetChrChipByIndex(0xF, 7)
    SetChrChipByIndex(0x10, 8)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_6D(1110, 0, 3380, 0)
    OP_67(0, 6670, -10000, 0)
    OP_6B(2230, 0)
    OP_6C(45000, 0)
    OP_6E(328, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #262
        0x8,
        (
            "#633F什么……\x01",
            "让通信器可以使用的装置吗！\x02\x03",

            "#631F这可是帮大忙啊！\x02\x03",

            "赶紧拿这个『零力场发生器』\x01",
            "来试试看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x11,
        "#1006F#6P好的。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, -180, 400)
    OP_8C(0x11, 90, 400)

    ChrTalk(    #264
        0x12,
        (
            "#1040F#5P提妲，\x01",
            "就全拜托你了可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xF,
        (
            "#061F嗯。\x01",
            "稍微等一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 90, 400)

    def lambda_7ADB():
        OP_6D(1020, 0, 3960, 2500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7ADB)

    def lambda_7AF3():

        label("loc_7AF3")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_7AF3")

    QueueWorkItem2(0x8, 1, lambda_7AF3)

    def lambda_7B04():

        label("loc_7B04")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_7B04")

    QueueWorkItem2(0x11, 1, lambda_7B04)

    def lambda_7B15():

        label("loc_7B15")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_7B15")

    QueueWorkItem2(0x12, 1, lambda_7B15)
    OP_8E(0xF, 0xF3C, 0x0, 0x758, 0xBB8, 0x0)
    OP_8E(0xF, 0xFFA, 0x0, 0x1374, 0xBB8, 0x0)
    OP_8E(0xF, 0x7B2, 0x0, 0x1252, 0xBB8, 0x0)

    def lambda_7B62():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7B62)

    def lambda_7B70():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7B70)

    def lambda_7B7E():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7B7E)
    OP_8C(0xF, 0, 400)
    Sleep(500)
    OP_44(0x8, 0x1)
    OP_44(0x11, 0x1)
    OP_44(0x12, 0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #266
        (
            "\x07\x05提妲打开了通信器的盖子，\x01",
            "把『零力场发生器』放进了里面。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #267
        0xF,
        "#062F#4P……………………………\x02",
    )

    CloseMessageWindow()
    OP_22(0xA, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xF, 225, 400)
    Sleep(500)

    ChrTalk(    #268
        0xF,
        (
            "#061F#5P……嗯。\x01",
            "这样就设定好了⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xE,
        "#052F是吗，可真快呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xF,
        (
            "#067F嘿嘿～～\x01",
            "只是把它固定在通信器中而已啦\x02\x03",

            "#560F那么……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 0, 400)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #271
        "\x07\x05提妲打开了通讯器的开关。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x83, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\mp001_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, 1880, 2000, 5270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #272
        0x8,
        "#633F#6P喔喔……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x11,
        "#1008F#6P成功了……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xB,
        (
            "#021F#6P呵呵，\x01",
            "看来导力器真的\x01",
            "能够不受『导力停止现象』的影响重新工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xF,
        (
            "#560F#4P那个，\x01",
            "接下来试试看信息能否确实\x01",
            "传送出去吧。\x02\x03",

            "我试着和留在埃尔赛尤\x01",
            "的爷爷进行联络。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #276
        "\x07\x05提妲拨起了通信器的拨号盘。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(500)
    OP_22(0xC3, 0x0, 0x46)
    Sleep(3000)
    OP_23(0xC3)
    Sleep(500)

    ChrTalk(    #277
        0xF,
        (
            "#064F#4P喂喂……\x02\x03",

            "#560F啊……爷爷！？\x02\x03",

            "#061F嗯！\x01",
            "我现在在柏斯的协会里。\x02\x03",

            "没事的。\x01",
            "发生装置的运作很正常。\x02\x03",

            "#560F……嗯……嗯。\x01",
            "爷爷也加油哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    Sleep(500)
    OP_8C(0xF, 225, 400)

    ChrTalk(    #278
        0xF,
        (
            "#061F#5P嘻嘻……\x01",
            "通信没问题，确实联系上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x11,
        "#1018F#6P成功了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x12,
        "#1040F#6P不愧是博士的新发明。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x8,
        (
            "#631F#6P哈哈哈。\x01",
            "应该怎么感谢博士才好呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7FFC():
        OP_6D(1110, 0, 3380, 1100)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7FFC)
    TurnDirection(0x8, 0x11, 400)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #282
        0x8,
        (
            "#633F#5P说起来，\x01",
            "拉赛尔博士好像留在埃尔赛尤了……\x02\x03",

            "那公主殿下和凯文神父去哪儿了？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8077():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8077)
    Sleep(50)

    def lambda_808A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_808A)
    Sleep(50)

    def lambda_809D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_809D)
    Sleep(50)

    def lambda_80B0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_80B0)
    Sleep(50)
    OP_8C(0x10, 0, 400)
    Sleep(200)

    ChrTalk(    #283
        0x11,
        (
            "#1006F#6P啊……\x01",
            "他们两个今早和亲卫队队员一起\x01",
            "前往王都了。\x02\x03",

            "两个人都有事情要做。\x01",
            "科洛丝想找女王殿下谈些事情，\x01",
            "凯文是想找大主教问些什么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x8,
        (
            "#634F#5P原来如此……\x02\x03",

            "#630F王室的找王室，教会的找教会，\x01",
            "正所谓各司其职啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x12,
        (
            "#1040F此外，\x01",
            "他们两个也接受了把『零力场发生器』\x01",
            "带去王都协会的任务。\x02\x03",

            "过一段时间，\x01",
            "我们这边也会收到他们的联络也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x8,
        (
            "#634F是吗……真是帮了大忙啊。\x02\x03",

            "#630F那么，\x01",
            "你们接下来要把剩下的三所协会\x01",
            "都走访一遍是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x11,
        (
            "#1006F#6P嗯，是这么打算的。\x02\x03",

            "#1003F……其实本来是想对那个浮游都市\x01",
            "采取点什么措施的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xB,
        (
            "#025F#6P是啊……\x02\x03",

            "况且『结社』的那帮人\x01",
            "好像已经进入浮游岛了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_832A():
        OP_8C(0x11, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_832A)
    Sleep(50)
    OP_8C(0x12, -180, 400)

    ChrTalk(    #289
        0xE,
        (
            "#552F但是，飞船无法使用的话，\x01",
            "想前往浮游都市基本是不可能的……\x02\x03",

            "#551F哼，真是进退两难的境地啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x12,
        "#1043F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x10,
        (
            "#074F也罢，干着急也无济于事。\x02\x03",

            "#070F现在，我们要做的，\x01",
            "就是把自己力所能及的事情处理完。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xE,
        "#051F#6P说的对……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xB,
        (
            "#020F#6P嗯……\x01",
            "加油吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_B7(0x4)
    OP_B7(0x8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(10350, 0, 17540, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84BB")
    Call(0, 28)

    label("loc_84BB")

    SetChrName("")

    AnonymousTalk(    #294
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择２名固定成员以外的同行者。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_31(0xFF, 0xFE, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T1101   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_27_78F5 end

    def Function_28_8556(): pass

    label("Function_28_8556")

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
        (0, "loc_85D0"),
        (1, "loc_85D6"),
        (SWITCH_DEFAULT, "loc_85DC"),
    )


    label("loc_85D0")

    OP_A2(0x1200)
    Jump("loc_85DC")

    label("loc_85D6")

    OP_A2(0x1201)
    Jump("loc_85DC")

    label("loc_85DC")

    Return()

    # Function_28_8556 end

    def Function_29_85DD(): pass

    label("Function_29_85DD")

    FadeToDark(0, 0, -1)
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
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
        (0, "loc_8694"),
        (1, "loc_869A"),
        (SWITCH_DEFAULT, "loc_86A0"),
    )


    label("loc_8694")

    OP_A2(0x1200)
    Jump("loc_86A0")

    label("loc_869A")

    OP_A2(0x1201)
    Jump("loc_86A0")

    label("loc_86A0")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_29_85DD end

    def Function_30_86DC(): pass

    label("Function_30_86DC")

    FadeToDark(0, 0, -1)
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x3, 0x0, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_30_86DC end

    SaveToFile()

Try(main)
