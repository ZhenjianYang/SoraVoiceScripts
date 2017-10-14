from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2710   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2710.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Targeting Camera',                     # 9
        'CWO Hahn',                             # 10
        'Renne',                                # 11
        "Renne's Father",                       # 12
        "Renne's Mother",                       # 13
        'Private Cromwell',                     # 14
        'Private Orta',                         # 15
        'Caesar',                               # 16
        'Warrant Officer Kientz',               # 17
        'Connor',                               # 18
        'Tico',                                 # 19
        'Morie',                                # 20
        'Private Nix',                          # 21
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
        'ED6_DT07/CH01310 ._CH',             # 00
        'ED6_DT27/CH03510 ._CH',             # 01
        'ED6_DT27/CH03910 ._CH',             # 02
        'ED6_DT27/CH03920 ._CH',             # 03
        'ED6_DT07/CH01300 ._CH',             # 04
        'ED6_DT07/CH01270 ._CH',             # 05
        'ED6_DT07/CH01143 ._CH',             # 06
        'ED6_DT07/CH01040 ._CH',             # 07
        'ED6_DT07/CH01050 ._CH',             # 08
        'ED6_DT07/CH01640 ._CH',             # 09
        'ED6_DT07/CH01140 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01310P._CP',             # 00
        'ED6_DT27/CH03510P._CP',             # 01
        'ED6_DT27/CH03910P._CP',             # 02
        'ED6_DT27/CH03920P._CP',             # 03
        'ED6_DT07/CH01300P._CP',             # 04
        'ED6_DT07/CH01270P._CP',             # 05
        'ED6_DT07/CH01143P._CP',             # 06
        'ED6_DT07/CH01040P._CP',             # 07
        'ED6_DT07/CH01050P._CP',             # 08
        'ED6_DT07/CH01640P._CP',             # 09
        'ED6_DT07/CH01140P._CP',             # 0A
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

    DeclNpc(
        X                   = 4750,
        Z                   = 0,
        Y                   = 90620,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
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
        TalkScenaIndex      = 16,
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
        TalkScenaIndex      = 17,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -4800,
        Z                   = 0,
        Y                   = 7900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 93480,
        Z                   = 0,
        Y                   = 85530,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 95300,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 93870,
        Z                   = 0,
        Y                   = 13580,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -3960,
        Z                   = 0,
        Y                   = 25000,
        Direction           = 273,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -2580,
        Z                   = 0,
        Y                   = 16760,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -2580,
        Z                   = 0,
        Y                   = 23040,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 96770,
        Z                   = 0,
        Y                   = 14030,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclEvent(
        X                   = -3939,
        Y                   = -1000,
        Z                   = 1820,
        Range               = 2122,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x0,
        Unknown_1C          = 25,
    )


    DeclActor(
        TriggerX            = -2990,
        TriggerZ            = 0,
        TriggerY            = 7710,
        TriggerRange        = 1000,
        ActorX              = -4800,
        ActorZ              = 1500,
        ActorY              = 7900,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 93600,
        TriggerZ            = 0,
        TriggerY            = 87450,
        TriggerRange        = 1000,
        ActorX              = 93480,
        ActorZ              = 1500,
        ActorY              = 85530,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 95800,
        TriggerZ            = 0,
        TriggerY            = 13660,
        TriggerRange        = 1000,
        ActorX              = 95300,
        ActorZ              = 1500,
        ActorY              = 16000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2990,
        TriggerZ            = 0,
        TriggerY            = 7710,
        TriggerRange        = 1000,
        ActorX              = -4800,
        ActorZ              = 1500,
        ActorY              = 7900,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_352",          # 00, 0
        "Function_1_560",          # 01, 1
        "Function_2_5E4",          # 02, 2
        "Function_3_6B2",          # 03, 3
        "Function_4_6D6",          # 04, 4
        "Function_5_806",          # 05, 5
        "Function_6_80B",          # 06, 6
        "Function_7_1251",         # 07, 7
        "Function_8_1256",         # 08, 8
        "Function_9_1CDF",         # 09, 9
        "Function_10_1CE4",        # 0A, 10
        "Function_11_27B0",        # 0B, 11
        "Function_12_31BF",        # 0C, 12
        "Function_13_3909",        # 0D, 13
        "Function_14_40AE",        # 0E, 14
        "Function_15_465B",        # 0F, 15
        "Function_16_5711",        # 10, 16
        "Function_17_5781",        # 11, 17
        "Function_18_587F",        # 12, 18
        "Function_19_58EC",        # 13, 19
        "Function_20_61A9",        # 14, 20
        "Function_21_795A",        # 15, 21
        "Function_22_79A1",        # 16, 22
        "Function_23_79DC",        # 17, 23
        "Function_24_7A17",        # 18, 24
        "Function_25_7AAF",        # 19, 25
        "Function_26_7F6B",        # 1A, 26
    )


    def Function_0_352(): pass

    label("Function_0_352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3A8")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_394")
    SetChrPos(0x10, -2580, 0, 93750, 180)
    SetChrPos(0x9, -710, 0, 92770, 277)
    Jump("loc_3A5")

    label("loc_394")

    SetChrPos(0x10, -2840, 0, 19000, 270)

    label("loc_3A5")

    Jump("loc_4F4")

    label("loc_3A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_3E7")
    SetChrFlags(0x11, 0x80)
    SetChrPos(0x12, -2710, 0, 18290, 0)
    SetChrPos(0x13, -2710, 0, 19610, 180)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    Jump("loc_4F4")

    label("loc_3E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_413")
    SetChrPos(0x9, -670, 0, 92690, 270)
    SetChrPos(0x10, -2400, 0, 92690, 90)
    Jump("loc_4F4")

    label("loc_413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_41D")
    Jump("loc_4F4")

    label("loc_41D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_442")
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0x10, -4800, 0, 7900, 90)
    Jump("loc_4F4")

    label("loc_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_44C")
    Jump("loc_4F4")

    label("loc_44C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 5)), scpexpr(EXPR_END)), "loc_4AB")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, 93664, 0, 87456, 180)
    SetChrPos(0xA, 95770, 0, 87453, 0)
    SetChrPos(0xC, 94561, 0, 88500, 0)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xC, 0xA, 0)
    SetChrFlags(0xC, 0x10)
    Jump("loc_4F4")

    label("loc_4AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_END)), "loc_4F4")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xA, -3410, 0, 19050, 270)
    SetChrPos(0xB, -1990, 0, 20610, 135)
    SetChrPos(0xC, -1010, 0, 19120, 315)

    label("loc_4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_506")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)

    label("loc_506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_53B")
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x11, 95590, 200, 7460, 180)
    SetChrFlags(0x11, 0x10)
    OP_44(0x11, 0x0)
    SetChrChipByIndex(0x11, 6)
    SetChrSubChip(0x11, 0)

    label("loc_53B")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_547"),
        (SWITCH_DEFAULT, "loc_55F"),
    )


    label("loc_547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55C")
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_55C")

    Jump("loc_55F")

    label("loc_55F")

    Return()

    # Function_0_352 end

    def Function_1_560(): pass

    label("Function_1_560")

    OP_64(0x3, 0x1)
    OP_1C(0x3, 0x0, 0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_573")
    Jump("loc_5BC")

    label("loc_573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_57D")
    Jump("loc_5BC")

    label("loc_57D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_58F")
    OP_65(0x0, 0x1)
    OP_64(0x3, 0x1)
    Jump("loc_5BC")

    label("loc_58F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_5A1")
    OP_64(0x0, 0x1)
    OP_65(0x3, 0x1)
    Jump("loc_5BC")

    label("loc_5A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_5AB")
    Jump("loc_5BC")

    label("loc_5AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 5)), scpexpr(EXPR_END)), "loc_5B5")
    Jump("loc_5BC")

    label("loc_5B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_END)), "loc_5BC")

    label("loc_5BC")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_5D8"),
        (101, "loc_5D8"),
        (102, "loc_5D8"),
        (104, "loc_5D8"),
        (106, "loc_5D8"),
        (SWITCH_DEFAULT, "loc_5E0"),
    )


    label("loc_5D8")

    OP_22(0x1C6, 0x1, 0x64)
    Jump("loc_5E3")

    label("loc_5E0")

    OP_23(0x1C6)

    label("loc_5E3")

    Return()

    # Function_1_560 end

    def Function_2_5E4(): pass

    label("Function_2_5E4")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_609")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_69C")

    label("loc_609")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_622")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_69C")

    label("loc_622")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63B")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_69C")

    label("loc_63B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_654")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_69C")

    label("loc_654")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66D")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_69C")

    label("loc_66D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_686")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_69C")

    label("loc_686")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69C")
    OP_99(0xFE, 0x6, 0x7, 0x546)

    label("loc_69C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_69C")

    label("loc_6B1")

    Return()

    # Function_2_5E4 end

    def Function_3_6B2(): pass

    label("Function_3_6B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D5")
    OP_8D(0xFE, -1070, 16329, -4540, 25330, 2000)
    Jump("Function_3_6B2")

    label("loc_6D5")

    Return()

    # Function_3_6B2 end

    def Function_4_6D6(): pass

    label("Function_4_6D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_763")

    ChrTalk(    #0
        0xFE,
        (
            "I'm not really sure why, but for some\x01",
            "reason I'm the only one on break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "So, I thought I'd have myself a little drink.\x02",
    )

    CloseMessageWindow()
    Jump("loc_802")

    label("loc_763")

    OP_A2(0x8)

    ChrTalk(    #2
        0xFE,
        (
            "Hey, I haven't heard the details, but word\x01",
            "is you guys solved the ghost mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Today I'm suddenly off shift, too, so\x01",
            "it's been a lot of good news.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_802")

    TalkEnd(0xFE)
    Return()

    # Function_4_6D6 end

    def Function_5_806(): pass

    label("Function_5_806")

    Call(0, 6)
    Return()

    # Function_5_806 end

    def Function_6_80B(): pass

    label("Function_6_80B")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_A43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97B")

    ChrTalk(    #4
        0xD,
        (
            "The Kaldia Tunnel is totally blacked\x01",
            "out right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xD,
        (
            "But, apparently, a lone traveler just\x01",
            "passed through a bit ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xD,
        (
            "Seems they were a researcher with the\x01",
            "central factory, but to cross the tunnel\x01",
            "as it is now... That takes some serious guts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xD,
        (
            "Honestly, it's hard for me to understand\x01",
            "the thoughts of capable people like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_A40")

    label("loc_97B")


    ChrTalk(    #8
        0xD,
        (
            "Oh, yeah, that person...\x01",
            "They also had a cat with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xD,
        (
            "Maybe cats are some kinda\x01",
            "monster repellent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xD,
        (
            "W-Well, having a pet with you certainly\x01",
            "might make you feel less scared, anyway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A40")

    Jump("loc_124D")

    label("loc_A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_C39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA3")

    ChrTalk(    #11
        0xD,
        (
            "The gate won't close, so we're having to\x01",
            "be stricter with our checks on travelers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xD,
        (
            "We've received orders to ensure bracers\x01",
            "pass freely, though, so don't worry. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xD,
        (
            "Apparently it's a special measure\x01",
            "to assist guild activities...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xD,
        (
            "It's pretty surprising. That kinda order would've\x01",
            "been unthinkable not that long ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_C36")

    label("loc_BA3")


    ChrTalk(    #15
        0xD,
        "Bracers are welcome to pass freely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xD,
        (
            "We've got orders to that extent from above.\x01",
            "Hard to believe considering how things\x01",
            "were before, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C36")

    Jump("loc_124D")

    label("loc_C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_D6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_CC2")

    ChrTalk(    #17
        0xD,
        (
            "The earthquakes in Zeiss seem\x01",
            "to have settled down already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xD,
        (
            "I'm SO glad the earthquakes\x01",
            "didn't come this far.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D6B")

    label("loc_CC2")


    ChrTalk(    #19
        0xD,
        (
            "The earthquakes in Zeiss seem\x01",
            "to have settled down already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xD,
        (
            "There was an announcement from the central factory\x01",
            "about it, apparently, so it's probably true.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_D6B")

    Jump("loc_124D")

    label("loc_D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_EA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DF7")

    ChrTalk(    #21
        0xD,
        (
            "We just got an emergency communique\x01",
            "from headquarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xD,
        (
            "Ever since then, the chief\x01",
            "won't come out of his room.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E9F")

    label("loc_DF7")


    ChrTalk(    #23
        0xD,
        (
            "We just got an emergency communique\x01",
            "from headquarters, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xD,
        (
            "Ever since then the chief\x01",
            "won't come out of his room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xD,
        "I-I wonder if something happened?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_E9F")

    Jump("loc_124D")

    label("loc_EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_FD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F12")

    ChrTalk(    #26
        0xD,
        (
            "Apparently there are earthquakes happening\x01",
            "in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xD,
        "I-I hope they don't hit here...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FCD")

    label("loc_F12")


    ChrTalk(    #28
        0xD,
        (
            "Apparently there are earthquakes happening\x01",
            "in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xD,
        "T-To be honest, I...I hate earthquakes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xD,
        (
            "I mean, the entire land shakes, right?\x01",
            "It's only natural to be freaked out.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_FCD")

    Jump("loc_124D")

    label("loc_FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_10C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_104B")

    ChrTalk(    #31
        0xD,
        "As usual, there aren't many tourists.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xD,
        (
            "I wonder if it'll be this way\x01",
            "until Ruan's election ends.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C3")

    label("loc_104B")


    ChrTalk(    #33
        0xD,
        "Hey, welcome to the Air-Letten Checkpoint.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xD,
        (
            "As always, we don't get many visitors,\x01",
            "so we're taking it easy.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_10C3")

    Jump("loc_124D")

    label("loc_10C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_113B")

    ChrTalk(    #35
        0xD,
        (
            "Both Mr. Hahn and Mr. Kent were\x01",
            "moaning on about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xD,
        "I wonder if something bad's come up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_124D")

    label("loc_113B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_124D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_11AC")

    ChrTalk(    #37
        0xD,
        "There's not many tourists right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xD,
        "Apparently Ruan's election is affecting tourism.\x02",
    )

    CloseMessageWindow()
    Jump("loc_124D")

    label("loc_11AC")

    OP_A2(0x1)

    ChrTalk(    #39
        0xD,
        "Hey, welcome to the Air-Letten Checkpoint.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xD,
        (
            "There aren't many tourists at the moment,\x01",
            "so you can take your time and really\x01",
            "appreciate the waterfall.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_124D")

    TalkEnd(0xD)
    Return()

    # Function_6_80B end

    def Function_7_1251(): pass

    label("Function_7_1251")

    Call(0, 8)
    Return()

    # Function_7_1251 end

    def Function_8_1256(): pass

    label("Function_8_1256")

    TalkBegin(0xE)
    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1273")
    OP_A9(0x79)
    TalkEnd(0xE)
    Return()

    label("loc_1273")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1284")
    TalkEnd(0xE)
    Return()

    label("loc_1284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1389")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1328")

    ChrTalk(    #41
        0xE,
        (
            "Apparently we got a transmission\x01",
            "from another squad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xE,
        "I wonder if something came up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xE,
        "Incidents haven't exactly been rare lately.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1386")

    label("loc_1328")


    ChrTalk(    #44
        0xE,
        (
            "Apparently we got a transmission\x01",
            "from another squad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xE,
        "I wonder if something came up.\x02",
    )

    CloseMessageWindow()

    label("loc_1386")

    Jump("loc_1CDB")

    label("loc_1389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_14E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1449")

    ChrTalk(    #46
        0xE,
        "Hey, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xE,
        (
            "It seems like the Orbment Charging Stations\x01",
            "aren't working, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xE,
        (
            "If you're tired, you should just go rest\x01",
            "at a lodge. Don't push yourself.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_14DF")

    label("loc_1449")


    ChrTalk(    #49
        0xE,
        (
            "It seems like the Orbment Charging Stations\x01",
            "aren't working, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xE,
        (
            "That's the situation, so be careful and\x01",
            "don't push yourselves too hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DF")

    Jump("loc_1CDB")

    label("loc_14E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_15F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_157A")

    ChrTalk(    #51
        0xE,
        (
            "Apparently there was an earthquake\x01",
            "at Leiston Fortress, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xE,
        (
            "There wasn't any damage, but I was\x01",
            "sure surprised when I heard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F2")

    label("loc_157A")


    ChrTalk(    #53
        0xE,
        (
            "Apparently there was an earthquake\x01",
            "at Leiston Fortress, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xE,
        (
            "No wonder the chief looked so\x01",
            "pale that time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_15F2")

    Jump("loc_1CDB")

    label("loc_15F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1739")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_168A")

    ChrTalk(    #55
        0xE,
        "We get a lot of communiques from HQ.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xE,
        (
            "If you get worked up every time one comes\x01",
            "in, you'll have a hard time with this job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1736")

    label("loc_168A")


    ChrTalk(    #57
        0xE,
        "Really, Cromwell's too nervous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xE,
        "We get a lot of communiques from HQ.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xE,
        (
            "If you get worked up every time one comes\x01",
            "in, you'll have a hard time with this job.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1736")

    Jump("loc_1CDB")

    label("loc_1739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_18BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_17DF")

    ChrTalk(    #60
        0xE,
        (
            "Ruan's election, and now the earthquakes\x01",
            "in Zeiss...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xE,
        (
            "We're kind of in the mid-point between those\x01",
            "two things, but everything's quiet here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18BB")

    label("loc_17DF")


    ChrTalk(    #62
        0xE,
        (
            "Everyone's talking about the earthquakes in\x01",
            "Zeiss. We're getting rumors even all the way\x01",
            "out here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xE,
        (
            "Apparently it was pretty small,\x01",
            "but it's kinda creepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xE,
        (
            "We almost never get earthquakes in\x01",
            "the kingdom.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_18BB")

    Jump("loc_1CDB")

    label("loc_18BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_19B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1958")

    ChrTalk(    #65
        0xE,
        (
            "Lately the highways have been even\x01",
            "more dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xE,
        (
            "Don't push yourself too hard. Be sure to\x01",
            "get some rest before you head out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B2")

    label("loc_1958")


    ChrTalk(    #67
        0xE,
        "Hey, welcome. You came at a good time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xE,
        "I've been so dang sleepy for a while.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_19B2")

    Jump("loc_1CDB")

    label("loc_19B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1AB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A48")

    ChrTalk(    #69
        0xE,
        (
            "I was really way too busy during\x01",
            "the birthday celebrations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xE,
        (
            "Thinking back on it now, though,\x01",
            "it's nicer when it's busy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AAF")

    label("loc_1A48")

    OP_A2(0x2)

    ChrTalk(    #71
        0xE,
        "Hey, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xE,
        (
            "We're totally empty around here right now,\x01",
            "so feel free to spend the night.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AAF")

    Jump("loc_1CDB")

    label("loc_1AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1B3D")

    ChrTalk(    #73
        0xE,
        (
            "The family that came by a while\x01",
            "ago seemed so happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xE,
        (
            "Seeing a family like that makes me\x01",
            "wish I had a family of my own.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CDB")

    label("loc_1B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 5)), scpexpr(EXPR_END)), "loc_1C5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1BD1")

    ChrTalk(    #75
        0xE,
        (
            "Seeing families traveling around together\x01",
            "makes me a little bit jealous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xE,
        (
            "Ahh, I hope I can have a family of\x01",
            "my own soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C57")

    label("loc_1BD1")

    OP_8C(0xE, 0, 0)
    OP_4A(0xB, 255)
    OP_A2(0x2)
    OP_A2(0xA)

    ChrTalk(    #77
        0xE,
        (
            "The three of you will be staying for\x01",
            "one night, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xB,
        "Yes, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xE,
        "Well, then, please sign here...\x02",
    )

    CloseMessageWindow()
    OP_4B(0xB, 255)

    label("loc_1C57")

    Jump("loc_1CDB")

    label("loc_1C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1CDB")

    ChrTalk(    #80
        0xE,
        (
            "Hey, welcome. This is a lodging\x01",
            "facility for travelers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xE,
        (
            "If you'd like to stay the night,\x01",
            "just give me the word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CDB")

    TalkEnd(0xE)
    Return()

    # Function_8_1256 end

    def Function_9_1CDF(): pass

    label("Function_9_1CDF")

    Call(0, 10)
    Return()

    # Function_9_1CDF end

    def Function_10_1CE4(): pass

    label("Function_10_1CE4")

    TalkBegin(0xF)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D01")
    OP_A9(0x78)
    TalkEnd(0xF)
    Return()

    label("loc_1D01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D12")
    TalkEnd(0xF)
    Return()

    label("loc_1D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1ED5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E4E")

    ChrTalk(    #82
        0xF,
        (
            "It seems this situation's not gonna end\x01",
            "any time soon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xF,
        (
            "In which case, my orbal stove's not\x01",
            "gonna be working for a while, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xF,
        (
            "I guess I'll have to reconsider\x01",
            "the menu at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xF,
        (
            "Though...as a man striving forward on the\x01",
            "path of cuisine, it's incredibly frustrating.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1ED2")

    label("loc_1E4E")


    ChrTalk(    #86
        0xF,
        (
            "I guess I'll have to reconsider\x01",
            "the menu at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xF,
        (
            "Well, if orbal devices start working\x01",
            "first that'd be best for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED2")

    Jump("loc_27AC")

    label("loc_1ED5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_202D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA9")

    ChrTalk(    #88
        0xF,
        (
            "To think orbal devices would\x01",
            "just stop like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xF,
        (
            "We're not that bad off here, but\x01",
            "I'm sure Zeiss is in an uproar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xF,
        (
            "After all, that city's practically\x01",
            "built on orbal devices.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_202A")

    label("loc_1FA9")


    ChrTalk(    #91
        0xF,
        (
            "If they can't use orbments, I'm sure\x01",
            "Zeiss is in an uproar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xF,
        (
            "After all, that city's practically\x01",
            "built on orbal devices.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_202A")

    Jump("loc_27AC")

    label("loc_202D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_20A9")

    ChrTalk(    #93
        0xF,
        (
            "Seems like the land has finally\x01",
            "settled down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xF,
        (
            "It's times like this that we\x01",
            "gotta be thankful to Aidios.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27AC")

    label("loc_20A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_218B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2127")

    ChrTalk(    #95
        0xF,
        (
            "Apparently there was some\x01",
            "big communique from HQ.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xF,
        (
            "It's gotta be related to the earthquakes,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2188")

    label("loc_2127")


    ChrTalk(    #97
        0xF,
        (
            "Apparently there was some big\x01",
            "communique from HQ.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xF,
        "The commander ran out in a panic.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2188")

    Jump("loc_27AC")

    label("loc_218B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_22BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2228")

    ChrTalk(    #99
        0xF,
        (
            "Seems like the earthquakes in Zeiss\x01",
            "are still going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xF,
        (
            "I guess I should at least clear the glass\x01",
            "bottles off the shelves, huh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B7")

    label("loc_2228")


    ChrTalk(    #101
        0xF,
        (
            "Seems like the earthquakes in Zeiss\x01",
            "are still going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xF,
        (
            "I guess I should at least clear the glass\x01",
            "bottles off the shelves, huh...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_22B7")

    Jump("loc_27AC")

    label("loc_22BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_234E")

    ChrTalk(    #103
        0xF,
        (
            "They don't happen much in Liberl,\x01",
            "but earthquakes are scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xF,
        (
            "After all, the friggin' earth just starts\x01",
            "jumpin' under your feet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27AC")

    label("loc_234E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_23EF")

    ChrTalk(    #105
        0xF,
        (
            "Seems like the commander is doin' the\x01",
            "customs checks himself for a change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xF,
        (
            "Heh heh, now ain't this a sight.\x01",
            "Maybe I'll go jeer at him later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27AC")

    label("loc_23EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2519")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_246D")

    ChrTalk(    #107
        0xF,
        "Still, though, that family sure looked happy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xF,
        (
            "Almost like the perfect family,\x01",
            "right out of a book.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2516")

    label("loc_246D")

    OP_A2(0x3)

    ChrTalk(    #109
        0xF,
        (
            "We had a family traveling together here\x01",
            "a while back. Don't see that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xF,
        (
            "We're pretty far from the towns, after all.\x01",
            "You don't see many guests with kids.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2516")

    Jump("loc_27AC")

    label("loc_2519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_27AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_25A0")

    ChrTalk(    #111
        0xF,
        "You already see our famous waterfall?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xF,
        (
            "Now's a good chance to take it in since\x01",
            "no one's around to bother ya.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27AC")

    label("loc_25A0")

    OP_A2(0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_265C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "Seen the Persuade Duke quest in previous game\x01",             # 0
            "Didn't see the Persuade Duke quest in previous game.\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_264C"),
        (1, "loc_2654"),
        (SWITCH_DEFAULT, "loc_265C"),
    )


    label("loc_264C")

    OP_28(0x23, 0x3, 0x10)
    Jump("loc_265C")

    label("loc_2654")

    OP_28(0x23, 0x4, 0x10)
    Jump("loc_265C")

    label("loc_265C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2718")

    ChrTalk(    #113
        0xF,
        "Oh, you're those bracers from that time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xF,
        (
            "There's not many guests right now,\x01",
            "so relax and enjoy yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xF,
        (
            "If you're hungry, why not try\x01",
            "out some of my new menu?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27AC")

    label("loc_2718")


    ChrTalk(    #116
        0xF,
        "Hey, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xF,
        (
            "There's not many guests right now,\x01",
            "so relax and enjoy yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xF,
        (
            "If you're hungry, why not try\x01",
            "out some of my new menu?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27AC")

    TalkEnd(0xF)
    Return()

    # Function_10_1CE4 end

    def Function_11_27B0(): pass

    label("Function_11_27B0")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2898")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2826")

    ChrTalk(    #119
        0xFE,
        (
            "Attacking a school at a time like this...?\x01",
            "That ain't human.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "What a terrible thing.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_2895")

    label("loc_2826")


    ChrTalk(    #121
        0xFE,
        "Attacking a school at a time like this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "There's some real crazy people out there,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2895")

    Jump("loc_31BB")

    label("loc_2898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_293D")

    ChrTalk(    #123
        0xFE,
        (
            "That guy who came from the guild is\x01",
            "really helping out with the patrols.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "After all, we ain't got any idea what\x01",
            "could happen given the situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BB")

    label("loc_293D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2A9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_29D7")

    ChrTalk(    #125
        0xFE,
        (
            "We gotta start making a plan for\x01",
            "the signing ceremony soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "If we don't send in the paperwork,\x01",
            "HQ's gonna be a pain in my ass.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A9B")

    label("loc_29D7")


    ChrTalk(    #127
        0xFE,
        (
            "Hey, seems like the earthquakes've settled\x01",
            "down, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "Finally, we can get to our next job\x01",
            "and not have anythin' behind us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "We gotta start making a plan\x01",
            "for the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2A9B")

    Jump("loc_31BB")

    label("loc_2A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2BD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2B26")

    ChrTalk(    #130
        0xFE,
        (
            "There was even an earthquake at\x01",
            "Leiston Fortress...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "Gotta say, feels a bit too specific\x01",
            "to be a coincidence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BCE")

    label("loc_2B26")


    ChrTalk(    #132
        0xFE,
        (
            "There was even an earthquake at\x01",
            "Leiston Fortress...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "Gotta say, feels a bit too specific\x01",
            "to be a coincidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "Well, I'm probably just overthinkin' it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2BCE")

    Jump("loc_31BB")

    label("loc_2BD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2D0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2C72")

    ChrTalk(    #135
        0xFE,
        (
            "After the Wolf Fort it was the Sanktheim Gate,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "Do earthquakes even work like this?\x01",
            "It's like they're bein' aimed or somethin'.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D0A")

    label("loc_2C72")


    ChrTalk(    #137
        0xFE,
        (
            "After the Wolf Fort it was the Sanktheim Gate,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "Ohh, can't forget Zeiss, either.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "Seems like there was an earthquake there, too.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2D0A")

    Jump("loc_31BB")

    label("loc_2D0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_2E39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2DB5")

    ChrTalk(    #140
        0x10,
        (
            "Sounds like there was an earthquake\x01",
            "over at the Wolf Fort a bit ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x10,
        (
            "The commander over there, Gerwin, he\x01",
            "joined around the same time I did.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E36")

    label("loc_2DB5")


    ChrTalk(    #142
        0x10,
        (
            "Sounds like there was an earthquake\x01",
            "over at the Wolf Fort a bit ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x10,
        "Heh heh, I bet the soldiers were freakin' out.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2E36")

    Jump("loc_31BB")

    label("loc_2E39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2F49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2E9E")

    ChrTalk(    #144
        0x10,
        "Why's the commander at the counter... you ask?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x10,
        "...Well, a lot's happened.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F46")

    label("loc_2E9E")

    OP_A2(0x4)

    ChrTalk(    #146
        0x10,
        (
            "So there was a member of a criminal organization\x01",
            "hiding on the royal academy's grounds, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x10,
        (
            "Seems like this case is way more complicated\x01",
            "than we thought.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F46")

    Jump("loc_31BB")

    label("loc_2F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_302D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2F91")

    ChrTalk(    #148
        0xFE,
        (
            "I'll be damned.\x01",
            "Guess Nix wasn't makin' stuff up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_302A")

    label("loc_2F91")

    OP_A2(0x4)

    ChrTalk(    #149
        0xFE,
        (
            "I heard from the C.W.O. that apparently\x01",
            "Nix WAS tellin' the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "Maaan, that puts me in a bad spot.\x01",
            "I really ran him through the wringer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_302A")

    Jump("loc_31BB")

    label("loc_302D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_31BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_30DA")

    ChrTalk(    #151
        0xFE,
        "Seems like our soldiers're gettin' lazy lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "Even though we still haven't caught either the\x01",
            "Intelligence Division remnants or the sky bandits.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BB")

    label("loc_30DA")

    OP_A2(0x4)

    ChrTalk(    #153
        0xFE,
        "Seems like our soldiers're gettin' lazy lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "Like a while back, there was an idiot who was\x01",
            "half asleep at his post and thought he saw\x01",
            "something and made a huge fuss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        "Man, I gotta do somethin' about this.\x02",
    )

    CloseMessageWindow()

    label("loc_31BB")

    TalkEnd(0x10)
    Return()

    # Function_11_27B0 end

    def Function_12_31BF(): pass

    label("Function_12_31BF")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_32C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3251")

    ChrTalk(    #156
        0xFE,
        "This guard post is the perfect place to read.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "Just like the cafe in the capital,\x01",
            "I'd give it 5/5 stars, personally.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32C4")

    label("loc_3251")


    ChrTalk(    #158
        0xFE,
        "I only just realized how long I've been here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "Now, then, I'd best prepare to get back\x01",
            "to the capital.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_32C4")

    Jump("loc_3905")

    label("loc_32C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_338C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_332E")

    ChrTalk(    #160
        0xFE,
        "Well, whatever. It has nothing to do with me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        "I should focus on my reading.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3389")

    label("loc_332E")


    ChrTalk(    #162
        0xFE,
        "It seems like the soldiers are all worked up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "I wonder if something happened.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_3389")

    Jump("loc_3905")

    label("loc_338C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_3449")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_33F3")

    ChrTalk(    #164
        0xFE,
        "Well, whatever. It has nothing to do with me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        "I should focus on my reading.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3446")

    label("loc_33F3")


    ChrTalk(    #166
        0xFE,
        "Hmm, an earthquake at the Wolf Fort...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        "That soldier is a little loud.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_3446")

    Jump("loc_3905")

    label("loc_3449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_34E5")

    ChrTalk(    #168
        0xFE,
        (
            "I feel like I can focus on my\x01",
            "reading more than normal here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "Perhaps because the sound of the water\x01",
            "echoing from a distance is so nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3905")

    label("loc_34E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_3661")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_357B")

    ChrTalk(    #170
        0xFE,
        (
            "Usually I do my reading at the\x01",
            "cafe in the capital, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "It's nice to read a book in an open,\x01",
            "free space like this, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_365E")

    label("loc_357B")

    OP_A2(0x5)

    ChrTalk(    #172
        0xFE,
        (
            "Usually I do my reading at the\x01",
            "cafe in the capital, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "It's nice to read a book in an open,\x01",
            "free space like this, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "Even reading the same book can feel different\x01",
            "if you do it in a different atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_365E")

    Jump("loc_3905")

    label("loc_3661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 3)), scpexpr(EXPR_END)), "loc_3754")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_36A6")

    ChrTalk(    #175
        0xFE,
        (
            "Seeing a happy family makes me\x01",
            "feel happy too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3751")

    label("loc_36A6")

    OP_A2(0x5)

    ChrTalk(    #176
        0xFE,
        (
            "Haha, I thought it sounded cheery.\x01",
            "Sure enough, there's a family with a child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "They look like they're having fun.\x01",
            "Is this their first trip in a while, maybe?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3751")

    Jump("loc_3905")

    label("loc_3754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_3905")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_37EE")

    ChrTalk(    #178
        0xFE,
        "I'd seen pictures in the Liberl News, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "There's no way to truly appreciate the power\x01",
            "of this place without standing here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3905")

    label("loc_37EE")

    OP_A2(0x5)

    ChrTalk(    #180
        0xFE,
        (
            "During the election, all the tourist\x01",
            "spots in Ruan are open, I heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "I came from the capital to indulge in\x01",
            "a little peaceful reading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "This waterfall is truly an astounding backdrop\x01",
            "when enjoying a book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "The sound of the water just echoes\x01",
            "through my body.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3905")

    TalkEnd(0x11)
    Return()

    # Function_12_31BF end

    def Function_13_3909(): pass

    label("Function_13_3909")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_3B87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_39DE")

    ChrTalk(    #184
        0xFE,
        (
            "I think I'll put off going to the capital for\x01",
            "now and head to the Haken Gate instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "The Pearl of Liberl, Grancel Castle, is hard\x01",
            "to give up, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        "Oooh, now my head hurts.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B84")

    label("loc_39DE")


    ChrTalk(    #187
        0xFE,
        "Hmm, where should I go next...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "Sanktheim Gate would be nice, but\x01",
            "I'd also like to see Grancel Castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "But, it sounds like there's a treaty signing\x01",
            "going to happen in the capital, so I bet the\x01",
            "security will be tighter than normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "In that case, maybe I should just\x01",
            "head to the Haken Gate in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "For a trip centered around the history of\x01",
            "the Hundred Days War, the Haken Gate\x01",
            "can't be skipped.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3B84")

    Jump("loc_40AA")

    label("loc_3B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_3D1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3C4D")

    ChrTalk(    #192
        0xFE,
        (
            "I'd also like to walk the Kaldia Tunnel\x01",
            "at least once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "I'd feel way safer taking the airship\x01",
            "from Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "I should probably talk to Morie and\x01",
            "see what she wants to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D1B")

    label("loc_3C4D")


    ChrTalk(    #195
        0xFE,
        "I'm thinking of going to Zeiss after this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "Hmm... If I did, though, I'd have to pass\x01",
            "through the Kaldia Tunnel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "I would like to walk it at least once,\x01",
            "but it's a bit scary to think about.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3D1B")

    Jump("loc_40AA")

    label("loc_3D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_3F6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3DFA")

    ChrTalk(    #198
        0xFE,
        (
            "Lately, Morie's been reading the\x01",
            "Liberl News a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "Apparently she's just been looking at\x01",
            "the pictures, and doesn't read the\x01",
            "articles themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        "After all, she really hates printed text.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F6C")

    label("loc_3DFA")


    ChrTalk(    #201
        0xFE,
        (
            "Lately, Morie's been reading the\x01",
            "Liberl News a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "Apparently she's just been looking at\x01",
            "the pictures, and doesn't read the\x01",
            "articles themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "She's the exact opposite of me and my love\x01",
            "of books. She hates the printed word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "We read a lot of picture books together\x01",
            "when we were kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "I wonder at what point it was that we\x01",
            "diverged so much.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3F6C")

    Jump("loc_40AA")

    label("loc_3F6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_40AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_400A")

    ChrTalk(    #206
        0xFE,
        (
            "We're touring the historical sites\x01",
            "of the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "The Air-Letten Checkpoint is a great place,\x01",
            "just like in the books.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40AA")

    label("loc_400A")


    ChrTalk(    #208
        0xFE,
        "Phew! So this is Air-Letten, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "Historical stone buildings, and\x01",
            "the Lhotse Waterway waterfall...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        "Ahhh, it's just as good as the books said.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_40AA")

    TalkEnd(0x12)
    Return()

    # Function_13_3909 end

    def Function_14_40AE(): pass

    label("Function_14_40AE")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_4219")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_413F")

    ChrTalk(    #211
        0xFE,
        (
            "It's a surprisingly good idea to\x01",
            "go to the Haken Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "Though it feels like a waste after\x01",
            "coming out all this way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4216")

    label("loc_413F")


    ChrTalk(    #213
        0xFE,
        (
            "The white walls of Grancel Castle, huh.\x01",
            "I'd really love to take a few pictures\x01",
            "at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "But, the Sanktheim Gate also has its\x01",
            "own charm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "I'm sure the plains from the\x01",
            "Ahnenburg look beautiful.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_4216")

    Jump("loc_4657")

    label("loc_4219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_43C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_42B1")

    ChrTalk(    #216
        0xFE,
        (
            "Moving subjects like waterfalls are\x01",
            "hard to take a good picture of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "I wonder how the cameraman\x01",
            "with the Liberl News does it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C3")

    label("loc_42B1")


    ChrTalk(    #218
        0xFE,
        (
            "Moving subjects like waterfalls are\x01",
            "hard to take a good picture of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "I'm trying to capture that sense of liveliness,\x01",
            "but that's just ended up in a lot of really\x01",
            "muddy shots... \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "So when I tried to focus on, well, focusing,\x01",
            "I lost some of the sense of speed.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_43C3")

    Jump("loc_4657")

    label("loc_43C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_4533")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_443E")

    ChrTalk(    #221
        0xFE,
        "The Liberl News shots are great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "If I could take pictures like that,\x01",
            "I'd have no complaints.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4530")

    label("loc_443E")


    ChrTalk(    #223
        0xFE,
        "The Liberl News shots are great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "If I could take pictures like that,\x01",
            "I'd have no complaints.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "That reminds me, the Liberl News had some\x01",
            "shots of this guard post way back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        "All right, I'll take enough to not lose to that.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_4530")

    Jump("loc_4657")

    label("loc_4533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_4657")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_45AD")

    ChrTalk(    #227
        0xFE,
        "My dream's to become a photographer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "This historical site trip is part of\x01",
            "practicing for that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4657")

    label("loc_45AD")


    ChrTalk(    #229
        0xFE,
        (
            "An old friend of mine, Tico, and I are\x01",
            "traveling across historic sites.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "I'm gonna take a ton of shots of these famous\x01",
            "buildings and practice my camera work.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_4657")

    TalkEnd(0x13)
    Return()

    # Function_14_40AE end

    def Function_15_465B(): pass

    label("Function_15_465B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_480E")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4793")

    ChrTalk(    #231
        0xFE,
        (
            "We just received word about\x01",
            "the incident at the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "It seems like we've taken control back without\x01",
            "too much damage, so I'm thankful for that, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "There may be more uprisings taking\x01",
            "advantage of the chaos like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        "Let's both keep our guard up and be careful.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_4808")

    label("loc_4793")


    ChrTalk(    #235
        0xFE,
        (
            "There may be more uprisings like\x01",
            "the incident at the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        "Let's both keep our guard up and be careful.\x02",
    )

    CloseMessageWindow()

    label("loc_4808")

    TalkEnd(0x9)
    Jump("loc_5710")

    label("loc_480E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4A4E")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49BA")

    ChrTalk(    #237
        0xFE,
        (
            "Even though our communicators are back up,\x01",
            "we still lack information...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "Anyway, at the moment I'm acting to prioritize\x01",
            "enhancing the guard post's security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "After all, we're still in a situation\x01",
            "where we can't shut the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "The lights in the Kaldia Tunnel are out,\x01",
            "and currently it's completely pitch black.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "Stepping in carelessly could cost you your life.\x01",
            "Be extremely careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_4A48")

    label("loc_49BA")


    ChrTalk(    #242
        0xFE,
        (
            "Right now I'm acting to prioritize\x01",
            "the safety of the guard post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "Panicking or acting disorganized\x01",
            "would only disturb the citizenry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A48")

    TalkEnd(0x9)
    Jump("loc_5710")

    label("loc_4A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 2)), scpexpr(EXPR_END)), "loc_570C")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_4C78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4B84")

    ChrTalk(    #244
        0x9,
        (
            "I plan to enhance security at the guard post\x01",
            "in accordance with the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x9,
        (
            "We not only have that criminal organization to\x01",
            "worry about, but there's also the remaining\x01",
            "Intelligence Division forces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x9,
        (
            "I can see why the Royal Army's\x01",
            "top brass is getting nervous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C75")

    label("loc_4B84")


    ChrTalk(    #247
        0x9,
        (
            "It seems like the earthquakes have finally\x01",
            "settled down without major harm done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x9,
        (
            "There wasn't any major damage to the fortress,\x01",
            "it seems, so that's a relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x9,
        (
            "Now we can safely move on to preparing\x01",
            "for the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4C75")

    Jump("loc_5706")

    label("loc_4C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_4D9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4CF6")

    ChrTalk(    #250
        0x9,
        (
            "Apparently there was a strong earthquake\x01",
            "at Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x9,
        "Hopefully there wasn't any damage...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D9B")

    label("loc_4CF6")


    ChrTalk(    #252
        0x9,
        (
            "Apparently there was a strong earthquake\x01",
            "at Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x9,
        "We just got word from them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x9,
        (
            "I had a bad feeling, but for\x01",
            "it to actually come true...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4D9B")

    Jump("loc_5706")

    label("loc_4D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_4EED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4E26")

    ChrTalk(    #255
        0x9,
        (
            "Apparently there was an earthquake\x01",
            "even at the Sanktheim Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x9,
        "I don't know why, but I've got a bad feeling.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EEA")

    label("loc_4E26")


    ChrTalk(    #257
        0x9,
        (
            "Apparently there was an earthquake\x01",
            "even at the Sanktheim Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x9,
        (
            "After the Wolf Fort, this is the second\x01",
            "military structure affected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x9,
        "I don't know why, but I've got a bad feeling.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4EEA")

    Jump("loc_5706")

    label("loc_4EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_5077")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4FAF")

    ChrTalk(    #260
        0x9,
        (
            "The Royal Army is also investigating\x01",
            "into that criminal organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x9,
        (
            "However, the investigation is being done in\x01",
            "secret so as not to cause the citizenry any\x01",
            "anxiety.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4FAF")


    ChrTalk(    #262
        0x9,
        "Ohh, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x9,
        (
            "The Royal Army is also investigating\x01",
            "into that criminal organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x9,
        (
            "Though, ultimately, it's being kept pretty quiet\x01",
            "so as not to cause the citizenry any anxiety.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_5074")

    Jump("loc_5706")

    label("loc_5077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_51F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_511A")

    ChrTalk(    #265
        0xFE,
        "It seems that case has somehow been resolved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "I still have a lot of misgivings about the whole\x01",
            "thing, but for now let me say good work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51F2")

    label("loc_511A")

    OP_A2(0x0)

    ChrTalk(    #267
        0xFE,
        "Hey, it seems like you solved that case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        (
            "Still, to think a member of that criminal\x01",
            "organization was hiding in the royal\x01",
            "academy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "It's a surprise to think that 'ghost' sighting\x01",
            "would lead to this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51F2")

    Jump("loc_5706")

    label("loc_51F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_538D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5274")

    ChrTalk(    #270
        0xFE,
        "We're enhancing our cooperation with the guild.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        (
            "We hope you bracers will in turn cooperate\x01",
            "with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_538A")

    label("loc_5274")

    OP_A2(0x0)

    ChrTalk(    #272
        0xFE,
        (
            "Oh, you all. Are you making any progress into\x01",
            "the investigation of the ghost disturbance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "If we get anything on our side, we'll\x01",
            "contact the guild immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "In an investigation like this, cooperation and\x01",
            "coordination between the army and guild\x01",
            "are critical.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_538A")

    Jump("loc_5706")

    label("loc_538D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 3)), scpexpr(EXPR_END)), "loc_55D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5408")

    ChrTalk(    #275
        0xFE,
        "I was sure Nix was just daydreaming.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        (
            "Hmm, I guess I'll have to make\x01",
            "it up to him at some point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55D3")

    label("loc_5408")

    OP_A2(0x0)

    ChrTalk(    #277
        0xFE,
        "Do you have any new information?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x101,
        "#1000FYeah, it seems it's true that it appeared.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_54A2")

    ChrTalk(    #279
        0x106,
        "#050FWe still don't know what it is, though.\x02",
    )

    Jump("loc_54D7")

    label("loc_54A2")


    ChrTalk(    #280
        0x103,
        "#020FYes, though we still don't know what it is.\x02",
    )


    label("loc_54D7")

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        "I see... I guess I owe Nix an apology.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "Hmm, I guess I'll have to make\x01",
            "it up to him at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x101,
        (
            "#1000FWell, then, we'll continue our investigation.\x02\x03",

            "Thank you for your help, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "Sure thing. If you find out anything,\x01",
            "contact us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55D3")

    Jump("loc_5706")

    label("loc_55D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_5706")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_565E")

    ChrTalk(    #285
        0xFE,
        (
            "The entrance to the tunnel is\x01",
            "on the roof of the guard post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        "Climb up the stairs to the side of the counter.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5706")

    label("loc_565E")

    OP_A2(0x0)

    ChrTalk(    #287
        0xFE,
        (
            "The one who witnessed the white shadow\x01",
            "was a soldier named Nix.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        (
            "He's on watch near the entrance to the Kaldia\x01",
            "Tunnel, so you should talk to him in person.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5706")

    TalkEnd(0x9)
    Jump("loc_5710")

    label("loc_570C")

    Call(0, 19)

    label("loc_5710")

    Return()

    # Function_15_465B end

    def Function_16_5711(): pass

    label("Function_16_5711")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_574C")

    ChrTalk(    #289
        0xA,
        "#260FIf we meet again, let's play, okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_577D")

    label("loc_574C")

    OP_A2(0x9)

    ChrTalk(    #290
        0xA,
        "#260FIf we meet again, let's play, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_577D")

    TalkEnd(0xA)
    Return()

    # Function_16_5711 end

    def Function_17_5781(): pass

    label("Function_17_5781")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_57EF")

    ChrTalk(    #291
        0xB,
        (
            "#1363FThis is my chance to do something for my family.\x02\x03",

            "After all, I'm always away on work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_587B")

    label("loc_57EF")

    OP_8C(0xFE, 180, 0)
    OP_4A(0xE, 255)
    OP_A2(0xA)
    OP_A2(0x2)

    ChrTalk(    #292
        0xE,
        (
            "The three of you will be staying for\x01",
            "one night, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xB,
        "#1360FYes, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xE,
        "Well, then, please sign here...\x02",
    )

    CloseMessageWindow()
    OP_4B(0xE, 255)

    label("loc_587B")

    TalkEnd(0xB)
    Return()

    # Function_17_5781 end

    def Function_18_587F(): pass

    label("Function_18_587F")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_58C2")

    ChrTalk(    #295
        0xC,
        "#1372FIt'll be over soon, so be patient, please.\x02",
    )

    CloseMessageWindow()
    Jump("loc_58E8")

    label("loc_58C2")

    OP_A2(0xB)

    ChrTalk(    #296
        0xC,
        "#1372FNow, Renne. Stay still.\x02",
    )

    CloseMessageWindow()

    label("loc_58E8")

    TalkEnd(0xC)
    Return()

    # Function_18_587F end

    def Function_19_58EC(): pass

    label("Function_19_58EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5906")
    Call(0, 24)
    FadeToBright(0, 0)

    label("loc_5906")

    EventBegin(0x0)
    OP_4A(0x9, 255)
    Fade(1000)
    SetChrPos(0x101, 2980, 0, 91080, 90)
    SetChrPos(0xF7, 2410, 0, 90010, 90)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    ChrTalk(    #297
        0x101,
        (
            "#1011F#6PUm, 'scuse me!\x01",
            "We're from the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A71")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set 'Convinced the duke' event in FC as not cleared\x01",      # 0
            "Set 'Convinced the duke' event in FC as cleared\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5A58"),
        (1, "loc_5A60"),
        (SWITCH_DEFAULT, "loc_5A68"),
    )


    label("loc_5A58")

    OP_28(0x23, 0x3, 0x10)
    Jump("loc_5A68")

    label("loc_5A60")

    OP_28(0x23, 0x4, 0x10)
    Jump("loc_5A68")

    label("loc_5A68")

    FadeToBright(300, 0)

    label("loc_5A71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5BAE")

    ChrTalk(    #298
        0x9,
        "Hey, welcome.\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #299
        0x9,
        (
            "Hmm? Wait a minute! You're that\x01",
            "bracer who dealt with the duke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x101,
        (
            "#1016F#6PHaha! Yeah, that's me. I'm surprised you\x01",
            "even remember that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x9,
        (
            "Of course! Things wouldn't have gone half\x01",
            "as smoothly without you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x9,
        "Well, what can we do for you today?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C0D")

    label("loc_5BAE")

    SetChrName("CWO Hahn")

    ChrTalk(    #303
        0x9,
        "Ah, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x9,
        (
            "Don't think I've seen you around here.\x01",
            "What can I do for you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C0D")


    ChrTalk(    #305
        0x101,
        (
            "#1002F#6PWell, sir, we're here about a soldier who\x01",
            "claims to have seen a 'white shadow'...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x9,
        (
            "What, even the guild's heard about that?\x01",
            "For the love of...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x9,
        (
            "This is ridiculous. He should be ashamed.\x01",
            "Honestly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x101,
        "#1004F#6PAshamed? What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x9,
        (
            "There wasn't any ghost. He was\x01",
            "just daydreaming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x9,
        (
            "And drifting off the way he did could\x01",
            "be disastrous if there was an actual\x01",
            "emergency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x9,
        (
            "As his commanding officer, his\x01",
            "actions are wholly my responsibility.\x01",
            "How embarrassing...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5E98")

    ChrTalk(    #312
        0x106,
        (
            "#053FI think you're getting a bit ahead\x01",
            "of yourself, sir.\x02\x03",

            "#050FThat thing, whatever it is, has apparently\x01",
            "been seen all over the region.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F40")

    label("loc_5E98")


    ChrTalk(    #313
        0x103,
        (
            "#020FAh, sir, I'm afraid you may be jumping\x01",
            "to conclusions a bit hastily.\x02\x03",

            "You see, there've been multiple sightings\x01",
            "of this 'white shadow' all over the province.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F40")


    ChrTalk(    #314
        0x9,
        "What? Are you...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #315
        (
            "\x07\x05Estelle and company explained the investigation to\x01",
            "Chief Warrant Officer Hahn.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #316
        0x9,
        (
            "I... I see. Goodness...\x01",
            "I'd thought he was simply half asleep, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x9,
        (
            "Perhaps I did jump to conclusions\x01",
            "too quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x9,
        (
            "I've been far too hard on Nix,\x01",
            "in that case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x101,
        "#1011F#6PSo Nix is the one who saw the white shadow?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x9,
        "That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x9,
        (
            "He's currently on duty at the entrance to\x01",
            "the Kaldia Tunnel. You should go speak\x01",
            "to him directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x9,
        (
            "Tell him he has my permission\x01",
            "to speak to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x101,
        "#1006F#6PThank you, sir!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)
    OP_4B(0x9, 255)
    OP_A2(0x1212)
    OP_28(0x82, 0x2, 0x2)
    OP_28(0x82, 0x1, 0x4)
    EventEnd(0x0)
    Return()

    # Function_19_58EC end

    def Function_20_61A9(): pass

    label("Function_20_61A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_61BA")
    Call(0, 24)

    label("loc_61BA")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(-8390, 1000, 6270, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xA, -3410, 0, 19050, 270)
    SetChrPos(0xB, -1990, 0, 20610, 225)
    SetChrPos(0xC, -1260, 0, 19050, 270)
    OP_8C(0x0, 90, 0)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    SetChrPos(0x101, -7600, 3000, 8050, 149)
    SetChrPos(0xF7, -8180, 3000, 8050, 180)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF7, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_43(0x101, 0x0, 0x0, 0x16)
    Sleep(600)
    OP_43(0xF7, 0x0, 0x0, 0x17)

    def lambda_62A4():
        OP_6D(-3350, 0, 5190, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_62A4)

    def lambda_62BC():
        OP_67(0, 8000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_62BC)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)

    NpcTalk(    #324
        0xA,
        "Girl's Voice",
        "#6PWooooow! Incredible!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #325
        0xA,
        "Girl's Voice",
        "#6PPapa, Mama, c'mere!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xF7, 0x0)

    def lambda_633B():
        OP_6D(-2740, 0, 19390, 3000)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_633B)

    def lambda_6353():
        OP_67(0, 4890, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6353)

    def lambda_636B():
        OP_6B(3330, 2000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_636B)

    def lambda_637B():
        OP_6E(262, 2000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_637B)
    TurnDirection(0x101, 0xA, 400)
    TurnDirection(0xF7, 0xA, 400)
    WaitChrThread(0xB, 0x1)

    def lambda_639E():
        TurnDirection(0xB, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_639E)
    WaitChrThread(0xC, 0x1)

    def lambda_63B1():
        TurnDirection(0xC, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_63B1)
    WaitChrThread(0xC, 0x1)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0xA, 0x2)
    WaitChrThread(0xA, 0x3)

    NpcTalk(    #326
        0xB,
        "Man",
        "#1363F#4PNow, now, slow down or you'll trip, pumpkin.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #327
        0xC,
        "Woman",
        "#1371F#6PIt really is lovely.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 400)
    Sleep(300)

    NpcTalk(    #328
        0xC,
        "Woman",
        (
            "#1372F#6PI'm glad we could come with you,\x01",
            "my love. Thank you.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)
    Sleep(300)

    NpcTalk(    #329
        0xB,
        "Man",
        (
            "#1361F#4PNo, I've always left you two alone\x01",
            "back home.\x02\x03",

            "This is the least I can do for my\x01",
            "family.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, -2060, 0, 7000, 0)
    SetChrPos(0xF7, -850, 0, 5500, 0)

    def lambda_652E():
        OP_6D(-2390, 0, 14690, 1800)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_652E)

    def lambda_6546():
        OP_67(0, 4890, -10000, 1800)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6546)
    Sleep(1000)

    def lambda_6563():
        OP_8E(0x101, 0xFFFFF858, 0x0, 0x23BE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6563)

    def lambda_657E():
        OP_8E(0xF7, 0xFFFFFE84, 0x0, 0x20F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_657E)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF7, 0x1)
    TurnDirection(0x101, 0xA, 0)
    TurnDirection(0xF7, 0xA, 0)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #330
        0x101,
        (
            "#1017F#1P(Aww, that's a really sweet family.)\x02\x03",

            "(Looks like they're on vacation or something?)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_666B")

    ChrTalk(    #331
        0x106,
        (
            "#051F#5P(Looks like, yeah.)\x02\x03",

            "(Think they might even be foreigners.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66C5")

    label("loc_666B")


    ChrTalk(    #332
        0x103,
        (
            "#021F#5P(Most likely, yes.)\x02\x03",

            "#020F(They may even be foreigners,\x01",
            "given where we are.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66C5")

    OP_A2(0x1214)

    NpcTalk(    #333
        0xA,
        "Girl",
        (
            "#261F#8PIt's so amazing!\x02\x03",

            "Just looking at it, I feel like it's\x01",
            "gonna swallow me whole!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xA, 0x101, 400)

    NpcTalk(    #334
        0xA,
        "Girl",
        (
            "#265F#4PExcuse me, miss!\x02\x03",

            "Do you know the name of this waterfall?\x02\x03",

            "Where does all this water come from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x101,
        "#1016F#5PAh, that's a little out of the blue. Umm...\x02",
    )

    CloseMessageWindow()

    def lambda_67FE():
        OP_6D(-3310, 0, 18760, 2000)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_67FE)

    def lambda_6816():
        OP_67(0, 4890, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6816)

    def lambda_682E():
        OP_8E(0x101, 0xFFFFF506, 0x0, 0x4286, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_682E)

    def lambda_6849():
        TurnDirection(0xB, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6849)
    TurnDirection(0xC, 0x101, 400)

    def lambda_685E():
        OP_8E(0xF7, 0xFFFFFC22, 0x0, 0x3E58, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_685E)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF7, 0x1)
    OP_44(0xB, 0x0)
    OP_44(0xB, 0x1)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #336
        0x101,
        (
            "#1006FWell, the waterfall is called Air-Letten.\x02\x03",

            "The water flows here from Valleria Lake,\x01",
            "through an ancient waterway.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #337
        0xA,
        "Girl",
        (
            "#265F#4POh, I know what Valleria Lake is!\x02\x03",

            "It's the big lake we saw before\x01",
            "the airship landed, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x101,
        (
            "#1004FYes, that's right, but...airship?\x01",
            "Are you from another country?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #339
        0xA,
        "Girl",
        (
            "#264F#4PYup! That's right.\x02\x03",

            "#263FI'm from far, faaar away.\x01",
            "By the way, my name's Renne!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x101,
        (
            "#1001FRenne, huh?\x02\x03",

            "That's a really cute name!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xA,
        (
            "#261F#4PHeehee, I know.\x02\x03",

            "Papa and Mama gave it to me.\x01",
            "Of course it'd be cute!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xA, 400)
    Sleep(300)

    ChrTalk(    #342
        0xC,
        "#1372F#4PRenne, don't bother the nice lady too much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xB,
        (
            "#1363FHaha! Our apologies if our Renne\x01",
            "is troubling you too much, miss.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xC, 400)

    ChrTalk(    #344
        0xA,
        "#262F#6PAwww, I wasn't doing anything bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x101,
        "#1016F#6PNo, no, it's no trouble.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6C02")

    ChrTalk(    #346
        0x106,
        (
            "#051F#1PHope you don't mind me prying,\x01",
            "but what brings you to Liberl, folks?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C34")

    label("loc_6C02")


    ChrTalk(    #347
        0x103,
        "#020F#1PIf I may, what brings you to Liberl?\x02",
    )

    CloseMessageWindow()

    label("loc_6C34")

    TurnDirection(0xC, 0xF7, 400)

    ChrTalk(    #348
        0xB,
        (
            "#1361FWell, I often come to Liberl for business.\x02\x03",

            "Every time I do, I'm struck by the beauty\x01",
            "of this country. So...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xC,
        (
            "#1370F#4PSo this time, he brought myself and\x01",
            "our daughter along.\x02\x03",

            "#1371FMiracles do happen, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x101,
        (
            "#1017F#6PHeh... You guys are, like, the most\x01",
            "picture-perfect family, you know?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #351
        0xA,
        (
            "#261F#4PHeheh! Jealous?\x02\x03",

            "#265FPapa's away a lot, but he aaalways\x01",
            "brings us lots of presents when he\x01",
            "comes home.\x02\x03",

            "And Mama's always full of smiles\x01",
            "and makes the best food!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x101,
        "#1008F#6PReally? I AM kinda jealous now, actually.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xB,
        "#1363FAhaha, goodness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0xC,
        "#1372F#4PI'm sorry... She's still very much a child.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xA,
        (
            "#260F#4PHey, what's yours, miss?\x02\x03",

            "What's your name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x101,
        (
            "#1006F#6POh, yeah, sorry. I haven't introduced myself!\x02\x03",

            "I'm Estelle! Estelle Bright.\x02\x03",

            "#1015FI'm a bracer. ...Er, wait, do you know\x01",
            "what a bracer is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0xA,
        (
            "#266F#4PHey, I'm not stupid! I'm a big girl.\x02\x03",

            "#265FBut that's neat! You're a bracer, huh?\x02\x03",

            "Do you slay lots of scaaary monsters?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x101,
        "#1006F#6PYep, that's part of the job sometimes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0xB,
        "#1362FA bracer? That's very impressive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xC,
        "#1371F#4PYes, especially at your age.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x101,
        "#1016F#6PHaha... I'm still pretty new at it, though.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7172")

    ChrTalk(    #362
        0x106,
        (
            "#051F#1PThere're guild branches in every major\x01",
            "city in Liberl.\x02\x03",

            "If you folks encounter any trouble during\x01",
            "your trip, you can count on us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7214")

    label("loc_7172")


    ChrTalk(    #363
        0x103,
        (
            "#020F#1PEach of Liberl's five major cities has\x01",
            "a guild branch.\x02\x03",

            "If you encounter trouble during your\x01",
            "travels, please do not hesitate to come\x01",
            "to us for help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7214")


    ChrTalk(    #364
        0xB,
        (
            "#1361FThank you! We'll keep that in mind.\x02\x03",

            "#1360FIf you'll pardon us, though, we need\x01",
            "to check into the inn.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xA, 400)

    ChrTalk(    #365
        0xC,
        "#1370F#4PCome along now, Renne.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xC, 400)

    ChrTalk(    #366
        0xA,
        "#262F#6PAww, I wanna talk to Miss Estelle more.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(300)

    ChrTalk(    #367
        0xA,
        (
            "#265F#4PHey, Miss Estelle! Will you play\x01",
            "with me next time we meet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x101,
        "#1006F#3PSure!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xA,
        (
            "#261F#4PHeehee, yay!\x02\x03",

            "#265FSee you, Miss Estelle!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7394():

        label("loc_7394")

        TurnDirection(0x101, 0xA, 0)
        OP_48()
        Jump("loc_7394")

    QueueWorkItem2(0x101, 1, lambda_7394)

    def lambda_73A5():

        label("loc_73A5")

        TurnDirection(0xF7, 0xB, 0)
        OP_48()
        Jump("loc_73A5")

    QueueWorkItem2(0xF7, 1, lambda_73A5)
    OP_43(0xB, 0x1, 0x0, 0x15)
    Sleep(1000)

    def lambda_73C2():
        OP_6D(-1800, 0, 18780, 2000)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_73C2)

    def lambda_73DA():
        OP_67(0, 4890, -10000, 200)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_73DA)
    OP_43(0xC, 0x1, 0x0, 0x15)
    Sleep(500)
    OP_43(0xA, 0x1, 0x0, 0x15)
    Sleep(200)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0xA, 0x2)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74AE")
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set 'Heard Orphanage Children's Testimony' to done\x01",      # 0
            "No Change\x01",                                               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74A5")
    OP_A2(0x121A)

    label("loc_74A5")

    FadeToBright(300, 0)

    label("loc_74AE")

    OP_69(0x101, 0x3E8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_76D5")

    ChrTalk(    #370
        0x106,
        (
            "#051F#6PPretty energetic little sprout, huh?\x02\x03",

            "A bit younger than Tita, even, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x101,
        (
            "#1017F#3PYeah, she might be.\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)
    Sleep(400)

    ChrTalk(    #372
        0x106,
        "#050F#6PWhat? They remind you of your old man?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Sleep(400)

    ChrTalk(    #373
        0x101,
        (
            "#1016F#3PHaha... Just a bit, yeah.\x02\x03",

            "#1025FI was thinking about how I was around\x01",
            "her age when Joshua and I first met.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_767C")
    OP_28(0x82, 0x1, 0x400)

    ChrTalk(    #374
        0x106,
        (
            "#053F#6PAh, I see...\x02\x03",

            "#051FAnyway, we've shaken down all our\x01",
            "witnesses. Shall we get back to Jean?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76D2")

    label("loc_767C")


    ChrTalk(    #375
        0x106,
        (
            "#053F#6PAh, I see...\x02\x03",

            "#051FC'mon, we have some more witnesses\x01",
            "to hit up, y'know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76D2")

    Jump("loc_7934")

    label("loc_76D5")


    ChrTalk(    #376
        0x103,
        (
            "#021F#6PWell, she was certainly a bundle of energy.\x02\x03",

            "I think she might've been a bit younger than\x01",
            "Tita, even.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x101,
        (
            "#1017F#3PYeah, she might be.\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    Sleep(400)

    ChrTalk(    #378
        0x103,
        (
            "#027F#6PDoes she remind you of a certain\x01",
            "someone and HER father?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(400)

    ChrTalk(    #379
        0x101,
        (
            "#1016F#3PHaha... Just a bit, yeah.\x02\x03",

            "#1025FI was thinking about how I was around\x01",
            "her age when Joshua and I first met.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_78C2")
    OP_28(0x82, 0x1, 0x400)

    ChrTalk(    #380
        0x103,
        (
            "#026F#6PAh... Yes, that's right.\x02\x03",

            "#020FRegardless, that's all the witnesses.\x01",
            "Shall we return to Ruan?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7934")

    label("loc_78C2")


    ChrTalk(    #381
        0x103,
        (
            "#026F#6PAh... Yes, that's right.\x02\x03",

            "#020FRegardless, we still have witnesses\x01",
            "to speak to, so shall we move on?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7934")


    ChrTalk(    #382
        0x101,
        "#1006F#3PSure!\x02",
    )

    CloseMessageWindow()
    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    OP_4B(0xC, 255)
    OP_A2(0x1215)
    EventEnd(0x0)
    Return()

    # Function_20_61A9 end

    def Function_21_795A(): pass

    label("Function_21_795A")

    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0xA46, 0x0, 0x51F4, 0x7D0, 0x0)

    def lambda_797B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_797B)
    OP_8E(0xFE, 0xDC0, 0x0, 0x523A, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_21_795A end

    def Function_22_79A1(): pass

    label("Function_22_79A1")


    def lambda_79A7():
        OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_79A7)
    OP_8E(0x101, 0xFFFFE296, 0x3E8, 0x137E, 0x7D0, 0x0)
    OP_8E(0x101, 0xFFFFF326, 0x0, 0x13A6, 0x7D0, 0x0)
    Return()

    # Function_22_79A1 end

    def Function_23_79DC(): pass

    label("Function_23_79DC")


    def lambda_79E2():
        OP_9F(0xF7, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_79E2)
    OP_8E(0xF7, 0xFFFFE14C, 0x3E8, 0x10EA, 0x7D0, 0x0)
    OP_8E(0xF7, 0xFFFFF11E, 0x0, 0xECE, 0x7D0, 0x0)
    Return()

    # Function_23_79DC end

    def Function_24_7A17(): pass

    label("Function_24_7A17")

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
        (0, "loc_7A90"),
        (1, "loc_7A96"),
        (SWITCH_DEFAULT, "loc_7A9C"),
    )


    label("loc_7A90")

    OP_A2(0x1200)
    Jump("loc_7A9C")

    label("loc_7A96")

    OP_A2(0x1201)
    Jump("loc_7A9C")

    label("loc_7A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_7AAA")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_7AAE")

    label("loc_7AAA")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_7AAE")

    Return()

    # Function_24_7A17 end

    def Function_25_7AAF(): pass

    label("Function_25_7AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BF5")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7B40")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7ADA")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_7AE1")

    label("loc_7ADA")

    TurnDirection(0x106, 0x0, 400)

    label("loc_7AE1")


    ChrTalk(    #383
        0x106,
        (
            "#050FThis way's to Ruan.\x02\x03",

            "We ain't got time to go to other regions.\x01",
            "Let's turn around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BDA")

    label("loc_7B40")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B56")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_7B5D")

    label("loc_7B56")

    TurnDirection(0x103, 0x0, 400)

    label("loc_7B5D")


    ChrTalk(    #384
        0x103,
        (
            "#020FOnce we get through here, it's the Ruan region.\x02\x03",

            "We don't have time to waste in other regions.\x01",
            "Let's just go back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BDA")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_7BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F6A")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_7C9E")

    ChrTalk(    #385
        0x108,
        (
            "#070FWalking is good training, but\x01",
            "it's also a waste of time.\x02\x03",

            "If we're headed to the capital,\x01",
            "it'd be wiser to use an airship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D40")

    label("loc_7C9E")


    ChrTalk(    #386
        0x108,
        (
            "#070FThis way is Ruan, right?\x02\x03",

            "Walking is good training, but\x01",
            "it's also a waste of time.\x02\x03",

            "If we're headed to the capital,\x01",
            "it'd be wiser to use an airship.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_7D40")

    Jump("loc_7F4F")

    label("loc_7D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7E43")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D60")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_7D67")

    label("loc_7D60")

    TurnDirection(0x106, 0x0, 400)

    label("loc_7D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_7DDB")

    ChrTalk(    #387
        0x106,
        (
            "#053FWalking is a waste of time.\x02\x03",

            "#050FIf we're headed to the capital,\x01",
            "let's go to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E40")

    label("loc_7DDB")


    ChrTalk(    #388
        0x106,
        (
            "#050FThis is the Ruan region.\x02\x03",

            "If we're headed to the capital,\x01",
            "let's go to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_7E40")

    Jump("loc_7F4F")

    label("loc_7E43")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E59")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_7E60")

    label("loc_7E59")

    TurnDirection(0x103, 0x0, 400)

    label("loc_7E60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_7EE4")

    ChrTalk(    #389
        0x103,
        (
            "#026FWalking is, frankly, a waste of time.\x02\x03",

            "#020FIf we're headed to the capital,\x01",
            "let's make use of the landing port.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F4F")

    label("loc_7EE4")


    ChrTalk(    #390
        0x103,
        (
            "#020FThis is the Ruan region.\x02\x03",

            "If we're headed to the capital,\x01",
            "let's make use of the landing port.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_7F4F")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_7F6A")

    Return()

    # Function_25_7AAF end

    def Function_26_7F6B(): pass

    label("Function_26_7F6B")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_26_7F6B end

    SaveToFile()

Try(main)
