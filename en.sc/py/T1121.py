from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Lugran',                               # 9
        'Mayor Maybelle',                       # 10
        'Lila',                                 # 11
        'Scherazard',                           # 12
        'Olivier',                              # 13
        'Kloe',                                 # 14
        'Agate',                                # 15
        'Tita',                                 # 16
        'Zin',                                  # 17
        'Estelle',                              # 18
        'Joshua',                               # 19
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
        "Function_5_1DEE",         # 05, 5
        "Function_6_1FDE",         # 06, 6
        "Function_7_2282",         # 07, 7
        "Function_8_24AB",         # 08, 8
        "Function_9_280C",         # 09, 9
        "Function_10_2A11",        # 0A, 10
        "Function_11_2C1A",        # 0B, 11
        "Function_12_2D80",        # 0C, 12
        "Function_13_2FEB",        # 0D, 13
        "Function_14_4E7B",        # 0E, 14
        "Function_15_5110",        # 0F, 15
        "Function_16_527E",        # 10, 16
        "Function_17_58E9",        # 11, 17
        "Function_18_596E",        # 12, 18
        "Function_19_59D1",        # 13, 19
        "Function_20_5A0A",        # 14, 20
        "Function_21_5A43",        # 15, 21
        "Function_22_5A68",        # 16, 22
        "Function_23_5A8D",        # 17, 23
        "Function_24_666E",        # 18, 24
        "Function_25_7111",        # 19, 25
        "Function_26_9075",        # 1A, 26
        "Function_27_988E",        # 1B, 27
        "Function_28_A766",        # 1C, 28
        "Function_29_A7EC",        # 1D, 29
        "Function_30_A8EA",        # 1E, 30
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_650")

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",             # 0
            "Report\x01",           # 1
            "Call Allies\x01",      # 2
            "Leave\x01",            # 3
        )
    )

    Jump("loc_66B")

    label("loc_650")


    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",        # 0
            "Report\x01",      # 1
            "Leave\x01",       # 2
        )
    )


    label("loc_66B")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_698"),
        (1, "loc_1B5C"),
        (2, "loc_1D01"),
        (SWITCH_DEFAULT, "loc_1DEA"),
    )


    label("loc_698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_B74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_72D")

    ChrTalk(    #0
        0x8,
        (
            "#632FHow did he manage to sneak in...?\x02\x03",

            "I'm gettin' on in years, but he's a\x01",
            "tricky one if he managed to pull a\x01",
            "fast one on me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B71")

    label("loc_72D")


    ChrTalk(    #1
        0x8,
        (
            "#630FHm? What is it?\x02\x03",

            "Sounded like there was a commotion\x01",
            "of some sort upstairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#1007FYou c-could say that, yeah...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "\x07\x05Estelle nervously explained that Bleublanc had managed to\x01",
            "sneak into the third floor of the guildhouse.\x02",
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
            "#633FI don't believe what I'm hearing!\x02\x03",

            "#632FAn intruder, breaking into MY guild?\x02\x03",

            "I may be gettin' on in years, but I never\x01",
            "thought my senses so dull that I'd miss\x01",
            "out on a break-in. What an embarrassment...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B5")

    ChrTalk(    #5
        0x106,
        (
            "#055FGeez, chill out.\x02\x03",

            "Your blood pressure's gonna go\x01",
            "through the roof if you keep that\x01",
            "up, old timer.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x106, 400)
    Jump("loc_A23")

    label("loc_9B5")


    ChrTalk(    #6
        0x101,
        (
            "#1016FAww, c'mon, Lugran!\x02\x03",

            "You don't need to be so hard\x01",
            "on yourself. Really, these things\x01",
            "happen!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    label("loc_A23")


    ChrTalk(    #7
        0x8,
        (
            "#632FNo, this is a matter of pride now.\x01",
            "The guild's reputation is at stake!\x02\x03",

            "What will the citizens think if we\x01",
            "can't even stop one fool from breaking\x01",
            "into one of our own branches?\x02\x03",

            "Listen up! You going to catch him and\x01",
            "drag him back here, even if you have to\x01",
            "look behind every stalk of grass!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1002FHeh! Will do!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_8C(0x8, 180, 0)

    label("loc_B71")

    Jump("loc_1B59")

    label("loc_B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_100E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D71")

    ChrTalk(    #9
        0x8,
        (
            "#630FWelcome back!\x01",
            "Good work with the generators.\x02\x03",

            "There was a call from Grancel.\x01",
            "Did you head over there already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#1002FWe'll be heading out that way\x01",
            "right after this, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        (
            "#1042FIt all sounded fairly secretive,\x01",
            "so we don't know any details yet,\x01",
            "unfortunately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#634FMmm, I see. Could explain why\x01",
            "Elnan didn't want to say anything\x01",
            "over the phone.\x02\x03",

            "#632FCould also mean that he plans\x01",
            "to have you kids walk through fire,\x01",
            "so be prepared for anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_DCC")

    label("loc_D71")


    ChrTalk(    #13
        0x8,
        (
            "#632FThat business in Grancel must be\x01",
            "something important.\x02\x03",

            "Be prepared for anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DCC")

    Jump("loc_100B")

    label("loc_DCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E78")

    ChrTalk(    #14
        0x8,
        (
            "#630FHey, kids. I've already heard from\x01",
            "Aina and Jean.\x02\x03",

            "You're doing a fine job distributing\x01",
            "those generators.\x02\x03",

            "All that's left now is Zeiss.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FBB")

    label("loc_E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F1A")

    ChrTalk(    #15
        0x8,
        (
            "#630FHey, kids. I've already heard from\x01",
            "Aina and Kilika.\x02\x03",

            "You're doing a fine job distributing\x01",
            "those generators.\x02\x03",

            "All that's left now is Ruan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FBB")

    label("loc_F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FBB")

    ChrTalk(    #16
        0x8,
        (
            "#630FHey, kids. I've already heard from\x01",
            "Jean and Kilika.\x02\x03",

            "You're doing a fine job distributing\x01",
            "those generators.\x02\x03",

            "All that's left now is Rolent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FBB")

    OP_A2(0x0)
    Jump("loc_100B")

    label("loc_FC1")


    ChrTalk(    #17
        0x8,
        (
            "#630FOnly one more branch left for\x01",
            "this job.\x02\x03",

            "Keep up the good work!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100B")

    Jump("loc_1B59")

    label("loc_100E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_110D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B5")

    ChrTalk(    #18
        0x8,
        (
            "#632FI'll leave distributing Russell's\x01",
            "generators to you.\x02\x03",

            "Remember, one each to the Rolent,\x01",
            "Ruan, and Zeiss branches.\x02\x03",

            "Be careful, you lot.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_110A")

    label("loc_10B5")


    ChrTalk(    #19
        0x8,
        (
            "#632FI'll leave distributing Russell's\x01",
            "generators to you.\x02\x03",

            "Be careful, ya hear?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_110A")

    Jump("loc_1B59")

    label("loc_110D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1355")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_119D")

    ChrTalk(    #20
        0x8,
        (
            "#632FWe're that poor woman's last resort.\x02\x03",

            "It's going to be a challenge, I suspect,\x01",
            "but do whatever it takes to solve it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1352")

    label("loc_119D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1238")

    ChrTalk(    #21
        0x8,
        (
            "#630FThe Kingfisher Inn is to the south\x01",
            "of Bose along the Valleria Lake.\x02\x03",

            "Just head out via the south gate\x01",
            "and go along the New Ansel Path.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1352")

    label("loc_1238")


    ChrTalk(    #22
        0x8,
        (
            "#630FThe Kingfisher Inn is to the south\x01",
            "of Bose along the Valleria Lake.\x02\x03",

            "Just head out via the south gate\x01",
            "and go along the New Ansel Path.\x02\x03",

            "#631FI've already called ahead for you,\x01",
            "so they know to expect you.\x02\x03",

            "Try to clear your heads and take\x01",
            "a load off while you're there.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1352")

    Jump("loc_1B59")

    label("loc_1355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_15FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1428")

    ChrTalk(    #23
        0x8,
        (
            "#630FMost sane folk wouldn't dare set\x01",
            "foot into the northwestern part of\x01",
            "Nebel Valley. Too dangerous.\x02\x03",

            "Lay out a plan to deal with the cliffs\x01",
            "and the cold climate before you go,\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15FC")

    label("loc_1428")


    ChrTalk(    #24
        0x8,
        (
            "#630FI got word from General Morgan.\x02\x03",

            "You're heading for Nebel Valley,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1002FYeah. We're used to working in\x01",
            "small groups.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x106,
        (
            "#050FWe're the best people for the job,\x01",
            "really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#634FWell, if you have Morgan's permission,\x01",
            "I've no objections, either.\x02\x03",

            "#630FThe army's saying they'll keep things\x01",
            "secure. You kids do what you do best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x106,
        "#051FHeh, that's the plan!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#1006FNo need to tell me twice!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        "#631FLookin' forward to some good news!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_15FC")

    Jump("loc_1B59")

    label("loc_15FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1857")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16BE")

    ChrTalk(    #31
        0x8,
        (
            "#630FYou'll be meeting the army at the\x01",
            "landing port, specifically port No. 1.\x02\x03",

            "You still have some time, so stock up\x01",
            "on whatever you need before you make\x01",
            "your way over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1854")

    label("loc_16BE")


    ChrTalk(    #32
        0x8,
        (
            "#630FYou'll be meeting the army at the\x01",
            "landing port, specifically port No. 1.\x02\x03",

            "You still have some time, so stock up\x01",
            "on whatever you need before you make\x01",
            "your way over.\x02\x03",

            "Most of the market merchants have\x01",
            "set up shop in the hotel for the moment,\x01",
            "so you can get supplies there.\x02\x03",

            "Just so you know, port No. 1 is the one\x01",
            "on the upper deck of the landing port.\x02\x03",

            "Make sure you meet 'em at the right one!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1854")

    Jump("loc_1B59")

    label("loc_1857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1956")

    ChrTalk(    #33
        0x8,
        (
            "#632FI know you've been to Ravennue before,\x01",
            "but a refresher can't hurt. Head out the west\x01",
            "gate and follow the road west for a bit.\x02\x03",

            "As soon as you come to a fork in the road,\x01",
            "follow the northern path and you'll be there\x01",
            "before you know it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B59")

    label("loc_1956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_196C")
    Call(0, 14)
    Jump("loc_1B59")

    label("loc_196C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1B59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A02")

    ChrTalk(    #34
        0x8,
        (
            "#630FOnce you've slain all three monsters,\x01",
            "come back here and report.\x02\x03",

            "Those monsters mean business.\x01",
            "Make sure you're prepared.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B59")

    label("loc_1A02")


    ChrTalk(    #35
        0x8,
        (
            "#630FWe have three monster cases\x01",
            "outstanding:\x02\x03",

            "First, there's a Blade Fang stalking around the Krone Pass.\x02\x03",

            "We've also got a Ghost Epitaph in Nebel Valley...\x02\x03",

            "...and finally, we have an Octobone raising hell in Amberl Tower.\x02\x03",

            "Once you've slain all three, come\x01",
            "back and report.\x02\x03",

            "Those monsters mean business.\x01",
            "Make sure you're prepared.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1B59")

    Jump("loc_1DEA")

    label("loc_1B5C")

    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BF6")
    OP_28(0xC3, 0x4, 0x20)
    OP_A9(0x36)

    ChrTalk(    #36
        0x8,
        (
            "#630FGood work! Always nice to see\x01",
            "some progress.\x02\x03",

            "If you complete any more jobs,\x01",
            "be sure to come back and report.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CFC")

    label("loc_1BF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x36)"), scpexpr(EXPR_END)), "loc_1C78")

    ChrTalk(    #37
        0x8,
        (
            "#630FGood work! Always nice to see\x01",
            "some progress.\x02\x03",

            "If you complete any more jobs,\x01",
            "be sure to come back and report.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CFC")

    label("loc_1C78")


    ChrTalk(    #38
        0x8,
        (
            "#630FDon't think you've finished any\x01",
            "new jobs since your last report.\x02\x03",

            "Let me know when you've made\x01",
            "some headway in your work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CFC")

    OP_56(0x0)
    Jump("loc_1DEA")

    label("loc_1D01")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DE7")

    ChrTalk(    #39
        0x8,
        (
            "#630FNeed everyone here?\x02\x03",

            "All right, I'll put the call out right away.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #40
        (
            "\x07\x05Lugran contacted the other branches and had the rest of the\x01",
            "party assemble.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_1DE7")

    Jump("loc_1DEA")

    label("loc_1DEA")

    TalkEnd(0x8)
    Return()

    # Function_4_5FB end

    def Function_5_1DEE(): pass

    label("Function_5_1DEE")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E7E")
    Jump("loc_1EC0")

    label("loc_1E7E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1E9A")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1EC0")

    label("loc_1E9A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EB6")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1EC0")

    label("loc_1EB6")

    OP_51(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EC0")

    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(    #41
        0xB,
        "#020FHm? What is it?\x02",
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
            "Change Party\x01",      # 0
            "Leave\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F55"),
        (SWITCH_DEFAULT, "loc_1F89"),
    )


    label("loc_1F55")


    ChrTalk(    #42
        0xB,
        "#020FNeed some help?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F82")
    Call(0, 12)
    Jump("loc_1F86")

    label("loc_1F82")

    Call(0, 11)

    label("loc_1F86")

    Jump("loc_1FD5")

    label("loc_1F89")


    ChrTalk(    #43
        0xB,
        (
            "#020FI'll hang around here for a bit, then.\x02\x03",

            "Keep up the good work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FD5")

    label("loc_1FD5")

    SetChrSubChip(0xB, 0)
    TalkEnd(0xB)
    Return()

    # Function_5_1DEE end

    def Function_6_1FDE(): pass

    label("Function_6_1FDE")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_206E")
    Jump("loc_20B0")

    label("loc_206E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_208A")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20B0")

    label("loc_208A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_20A6")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20B0")

    label("loc_20A6")

    OP_51(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20B0")

    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(    #44
        0xC,
        (
            "#030FGood day.\x02\x03",

            "There is purpose etched upon your\x01",
            "lovely features...but first, perhaps a\x01",
            "song?\x02",
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
            "Change Party\x01",      # 0
            "Leave\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_218F"),
        (SWITCH_DEFAULT, "loc_2209"),
    )


    label("loc_218F")


    ChrTalk(    #45
        0xC,
        (
            "#030FAh, of course!\x02\x03",

            "You need the power of my genius.\x01",
            "Not to worry; I understand entirely.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2202")
    Call(0, 12)
    Jump("loc_2206")

    label("loc_2202")

    Call(0, 11)

    label("loc_2206")

    Jump("loc_2279")

    label("loc_2209")


    ChrTalk(    #46
        0xC,
        (
            "#033FOh? Changed your mind?\x02\x03",

            "#035FWell, should you ever long for my\x01",
            "dulcet tones, simply give the word.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2279")

    label("loc_2279")

    SetChrSubChip(0xC, 0)
    TalkEnd(0xC)
    Return()

    # Function_6_1FDE end

    def Function_7_2282(): pass

    label("Function_7_2282")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2312")
    Jump("loc_2354")

    label("loc_2312")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_232E")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2354")

    label("loc_232E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_234A")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2354")

    label("loc_234A")

    OP_51(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2354")

    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)

    ChrTalk(    #47
        0xD,
        (
            "#040FHi, guys.\x02\x03",

            "Did you need something?\x02",
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
            "Change Party\x01",      # 0
            "Leave\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23FC"),
        (SWITCH_DEFAULT, "loc_2440"),
    )


    label("loc_23FC")


    ChrTalk(    #48
        0xD,
        "#040FI'd be more than happy to help.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2439")
    Call(0, 12)
    Jump("loc_243D")

    label("loc_2439")

    Call(0, 11)

    label("loc_243D")

    Jump("loc_24A2")

    label("loc_2440")


    ChrTalk(    #49
        0xD,
        (
            "#040FI'll stay here for a bit, then.\x02\x03",

            "If you need me for anything,\x01",
            "don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A2")

    label("loc_24A2")

    SetChrSubChip(0xD, 0)
    TalkEnd(0xD)
    Return()

    # Function_7_2282 end

    def Function_8_24AB(): pass

    label("Function_8_24AB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24BD")
    TalkBegin(0xF)
    Jump("loc_25B4")

    label("loc_24BD")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    OP_51(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_254D")
    Jump("loc_258F")

    label("loc_254D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2569")
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_258F")

    label("loc_2569")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2585")
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_258F")

    label("loc_2585")

    OP_51(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_258F")

    OP_51(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    label("loc_25B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25F1")

    ChrTalk(    #50
        0xF,
        (
            "#560FOh, hi, Agate!\x02\x03",

            "Is everything okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2654")

    label("loc_25F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_262B")

    ChrTalk(    #51
        0xF,
        "#060FHi, Estelle! What's up?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2654")

    label("loc_262B")


    ChrTalk(    #52
        0xF,
        (
            "#060FHi, guys!\x02\x03",

            "Is everything okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2654")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Change Party\x01",      # 0
            "Leave\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_26AA"),
        (SWITCH_DEFAULT, "loc_2726"),
    )


    label("loc_26AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_26E7")

    ChrTalk(    #53
        0xF,
        "#060FYeah, I can come with you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_270C")

    label("loc_26E7")


    ChrTalk(    #54
        0xF,
        "#560FYeah, I can come with you.\x02",
    )

    CloseMessageWindow()

    label("loc_270C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271F")
    Call(0, 12)
    Jump("loc_2723")

    label("loc_271F")

    Call(0, 11)

    label("loc_2723")

    Jump("loc_27F1")

    label("loc_2726")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2796")

    ChrTalk(    #55
        0xF,
        (
            "#064FHuh? Are you sure?\x02\x03",

            "#060FWell, I'll be here. Just call for\x01",
            "me if you need me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27EE")

    label("loc_2796")


    ChrTalk(    #56
        0xF,
        (
            "#064FHuh? Are you sure?\x02\x03",

            "#060FWell, I'll be here. Just call for\x01",
            "me if you need me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27EE")

    Jump("loc_27F1")

    label("loc_27F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2803")
    TalkEnd(0xF)
    Jump("loc_280B")

    label("loc_2803")

    SetChrSubChip(0xF, 0)
    TalkEnd(0xF)

    label("loc_280B")

    Return()

    # Function_8_24AB end

    def Function_9_280C(): pass

    label("Function_9_280C")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x10)
    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x10, 0x0, 0)
    OP_51(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_289C")
    Jump("loc_28DE")

    label("loc_289C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_28B8")
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28DE")

    label("loc_28B8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_28D4")
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28DE")

    label("loc_28D4")

    OP_51(0x10, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28DE")

    OP_51(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x10)

    ChrTalk(    #57
        0x10,
        "#070FHey, how's it going?\x02",
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
            "Change Party\x01",      # 0
            "Leave\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2978"),
        (SWITCH_DEFAULT, "loc_29BE"),
    )


    label("loc_2978")


    ChrTalk(    #58
        0x10,
        "#070FNeed me to sub in, huh? I'm game!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29B7")
    Call(0, 12)
    Jump("loc_29BB")

    label("loc_29B7")

    Call(0, 11)

    label("loc_29BB")

    Jump("loc_2A08")

    label("loc_29BE")


    ChrTalk(    #59
        0x10,
        (
            "#070FChanged your mind? No worries.\x02\x03",

            "I'll be here if you need me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A08")

    label("loc_2A08")

    SetChrSubChip(0x10, 0)
    TalkEnd(0x10)
    Return()

    # Function_9_280C end

    def Function_10_2A11(): pass

    label("Function_10_2A11")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AA1")
    Jump("loc_2AE3")

    label("loc_2AA1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2ABD")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AE3")

    label("loc_2ABD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2AD9")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AE3")

    label("loc_2AD9")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2AE3")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(    #60
        0xE,
        "#051FYo, what's up?\x02",
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
            "Change Party\x01",      # 0
            "Leave\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2B77"),
        (SWITCH_DEFAULT, "loc_2B9E"),
    )


    label("loc_2B77")


    ChrTalk(    #61
        0xE,
        "#051FYeah, yeah, I got it.\x02",
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_2C11")

    label("loc_2B9E")


    ChrTalk(    #62
        0xE,
        (
            "#052FWhat, changed your mind?\x02\x03",

            "#050FWell, if you ever need somebody to\x01",
            "swing a sword around, gimme a call.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C11")

    label("loc_2C11")

    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Return()

    # Function_10_2A11 end

    def Function_11_2C1A(): pass

    label("Function_11_2C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2C39")
    OP_C9(0x1, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    Jump("loc_2C76")

    label("loc_2C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2C58")
    OP_C9(0x1, 0x4, 0x0, 0x6, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    Jump("loc_2C76")

    label("loc_2C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2C76")
    OP_C9(0x1, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)

    label("loc_2C76")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2CCA")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 9)
    SetChrPos(0xB, 26770, 200, -3440, 270)

    label("loc_2CCA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2CF7")
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 10)
    SetChrPos(0xC, 28510, 200, -3980, 90)

    label("loc_2CF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D24")
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x4)
    SetChrChipByIndex(0xD, 11)
    SetChrPos(0xD, 24150, 200, -3440, 90)

    label("loc_2D24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D51")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x4)
    SetChrChipByIndex(0xF, 12)
    SetChrPos(0xF, 25420, 200, -2270, 180)

    label("loc_2D51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D7E")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 13)
    SetChrPos(0x10, 30780, 200, -3130, 270)

    label("loc_2D7E")

    OP_0D()
    Return()

    # Function_11_2C1A end

    def Function_12_2D80(): pass

    label("Function_12_2D80")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_A3(0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E1D")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 9)
    SetChrPos(0xB, 24140, 200, -3410, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E02")
    OP_41(0x2, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x2)

    label("loc_2E02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E1D")
    OP_41(0x2, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x2)

    label("loc_2E1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E80")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 16)
    SetChrPos(0xE, 26770, 200, -3440, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E65")
    OP_41(0x5, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x2)

    label("loc_2E65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E80")
    OP_41(0x5, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x2)

    label("loc_2E80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2EE0")
    ClearChrFlags(0xF, 0x80)
    OP_43(0xF, 0x0, 0x0, 0x2)
    SetChrPos(0xF, 34230, 0, -1860, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EC5")
    OP_41(0x6, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x2)

    label("loc_2EC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EE0")
    OP_41(0x6, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x2)

    label("loc_2EE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F43")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 13)
    SetChrPos(0x10, 25420, 200, -2270, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F28")
    OP_41(0x7, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x2)

    label("loc_2F28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F43")
    OP_41(0x7, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x2)

    label("loc_2F43")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2FEA")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #63
        (
            "\x07\x05※A standby member was equipped with a Zero Field Generator.\x01",
            "It has been recovered and added to party inventory.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_2FEA")

    Return()

    # Function_12_2D80 end

    def Function_13_2FEB(): pass

    label("Function_13_2FEB")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FFE")
    Call(0, 28)

    label("loc_2FFE")

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
            "#631FEveryone, hello!\x01",
            "Good work out there in Rolent.\x02\x03",

            "#633FHah... The Silver Streak, the Heavy Blade,\x01",
            "the Immovable, and our rising star rookie\x01",
            "all together.\x02\x03",

            "Brings a tear to my eye, it does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#1004F#2PUm, 'rising star rookie'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#631FHahaha! You, of course!\x02\x03",

            "You're our little walking miracle who's\x01",
            "managed to stop the society in four\x01",
            "different regions!\x02\x03",

            "That's been the gossip, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#1019F#2PY-You've GOT to be kidding.\x02\x03",

            "#1007FSaying I 'stopped' anything is overstating\x01",
            "it more than a LITTLE.\x02\x03",

            "They just ran off once their experiments\x01",
            "were done...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 315, 400)
    Sleep(500)

    ChrTalk(    #68
        0xB,
        (
            "#021F#2PYou did handle yourself well in the Rolent\x01",
            "case, Estelle.\x02\x03",

            "#027FDon't sell yourself too short.\x01",
            "I think you can be a little bit proud.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #69
        0x101,
        (
            "#1013F#5PYeah, but that was just, um, a bunch of\x01",
            "coincidences coming together, and--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10,
        (
            "#071FHaha! No need to get so embarrassed.\x02\x03",

            "You just need to live up to your\x01",
            "reputation, is all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1007F#5PYeah, thanks, Zin.\x01",
            "You make that sound like a cakewalk.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #72
        0x101,
        (
            "#1002F#2PAnyway, all that aside... What's the\x01",
            "situation like here in Bose?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_353A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_353A)
    Sleep(10)
    OP_8C(0x10, 0, 400)

    ChrTalk(    #73
        0x8,
        (
            "#630FThere's been no sign of the society\x01",
            "whatsoever.\x02\x03",

            "No surprise, I suppose. Since the sky bandits\x01",
            "were caught, the army's been patrolling\x01",
            "the region pretty heavily.\x02\x03",

            "#634FOne thing sticks out, though. There've\x01",
            "been a few too many dangerous monsters\x01",
            "prowling around here these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xE,
        "#555F#4PReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1015F#2PY'know, I noticed that the last time\x01",
            "I was here.\x02\x03",

            "Bose seems to usually have more wanted\x01",
            "monsters than other regions. Why is that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "#634FMost of it comes down to Bose being huge\x01",
            "and filled with rough terrain.\x02\x03",

            "Makes it common to see monsters come\x01",
            "down from the less-inhabited areas.\x02\x03",

            "#632FThing is, though, we've had ten cases just\x01",
            "since the beginning of the month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xB,
        (
            "#023FTen? That IS a lot...\x02\x03",

            "#020FI'm guessing that's kept Sting and the\x01",
            "rest of the crew busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        (
            "#630FYes, and Kurt's team stopped by the other\x01",
            "day to slay several of them.\x02\x03",

            "Be in your debt if you could take care of\x01",
            "a few of 'em for us, as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10,
        (
            "#074FThat strikes me as a good course of action.\x02\x03",

            "#072FIt's possible the society is involved\x01",
            "with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#1006FYeah. And they could hurt someone if we just\x01",
            "leave them alone, so we should get out there\x01",
            "and take them down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xE,
        "#552F#4P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 400)

    ChrTalk(    #82
        0xF,
        (
            "#064F#5PHuuuh?\x02\x03",

            "Agate, what's wrong?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A30():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A30)
    Sleep(50)

    def lambda_3A43():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3A43)
    Sleep(50)

    def lambda_3A56():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3A56)
    Sleep(50)

    def lambda_3A69():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3A69)
    Sleep(50)
    TurnDirection(0x10, 0xE, 400)

    ChrTalk(    #83
        0x101,
        "#1004FYeah, what's up? You're really quiet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xE,
        "#053F#4PNah... It's nothin'.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 400)
    Sleep(500)

    ChrTalk(    #85
        0xE,
        (
            "#051F#6PAnyway, let's get out there and bring back\x01",
            "some monster heads.\x02",
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
        "Woman's Voice",
        "#5PPardon me!\x02",
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

    def lambda_3C5A():
        OP_6D(800, 0, 800, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C5A)

    def lambda_3C72():
        OP_8E(0xFE, 0xFFFFFE16, 0x0, 0xFFFFF93E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3C72)

    def lambda_3C8D():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C8D)

    def lambda_3C9B():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3C9B)

    def lambda_3CA9():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3CA9)

    def lambda_3CB7():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3CB7)

    def lambda_3CC5():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3CC5)

    def lambda_3CD3():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3CD3)

    def lambda_3CE1():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3CE1)
    Sleep(500)
    ClearChrFlags(0xA, 0x80)

    def lambda_3CF9():
        OP_8E(0xFE, 0x14A, 0x0, 0xFFFFF6A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3CF9)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #87
        0x101,
        "#1018F#6PMayor Maybelle! And Lila!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x9,
        (
            "#611F#2PHaha. Good day.\x02\x03",

            "Estelle, it's so good to see you again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        "#621F...I am glad to see you are well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1008F#6PWoooow, it's seriously been forever.\x02\x03",

            "I think we last met at the queen's\x01",
            "birthday celebrations, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        (
            "#611F#2PYes, it feels as though it's been ages.\x02\x03",

            "I've been hearing all about your exploits\x01",
            "in the news, though, Estelle.\x02\x03",

            "#610FThat goes for everyone else, as well.\x01",
            "I'm glad to see you all safe.\x02\x03",

            "Especially you, Kloe.\x01",
            "Are you on...'school break' already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xD,
        (
            "#045F#6PAh, I, um, ended up taking a little time\x01",
            "off early.\x02\x03",

            "#048FIt's good to see you again, Maybelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#1004F#6PHuh, you two seem, uh, pretty familiar.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 90, 400)

    ChrTalk(    #94
        0xD,
        (
            "#542F#6PWell, Maybelle used to be a student at the\x01",
            "academy. We met before she graduated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x9,
        "#611F#2PHeehee... And I'm certainly glad we met, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1016F#6PAh-haha, I see!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 180, 400)

    ChrTalk(    #97
        0x9,
        (
            "#610F#2PAnd...Agate Crosner.\x02\x03",

            "It has been some time, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xE,
        "#552F#6P...S'pose so.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #99
        0x101,
        "#1004F#6PHang on. Agate, Mayor Maybelle, YOU know each other?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x9,
        (
            "#610F#2POh, my, yes. I've relied on Mr. Crosner a number\x01",
            "of times for various jobs only he could do.\x02\x03",

            "And ten years ago--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xE,
        "#555F#6PHey...Mayor.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #102
        0x9,
        (
            "#615F#2P...I forgot myself. Pardon me.\x02\x03",

            "#610FRegardless. I simply wished to stop by\x01",
            "today to welcome you back.\x02\x03",

            "From the sound of things, you're pursuing\x01",
            "an international criminal syndicate which\x01",
            "threatens the safety of the entire country?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#1015F#6PAn 'international criminal syndicate'...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xB,
        (
            "#022F#6PSometimes they feel more like a society\x01",
            "of supervillains, but that's one way to\x01",
            "think of them, yes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x9,
        (
            "#612F#2PSo far as the City of Bose is concerned, the\x01",
            "threat these criminals pose is not someone\x01",
            "else's problem. It's everyone's.\x02\x03",

            "If I can do anything to assist you in your\x01",
            "investigation, anything at all, you only need\x01",
            "to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#1006F#6PThanks. If we need help,\x01",
            "we'll definitely ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xE,
        (
            "#051F#6PHeh... We'll be expecting a lot\x01",
            "from you, Mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x9,
        (
            "#615F#2PExcellent. Now, I'm afraid I must excuse\x01",
            "myself here.\x02\x03",

            "#611FShould anything come up, please come visit\x01",
            "me at my residence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xA,
        "#620FPardon us.\x02",
    )

    CloseMessageWindow()

    def lambda_457F():
        OP_6D(10, 0, -1540, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_457F)
    OP_8C(0x9, 180, 400)

    def lambda_459E():
        OP_8E(0xFE, 0xFFFFFDF8, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_459E)
    Sleep(800)
    OP_8C(0xA, 270, 400)
    OP_8C(0xA, 180, 400)

    def lambda_45CC():
        OP_8E(0xFE, 0xFFFFFDF8, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_45CC)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x4)

    def lambda_45F1():
        OP_8E(0xFE, 0xFFFFFDA8, 0x0, 0xFFFFE3EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_45F1)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x80)
    WaitChrThread(0xA, 0x1)
    SetChrFlags(0xA, 0x4)

    def lambda_462B():
        OP_8E(0xFE, 0xFFFFFDA8, 0x0, 0xFFFFE3EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_462B)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0xA, 0x80)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    def lambda_4665():
        OP_6D(590, 0, 3270, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4665)
    Sleep(1000)

    def lambda_4682():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4682)
    Sleep(50)

    def lambda_4695():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4695)
    Sleep(100)

    def lambda_46A8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_46A8)
    Sleep(50)

    def lambda_46BB():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_46BB)
    Sleep(100)

    def lambda_46CE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_46CE)
    Sleep(50)

    def lambda_46E1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_46E1)
    Sleep(100)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #110
        0x8,
        (
            "#634F*sigh* Come on, Agate.\x02\x03",

            "#632FCouldn't you have been a little more civil?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xE,
        (
            "#552F#4PIt's who I am.\x02\x03",

            "We ain't runnin' a butler service here.\x01",
            "Gimme a break.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(    #112
        0x101,
        (
            "#1015F#5PHmmm... Agate can be kind of arrogant to\x01",
            "people sometimes...\x02\x03",

            "He's usually polite towards clients,\x01",
            "though.\x02\x03",

            "You WERE kinda short with the mayor,\x01",
            "Agate.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 400)

    ChrTalk(    #113
        0xF,
        "#063F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xE,
        (
            "#053F#4PYou're imagining things.\x02\x03",

            "#050FMore to the point.\x01",
            "I remember talkin' about us bringin' back\x01",
            "some monster heads.\x02\x03",

            "Lugran, give us the breakdown.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #115
        0x8,
        "#630FRight... We have three cases outstanding.\x02",
    )

    CloseMessageWindow()
    OP_AD(0x240099, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_8C(0xF, 0, 0)
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Lugran")

    AnonymousTalk(    #116
        "\x07\x00#634FFirst, there's a Blade Fang stalking around in the Krone Pass.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x24009B, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Lugran")

    AnonymousTalk(    #117
        "\x07\x00#632FWe've also got a Ghost Epitaph in the Nebel Valley...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x24009A, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Lugran")

    AnonymousTalk(    #118
        "\x07\x00#634F...and finally, an Octobone raising hell at the Amberl Tower.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(0, 0)
    OP_0D()
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #119
        0x101,
        "#1006F#2POoooo...kay. Got those written down.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 225, 400)
    Sleep(500)

    ChrTalk(    #120
        0xE,
        (
            "#050F#6PAll right... Monster slaying's the perfect\x01",
            "task for my greatsword.\x02\x03",

            "I'll be takin' charge this time around.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4BA8():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BA8)
    Sleep(100)

    def lambda_4BBB():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4BBB)
    Sleep(50)

    def lambda_4BCE():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4BCE)
    Sleep(50)

    def lambda_4BE1():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4BE1)
    Sleep(100)
    TurnDirection(0x10, 0xE, 400)

    ChrTalk(    #121
        0x101,
        "#1004F#5PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xB,
        (
            "#027FWell, you are a Bose native,\x01",
            "my good Heavy Blade.\x02\x03",

            "You're probably the best-suited\x01",
            "out of all of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x10,
        "#070FI have no objections.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xE,
        "#053F#6PHeh. Decided, then.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 270, 400)
    Sleep(500)

    ChrTalk(    #125
        0xE,
        (
            "#051F#4PGo ahead and pick us a team,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#1019F#5PMrrrrgh. You're being suspiciously gung-ho\x01",
            "about this, you know.\x02",
        )
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
            "\x07\x05Please form your party.\x01",
            "You may choose two other members aside from the\x01",
            "mandatory members.\x07\x00\x02",
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

    # Function_13_2FEB end

    def Function_14_4E7B(): pass

    label("Function_14_4E7B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E9C")
    Call(0, 29)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_4E9C")

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
        "#1018F#2PLugraaan! We're back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x106,
        "#051F#4PThat's three more monsters for the trophy room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x8,
        (
            "#631F#6POho! Good work, kids!\x02\x03",

            "#630FHere, let me pay out for that before you report.\x02",
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
            "#630F#6PSounds like they were pretty violent,\x01",
            "but you kids seemed to handle them okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1007F#2PWell, about that.\x02\x03",

            "#1002FSomething's been bothering us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x8,
        "#633F#6PHm? What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x106,
        "#552F#4PIt's like this...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x1A12)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_4E7B end

    def Function_15_5110(): pass

    label("Function_15_5110")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5149")
    AddParty(0x2, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_5149")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5196")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_517E")
    AddParty(0x6, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_5196")

    label("loc_517E")

    AddParty(0x6, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_5196")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_520B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51CB")
    AddParty(0x3, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_520B")

    label("loc_51CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51F3")
    AddParty(0x3, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_520B")

    label("loc_51F3")

    AddParty(0x3, 0xFC, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_520B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5258")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5240")
    AddParty(0x4, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_5258")

    label("loc_5240")

    AddParty(0x4, 0xFC, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_5258")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_527D")
    AddParty(0x7, 0xFC, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_527D")

    Return()

    # Function_15_5110 end

    def Function_16_527E(): pass

    label("Function_16_527E")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5296")
    Call(0, 29)
    Sleep(100)

    label("loc_5296")

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
            "#632F#6PSo the monsters were acting in a way\x01",
            "that suggested they were disturbed by\x01",
            "something...\x02\x03",

            "Aye, that does bother me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        "#1002F#2PYeah, it seemed kinda creepy.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(400)

    ChrTalk(    #137
        0x101,
        (
            "#1015FOh, yeah, Agate.\x02\x03",

            "You said something like this happened here\x01",
            "in Bose before, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        "#633F#6PMmm? Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x106,
        (
            "#053F#4PYeah...sort of.\x02\x03",

            "#050FIt was before your time here, Lugran.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #140
        0x101,
        (
            "#1004F#2PHuh? Wait, Lugran, you haven't always\x01",
            "been here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x8,
        (
            "#630F#6PNo, no, I settled here after the Hundred\x01",
            "Days War.\x02\x03",

            "#634FBefore the war, there was just the one\x01",
            "guildhouse in Grancel, you see.\x02\x03",

            "The other branches were set up after we\x01",
            "kicked the Erebonians back across the\x01",
            "Krone.\x02\x03",

            "#630FBack then, I was the receptionist and\x01",
            "coordinator over at the Grancel house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1006F#2POh, right, I think Dad mentioned\x01",
            "something like this once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x106,
        (
            "#552F#4PIt was right before that damn war.\x02\x03",

            "That's when the monsters were acting\x01",
            "so strangely.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 500)

    ChrTalk(    #144
        0x101,
        "#1004FHuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x8,
        "#632F#6PWait, d'you mean to--\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5795")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_57D3")

    label("loc_5795")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57BC")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_57D3")

    label("loc_57BC")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_57D3")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57FF")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_583D")

    label("loc_57FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5826")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_583D")

    label("loc_5826")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_583D")

    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #146
        0x8,
        "#633F#6PWHAT IN AIDIOS' NAME?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        "#1020FWh-Wh-What was THAT?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 180, 600)
    Sleep(300)

    ChrTalk(    #148
        0x106,
        "#054F#6POutside...Come on!\x02",
    )

    CloseMessageWindow()
    NewScene("ED6_DT21/T1103   ._SN", 110, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_16_527E end

    def Function_17_58E9(): pass

    label("Function_17_58E9")

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

    # Function_17_58E9 end

    def Function_18_596E(): pass

    label("Function_18_596E")

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

    # Function_18_596E end

    def Function_19_59D1(): pass

    label("Function_19_59D1")

    OP_8E(0xFE, 0x6D6, 0x0, 0x5B4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFFD8A, 0x0, 0xFFFFE674, 0x1388, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_19_59D1 end

    def Function_20_5A0A(): pass

    label("Function_20_5A0A")

    OP_8E(0xFE, 0xFFFFF81C, 0x0, 0x5AA, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFFD8A, 0x0, 0xFFFFE674, 0x1388, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_5A0A end

    def Function_21_5A43(): pass

    label("Function_21_5A43")

    OP_8E(0xFE, 0xFFFFFD8A, 0x0, 0xFFFFE674, 0x1388, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_21_5A43 end

    def Function_22_5A68(): pass

    label("Function_22_5A68")

    OP_8E(0xFE, 0xFFFFFD8A, 0x0, 0xFFFFE674, 0x1388, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_22_5A68 end

    def Function_23_5A8D(): pass

    label("Function_23_5A8D")

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
            "#634F#6PWell...good work, everyone.\x02\x03",

            "#632FI've gotten word that a Royal Army\x01",
            "detachment is heading here from the\x01",
            "Haken Gate.\x02\x03",

            "You can leave the...situation...at the\x01",
            "market to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        (
            "#1007FR-Right...\x02\x03",

            "#1003FTo think they'd bring out a monster like that...\x02\x03",

            "And Lorence...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xB,
        (
            "#026F#4PThe second Enforcer.\x01",
            "Leonhardt the Bladelord.\x02\x03",

            "#022FSo he's our 'Loewe,' huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xC,
        (
            "#035F#2PHeh... At last, our masked villain is\x01",
            "revealed to the audience in full.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xD,
        (
            "#049F#2PHe never seemed like the kind of man to do\x01",
            "something so heinous when we encountered\x01",
            "him in the castle, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x10,
        "#072FHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xF,
        (
            "#063F#2PM-Mr. Lugran?\x02\x03",

            "Have we heard from Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x8,
        (
            "#634F#6PUnfortunately not, little missy.\x02\x03",

            "#632FThat hotheaded fool... What in Aidios' name\x01",
            "does he think he's doing?\x02",
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
        "#064F#2PAgate...\x02",
    )


    def lambda_5EEE():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5EEE)
    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        "#1025F#6PHey, could that be--\x02",
    )

    CloseMessageWindow()

    def lambda_5F20():

        label("loc_5F20")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_5F20")

    QueueWorkItem2(0x101, 1, lambda_5F20)

    def lambda_5F31():

        label("loc_5F31")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_5F31")

    QueueWorkItem2(0xD, 1, lambda_5F31)

    def lambda_5F42():

        label("loc_5F42")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_5F42")

    QueueWorkItem2(0xB, 1, lambda_5F42)

    def lambda_5F53():

        label("loc_5F53")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_5F53")

    QueueWorkItem2(0xC, 1, lambda_5F53)

    def lambda_5F64():

        label("loc_5F64")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_5F64")

    QueueWorkItem2(0xF, 1, lambda_5F64)

    def lambda_5F75():

        label("loc_5F75")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_5F75")

    QueueWorkItem2(0x10, 1, lambda_5F75)

    def lambda_5F86():
        OP_6D(1160, 0, 4059, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5F86)
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
            "#632F#6PThis is the Bracer Guild, Bose branch.\x02\x03",

            "#633FAh, you. What--\x02\x03",

            "...\x02\x03",

            "#632FWHAT?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        "#1026F#5P(Wh-What happened?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xB,
        "#022F(Nothing good, from the sound of it...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x8,
        (
            "#634F#6PYes, I understand.\x01",
            "I'll send the others at once.\x02\x03",

            "#632FRight, right, keep it together, man.\x01",
            "Help is coming.\x02",
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
            "#632F#6PThat was the elder of Ravennue Village,\x01",
            "Reisen.\x02\x03",

            "The dragon...just attacked Ravennue\x01",
            "moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        "#1002F#3S#5POh, no!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xB,
        "#024F#2PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x8,
        (
            "#634F#6PThe dragon torched their orchards and then\x01",
            "flew away, from the sound of it.\x02\x03",

            "#632FAgate showed up afterward and helped\x01",
            "with the firefighting, bu--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        "#1005F#5PRight! We're off!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)
    OP_62(0xF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #168
        0xF,
        "#065F#5PE-Estelle! Let me come with you, please!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        "#1004F#5PHuh?!\x02",
    )

    CloseMessageWindow()

    def lambda_633A():
        OP_6D(860, 0, 2860, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_633A)

    def lambda_6352():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6352)
    Sleep(50)

    def lambda_6365():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6365)
    Sleep(50)

    def lambda_6378():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6378)
    Sleep(50)

    def lambda_638B():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_638B)
    Sleep(50)
    TurnDirection(0xC, 0xF, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #170
        0xF,
        (
            "#062F#5PMy cannon would probably help against\x01",
            "a flying target like, um, a dragon, and...\x02\x03",

            "And... And...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        (
            "#1025F#5PRight, I get it, I get it.\x02\x03",

            "Just...safety first, okay?\x01",
            "If there's trouble...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xF,
        "#560F#5POkay!\x02",
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
            "\x07\x05Please form your party.\x01",
            "You may choose two other members aside from the\x01",
            "mandatory members.\x07\x00\x02",
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

    # Function_23_5A8D end

    def Function_24_666E(): pass

    label("Function_24_666E")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6685")
    Call(0, 28)
    Call(0, 30)

    label("loc_6685")

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
            "#1017FSo the market's already being repaired?\x01",
            "That's wonderful!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xB,
        (
            "#021F#4PThey certainly got to it quickly.\x01",
            "It only happened yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x8,
        (
            "#631FYes, Mayor Maybelle's throwing herself into it.\x02\x03",

            "#630FShe's already sent aid to Ravennue as well,\x01",
            "or so I heard.\x02\x03",

            "Everyone's doing their best, even through\x01",
            "their fear.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 90, 400)
    Sleep(500)

    ChrTalk(    #177
        0xD,
        (
            "#047F#5PI've heard word from Grancel, as well, \x01",
            "and Grandmother has issued a proclamation.\x02\x03",

            "#040FShe has stated that the government will\x01",
            "respond immediately to the threat of the\x01",
            "dragon and will send aid to the affected areas.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)

    def lambda_699E():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_699E)

    def lambda_69AC():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_69AC)

    def lambda_69BA():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_69BA)
    Sleep(500)

    ChrTalk(    #178
        0x101,
        "#1001F#4PThat's our queen! Awesome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xC,
        (
            "#035FHeh. I can think of certain lords and\x01",
            "ministers of Erebonia who could stand\x01",
            "to learn from such an example.\x02\x03",

            "They're far more interested in attending\x01",
            "fancy parties than addressing the concerns\x01",
            "of the citizenry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x10,
        (
            "#075FIronically, I could say a lot of the same\x01",
            "for the Republic.\x02\x03",

            "Half the time, our politicians seem to spend\x01",
            "so much time dancing around each other\x01",
            "that they never get anything done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xD,
        (
            "#045F#5PHaha, well, it may help that we're such\x01",
            "a small country.\x02\x03",

            "#048FRegardless... Preparations for the\x01",
            "plan against the dragon should be\x01",
            "almost complete..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        (
            "#1006F#4PTime to go see what the Royal Army\x01",
            "can do, then!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    def lambda_6C79():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6C79)

    def lambda_6C87():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6C87)

    def lambda_6C95():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6C95)

    def lambda_6CA3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6CA3)

    ChrTalk(    #183
        0x101,
        (
            "#1015FSo we should just head for the landing port,\x01",
            "I guess, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x8,
        (
            "#631FYes, you're scheduled to depart at\x01",
            "10:00 AM at Port No. 1.\x02\x03",

            "It's about nine now, so you should have\x01",
            "time to pick up some supplies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        "#1006FRight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xB,
        (
            "#023F#4PWon't that be a little difficult with the\x01",
            "market, er, in the state it's in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x8,
        (
            "#630FThe market's merchants have been put up\x01",
            "in the hotel for now.\x02\x03",

            "They're still open for business, seemingly,\x01",
            "so you should be able to pick up some\x01",
            "necessities there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xB,
        "#021F#4PNothing like persistence.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x10,
        (
            "#070FIt would be wise to visit them before\x01",
            "we head for the landing port.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6F52")
    AddParty(0x2, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_6F52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6F9F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F87")
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_6F9F")

    label("loc_6F87")

    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_6F9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6FEC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FD4")
    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_6FEC")

    label("loc_6FD4")

    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_6FEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7011")
    AddParty(0x7, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_7011")

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

    # Function_24_666E end

    def Function_25_7111(): pass

    label("Function_25_7111")

    EventBegin(0x0)
    OP_D6(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7126")
    Call(0, 28)

    label("loc_7126")

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

    def lambda_721D():
        OP_6D(790, 0, 2790, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_721D)

    def lambda_7235():
        OP_67(0, 6000, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7235)
    FadeToBright(1500, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #190
        0x11,
        (
            "#1007FOh, boy. I was wondering if he wanted\x01",
            "to get the last word in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xB,
        "#022FThe Bladelord is bold, if nothing else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xE,
        (
            "#053FNo kiddin'.\x02\x03",

            "#555FAnd I really screwed up in lettin'\x01",
            "him get away...\x02\x03",

            "Sorry, guys. I've got no excuse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x8,
        (
            "#634FNo. You made the right choice in letting\x01",
            "him go.\x02\x03",

            "A graveyard is no place for the living\x01",
            "to settle their arguments.\x02\x03",

            "#632FHamel, though... Why's that causing an\x01",
            "itch in the back of m'skull?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x11,
        "#1003FYeah, didn't Loewe mention that before?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)
    Sleep(300)

    ChrTalk(    #195
        0x11,
        "#1015F#3PDo you know anything, Kloe?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 0, 400)

    def lambda_7486():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7486)
    Sleep(50)

    def lambda_7499():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7499)

    ChrTalk(    #196
        0xD,
        (
            "#043F#4PI don't, I'm sorry.\x02\x03",

            "#049FI imagine Grandmother would know\x01",
            "something, but...\x02\x03",

            "Given that it seems to be some kind\x01",
            "of state secret, she may not be willing\x01",
            "to tell me until I'm older.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x11,
        (
            "#1007F#3PArgh. Good point.\x02\x03",

            "#1015FHow about you, Olivier?\x01",
            "Hamel's in Erebonia, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xC,
        (
            "#035FIt is, although...\x02\x03",

            "#030FEven we don't speak of it much,\x01",
            "so it's always a surprise to hear it\x01",
            "brought up in conversation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x11,
        "#1004F#3POh. Why's that?\x02",
    )

    CloseMessageWindow()

    def lambda_7667():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7667)
    Sleep(50)

    def lambda_767A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_767A)
    Sleep(50)

    def lambda_768D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_768D)

    def lambda_769B():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_769B)
    Sleep(50)

    def lambda_76AE():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_76AE)
    Sleep(400)

    ChrTalk(    #200
        0xC,
        (
            "#032FHamel was a village in the southernmost\x01",
            "reaches of the Empire, near the Liberlian\x01",
            "border.\x02\x03",

            "I say 'was,' for you will find it on no map\x01",
            "of the Empire today.\x02",
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
        "#1020F#3PHuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xF,
        "#064F#4PIt's not gone, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xC,
        (
            "#035FThe village was demolished in a\x01",
            "landslide some time ago. A number\x01",
            "of the residents lost their lives then.\x02\x03",

            "As I understand it, it is now little more\x01",
            "than empty ruins and ghosts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xF,
        "#063F#4PThat's awful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xE,
        "#552F#6PSo that's it, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x11,
        (
            "#1020F#3PB-But still, even if a lot of people died,\x01",
            "there's no excuse for his actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xC,
        (
            "#032FI have...undersold the scale of the disaster,\x01",
            "I think. Rumor says that VERY few of the\x01",
            "villagers survived.\x02\x03",

            "Only rescue units saw precisely what\x01",
            "happened. But few living these days can\x01",
            "claim to know a Hamel resident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x11,
        "#1026F#3PIt was that bad...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x10,
        (
            "#074F#3PIt's not unheard of for landslides to\x01",
            "swallow entire settlements.\x02\x03",

            "#072FThey're sometimes called 'mountain\x01",
            "tsunamis' because of how they create\x01",
            "waves of pure rock and earth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xB,
        (
            "#025F#5PIt's an odd thing to suddenly\x01",
            "bring up in context, however.\x02\x03",

            "#522FI mean, what in the world would\x01",
            "Hamel have to do with Her Majesty and\x01",
            "General Morgan? Or Liberl at all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xC,
        (
            "#035FAlas, at this point we don't know\x01",
            "enough to confirm or deny anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x8,
        (
            "#634FMmm. Let me poke my old nose\x01",
            "around the various corners of the\x01",
            "guild to see what I can find out.\x02\x03",

            "#630FAnd enough about Hamel for now.\x01",
            "We've other business!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7CF8():
        OP_6D(870, 0, 3840, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7CF8)

    def lambda_7D10():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7D10)

    def lambda_7D1E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7D1E)
    Sleep(50)

    def lambda_7D31():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7D31)

    def lambda_7D3F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7D3F)

    def lambda_7D4D():
        OP_8C(0xFE, 5, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7D4D)
    Sleep(50)

    def lambda_7D60():
        OP_8C(0xFE, 5, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7D60)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #213
        0x8,
        (
            "#630FFirst of all, let me give you payment\x01",
            "for all you've done.\x02",
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
            "#631F#3PYou went through quite a lot with this\x01",
            "dragon mess!\x02\x03",

            "You've done the name of the guild proud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x11,
        "#1008F#7PAh-haha... You really think so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xE,
        (
            "#552F#4PWe still didn't stop whatever experiment\x01",
            "they were runnin'.\x02\x03",

            "Don't think we can claim much of a\x01",
            "victory on this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xB,
        (
            "#022F#2PThis also means they've conducted\x01",
            "experiments in all of Liberl's major\x01",
            "regions.\x02\x03",

            "We have to figure out what the society\x01",
            "plans to do next as soon as we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x8,
        (
            "#634F#3PYes, about that.\x02\x03",

            "#630FWhy don't you all take a break\x01",
            "for a little while?\x02",
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
        "#1004F#7PHuh?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_80DA")

    ChrTalk(    #220
        0xE,
        "#052F#4PRest? But Schera just said--\x02",
    )

    CloseMessageWindow()
    Jump("loc_80FD")

    label("loc_80DA")


    ChrTalk(    #221
        0xB,
        "#023F#2PRest? But as I said--\x02",
    )

    CloseMessageWindow()

    label("loc_80FD")


    ChrTalk(    #222
        0x8,
        (
            "#630F#3POh, I heard, but I'm serious.\x02\x03",

            "You've been running around from Ruan to\x01",
            "Grancel to here, solving case after case\x01",
            "with barely so much as time to sleep.\x02\x03",

            "If you don't take at least a single moment\x01",
            "to unwind, you'll snap your springs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x11,
        (
            "#1026F#7PBut we can't just take a break in the\x01",
            "middle of something so important.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_82E0")

    ChrTalk(    #224
        0xE,
        (
            "#555F#4PWe need to be able to get out there\x01",
            "if they pull something.\x02\x03",

            "I dunno if we can just slack off,\x01",
            "but the old man does have a point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8379")

    label("loc_82E0")


    ChrTalk(    #225
        0xB,
        (
            "#022F#2PWe will still need to act if Ouroboros\x01",
            "makes another move.\x02\x03",

            "I don't know how much time we\x01",
            "would have to rest, but Lugran does\x01",
            "have a point.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8379")


    ChrTalk(    #226
        0x8,
        (
            "#634F#3PThe army's patrols have kicked into high\x01",
            "gear thanks to all the dragon shenanigans.\x02\x03",

            "They should be able to handle any\x01",
            "immediate danger, I think.\x02\x03",

            "#632FAnd I've been meaning to mention...\x01",
            "It seems Kurt's team has found IT.\x02",
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
        "#1005F#7P#4SHuh? 'It'? Wait, like--\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_858C")

    ChrTalk(    #228
        0xB,
        "#024F#2PYou mean they found Ouroboros' base?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_85BF")

    label("loc_858C")


    ChrTalk(    #229
        0xE,
        "#054F#4PYou mean they found Ouroboros' base?!\x02",
    )

    CloseMessageWindow()

    label("loc_85BF")


    ChrTalk(    #230
        0x8,
        (
            "#634F#3PYes. Kurt reported they got a solid lead\x01",
            "a few days ago.\x02\x03",

            "#630FIf they can pinpoint the base, you'll be\x01",
            "busy again soon enough.\x02\x03",

            "So I really think it would be a good idea\x01",
            "to rest while you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x11,
        "#1015F#7PYeah, I see... Hrm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x10,
        (
            "#070F#4PIn that case, I'll take you up on that, Lugran.\x02\x03",

            "Remember, part of a bracer's duty is to\x01",
            "ensure he can keep performing his duties.\x01",
            "Getting rest is a part of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xB,
        "#027F#2PTrue enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xE,
        (
            "#051F#4PWell, I guess the world ain't gonna end\x01",
            "if we take a breather.\x02",
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
            "#031FBracer wisdom prevails again.\x01",
            "Zin, you are a sage and a gentleman!\x02\x03",

            "#030FStill, Lugran, given that you're\x01",
            "suggesting a break...\x02\x03",

            "I assume you have a destination\x01",
            "in mind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x8,
        (
            "#631F#3PHeh heh! Sharp, Olivier.\x02\x03",

            "#630FTruth be told, I got a little something\x01",
            "nice from Mayor Maybelle.\x02\x03",

            "She wanted it separate from your normal\x01",
            "pay for the dragon business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x11,
        (
            "#1004F#7PHuh? What else could she be\x01",
            "paying us with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x8,
        (
            "#631F#3POh, just a reservation at the\x01",
            "Kingfisher Inn on the lakefront\x01",
            "to the south.\x02\x03",

            "She's paid for all of you to stay\x01",
            "there for three days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x11,
        "#1018F#7PSERIOUSLY?! SWEET!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #240
        "\x07\x00Received #1049i.\x02",
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
            "#031FAh! The hospitality of Bose's beautiful mayor\x01",
            "once again shines like a beacon through the\x01",
            "fog of weariness!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xD,
        (
            "#048FHaha. Yes, it's just like Maybelle to do\x01",
            "something like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 270, 400)

    ChrTalk(    #243
        0xF,
        (
            "#560F#2PSo we're going on a vacation,\x01",
            "right?\x02\x03",

            "To the Kingfisher Inn?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8B92():
        OP_8C(0xB, 90, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8B92)
    Sleep(50)

    def lambda_8BA5():
        OP_8C(0xD, 90, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8BA5)
    Sleep(50)

    def lambda_8BB8():
        OP_8C(0x10, 90, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8BB8)
    Sleep(50)

    def lambda_8BCB():
        OP_8C(0xE, 225, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8BCB)
    Sleep(50)

    def lambda_8BDE():
        OP_8C(0x11, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8BDE)
    Sleep(300)

    ChrTalk(    #244
        0xB,
        (
            "#021F#5PMm-hmm! That's right.\x02\x03",

            "#027FIt's a luxurious inn with a fantastic view\x01",
            "of Valleria Lake.\x02\x03",

            "They're famous for their food, fine spirits,\x01",
            "and they provide boats for going out onto\x01",
            "the lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xF,
        "#061F#2PHee, that sounds great!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x10,
        (
            "#071F#3PThis does sound like a nice\x01",
            "little vacation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xE,
        (
            "#051F#6PYeah, if we gotta take a load off,\x01",
            "Kingfisher's close to the best place\x01",
            "in Liberl to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x11,
        (
            "#1001F#3PYou got that right!\x02\x03",

            "#1018FLet's not waste Mayor Maybelle's kindness,\x01",
            "guys! C'mon!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A3(0x4)

    label("loc_8DEA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9060")
    SetMessageWindowPos(-1, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #249
        (
            "\x06\x18\x07\x05You may now reconfigure your party. Swap party members\x01",
            "and their gear in and out as needed, and select 'move out'\x01",
            "when ready.\x07\x00\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        180,
        80,
        0,
        (
            "Form Party\x01",            # 0
            "Change Equipment\x01",      # 1
            "Move Out\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F57")
    OP_A2(0x4)
    SetChrName("")

    AnonymousTalk(    #250
        (
            "\x07\x05Please form your party.\x01",
            "You may choose three other members aside from Estelle.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0xFF, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    Jump("loc_905D")

    label("loc_8F57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8F90")
    OP_C0(0x13, 0x78, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_8FBC")

    label("loc_8F90")


    AnonymousTalk(    #251
        "\x07\x05Please form your party first.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)

    label("loc_8FBC")

    Jump("loc_905D")

    label("loc_8FBF")

    SetChrName("")

    AnonymousTalk(    #252
        "\x06\x18\x07\x05Are you ready to continue?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9058")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9052")

    AnonymousTalk(    #253
        "\x07\x05Please form your party first.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    Jump("loc_9055")

    label("loc_9052")

    Jump("loc_9060")

    label("loc_9055")

    Jump("loc_905D")

    label("loc_9058")

    Sleep(300)

    label("loc_9060")

    Sleep(1000)
    OP_A2(0x1C01)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T1101   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    label("loc_905D")

    Jump("loc_8DEA")

    # Function_25_7111 end

    def Function_26_9075(): pass

    label("Function_26_9075")

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

    ChrTalk(    #254
        0x8,
        (
            "#634FMmmmmmm... So that's what the\x01",
            "light show at the towers was about.\x02\x03",

            "#632FBut you kids pulled off a genuine\x01",
            "miracle this time.\x02\x03",

            "Let me give you your reward first.\x01",
            "Aidios knows you've earned it.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x9A, 0x4, 0x10)
    OP_AF(0x36, 0x9A)
    Sleep(100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #255
        0x8,
        (
            "#634FStill... What madness we've fallen into.\x02\x03",

            "#632FI never thought being deprived of orbments\x01",
            "would throw us into this much chaos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x11,
        (
            "#1007F#2PNo kidding...\x02\x03",

            "#1003FSorta makes you realize just how dependent\x01",
            "we've become on orbal power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x12,
        (
            "#1043F#4PIt's true. Communication, transportation,\x01",
            "defense, production...\x02\x03",

            "#1035FEvery single major function of society\x01",
            "is effectively paralyzed at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xB,
        (
            "#025F#2PFor most people, I think the real worry\x01",
            "will be the lights and the kitchen.\x02\x03",

            "#022FFrom the sounds of it, the city\x01",
            "was really in a tizzy last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x8,
        (
            "#632FThat's being kind about it.\x02\x03",

            "People were mobbing the guildhouse,\x01",
            "the orbal workshop, the mayor's mansion,\x01",
            "all demanding answers. It was awful.\x02\x03",

            "Everyone wanted to know what had\x01",
            "happened, and I had no answers to give.\x02\x03",

            "#634FFrenzied fools practically kept\x01",
            "me up all night. *yawn*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x11,
        "#1015F#2PI see... Sorry, Lugran.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xE,
        (
            "#555FWith the floating city on top of\x01",
            "all this, this crap's getting dire.\x02\x03",

            "Feels like we're one step\x01",
            "away from a friggin' panic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x10,
        (
            "#074FWell...the people of Liberl love\x01",
            "peace, so I do not personally\x01",
            "expect a riot...immediately.\x02\x03",

            "#072FShould the situation continue\x01",
            "for too long, however...people\x01",
            "may begin to lose hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x8,
        (
            "#634FYes. We must do something\x01",
            "about this, and quickly.\x02\x03",

            "#630FSo, then, everyone.\x02\x03",

            "What's this plan you said Russell \x01",
            "has to bring back the dead, turn water\x01",
            "to ambrosia, and save us all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x11,
        "#1025F#2PBring back the dead? Welllllll...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x12,
        (
            "#1040F#4PProfessor Russell's come up with a\x01",
            "new invention...that isn't too far off.\x02",
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

    # Function_26_9075 end

    def Function_27_988E(): pass

    label("Function_27_988E")

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

    ChrTalk(    #266
        0x8,
        (
            "#633FWhat?\x01",
            "You can get the phone working?!\x02\x03",

            "#631FThat would be a great help!\x02\x03",

            "Please, set up that Zero...\x01",
            "whatever it was right away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x11,
        "#1006F#2PNo problem!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, -180, 400)
    OP_8C(0x11, 90, 400)

    ChrTalk(    #268
        0x12,
        "#1040F#6PTita, would you do the honors?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xF,
        "#061F#2PSure! Gimme just a second...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF, 90, 400)

    def lambda_9AA7():
        OP_6D(1020, 0, 3960, 2500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9AA7)

    def lambda_9ABF():

        label("loc_9ABF")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_9ABF")

    QueueWorkItem2(0x8, 1, lambda_9ABF)

    def lambda_9AD0():

        label("loc_9AD0")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_9AD0")

    QueueWorkItem2(0x11, 1, lambda_9AD0)

    def lambda_9AE1():

        label("loc_9AE1")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_9AE1")

    QueueWorkItem2(0x12, 1, lambda_9AE1)
    OP_8E(0xF, 0xF3C, 0x0, 0x758, 0xBB8, 0x0)
    OP_8E(0xF, 0xFFA, 0x0, 0x1374, 0xBB8, 0x0)
    OP_8E(0xF, 0x7B2, 0x0, 0x1252, 0xBB8, 0x0)

    def lambda_9B2E():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9B2E)

    def lambda_9B3C():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9B3C)

    def lambda_9B4A():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9B4A)
    OP_8C(0xF, 0, 400)
    Sleep(500)
    OP_44(0x8, 0x1)
    OP_44(0x11, 0x1)
    OP_44(0x12, 0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #270
        (
            "\x07\x05Tita opened the lid to the phone\x01",
            "and put the ZFG inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #271
        0xF,
        "#062F#4POkaaaaaay...\x02",
    )

    CloseMessageWindow()
    OP_22(0xA, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xF, 225, 400)
    Sleep(500)

    ChrTalk(    #272
        0xF,
        "#061F#6P...Done! It's all set to go! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xE,
        (
            "#052F#5PThat was, uh, kind of faster\x01",
            "than I thought it'd be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xF,
        (
            "#067FHeehee! All you really need to do is put\x01",
            "it in the right spot inside the phone.\x02\x03",

            "#560FOkay, now for the moment of truth!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 0, 400)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #275
        "\x07\x05Tita flipped the switch on the phone.\x02",
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

    ChrTalk(    #276
        0x8,
        "#633F#6POooh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x11,
        "#1008F#5PYou did it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xB,
        (
            "#021F#5PNice! Looks like it really\x01",
            "does let orbal devices work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xF,
        (
            "#560F#4PUm, so, next I need to test to see\x01",
            "if the phone will actually connect.\x02\x03",

            "I'll try calling Grandpa. He's on the Arseille,\x01",
            "which should have a working phone.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #280
        "\x07\x05Tita dialed in a phone number...\x02",
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

    ChrTalk(    #281
        0xF,
        (
            "#064F#4PHello...?\x02\x03",

            "#560FAh! Grandpa!\x02\x03",

            "#061FYeah, it's me! I'm at the guildhouse\x01",
            "in Bose right now!\x02\x03",

            "Yeah, it's okay. It works great!\x02\x03",

            "#560FUh-huh... Uh-huh! Okay, I will!\x01",
            "You do your best too, Grandpa!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    Sleep(500)
    OP_8C(0xF, 225, 400)

    ChrTalk(    #282
        0xF,
        "#061F#6PHeehee... Umm, I think it's connecting okay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x11,
        "#1018F#5PNo kidding!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x12,
        (
            "#1040F#6PProfessor Russell's saved us\x01",
            "again, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x8,
        (
            "#631F#6PI'll have to drown Russell in beer\x01",
            "and steak next I see him!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A0F8():
        OP_6D(1110, 0, 3380, 1100)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A0F8)
    TurnDirection(0x8, 0x11, 400)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #286
        0x8,
        (
            "#633F#6PSpeaking of thanks, Russell seems\x01",
            "to be aboard the Arseille still, but...\x02\x03",

            "Where did the princess and\x01",
            "that churchman get off to?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A1AA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A1AA)
    Sleep(50)

    def lambda_A1BD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A1BD)
    Sleep(50)

    def lambda_A1D0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A1D0)
    Sleep(50)

    def lambda_A1E3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A1E3)
    Sleep(50)
    OP_8C(0x10, 0, 400)
    Sleep(200)

    ChrTalk(    #287
        0x11,
        (
            "#1006F#2POh, they both headed to Grancel\x01",
            "at dawn with Captain Schwarz.\x02\x03",

            "Kloe said she wanted to talk to the\x01",
            "queen, and Kevin said something\x01",
            "about the archbishop, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x8,
        (
            "#634F#6PI see...\x02\x03",

            "#630FI imagine the Royal Family and\x01",
            "the church have their own crises\x01",
            "to deal with right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x12,
        (
            "#1040F#4PThe good news is, they agreed\x01",
            "to deliver a Zero Field Generator\x01",
            "to the capital guildhouse for us.\x02\x03",

            "I would expect to get a call\x01",
            "from Elnan at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x8,
        (
            "#634FExcellent.\x01",
            "Coordinating with him will help.\x02\x03",

            "#630FYou lot are off to the remaining\x01",
            "guildhouses, I take it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x11,
        (
            "#1006F#2PYep, that's the plan.\x02\x03",

            "#1003FWhat I'd really like to deal with\x01",
            "is that floating city, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xB,
        (
            "#025F#2PWouldn't we all.\x02\x03",

            "It seems like our society friends\x01",
            "are already there, too.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A507():
        OP_8C(0x11, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A507)
    Sleep(50)
    OP_8C(0x12, -180, 400)

    ChrTalk(    #293
        0xE,
        (
            "#552FWe can't lay a damn finger on\x01",
            "them with our airships grounded.\x02\x03",

            "#551FPfeh... Real heroic spot to be in, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x12,
        "#1043F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x10,
        (
            "#074FThere's little point in flogging\x01",
            "ourselves over it.\x02\x03",

            "#070FRight now we must focus\x01",
            "on what CAN be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xE,
        "#051F#2PYeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xB,
        "#020F#2PYes... Let's get to it!\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A6AA")
    Call(0, 28)

    label("loc_A6AA")

    SetChrName("")

    AnonymousTalk(    #298
        (
            "\x07\x05Please form your party. You may choose two other\x01",
            "members aside from the mandatory members.\x07\x00\x02",
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

    # Function_27_988E end

    def Function_28_A766(): pass

    label("Function_28_A766")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A7DF"),
        (1, "loc_A7E5"),
        (SWITCH_DEFAULT, "loc_A7EB"),
    )


    label("loc_A7DF")

    OP_A2(0x1200)
    Jump("loc_A7EB")

    label("loc_A7E5")

    OP_A2(0x1201)
    Jump("loc_A7EB")

    label("loc_A7EB")

    Return()

    # Function_28_A766 end

    def Function_29_A7EC(): pass

    label("Function_29_A7EC")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A8A2"),
        (1, "loc_A8A8"),
        (SWITCH_DEFAULT, "loc_A8AE"),
    )


    label("loc_A8A2")

    OP_A2(0x1200)
    Jump("loc_A8AE")

    label("loc_A8A8")

    OP_A2(0x1201)
    Jump("loc_A8AE")

    label("loc_A8AE")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_29_A7EC end

    def Function_30_A8EA(): pass

    label("Function_30_A8EA")

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

    # Function_30_A8EA end

    SaveToFile()

Try(main)
