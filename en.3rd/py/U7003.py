from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U7003   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7003.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60210",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            'ED6_DT21/U7003_6 ._SN',
            'ED6_DT21/U7003_4 ._SN',
            'ED6_DT21/U7003_5 ._SN',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Kevin',                                # 9
        'Ries',                                 # 10
        'Tita',                                 # 11
        'Julia',                                # 12
        'Mueller',                              # 13
        'Josette',                              # 14
        'Joshua',                               # 15
        'Kloe',                                 # 16
        'Sieg',                                 # 17
        'Olivier',                              # 18
        'Zin',                                  # 19
        'Anelace',                              # 20
        'Scherazard',                           # 21
        'Agate',                                # 22
        'Estelle',                              # 23
        'Richard',                              # 24
        'Renne',                                # 25
        'Anelace',                              # 26
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT26/CH20625 ._CH',             # 00
        'ED6_DT27/CH03080 ._CH',             # 01
        'ED6_DT27/CH03150 ._CH',             # 02
        'ED6_DT07/CH00060 ._CH',             # 03
        'ED6_DT27/CH03580 ._CH',             # 04
        'ED6_DT27/CH03570 ._CH',             # 05
        'ED6_DT27/CH03100 ._CH',             # 06
        'ED6_DT27/CH03250 ._CH',             # 07
        'ED6_DT27/CH03210 ._CH',             # 08
        'ED6_DT07/CH02323 ._CH',             # 09
        'ED6_DT27/CH03260 ._CH',             # 0A
        'ED6_DT07/CH00070 ._CH',             # 0B
        'ED6_DT07/CH01630 ._CH',             # 0C
        'ED6_DT27/CH03240 ._CH',             # 0D
        'ED6_DT06/CH20053 ._CH',             # 0E
        'ED6_DT26/CH20255 ._CH',             # 0F
        'ED6_DT07/CH02030 ._CH',             # 10
        'ED6_DT27/CH03510 ._CH',             # 11
        'ED6_DT27/CH03263 ._CH',             # 12
        'ED6_DT27/CH03573 ._CH',             # 13
        'ED6_DT27/CH03213 ._CH',             # 14
        'ED6_DT27/CH03264 ._CH',             # 15
        'ED6_DT27/CH03513 ._CH',             # 16
        'ED6_DT26/CH20607 ._CH',             # 17
        'ED6_DT27/CH03153 ._CH',             # 18
        'ED6_DT07/CH00063 ._CH',             # 19
        'ED6_DT27/CH03470 ._CH',             # 1A
        'ED6_DT27/CH03473 ._CH',             # 1B
        'ED6_DT07/CH00073 ._CH',             # 1C
        'ED6_DT07/CH00053 ._CH',             # 1D
        'ED6_DT26/CH20822 ._CH',             # 1E
        'ED6_DT27/CH03000 ._CH',             # 1F
        'ED6_DT27/CH03001 ._CH',             # 20
        'ED6_DT26/CH20822 ._CH',             # 21
        'ED6_DT07/CH02093 ._CH',             # 22
    )

    AddCharChipPat(
        'ED6_DT26/CH20625P._CP',             # 00
        'ED6_DT27/CH03080P._CP',             # 01
        'ED6_DT27/CH03150P._CP',             # 02
        'ED6_DT07/CH00060P._CP',             # 03
        'ED6_DT27/CH03580P._CP',             # 04
        'ED6_DT27/CH03570P._CP',             # 05
        'ED6_DT27/CH03100P._CP',             # 06
        'ED6_DT27/CH03250P._CP',             # 07
        'ED6_DT27/CH03210P._CP',             # 08
        'ED6_DT07/CH02323P._CP',             # 09
        'ED6_DT27/CH03260P._CP',             # 0A
        'ED6_DT07/CH00070P._CP',             # 0B
        'ED6_DT07/CH01630P._CP',             # 0C
        'ED6_DT27/CH03240P._CP',             # 0D
        'ED6_DT06/CH20053P._CP',             # 0E
        'ED6_DT26/CH20255P._CP',             # 0F
        'ED6_DT07/CH02030P._CP',             # 10
        'ED6_DT27/CH03510P._CP',             # 11
        'ED6_DT27/CH03263P._CP',             # 12
        'ED6_DT27/CH03573P._CP',             # 13
        'ED6_DT27/CH03213P._CP',             # 14
        'ED6_DT27/CH03264P._CP',             # 15
        'ED6_DT27/CH03513P._CP',             # 16
        'ED6_DT26/CH20607P._CP',             # 17
        'ED6_DT27/CH03153P._CP',             # 18
        'ED6_DT07/CH00063P._CP',             # 19
        'ED6_DT27/CH03470P._CP',             # 1A
        'ED6_DT27/CH03473P._CP',             # 1B
        'ED6_DT07/CH00073P._CP',             # 1C
        'ED6_DT07/CH00053P._CP',             # 1D
        'ED6_DT26/CH20822P._CP',             # 1E
        'ED6_DT27/CH03000P._CP',             # 1F
        'ED6_DT27/CH03001P._CP',             # 20
        'ED6_DT26/CH20822P._CP',             # 21
        'ED6_DT07/CH02093P._CP',             # 22
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 15,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 5,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 4,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 18,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 4,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 3,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 4930,
        Y                   = 0,
        Z                   = -3270,
        Range               = 4000,
        Unknown_10          = 0x3E80,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 26,
    )

    DeclEvent(
        X                   = 48310,
        Y                   = 0,
        Z                   = -46340,
        Range               = 4000,
        Unknown_10          = 0x2710,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = 0,
        Y                   = 0,
        Z                   = 0,
        Range               = 0,
        Unknown_10          = 0x0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x2,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = 83340,
        Y                   = -15000,
        Z                   = -48360,
        Range               = 85140,
        Unknown_10          = 0xFFFFD508,
        Unknown_14          = 0xFFFF2522,
        Unknown_18          = 0x0,
        Unknown_1C          = 20,
    )

    DeclEvent(
        X                   = 85340,
        Y                   = -15000,
        Z                   = -48360,
        Range               = 87140,
        Unknown_10          = 0xFFFFD508,
        Unknown_14          = 0xFFFF2522,
        Unknown_18          = 0x0,
        Unknown_1C          = 21,
    )


    DeclActor(
        TriggerX            = 54440,
        TriggerZ            = 1800,
        TriggerY            = -47860,
        TriggerRange        = 1000,
        ActorX              = 54440,
        ActorZ              = 3000,
        ActorY              = -47860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 52420,
        TriggerZ            = 2000,
        TriggerY            = -48240,
        TriggerRange        = 1500,
        ActorX              = 52420,
        ActorZ              = 2500,
        ActorY              = -48240,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 59580,
        TriggerZ            = 1000,
        TriggerY            = -41040,
        TriggerRange        = 1500,
        ActorX              = 57260,
        ActorZ              = 2500,
        ActorY              = -41880,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 63660,
        TriggerZ            = -11000,
        TriggerY            = -56430,
        TriggerRange        = 1800,
        ActorX              = 63660,
        ActorZ              = -10000,
        ActorY              = -56430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 64129,
        TriggerZ            = -11000,
        TriggerY            = -49610,
        TriggerRange        = 1800,
        ActorX              = 64129,
        ActorZ              = -10000,
        ActorY              = -49610,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_556",          # 00, 0
        "Function_1_5E3",          # 01, 1
        "Function_2_7CF",          # 02, 2
        "Function_3_DF1",          # 03, 3
        "Function_4_E35",          # 04, 4
        "Function_5_E6A",          # 05, 5
        "Function_6_10C8",         # 06, 6
        "Function_7_1D9A",         # 07, 7
        "Function_8_1E47",         # 08, 8
        "Function_9_1F13",         # 09, 9
        "Function_10_2F17",        # 0A, 10
        "Function_11_2F68",        # 0B, 11
        "Function_12_347C",        # 0C, 12
        "Function_13_34AD",        # 0D, 13
        "Function_14_3560",        # 0E, 14
        "Function_15_35A4",        # 0F, 15
        "Function_16_3601",        # 10, 16
        "Function_17_3606",        # 11, 17
        "Function_18_360B",        # 12, 18
        "Function_19_364B",        # 13, 19
        "Function_20_366F",        # 14, 20
        "Function_21_369E",        # 15, 21
        "Function_22_36CD",        # 16, 22
        "Function_23_40F1",        # 17, 23
        "Function_24_4173",        # 18, 24
        "Function_25_4323",        # 19, 25
        "Function_26_450E",        # 1A, 26
        "Function_27_454E",        # 1B, 27
    )


    def Function_0_556(): pass

    label("Function_0_556")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BE")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_56E"),
        (SWITCH_DEFAULT, "loc_5BE"),
    )


    label("loc_56E")

    SetChrPos(0x0, 16880, 1000, -14940, 135)
    SetChrPos(0x1, 16880, 1000, -14940, 135)
    SetChrPos(0x2, 16880, 1000, -14940, 135)
    SetChrPos(0x3, 16880, 1000, -14940, 135)
    OP_30(0x1)
    OP_69(0x0, 0x0)
    Jump("loc_5BE")

    label("loc_5BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_5DA")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)

    label("loc_5DA")

    Call(0, 11)
    Call(0, 9)
    Return()

    # Function_0_556 end

    def Function_1_5E3(): pass

    label("Function_1_5E3")

    OP_16(0x2, 0xFA0, 0xFFFE2082, 0xFFFD8D0C, 0x23007B)
    OP_10(0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_60D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_60D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62B")
    OP_65(0x1, 0x1)
    Jump("loc_62F")

    label("loc_62B")

    OP_64(0x1, 0x1)

    label("loc_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64D")
    OP_65(0x2, 0x1)
    Jump("loc_651")

    label("loc_64D")

    OP_64(0x2, 0x1)

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 7)), scpexpr(EXPR_END)), "loc_6AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A8")
    LoadEffect(0x1, "map\\mp257_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, 63660, -10000, -56430, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_6A8")

    Jump("loc_71B")

    label("loc_6AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x501, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_707")
    LoadEffect(0x1, "map\\mp257_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, 63660, -10000, -56430, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_707")

    Jump("loc_71B")

    label("loc_70A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71B")
    OP_64(0x3, 0x1)

    label("loc_71B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_777")
    LoadEffect(0x1, "map\\mp257_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, 64129, -10000, -49610, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_777")

    Jump("loc_786")

    label("loc_77A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_786")
    OP_64(0x4, 0x1)

    label("loc_786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C1")
    OP_64(0x0, 0x1)
    OP_E5(0x1, 0xFF, 0x10, 262144)
    OP_E5(0x1, 0xFF, 0x11, 262144)
    OP_E5(0x1, 0xFF, 0x12, 262144)
    OP_E5(0x1, 0xFF, 0x13, 262144)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)

    label("loc_7C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 0)), scpexpr(EXPR_END)), "loc_7CE")
    OP_C4(0x0, 0x200)

    label("loc_7CE")

    Return()

    # Function_1_5E3 end

    def Function_2_7CF(): pass

    label("Function_2_7CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 4)), scpexpr(EXPR_END)), "loc_7D7")
    Return()

    label("loc_7D7")

    EventBegin(0x0)
    OP_8C(0x0, 135, 400)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    SetChrPos(0x109, 39490, 1000, -38490, 135)
    SetChrPos(0x10F, 39420, 1000, -37080, 135)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(54910, 6000, -43800, 0)
    OP_67(0, 10110, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(20000, 0)
    OP_6E(463, 0)
    OP_43(0x109, 0x0, 0x0, 0x3)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    OP_0D()
    Sleep(1000)

    def lambda_88E():
        OP_6D(53620, 4350, -46260, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_88E)

    def lambda_8A6():
        OP_67(0, 5190, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8A6)

    def lambda_8BE():
        OP_6B(3030, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_8BE)

    def lambda_8CE():
        OP_6C(8000, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_8CE)

    def lambda_8DE():
        OP_6E(432, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_8DE)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(300)

    ChrTalk(    #0
        0x109,
        (
            "#1079F#5PWhat's a huge tree doing here?\x02\x03",

            "#1067FThere's no sign of any others in the surrounding\x01",
            "area, either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10F,
        (
            "#1443F#5P...\x02\x03",

            "#1445FAs big as it is, it doesn't seem to be a fruit tree.\x01",
            "Unfortunately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        "#1840F#5PHeh. Figures we wouldn't get that lucky.\x02",
    )

    CloseMessageWindow()

    def lambda_A0B():
        OP_6D(50190, 1000, -47300, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A0B)

    def lambda_A23():
        OP_67(0, 5190, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A23)

    def lambda_A3B():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A3B)

    def lambda_A4B():
        OP_6C(8000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_A4B)

    def lambda_A5B():
        OP_6E(406, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_A5B)
    Sleep(1000)
    OP_8C(0x109, 315, 400)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #3
        0x109,
        (
            "#1063F#6PCome to think of it, though, you were always an\x01",
            "expert on plants and medicinal herbs and stuff,\x01",
            "right?\x02\x03",

            "You don't recognize what kind of tree this is?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 135, 400)
    Sleep(300)

    ChrTalk(    #4
        0x10F,
        (
            "#1446F#5P...I wish I did, but no.\x02\x03",

            "#1802FAt the very least, it isn't one that grows on the\x01",
            "western side of the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x109,
        "#1067F#6PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10F,
        (
            "#1440F#5P...?\x02\x03",

            "Did you work something out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        (
            "#1065F#6PMaybe. Maybe not.\x02\x03",

            "#1060FWe should try looking somewhere else now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10F,
        (
            "#1444F#5POh... Right.\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 45, 400)
    Sleep(500)

    ChrTalk(    #9
        0x10F,
        (
            "#1446F#5PStill, even if it doesn't bear fruit, maybe it has\x01",
            "sweet sap inside like maple trees.\x02\x03",

            "#1448FMay I cut into the trunk a bit to see?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #10
        0x109,
        "#1068F#6PNo. No, you cannot.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2604)
    Sleep(300)
    OP_30(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6E")

    def lambda_D59():
        OP_6D(50070, 1000, -50210, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_D59)
    Jump("loc_D92")

    label("loc_D6E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D92")

    def lambda_D80():
        OP_6D(49080, 1000, -49390, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_D80)

    label("loc_D92")


    def lambda_D98():
        OP_67(0, 7900, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D98)

    def lambda_DB0():
        OP_6B(2530, 1000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_DB0)

    def lambda_DC0():
        OP_6C(0, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_DC0)

    def lambda_DD0():
        OP_6E(450, 1000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_DD0)
    Sleep(1000)
    SetMapFlags(0x1)
    ClearMapFlags(0x80)
    EventEnd(0x2)
    SetMapFlags(0x2000000)
    Return()

    # Function_2_7CF end

    def Function_3_DF1(): pass

    label("Function_3_DF1")

    OP_8E(0xFE, 0xB2A2, 0x3E8, 0xFFFF51AA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xC396, 0x3E8, 0xFFFF3BDE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xC396, 0x3E8, 0xFFFF3BDE, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_3_DF1 end

    def Function_4_E35(): pass

    label("Function_4_E35")

    Sleep(200)
    OP_8E(0xFE, 0xB25C, 0x3E8, 0xFFFF5650, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBFB8, 0x3E8, 0xFFFF3F12, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_4_E35 end

    def Function_5_E6A(): pass

    label("Function_5_E6A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x10F, 0x80)
    OP_6D(54810, 3500, -44170, 0)
    OP_67(0, 4680, -10000, 0)
    OP_6B(2410, 0)
    OP_6C(300000, 0)
    OP_6E(591, 0)
    OP_E5(0x1, 0xFF, 0x10, 262144)
    OP_E5(0x1, 0xFF, 0x11, 262144)
    OP_E5(0x1, 0xFF, 0x12, 262144)
    OP_E5(0x1, 0xFF, 0x13, 262144)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)

    def lambda_EF2():
        OP_6D(54810, 4750, -44170, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_EF2)

    def lambda_F0A():
        OP_67(0, 6610, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F0A)

    def lambda_F22():
        OP_6B(2510, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F22)

    def lambda_F32():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_F32)

    def lambda_F42():
        OP_6E(600, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_F42)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(4000)
    OP_22(0x15F, 0x0, 0x64)
    Fade(1000)
    OP_E5(0x0, 0xFF, 0x10, 262144)
    OP_E5(0x0, 0xFF, 0x11, 262144)
    OP_E5(0x0, 0xFF, 0x12, 262144)
    OP_E5(0x0, 0xFF, 0x13, 262144)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1094():
        OP_6B(2200, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1094)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U7002   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_5_E6A end

    def Function_6_10C8(): pass

    label("Function_6_10C8")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(54290, 1000, -43900, 0)
    OP_67(0, 3960, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(0, 0)
    OP_6E(349, 0)
    SetChrPos(0x109, 54420, 1000, -51530, 0)
    SetChrPos(0x10F, 53160, 1000, -52020, 45)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #11
        0x109,
        "#1078F#6PHoly Stregas... Now, this is something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10F,
        (
            "#1442F#6PIt really is...\x02\x03",

            "It's as if petals of pure light are floating \x01",
            "through the air around us...\x02",
        )
    )

    CloseMessageWindow()
    OP_C4(0x0, 0x800)
    Sleep(150)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #13
        "\x07\x05#2S#40WI welcome you, dear guests...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #14
        0x109,
        "#1079F#6PWas that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10F,
        "#1444F#6PDid the tree just talk to us?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #16
        (
            "\x07\x05#2S#40W...In accordance with my master's wishes...\x01",
            "#800W \x01",
            "#40W...I shall grant you the blessings of the earth...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #17
        (
            "\x07\x05#2S#40WHowever, my power is not without its limits...\x01",
            "#800W \x01",
            "#40WI require compensation in exchange for its use...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1417")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1486")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Buy Ingredients\x01",      # 0
            "End\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1467"),
        (SWITCH_DEFAULT, "loc_1476"),
    )


    label("loc_1467")

    OP_A9(0xF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1483")

    label("loc_1476")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1483")

    label("loc_1483")

    Jump("loc_1417")

    label("loc_1486")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #18
        (
            "\x07\x05#2S#40WWhen my master's power returns...\x01",
            "#800W \x01",
            "#40W...the variety of blessings I offer shall increase...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #19
        "\x07\x05#2S#40W...May the blessings of the earth be upon you...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    OP_63(0x10F)
    Sleep(300)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #20
        0x109,
        (
            "#1840F#6PHaha... Man...\x02\x03",

            "#1068FIf someone told me a tree just chatted them up\x01",
            "and offered to sell them ingredients, I'd tell 'em\x01",
            "they've had one too many drinks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10F,
        "#1443F#6P#40W...\x02",
    )

    CloseMessageWindow()

    def lambda_1681():
        OP_6D(53990, 1000, -49500, 1200)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1681)

    def lambda_1699():
        OP_67(0, 4960, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1699)

    def lambda_16B1():
        OP_6B(2850, 1200)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_16B1)
    OP_8C(0x109, 225, 400)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #22
        0x109,
        (
            "#1079F#2PRies?\x02\x03",

            "#1063FSomething up?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 0)
    SetChrSubChip(0x10F, 0)
    SetChrFlags(0x10F, 0x2)
    OP_0D()
    Sleep(500)

    ChrTalk(    #23
        0x10F,
        (
            "#1442F#6P'That great tree took root near to a seven-colored\x01",
            "spring, and there it granted blessings and joy...'\x02\x03",

            "A excerpt from the Book of Genesis, Verse 7,\x01",
            "'The Primal Ground.'\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x10F, 0)
    SetChrSubChip(0x10F, 1)
    OP_0D()
    Sleep(300)
    OP_99(0x10F, 0x2, 0x4, 0x5DC)
    Sleep(300)

    ChrTalk(    #24
        0x10F,
        (
            "#1447F#6POh, hallowed Aidios...\x02\x03",

            "Thank you for the divine protection and\x01",
            "mercy you have bestowed upon us.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #25
        0x109,
        (
            "#1840F#2PWell, aren't you just tickled pink?\x02\x03",

            "I'm not sure this tree has anything to do\x01",
            "with the Goddess, though.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0x10F, 0x2)
    OP_0D()
    Sleep(300)

    ChrTalk(    #26
        0x10F,
        (
            "#1443F#6PI disagree.\x02\x03",

            "#1446FEven the Testaments of the Goddess say that\x01",
            "'all roads lead to food.' Food is the fundamental\x01",
            "basis of everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        (
            "#1068F#2PThat's not in any Testament I've ever laid eyes \x01",
            "on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10F,
        "#1440F#6PThat said, let me give you this.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05Ries handed a \x1F\x0D\x02\x07\x05 to Kevin.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x20D, 1)
    OP_AC(0x16)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x109,
        (
            "#1064F#2PHuh?\x02\x03",

            "Why're you giving this to me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10F,
        (
            "#1446F#6PBecause you are remarkably impious for a knight\x01",
            "of the church.\x02\x03",

            "#1801FYou should work on becoming more devout through\x01",
            "cooking in Her name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x109,
        (
            "#1068F#2PThat doesn't even make sense!\x02\x03",

            "#1063FBesides, can't you just do the cooking yourself?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10F,
        (
            "#1447F#6PBut you've always been better at it than me...\x02\x03",

            "I'm sure it's the wish of the ingredients to be\x01",
            "used by the best chef possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        "#1060F#2PBut still...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10F,
        (
            "#1802F#6P...\x02\x03",

            "#1445F...Please?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #36
        0x109,
        (
            "#1079F#2PNgh...\x02\x03",

            "#1068F(I'm too soft for my own good sometimes.)\x02\x03",

            "#1840FWell, fine...but you have to help me. Deal?\x02\x03",

            "Also, the second I catch you snacking on\x01",
            "something while we're making it, I'm done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10F,
        "#1442F#6PHaha... I know.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2609)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_6_10C8 end

    def Function_7_1D9A(): pass

    label("Function_7_1D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DAB")
    Call(0, 6)
    Return()

    label("loc_1DAB")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DCB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E3A")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Buy Ingredients\x01",      # 0
            "End\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E1B"),
        (SWITCH_DEFAULT, "loc_1E2A"),
    )


    label("loc_1E1B")

    OP_A9(0xF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E37")

    label("loc_1E2A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E37")

    label("loc_1E37")

    Jump("loc_1DCB")

    label("loc_1E3A")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFF)
    Return()

    # Function_7_1D9A end

    def Function_8_1E47(): pass

    label("Function_8_1E47")

    OP_A3(0x10)
    Call(0, 11)
    Call(0, 9)
    Call(0, 12)
    OP_C0(0x27, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_END)), "loc_1E82")
    Call(0, 12)

    label("loc_1E82")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EAF")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_1EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ED0")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_1ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EF1")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_1EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F12")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_1F12")

    Return()

    # Function_8_1E47 end

    def Function_9_1F13(): pass

    label("Function_9_1F13")

    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_2000")
    SetChrPos(0x1E, 55220, 1800, -49210, 0)
    SetChrPos(0x11, 54510, 1220, -50260, 0)
    SetChrPos(0x16, 58670, 1000, -49340, 177)
    SetChrPos(0x20, 52150, 1000, -53260, 322)
    SetChrPos(0x12, 50890, 1000, -51800, 142)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F8F")
    OP_43(0x12, 0x0, 0x0, 0x13)
    Jump("loc_1F96")

    label("loc_1F8F")

    OP_43(0x12, 0x0, 0x6, 0x2)

    label("loc_1F96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FAE")
    OP_43(0x20, 0x0, 0x0, 0x13)
    Jump("loc_1FB5")

    label("loc_1FAE")

    OP_43(0x20, 0x0, 0x6, 0x2)

    label("loc_1FB5")

    SetChrChipByIndex(0x1A, 28)
    SetChrSubChip(0x1A, 0)
    OP_44(0x1A, 0x0)
    SetChrFlags(0x1A, 0x4)
    SetChrPos(0x1A, 76920, -11300, -53500, 90)
    SetChrChipByIndex(0x1D, 29)
    SetChrSubChip(0x1D, 0)
    OP_44(0x1D, 0x0)
    SetChrFlags(0x1D, 0x4)
    SetChrPos(0x1D, 77120, -11300, -52420, 90)
    Jump("loc_2F12")

    label("loc_2000")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_2247")
    SetChrChipByIndex(0x12, 25)
    SetChrSubChip(0x12, 0)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 98770, -13900, -52140, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_203E")
    SetChrSubChip(0x12, 2)

    label("loc_203E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_206B")
    SetChrPos(0x1B, 100250, -14000, -51650, 66)
    Jump("loc_20C4")

    label("loc_206B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 4)), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2091")
    SetChrPos(0x1B, 100250, -14000, -51650, 199)
    Jump("loc_20C4")

    label("loc_2091")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20B3")
    SetChrPos(0x1B, 100240, -14000, -52310, 230)
    Jump("loc_20C4")

    label("loc_20B3")

    SetChrPos(0x1B, 100250, -14000, -51650, 230)

    label("loc_20C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 4)), scpexpr(EXPR_END)), "loc_20F2")
    SetChrChipByIndex(0x11, 24)
    SetChrSubChip(0x11, 0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 98770, -13900, -53060, 90)
    Jump("loc_2187")

    label("loc_20F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 4)), scpexpr(EXPR_END)), "loc_211C")
    SetChrChipByIndex(0x11, 23)
    SetChrPos(0x11, 99670, -14000, -53130, 90)
    OP_43(0x11, 0x0, 0x0, 0xE)
    OP_A2(0x10)
    Jump("loc_2187")

    label("loc_211C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2163")
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 100490, -14000, -55300, 133)
    OP_43(0x11, 0x0, 0x6, 0x2)
    Jump("loc_2187")

    label("loc_2163")

    SetChrChipByIndex(0x11, 24)
    SetChrSubChip(0x11, 0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 98770, -13900, -53060, 90)

    label("loc_2187")

    SetChrPos(0x1A, 51210, 1000, -60260, 205)
    SetChrPos(0x14, 57200, 1000, -49150, 148)
    SetChrPos(0x1F, 60170, 1000, -46660, 176)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21DC")
    SetChrPos(0x13, 62820, 1000, -45530, 27)
    Jump("loc_21ED")

    label("loc_21DC")

    SetChrPos(0x13, 60350, 1000, -49000, 356)

    label("loc_21ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_220F")
    SetChrPos(0x15, 59210, 1000, -56500, 127)
    Jump("loc_2244")

    label("loc_220F")

    SetChrChipByIndex(0x17, 20)
    SetChrSubChip(0x17, 0)
    OP_44(0x17, 0x0)
    SetChrFlags(0x17, 0x4)
    SetChrPos(0x17, 59340, 1300, -57340, 315)
    SetChrPos(0x15, 58310, 1000, -56210, 135)

    label("loc_2244")

    Jump("loc_2F12")

    label("loc_2247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_22A8")
    SetChrPos(0x1B, 95180, -14000, -52580, 126)
    SetChrPos(0x14, 60170, 1000, -46660, 180)
    SetChrPos(0x1F, 54480, 1000, -52730, 0)
    SetChrChipByIndex(0x1A, 28)
    SetChrSubChip(0x1A, 0)
    OP_44(0x1A, 0x0)
    SetChrFlags(0x1A, 0x4)
    SetChrPos(0x1A, 54410, 1300, -59300, 0)
    Jump("loc_2F12")

    label("loc_22A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_246B")
    SetChrChipByIndex(0x21, 33)
    SetChrSubChip(0x21, 0)
    OP_44(0x21, 0x0)
    SetChrFlags(0x21, 0x4)
    SetChrPos(0x21, 57260, 2000, -41880, 225)
    SetChrFlags(0x1B, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22EE")
    SetChrFlags(0x21, 0x80)
    Jump("loc_22F7")

    label("loc_22EE")

    ClearChrFlags(0x21, 0x80)
    OP_65(0x2, 0x1)

    label("loc_22F7")

    SetChrChipByIndex(0x1A, 28)
    SetChrSubChip(0x1A, 0)
    OP_44(0x1A, 0x0)
    SetChrFlags(0x1A, 0x4)
    SetChrPos(0x1A, 54410, 1300, -59300, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2392")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_234B")
    SetChrPos(0x14, 52280, 1000, -61100, 192)
    Jump("loc_238F")

    label("loc_234B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_236D")
    SetChrPos(0x13, 56320, 1000, -59850, 171)
    Jump("loc_238F")

    label("loc_236D")

    SetChrPos(0x14, 53410, 1000, -57430, 90)
    SetChrPos(0x13, 55360, 1000, -57610, 275)

    label("loc_238F")

    Jump("loc_23F8")

    label("loc_2392")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23B4")
    SetChrPos(0x14, 54420, 1000, -56910, 179)
    Jump("loc_23F8")

    label("loc_23B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23D6")
    SetChrPos(0x13, 54420, 1000, -56910, 179)
    Jump("loc_23F8")

    label("loc_23D6")

    SetChrPos(0x14, 53410, 1000, -57430, 150)
    SetChrPos(0x13, 55360, 1000, -57610, 219)

    label("loc_23F8")

    SetChrPos(0x1E, 55220, 1800, -49210, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 0)), scpexpr(EXPR_END)), "loc_2424")
    SetChrPos(0x20, 97450, -14000, -47720, 37)
    Jump("loc_2468")

    label("loc_2424")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2457")
    SetChrPos(0x11, 93410, -14000, -52280, 96)
    SetChrPos(0x20, 97090, -14000, -52560, 264)
    Jump("loc_2468")

    label("loc_2457")

    SetChrPos(0x11, 65290, -11000, -47010, 30)

    label("loc_2468")

    Jump("loc_2F12")

    label("loc_246B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_267A")
    SetChrPos(0x13, 61630, 1000, -50010, 313)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24C1")
    SetChrPos(0x1B, 61330, 1000, -57980, 214)
    SetChrPos(0x1F, 60450, 1000, -59270, 54)
    Jump("loc_2502")

    label("loc_24C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24E3")
    SetChrPos(0x1F, 61200, 1000, -59080, 134)
    Jump("loc_2502")

    label("loc_24E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2502")
    SetChrPos(0x1B, 61200, 1000, -59080, 134)

    label("loc_2502")

    SetChrPos(0x11, 65290, -11000, -47010, 30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2535")
    SetChrChipByIndex(0x11, 23)
    SetChrSubChip(0x11, 0)
    OP_43(0x11, 0x0, 0x0, 0xD)
    Jump("loc_253F")

    label("loc_2535")

    OP_43(0x11, 0x0, 0x6, 0x2)
    OP_63(0x11)

    label("loc_253F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_257D")
    SetChrPos(0x14, 47340, 1000, -58740, 129)
    SetChrPos(0x19, 48290, 1000, -59730, 299)
    Jump("loc_25B0")

    label("loc_257D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_259F")
    SetChrPos(0x19, 49980, 1000, -56720, 50)
    Jump("loc_25B0")

    label("loc_259F")

    SetChrPos(0x14, 41330, 1000, -53920, 250)

    label("loc_25B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_261E")
    SetChrChipByIndex(0x20, 22)
    SetChrSubChip(0x20, 0)
    OP_44(0x20, 0x0)
    SetChrFlags(0x20, 0x4)
    SetChrPos(0x20, 98730, -13900, -52200, 90)
    SetChrChipByIndex(0x12, 25)
    SetChrSubChip(0x12, 0)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 98830, -13900, -53010, 90)
    SetChrSubChip(0x12, 1)
    SetChrSubChip(0x20, 2)
    Jump("loc_2677")

    label("loc_261E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2653")
    SetChrChipByIndex(0x20, 22)
    SetChrSubChip(0x20, 0)
    OP_44(0x20, 0x0)
    SetChrFlags(0x20, 0x4)
    SetChrPos(0x20, 98770, -13900, -52490, 90)
    Jump("loc_2677")

    label("loc_2653")

    SetChrChipByIndex(0x12, 25)
    SetChrSubChip(0x12, 0)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 98770, -13900, -52490, 90)

    label("loc_2677")

    Jump("loc_2F12")

    label("loc_267A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_279D")
    SetChrPos(0x14, 41330, 1000, -53920, 250)
    SetChrChipByIndex(0x19, 18)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, 61420, 1200, -52290, 267)
    SetChrPos(0x13, 54410, 1000, -57870, 1)
    SetChrChipByIndex(0x20, 22)
    SetChrSubChip(0x20, 0)
    OP_44(0x20, 0x0)
    SetChrFlags(0x20, 0x4)
    SetChrPos(0x20, 97610, -13900, -53060, 269)
    SetChrChipByIndex(0x12, 25)
    SetChrSubChip(0x12, 0)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 97600, -13900, -52140, 269)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_272D")
    SetChrSubChip(0x12, 1)

    label("loc_272D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_274B")
    SetChrSubChip(0x20, 2)

    label("loc_274B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2778")
    SetChrPos(0x1B, 99110, -14000, -49420, 55)
    Jump("loc_2789")

    label("loc_2778")

    SetChrPos(0x1B, 95970, -14000, -52590, 79)

    label("loc_2789")

    SetChrPos(0x1F, 51740, 1000, -48810, 220)
    Jump("loc_2F12")

    label("loc_279D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_2903")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27E2")
    SetChrPos(0x17, 61440, 1000, -58160, 221)
    SetChrPos(0x16, 60340, 1000, -59400, 47)
    Jump("loc_2823")

    label("loc_27E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2804")
    SetChrPos(0x16, 61140, 1000, -59050, 132)
    Jump("loc_2823")

    label("loc_2804")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2823")
    SetChrPos(0x17, 61140, 1000, -59050, 132)

    label("loc_2823")

    SetChrChipByIndex(0x13, 34)
    SetChrSubChip(0x13, 0)
    OP_44(0x13, 0x0)
    SetChrFlags(0x13, 0x4)
    SetChrPos(0x13, 54350, 1300, -59320, 0)
    SetChrPos(0x14, 41330, 1000, -53920, 250)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28A9")
    SetChrPos(0x12, 96280, -14000, -52650, 90)
    SetChrChipByIndex(0x20, 22)
    SetChrSubChip(0x20, 0)
    OP_44(0x20, 0x0)
    SetChrFlags(0x20, 0x4)
    SetChrPos(0x20, 97700, -13900, -52560, 269)
    Jump("loc_28EF")

    label("loc_28A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28DE")
    SetChrChipByIndex(0x20, 22)
    SetChrSubChip(0x20, 0)
    OP_44(0x20, 0x0)
    SetChrFlags(0x20, 0x4)
    SetChrPos(0x20, 98920, -13900, -52540, 90)
    Jump("loc_28EF")

    label("loc_28DE")

    SetChrPos(0x12, 96280, -14000, -52650, 90)

    label("loc_28EF")

    SetChrPos(0x1F, 63520, 1000, -42950, 42)
    Jump("loc_2F12")

    label("loc_2903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_2A1C")
    SetChrPos(0x1F, 54780, 1000, -51140, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2948")
    SetChrPos(0x14, 54410, 1000, -57870, 15)
    Jump("loc_2959")

    label("loc_2948")

    SetChrPos(0x14, 54410, 1000, -57870, 0)

    label("loc_2959")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2986")
    SetChrPos(0x17, 55790, 1000, -57780, 335)
    Jump("loc_2997")

    label("loc_2986")

    SetChrPos(0x17, 55790, 1000, -57780, 0)

    label("loc_2997")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29B9")
    SetChrPos(0x13, 55820, 1000, -53090, 332)
    Jump("loc_2A19")

    label("loc_29B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29E6")
    SetChrPos(0x13, 54950, 1000, -56000, 180)
    Jump("loc_2A19")

    label("loc_29E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A08")
    SetChrPos(0x13, 54950, 1000, -56000, 155)
    Jump("loc_2A19")

    label("loc_2A08")

    SetChrPos(0x13, 54950, 1000, -56000, 195)

    label("loc_2A19")

    Jump("loc_2F12")

    label("loc_2A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_2A7D")
    SetChrChipByIndex(0x14, 19)
    SetChrSubChip(0x14, 0)
    OP_44(0x14, 0x0)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x14, 54350, 1300, -59320, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A69")
    SetChrPos(0x13, 55700, 1000, -58390, 281)
    Jump("loc_2A7A")

    label("loc_2A69")

    SetChrPos(0x13, 56970, 1000, -59720, 160)

    label("loc_2A7A")

    Jump("loc_2F12")

    label("loc_2A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_2AFE")
    SetChrPos(0x14, 54440, 1000, -61430, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AB7")
    SetChrPos(0x17, 50110, 1000, -48610, 145)
    Jump("loc_2AC8")

    label("loc_2AB7")

    SetChrPos(0x17, 50110, 1000, -48610, 34)

    label("loc_2AC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AEA")
    SetChrPos(0x13, 51570, 1000, -50010, 316)
    Jump("loc_2AFB")

    label("loc_2AEA")

    SetChrPos(0x13, 51250, 1000, -51050, 38)

    label("loc_2AFB")

    Jump("loc_2F12")

    label("loc_2AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_2BB3")
    SetChrChipByIndex(0x14, 19)
    SetChrSubChip(0x14, 0)
    OP_44(0x14, 0x0)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x14, 61460, 1400, -52370, 271)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B4B")
    SetChrPos(0x13, 50180, 1000, -48600, 90)
    Jump("loc_2B5C")

    label("loc_2B4B")

    SetChrPos(0x13, 51640, 1000, -49210, 212)

    label("loc_2B5C")

    SetChrChipByIndex(0x17, 20)
    SetChrSubChip(0x17, 1)
    OP_44(0x17, 0x0)
    SetChrFlags(0x17, 0x4)
    SetChrPos(0x17, 51970, 1500, -47860, 209)
    SetChrPos(0x18, 52240, 1600, -48050, 283)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BA7")
    SetChrFlags(0x18, 0x80)
    Jump("loc_2BB0")

    label("loc_2BA7")

    ClearChrFlags(0x18, 0x80)
    OP_65(0x1, 0x1)

    label("loc_2BB0")

    Jump("loc_2F12")

    label("loc_2BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_2E33")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BF6")
    SetChrChipByIndex(0x19, 10)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, 96290, -14000, -51540, 180)
    OP_43(0x19, 0x0, 0x6, 0x2)
    Jump("loc_2C1A")

    label("loc_2BF6")

    SetChrChipByIndex(0x19, 18)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, 97800, -13900, -52620, 264)

    label("loc_2C1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C56")
    SetChrChipByIndex(0x14, 5)
    SetChrSubChip(0x14, 0)
    OP_44(0x14, 0x0)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x14, 96290, -14000, -53640, 0)
    OP_43(0x14, 0x0, 0x6, 0x2)
    Jump("loc_2C7A")

    label("loc_2C56")

    SetChrChipByIndex(0x14, 19)
    SetChrSubChip(0x14, 0)
    OP_44(0x14, 0x0)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x14, 97800, -13900, -52620, 264)

    label("loc_2C7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CB2")
    SetChrPos(0x17, 54450, 1000, -58360, 6)
    Jump("loc_2E30")

    label("loc_2CB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CEA")
    SetChrPos(0x13, 54450, 1000, -58360, 6)
    Jump("loc_2E30")

    label("loc_2CEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D22")
    SetChrPos(0x1A, 54450, 1000, -58360, 6)
    Jump("loc_2E30")

    label("loc_2D22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D6B")
    SetChrPos(0x13, 55340, 1000, -57810, 248)
    SetChrPos(0x17, 53840, 1000, -57840, 94)
    Jump("loc_2E30")

    label("loc_2D6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DB4")
    SetChrPos(0x17, 55340, 1000, -57810, 248)
    SetChrPos(0x1A, 53840, 1000, -57840, 94)
    Jump("loc_2E30")

    label("loc_2DB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DFD")
    SetChrPos(0x13, 55340, 1000, -57810, 248)
    SetChrPos(0x1A, 53840, 1000, -57840, 94)
    Jump("loc_2E30")

    label("loc_2DFD")

    SetChrPos(0x1A, 53340, 1000, -57770, 39)
    SetChrPos(0x13, 55020, 1000, -57740, 305)
    SetChrPos(0x17, 54170, 1000, -56200, 185)

    label("loc_2E30")

    Jump("loc_2F12")

    label("loc_2E33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_2F0B")
    SetChrPos(0x14, 60400, 1000, -49520, 180)
    SetChrChipByIndex(0x19, 18)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, 61420, 1200, -52290, 267)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E91")
    SetChrPos(0x17, 59530, 1000, -52170, 315)
    Jump("loc_2EA2")

    label("loc_2E91")

    SetChrPos(0x17, 59530, 1000, -52170, 90)

    label("loc_2EA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EC4")
    SetChrPos(0x13, 58300, 1000, -53260, 45)
    Jump("loc_2ED5")

    label("loc_2EC4")

    SetChrPos(0x13, 55340, 1000, -57810, 248)

    label("loc_2ED5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EF7")
    SetChrPos(0x1A, 53840, 1000, -57840, 180)
    Jump("loc_2F08")

    label("loc_2EF7")

    SetChrPos(0x1A, 53840, 1000, -57840, 94)

    label("loc_2F08")

    Jump("loc_2F12")

    label("loc_2F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_END)), "loc_2F12")

    label("loc_2F12")

    Call(0, 10)
    Return()

    # Function_9_1F13 end

    def Function_10_2F17(): pass

    label("Function_10_2F17")

    OP_BC(0xE, 0x1, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F67")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F48")
    OP_51(0x11, 0xA, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F48")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0xA), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F67")
    OP_51(0x11, 0xA, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F67")

    Return()

    # Function_10_2F17 end

    def Function_11_2F68(): pass

    label("Function_11_2F68")

    OP_C0(0x23, 0x10, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x11, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x12, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x13, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x14, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x15, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x16, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x17, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x18, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x19, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1A, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1B, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1C, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1D, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1E, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1F, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x20, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x10, 9000000, 9000000, 0, 0)
    SetChrPos(0x11, 9000000, 9000000, 0, 0)
    SetChrPos(0x12, 9000000, 9000000, 0, 0)
    SetChrPos(0x13, 9000000, 9000000, 0, 0)
    SetChrPos(0x14, 9000000, 9000000, 0, 0)
    SetChrPos(0x15, 9000000, 9000000, 0, 0)
    SetChrPos(0x16, 9000000, 9000000, 0, 0)
    SetChrPos(0x17, 9000000, 9000000, 0, 0)
    SetChrPos(0x18, 9000000, 9000000, 0, 0)
    SetChrPos(0x19, 9000000, 9000000, 0, 0)
    SetChrPos(0x1A, 9000000, 9000000, 0, 0)
    SetChrPos(0x1B, 9000000, 9000000, 0, 0)
    SetChrPos(0x1C, 9000000, 9000000, 0, 0)
    SetChrPos(0x1D, 9000000, 9000000, 0, 0)
    SetChrPos(0x1E, 9000000, 9000000, 0, 0)
    SetChrPos(0x1F, 9000000, 9000000, 0, 0)
    SetChrPos(0x20, 9000000, 9000000, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32E1")
    SetChrFlags(0x12, 0x80)
    Jump("loc_32E6")

    label("loc_32E1")

    ClearChrFlags(0x12, 0x80)

    label("loc_32E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32FC")
    SetChrFlags(0x13, 0x80)
    Jump("loc_3301")

    label("loc_32FC")

    ClearChrFlags(0x13, 0x80)

    label("loc_3301")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3317")
    SetChrFlags(0x14, 0x80)
    Jump("loc_331C")

    label("loc_3317")

    ClearChrFlags(0x14, 0x80)

    label("loc_331C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3332")
    SetChrFlags(0x15, 0x80)
    Jump("loc_3337")

    label("loc_3332")

    ClearChrFlags(0x15, 0x80)

    label("loc_3337")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_334D")
    SetChrFlags(0x16, 0x80)
    Jump("loc_3352")

    label("loc_334D")

    ClearChrFlags(0x16, 0x80)

    label("loc_3352")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3368")
    SetChrFlags(0x17, 0x80)
    Jump("loc_336D")

    label("loc_3368")

    ClearChrFlags(0x17, 0x80)

    label("loc_336D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3383")
    SetChrFlags(0x19, 0x80)
    Jump("loc_3388")

    label("loc_3383")

    ClearChrFlags(0x19, 0x80)

    label("loc_3388")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_339E")
    SetChrFlags(0x1A, 0x80)
    Jump("loc_33A3")

    label("loc_339E")

    ClearChrFlags(0x1A, 0x80)

    label("loc_33A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33B9")
    SetChrFlags(0x1B, 0x80)
    Jump("loc_33BE")

    label("loc_33B9")

    ClearChrFlags(0x1B, 0x80)

    label("loc_33BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33D4")
    SetChrFlags(0x1C, 0x80)
    Jump("loc_33D9")

    label("loc_33D4")

    ClearChrFlags(0x1C, 0x80)

    label("loc_33D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33EF")
    SetChrFlags(0x1D, 0x80)
    Jump("loc_33F4")

    label("loc_33EF")

    ClearChrFlags(0x1D, 0x80)

    label("loc_33F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_340A")
    SetChrFlags(0x1E, 0x80)
    Jump("loc_340F")

    label("loc_340A")

    ClearChrFlags(0x1E, 0x80)

    label("loc_340F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3425")
    SetChrFlags(0x1F, 0x80)
    Jump("loc_342A")

    label("loc_3425")

    ClearChrFlags(0x1F, 0x80)

    label("loc_342A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3440")
    SetChrFlags(0x20, 0x80)
    Jump("loc_3445")

    label("loc_3440")

    ClearChrFlags(0x20, 0x80)

    label("loc_3445")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_345B")
    SetChrFlags(0x11, 0x80)
    Jump("loc_3460")

    label("loc_345B")

    ClearChrFlags(0x11, 0x80)

    label("loc_3460")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3476")
    SetChrFlags(0x10, 0x80)
    Jump("loc_347B")

    label("loc_3476")

    ClearChrFlags(0x10, 0x80)

    label("loc_347B")

    Return()

    # Function_11_2F68 end

    def Function_12_347C(): pass

    label("Function_12_347C")

    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    OP_A3(0x4)
    OP_A3(0x5)
    OP_A3(0x6)
    OP_A3(0x7)
    OP_A3(0x8)
    OP_A3(0x9)
    OP_A3(0xA)
    OP_A3(0xB)
    OP_A3(0xC)
    OP_A3(0xD)
    OP_A3(0xE)
    OP_A3(0xF)
    Return()

    # Function_12_347C end

    def Function_13_34AD(): pass

    label("Function_13_34AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_355B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3558")
    Sleep(500)

    label("loc_34CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3558")
    OP_8C(0xFE, 30, 400)
    SetChrChipByIndex(0xFE, 23)
    SetChrSubChip(0xFE, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    SetChrSubChip(0xFE, 2)
    Sleep(1500)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0xFE)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 23)
    SetChrSubChip(0xFE, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    SetChrSubChip(0xFE, 2)
    Sleep(1500)
    Sleep(1500)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    Jump("loc_34CC")

    label("loc_3558")

    Jump("loc_355F")

    label("loc_355B")

    Call(6, 2)

    label("loc_355F")

    Return()

    # Function_13_34AD end

    def Function_14_3560(): pass

    label("Function_14_3560")

    Sleep(500)

    label("loc_3565")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_35A3")
    SetChrChipByIndex(0xFE, 23)
    SetChrSubChip(0xFE, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    SetChrSubChip(0xFE, 2)
    Sleep(1500)
    Sleep(2000)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    Jump("loc_3565")

    label("loc_35A3")

    Return()

    # Function_14_3560 end

    def Function_15_35A4(): pass

    label("Function_15_35A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3600")
    SetChrSubChip(0xFE, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 1)
    Sleep(100)
    SetChrSubChip(0xFE, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 2)
    Sleep(2000)
    SetChrSubChip(0xFE, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 1)
    Sleep(1000)
    SetChrSubChip(0xFE, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 2)
    Sleep(1500)
    Jump("Function_15_35A4")

    label("loc_3600")

    Return()

    # Function_15_35A4 end

    def Function_16_3601(): pass

    label("Function_16_3601")

    Call(3, 4)
    Return()

    # Function_16_3601 end

    def Function_17_3606(): pass

    label("Function_17_3606")

    Call(5, 9)
    Return()

    # Function_17_3606 end

    def Function_18_360B(): pass

    label("Function_18_360B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_3619")
    Call(6, 2)
    Jump("loc_364A")

    label("loc_3619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_3646")

    label("loc_3620")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3643")
    OP_8D(0xFE, 92770, -50060, 96780, -55920, 1500)
    Jump("loc_3620")

    label("loc_3643")

    Jump("loc_364A")

    label("loc_3646")

    Call(6, 2)

    label("loc_364A")

    Return()

    # Function_18_360B end

    def Function_19_364B(): pass

    label("Function_19_364B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_366E")
    OP_8D(0xFE, 49060, -49630, 53360, -54740, 1500)
    Jump("Function_19_364B")

    label("loc_366E")

    Return()

    # Function_19_364B end

    def Function_20_366F(): pass

    label("Function_20_366F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_369D")
    OP_A2(0x11)
    Call(3, 2)

    label("loc_369D")

    Return()

    # Function_20_366F end

    def Function_21_369E(): pass

    label("Function_21_369E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36CC")
    OP_A2(0x12)
    Call(3, 2)

    label("loc_36CC")

    Return()

    # Function_21_369E end

    def Function_22_36CD(): pass

    label("Function_22_36CD")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3745")
    OP_22(0x17, 0x0, 0x64)
    OP_82(0x0, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #38
        "\x07\x05There are several issues of the Liberl News on the bookshelf.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x2676)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_40D0")

    label("loc_3745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x501, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37BB")
    OP_22(0x17, 0x0, 0x64)
    OP_82(0x0, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #39
        "\x07\x05There are several issues of the Liberl News on the bookshelf.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x2671)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_40D0")

    label("loc_37BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C00")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #40
        "\x07\x05There are several issues of the Liberl News on the bookshelf.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "Early 1202 - Mid 1202\x01",       # 0
            "Late 1202 - Early 1203\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3875"),
        (1, "loc_3A00"),
        (SWITCH_DEFAULT, "loc_3BEE"),
    )


    label("loc_3875")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "Read Issue 1\x01",      # 0
            "Read Issue 2\x01",      # 1
            "Read Issue 3\x01",      # 2
            "Read Issue 4\x01",      # 3
            "Read Issue 5\x01",      # 4
            "Read Issue 6\x01",      # 5
            "Read Issue 7\x01",      # 6
            "Read Issue 8\x01",      # 7
            "Read Issue 9\x01",      # 8
            "Read Special\x01",      # 9
            "Leave\x01",             # 10
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_395B")
    OP_B8(0xD2, 0x0)

    label("loc_395B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_396D")
    OP_B8(0xD3, 0x0)

    label("loc_396D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_397F")
    OP_B8(0xD4, 0x0)

    label("loc_397F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3991")
    OP_B8(0xD5, 0x0)

    label("loc_3991")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39A3")
    OP_B8(0xD6, 0x0)

    label("loc_39A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B5")
    OP_B8(0xD7, 0x0)

    label("loc_39B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39C7")
    OP_B8(0xD8, 0x0)

    label("loc_39C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39D9")
    OP_B8(0xD9, 0x0)

    label("loc_39D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39EB")
    OP_B8(0xDA, 0x0)

    label("loc_39EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39FD")
    OP_B8(0xDB, 0x0)

    label("loc_39FD")

    Jump("loc_3BEE")

    label("loc_3A00")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "Read Issue 1\x01",        # 0
            "Read Issue 2\x01",        # 1
            "Read Issue 3\x01",        # 2
            "Read Issue 4\x01",        # 3
            "Read Issue 5\x01",        # 4
            "Read Issue 6\x01",        # 5
            "Read Issue 7\x01",        # 6
            "Read Special 1\x01",      # 7
            "Read Issue 8\x01",        # 8
            "Read Issue 9\x01",        # 9
            "Read Issue 10\x01",       # 10
            "Read Issue 11\x01",       # 11
            "Read Special 2\x01",      # 12
            "Leave\x01",               # 13
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B13")
    OP_B8(0xF1, 0x0)

    label("loc_3B13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B25")
    OP_B8(0xF2, 0x0)

    label("loc_3B25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B37")
    OP_B8(0xF3, 0x0)

    label("loc_3B37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B49")
    OP_B8(0xF4, 0x0)

    label("loc_3B49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B5B")
    OP_B8(0xF5, 0x0)

    label("loc_3B5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B6D")
    OP_B8(0xF6, 0x0)

    label("loc_3B6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B7F")
    OP_B8(0xF7, 0x0)

    label("loc_3B7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B91")
    OP_B8(0xF8, 0x0)

    label("loc_3B91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA3")
    OP_B8(0xF9, 0x0)

    label("loc_3BA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BB5")
    OP_B8(0xFA, 0x0)

    label("loc_3BB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BC7")
    OP_B8(0xFB, 0x0)

    label("loc_3BC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BD9")
    OP_B8(0xFC, 0x0)

    label("loc_3BD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BEB")
    OP_B8(0x326, 0x0)

    label("loc_3BEB")

    Jump("loc_3BEE")

    label("loc_3BEE")

    FadeToBright(300, 0)
    OP_5F(0x0)
    TalkEnd(0xFF)
    Jump("loc_40D0")

    label("loc_3C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 6)), scpexpr(EXPR_END)), "loc_3E9B")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #41
        "\x07\x05There are several issues of the Liberl News on the bookshelf.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        "Late 1202 - Early 1203\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3C98"),
        (1, "loc_3E86"),
        (SWITCH_DEFAULT, "loc_3E89"),
    )


    label("loc_3C98")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "Read Issue 1\x01",        # 0
            "Read Issue 2\x01",        # 1
            "Read Issue 3\x01",        # 2
            "Read Issue 4\x01",        # 3
            "Read Issue 5\x01",        # 4
            "Read Issue 6\x01",        # 5
            "Read Issue 7\x01",        # 6
            "Read Special 1\x01",      # 7
            "Read Issue 8\x01",        # 8
            "Read Issue 9\x01",        # 9
            "Read Issue 10\x01",       # 10
            "Read Issue 11\x01",       # 11
            "Read Special 2\x01",      # 12
            "Leave\x01",               # 13
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DAB")
    OP_B8(0xF1, 0x0)

    label("loc_3DAB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DBD")
    OP_B8(0xF2, 0x0)

    label("loc_3DBD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DCF")
    OP_B8(0xF3, 0x0)

    label("loc_3DCF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DE1")
    OP_B8(0xF4, 0x0)

    label("loc_3DE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DF3")
    OP_B8(0xF5, 0x0)

    label("loc_3DF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E05")
    OP_B8(0xF6, 0x0)

    label("loc_3E05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E17")
    OP_B8(0xF7, 0x0)

    label("loc_3E17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E29")
    OP_B8(0xF8, 0x0)

    label("loc_3E29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E3B")
    OP_B8(0xF9, 0x0)

    label("loc_3E3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E4D")
    OP_B8(0xFA, 0x0)

    label("loc_3E4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E5F")
    OP_B8(0xFB, 0x0)

    label("loc_3E5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E71")
    OP_B8(0xFC, 0x0)

    label("loc_3E71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E83")
    OP_B8(0x326, 0x0)

    label("loc_3E83")

    Jump("loc_3E89")

    label("loc_3E86")

    Jump("loc_3E89")

    label("loc_3E89")

    FadeToBright(300, 0)
    OP_5F(0x0)
    TalkEnd(0xFF)
    Jump("loc_40D0")

    label("loc_3E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 1)), scpexpr(EXPR_END)), "loc_40D0")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #42
        "\x07\x05There are several issues of the Liberl News on the bookshelf.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        "Early 1202 - Mid 1202\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3F36"),
        (SWITCH_DEFAULT, "loc_40C1"),
    )


    label("loc_3F36")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "Read Issue 1\x01",      # 0
            "Read Issue 2\x01",      # 1
            "Read Issue 3\x01",      # 2
            "Read Issue 4\x01",      # 3
            "Read Issue 5\x01",      # 4
            "Read Issue 6\x01",      # 5
            "Read Issue 7\x01",      # 6
            "Read Issue 8\x01",      # 7
            "Read Issue 9\x01",      # 8
            "Read Special\x01",      # 9
            "Leave\x01",             # 10
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_401C")
    OP_B8(0xD2, 0x0)

    label("loc_401C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_402E")
    OP_B8(0xD3, 0x0)

    label("loc_402E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4040")
    OP_B8(0xD4, 0x0)

    label("loc_4040")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4052")
    OP_B8(0xD5, 0x0)

    label("loc_4052")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4064")
    OP_B8(0xD6, 0x0)

    label("loc_4064")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4076")
    OP_B8(0xD7, 0x0)

    label("loc_4076")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4088")
    OP_B8(0xD8, 0x0)

    label("loc_4088")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_409A")
    OP_B8(0xD9, 0x0)

    label("loc_409A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40AC")
    OP_B8(0xDA, 0x0)

    label("loc_40AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40BE")
    OP_B8(0xDB, 0x0)

    label("loc_40BE")

    Jump("loc_40C1")

    label("loc_40C1")

    FadeToBright(300, 0)
    OP_5F(0x0)
    TalkEnd(0xFF)

    label("loc_40D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40F0")
    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_40F0")
    Call(0, 24)
    Jump("loc_40F0")

    label("loc_40F0")

    Return()

    # Function_22_36CD end

    def Function_23_40F1(): pass

    label("Function_23_40F1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 0)), scpexpr(EXPR_END)), "loc_410C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_410C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 1)), scpexpr(EXPR_END)), "loc_411D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_411D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 2)), scpexpr(EXPR_END)), "loc_412E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_412E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 3)), scpexpr(EXPR_END)), "loc_413F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_413F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 4)), scpexpr(EXPR_END)), "loc_4150")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 5)), scpexpr(EXPR_END)), "loc_4161")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4161")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 6)), scpexpr(EXPR_END)), "loc_4172")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4172")

    Return()

    # Function_23_40F1 end

    def Function_24_4173(): pass

    label("Function_24_4173")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 65110, -11000, -56600, 289)
    SetChrPos(0x1, 64519, -11000, -57970, 313)
    SetChrPos(0x2, 66560, -11000, -56870, 282)
    SetChrPos(0x3, 65570, -11000, -59420, 294)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)
    OP_6D(65560, -10000, -57380, 0)
    OP_67(0, 5230, -10000, 0)
    OP_6B(2110, 0)
    OP_6C(339000, 0)
    OP_6E(450, 0)
    OP_0D()
    Sleep(500)

    AnonymousTalk(    #43
        (
            "\x07\x05#40WYou have done well to read all of my\x01",
            "fragments of knowledge...\x01",
            "#500W \x01",
            "#40WIn praise of your inquisitiveness,\x01",
            "allow me to grant you my blessing... \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_3E(0x15D, 1)

    AnonymousTalk(    #44
        "\x07\x05Received a single \x1F\x5D\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2677)
    FadeToBright(300, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_24_4173 end

    def Function_25_4323(): pass

    label("Function_25_4323")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4394")
    OP_22(0x17, 0x0, 0x64)
    OP_82(0x0, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #45
        "\x07\x05There are some challenging-looking books on the bookshelf.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x2675)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_450D")

    label("loc_4394")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #46
        "\x07\x05There are some challenging-looking books on the bookshelf.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "Read 'Hundred Days War'\x01",          # 0
            "Read 'Ruan Economics I'\x01",          # 1
            "Read 'Ruan Economics II'\x01",         # 2
            "Read 'Ruan Economics III'\x01",        # 3
            "Read 'Septium Optic Annals'\x01",      # 4
            "Leave\x01",                            # 5
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44B6")
    OP_B8(0xDC, 0x0)

    label("loc_44B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44C8")
    OP_B8(0xDD, 0x0)

    label("loc_44C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44DA")
    OP_B8(0xDE, 0x0)

    label("loc_44DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44EC")
    OP_B8(0xDF, 0x0)

    label("loc_44EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44FE")
    OP_B8(0xE0, 0x0)

    label("loc_44FE")

    FadeToBright(300, 0)
    OP_5F(0x0)
    TalkEnd(0xFF)

    label("loc_450D")

    Return()

    # Function_25_4323 end

    def Function_26_450E(): pass

    label("Function_26_450E")

    SetMapFlags(0x80)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(500, 0, -1)

    def lambda_452C():
        OP_90(0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_452C)
    OP_0D()
    NewScene("ED6_DT21/U7000   ._SN", 102, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_26_450E end

    def Function_27_454E(): pass

    label("Function_27_454E")

    SetMapFlags(0x80)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 16880, 1000, -14940, 135)
    SetChrPos(0x1, 16880, 1000, -14940, 135)
    SetChrPos(0x2, 16880, 1000, -14940, 135)
    SetChrPos(0x3, 16880, 1000, -14940, 135)
    OP_69(0x0, 0x0)
    Sleep(1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(300, 0)
    ClearMapFlags(0x80)
    EventEnd(0x2)
    Return()

    # Function_27_454E end

    SaveToFile()

Try(main)
