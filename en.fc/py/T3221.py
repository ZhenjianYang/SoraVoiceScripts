from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3221   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3221.x',
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
        'Mrs. Mao',                             # 9
        'Ed',                                   # 10
        'Percy',                                # 11
        'Lynn',                                 # 12
        'Recia',                                # 13
        'Cyril',                                # 14
        'Addy',                                 # 15
        'Lucky',                                # 16
        'Sima',                                 # 17
        'Quantay',                              # 18
        'Seagaro',                              # 19
        'Edel',                                 # 20
        'Eastern Man',                          # 21
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
        'ED6_DT07/CH02430 ._CH',             # 00
        'ED6_DT07/CH01270 ._CH',             # 01
        'ED6_DT07/CH01460 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01150 ._CH',             # 04
        'ED6_DT07/CH01120 ._CH',             # 05
        'ED6_DT07/CH01130 ._CH',             # 06
        'ED6_DT07/CH01160 ._CH',             # 07
        'ED6_DT07/CH01020 ._CH',             # 08
        'ED6_DT07/CH01060 ._CH',             # 09
        'ED6_DT07/CH01040 ._CH',             # 0A
        'ED6_DT07/CH01210 ._CH',             # 0B
        'ED6_DT07/CH01043 ._CH',             # 0C
        'ED6_DT07/CH01213 ._CH',             # 0D
        'ED6_DT07/CH00073 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH02430P._CP',             # 00
        'ED6_DT07/CH01270P._CP',             # 01
        'ED6_DT07/CH01460P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01150P._CP',             # 04
        'ED6_DT07/CH01120P._CP',             # 05
        'ED6_DT07/CH01130P._CP',             # 06
        'ED6_DT07/CH01160P._CP',             # 07
        'ED6_DT07/CH01020P._CP',             # 08
        'ED6_DT07/CH01060P._CP',             # 09
        'ED6_DT07/CH01040P._CP',             # 0A
        'ED6_DT07/CH01210P._CP',             # 0B
        'ED6_DT07/CH01043P._CP',             # 0C
        'ED6_DT07/CH01213P._CP',             # 0D
        'ED6_DT07/CH00073P._CP',             # 0E
    )

    DeclNpc(
        X                   = 2590,
        Z                   = 250,
        Y                   = 5360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 14070,
        Z                   = 0,
        Y                   = 2040,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )


    DeclActor(
        TriggerX            = 8960,
        TriggerZ            = 250,
        TriggerY            = 13840,
        TriggerRange        = 1000,
        ActorX              = 9100,
        ActorZ              = 1750,
        ActorY              = 13840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5290,
        TriggerZ            = 0,
        TriggerY            = 71030,
        TriggerRange        = 800,
        ActorX              = 5290,
        ActorZ              = 1000,
        ActorY              = 71030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2670,
        TriggerZ            = 250,
        TriggerY            = 3820,
        TriggerRange        = 400,
        ActorX              = 2590,
        ActorZ              = 1750,
        ActorY              = 5360,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9940,
        TriggerZ            = 0,
        TriggerY            = 90,
        TriggerRange        = 400,
        ActorX              = 8490,
        ActorZ              = 1500,
        ActorY              = 340,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_352",          # 00, 0
        "Function_1_6E3",          # 01, 1
        "Function_2_71D",          # 02, 2
        "Function_3_733",          # 03, 3
        "Function_4_757",          # 04, 4
        "Function_5_9D2",          # 05, 5
        "Function_6_CC5",          # 06, 6
        "Function_7_13F1",         # 07, 7
        "Function_8_175A",         # 08, 8
        "Function_9_1761",         # 09, 9
        "Function_10_1768",        # 0A, 10
        "Function_11_1B9F",        # 0B, 11
        "Function_12_1BA4",        # 0C, 12
        "Function_13_2157",        # 0D, 13
        "Function_14_21D4",        # 0E, 14
        "Function_15_21DB",        # 0F, 15
        "Function_16_21E2",        # 10, 16
        "Function_17_21E9",        # 11, 17
        "Function_18_21EE",        # 12, 18
        "Function_19_3402",        # 13, 19
        "Function_20_3B86",        # 14, 20
        "Function_21_46E9",        # 15, 21
        "Function_22_4A32",        # 16, 22
        "Function_23_4A75",        # 17, 23
    )


    def Function_0_352(): pass

    label("Function_0_352")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_362"),
        (109, "loc_390"),
        (SWITCH_DEFAULT, "loc_3A6"),
    )


    label("loc_362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_375")
    OP_A2(0x51D)
    Event(0, 19)

    label("loc_375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38D")
    SetMapFlags(0x10000000)
    OP_A2(0x520)
    Event(0, 20)

    label("loc_38D")

    Jump("loc_3A6")

    label("loc_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A3")
    OP_A2(0x526)
    Event(0, 21)

    label("loc_3A3")

    Jump("loc_3A6")

    label("loc_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3DC")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -30310, -250, 8840, 81)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 8490, 0, 340, 102)
    Jump("loc_6E2")

    label("loc_3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_45B")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10430, 0, 1740, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -30310, -250, 8840, 81)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -1040, 0, 40770, 2)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -28880, 0, 43500, 9)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -28740, 0, 38750, 93)
    OP_43(0x13, 0x0, 0x0, 0x3)
    Jump("loc_6E2")

    label("loc_45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4D1")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10430, 0, 1740, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -30310, -250, 8840, 81)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 8490, 0, 340, 102)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -28740, 0, 38750, 93)
    OP_43(0x13, 0x0, 0x0, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CE")
    ClearChrFlags(0x14, 0x80)

    label("loc_4CE")

    Jump("loc_6E2")

    label("loc_4D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_559")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -30310, -250, 8840, 81)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 8490, 0, 340, 102)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 12)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 11260, 150, 10650, 180)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 13)
    OP_44(0x13, 0x0)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x13, 0x4)
    SetChrPos(0x13, 11070, 150, 8460, 358)
    Jump("loc_6E2")

    label("loc_559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_5A5")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10430, 0, 1740, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -30310, -250, 8840, 81)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 8490, 0, 340, 102)
    Jump("loc_6E2")

    label("loc_5A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_643")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -30310, -250, 8840, 81)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 8490, 0, 340, 102)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -1040, 0, 40770, 2)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 12)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 11260, 150, 10650, 180)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 13)
    OP_44(0x13, 0x0)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x13, 0x4)
    SetChrPos(0x13, 11070, 150, 8460, 358)
    Jump("loc_6E2")

    label("loc_643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_679")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10430, 0, 1740, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 2230, 250, 3550, 0)
    Jump("loc_6E2")

    label("loc_679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_699")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 11910, 0, 67870, 180)
    Jump("loc_6E2")

    label("loc_699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6E2")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -30310, -250, 8840, 81)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 8490, 0, 340, 102)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -2080, 250, 6150, 195)

    label("loc_6E2")

    Return()

    # Function_0_352 end

    def Function_1_6E3(): pass

    label("Function_1_6E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FB")
    OP_B1("t3221_y")
    Jump("loc_704")

    label("loc_6FB")

    OP_B1("t3221_n")

    label("loc_704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_718")
    OP_72(0x2, 0x10)
    Jump("loc_71C")

    label("loc_718")

    OP_64(0x1, 0x1)

    label("loc_71C")

    Return()

    # Function_1_6E3 end

    def Function_2_71D(): pass

    label("Function_2_71D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_732")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_71D")

    label("loc_732")

    Return()

    # Function_2_71D end

    def Function_3_733(): pass

    label("Function_3_733")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_756")
    OP_8D(0xFE, -30720, 37410, -25780, 40750, 1500)
    Jump("Function_3_733")

    label("loc_756")

    Return()

    # Function_3_733 end

    def Function_4_757(): pass

    label("Function_4_757")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_764")
    Jump("loc_9CE")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_7F5")

    ChrTalk(    #0
        0xFE,
        (
            "It'll be back to life as usual when\x01",
            "we go home to the capital...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I'd better take it easy here\x01",
            "while I still have the chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CE")

    label("loc_7F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_8A4")

    ChrTalk(    #2
        0xFE,
        (
            "I heard a little from the staff,\x01",
            "but was there really an\x01",
            "attack in Zeiss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "News has spread here just by\x01",
            "word of mouth, so it must be\x01",
            "quite a mess in Zeiss.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CE")

    label("loc_8A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_90E")

    ChrTalk(    #4
        0xFE,
        "Ah, relaxing in the hot springs...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Gotta get my energy up for\x01",
            "the next shopping trip!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CE")

    label("loc_90E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_918")
    Jump("loc_9CE")

    label("loc_918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_9B3")

    ChrTalk(    #6
        0xFE,
        (
            "I bought a couple of the cutest\x01",
            "plates today without even\x01",
            "thinking about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "There are still things to see in\x01",
            "that souvenir shop, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CE")

    label("loc_9B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_9BD")
    Jump("loc_9CE")

    label("loc_9BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_9C7")
    Jump("loc_9CE")

    label("loc_9C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9CE")

    label("loc_9CE")

    TalkEnd(0xFE)
    Return()

    # Function_4_757 end

    def Function_5_9D2(): pass

    label("Function_5_9D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_9DF")
    Jump("loc_CC1")

    label("loc_9DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_A85")

    ChrTalk(    #8
        0xFE,
        (
            "After talking it over with my wife,\x01",
            "I've decided to stay here for a\x01",
            "bit longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I plan to get back just before the\x01",
            "queen's birthday celebrations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC1")

    label("loc_A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_A8F")
    Jump("loc_CC1")

    label("loc_A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_ACC")

    ChrTalk(    #10
        0xFE,
        "I think I'll take a quick morning dip.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0E")

    label("loc_ACC")

    OP_A2(0xA)

    ChrTalk(    #11
        0xFE,
        "Are you leaving already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "We're going to stay longer.\x02",
    )

    CloseMessageWindow()

    label("loc_B0E")

    Jump("loc_CC1")

    label("loc_B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_B1B")
    Jump("loc_CC1")

    label("loc_B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_CA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_BD8")

    ChrTalk(    #13
        0xFE,
        (
            "The minute I take my eyes off\x01",
            "her, my wife goes scurrying to\x01",
            "the gift shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "There's nothing wrong with the\x01",
            "shopping itself, but I wish she'd\x01",
            "show more restraint.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA3")

    label("loc_BD8")

    OP_A2(0xA)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0xFE,
        (
            "The minute I take my eyes off\x01",
            "her, my wife goes scurrying to\x01",
            "the gift shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "There's nothing wrong with the\x01",
            "shopping itself, but I wish she'd\x01",
            "show more restraint.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA3")

    Jump("loc_CC1")

    label("loc_CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_CB0")
    Jump("loc_CC1")

    label("loc_CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_CBA")
    Jump("loc_CC1")

    label("loc_CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_CC1")

    label("loc_CC1")

    TalkEnd(0xFE)
    Return()

    # Function_5_9D2 end

    def Function_6_CC5(): pass

    label("Function_6_CC5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_E76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D9B")

    ChrTalk(    #17
        0xFE,
        (
            "Ah, it's nice to have some down\x01",
            "time for a change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "May as well make the most\x01",
            "of it and check my stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "You never know when the next\x01",
            "batch of customers will walk\x01",
            "through the door.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E73")

    label("loc_D9B")

    OP_A2(0x2)

    ChrTalk(    #20
        0xFE,
        (
            "Ah, it's nice to have some down\x01",
            "time for a change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "Still though, why do people always\x01",
            "come on the same days?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "If they'd just stagger their visits\x01",
            "they'd have more room in the\x01",
            "springs for themselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E73")

    Jump("loc_13ED")

    label("loc_E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_EF3")

    ChrTalk(    #23
        0xFE,
        (
            "So, is the investigation coming\x01",
            "along smoothly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "I'm busy as usual here. Then again,\x01",
            "it's always just me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13ED")

    label("loc_EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_FB6")

    ChrTalk(    #25
        0xFE,
        (
            "Oh, so it's my turn for\x01",
            "your questions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Word's spread already. Something was\x01",
            "stolen from the central factory, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "You bracers sure are a hard workin'\x01",
            "bunch of people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13ED")

    label("loc_FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1013")

    ChrTalk(    #28
        0xFE,
        "Are you leaving already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "When you have some time off,\x01",
            "come and visit us!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13ED")

    label("loc_1013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_112E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_10B4")

    ChrTalk(    #30
        0xFE,
        (
            "This Eastern cooking's not\x01",
            "only good, but healthy too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "It takes more time to prepare,\x01",
            "but it's worth it when you sit\x01",
            "down and eat it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_112B")

    label("loc_10B4")

    OP_A2(0x2)

    ChrTalk(    #32
        0xFE,
        "Off to the bath? Enjoy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "I'll be preparing your exotic\x01",
            "Eastern dinner while you're\x01",
            "freshening up in there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112B")

    Jump("loc_13ED")

    label("loc_112E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_123E")

    ChrTalk(    #34
        0xFE,
        (
            "Sorry about that little problem\x01",
            "we had before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "I was relieved to hear that the\x01",
            "guest was okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Which is all well and good, but\x01",
            "I should get dinner cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "We're going to have much better\x01",
            "business now that we've finally\x01",
            "got customers coming.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13ED")

    label("loc_123E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_12D0")

    ChrTalk(    #38
        0xFE,
        (
            "I can't believe there are bracers here.\x01",
            "That makes me feel a lot better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "I leave the customer's safety in\x01",
            "your capable hands!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13ED")

    label("loc_12D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_12DA")
    Jump("loc_13ED")

    label("loc_12DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_13ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_135D")

    ChrTalk(    #40
        0xFE,
        (
            "It's nice to have slow days like\x01",
            "this sometimes...but every day\x01",
            "would be bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "People love their luxury.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13ED")

    label("loc_135D")

    OP_A2(0x2)

    ChrTalk(    #42
        0xFE,
        "What a quiet day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Days like this are nice from\x01",
            "time to time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "If every day was like this though,\x01",
            "it would be bad for business.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13ED")

    TalkEnd(0xFE)
    Return()

    # Function_6_CC5 end

    def Function_7_13F1(): pass

    label("Function_7_13F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_13FE")
    Jump("loc_1756")

    label("loc_13FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_14CC")

    ChrTalk(    #45
        0xFE,
        "I feel all rested up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "I get the feeling that if I cast\x01",
            "some bait, I'll catch the\x01",
            "biggest fish of my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "But it won't last. I better get\x01",
            "fishing while I still feel this\x01",
            "motivated!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1756")

    label("loc_14CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1548")

    ChrTalk(    #48
        0xFE,
        (
            "I heard you mention it, but was\x01",
            "there some kind of incident\x01",
            "in Zeiss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Hmph.\x01",
            "What's the world coming to?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1756")

    label("loc_1548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1552")
    Jump("loc_1756")

    label("loc_1552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_15E6")

    ChrTalk(    #50
        0xFE,
        (
            "Are you all staying the night\x01",
            "here as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "You should really try the outdoor\x01",
            "bath at least once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "It made a fan out of me!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1756")

    label("loc_15E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_15F0")
    Jump("loc_1756")

    label("loc_15F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_174F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_16CE")

    ChrTalk(    #53
        0xFE,
        (
            "Even when you can't get into the\x01",
            "bath, there's lots of stuff you can\x01",
            "go do around here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "The big draw of the Maple Leaf\x01",
            "Inn is its cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "It's heaven. I can hardly wait\x01",
            "for dinnertime!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_174C")

    label("loc_16CE")

    OP_A2(0x1)

    ChrTalk(    #56
        0xFE,
        (
            "It seems like the pump that \x01",
            "carries the water is broken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Well, this is an old resort town.\x01",
            "Those things happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_174C")

    Jump("loc_1756")

    label("loc_174F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1756")

    label("loc_1756")

    TalkEnd(0xFE)
    Return()

    # Function_7_13F1 end

    def Function_8_175A(): pass

    label("Function_8_175A")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_8_175A end

    def Function_9_1761(): pass

    label("Function_9_1761")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_9_1761 end

    def Function_10_1768(): pass

    label("Function_10_1768")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1775")
    Jump("loc_1B9B")

    label("loc_1775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_189E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1810")

    ChrTalk(    #58
        0xFE,
        (
            "I hope the criminals behind the\x01",
            "factory attack are found and\x01",
            "arrested soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "We can't just let people like\x01",
            "that run around free!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189B")

    label("loc_1810")

    OP_A2(0x5)

    ChrTalk(    #60
        0xFE,
        "Hello there. Still busy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "I heard about you guys from Ed.\x01",
            "So, you're all bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Well, good luck. We're rooting\x01",
            "for you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_189B")

    Jump("loc_1B9B")

    label("loc_189E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_18A8")
    Jump("loc_1B9B")

    label("loc_18A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_18B2")
    Jump("loc_1B9B")

    label("loc_18B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_18BC")
    Jump("loc_1B9B")

    label("loc_18BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_19E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_END)), "loc_18FD")

    ChrTalk(    #63
        0xFE,
        "Hi there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "The Yuzu room is next door.\x02",
    )

    CloseMessageWindow()
    Jump("loc_19E2")

    label("loc_18FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_196D")

    ChrTalk(    #65
        0xFE,
        "I need to turn the beds down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "And I need to get dinner ready\x01",
            "before the customers return...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E2")

    label("loc_196D")

    OP_A2(0x5)

    ChrTalk(    #67
        0xFE,
        (
            "The pump's been fixed?\x01",
            "That's wonderful news!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "We're so indebted to the people\x01",
            "from the central factory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E2")

    Jump("loc_1B9B")

    label("loc_19E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1AE8")

    ChrTalk(    #69
        0xFE,
        "I've got this problem...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "It seems the pump for the hot\x01",
            "springs is broken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "If we don't hurry and fix it, we risk\x01",
            "losing a lot of our customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "I mean, this IS a hot springs resort.\x01",
            "The operative word here being 'hot.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B91")

    label("loc_1AE8")

    OP_A2(0x5)

    ChrTalk(    #73
        0xFE,
        "Welcome to the Maple Leaf Inn!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "All of our rooms have special names.\x01",
            "This is the Yuzu room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "I feel the names are so much more\x01",
            "personal than 'Room 201.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B91")

    Jump("loc_1B9B")

    label("loc_1B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1B9B")

    label("loc_1B9B")

    TalkEnd(0xFE)
    Return()

    # Function_10_1768 end

    def Function_11_1B9F(): pass

    label("Function_11_1B9F")

    Call(0, 12)
    Return()

    # Function_11_1B9F end

    def Function_12_1BA4(): pass

    label("Function_12_1BA4")

    TalkBegin(0xE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                              # 0
            "Shop\x01",                              # 1
            "[Wild Veggie Pot] - 700 mira\x01",      # 2
            "Leave\x01",                             # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C21")
    OP_0D()
    OP_A9(0x46)
    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_1C21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D2F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1CF5")
    SubMira(700)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #76
        "\x06\x07\x00Ate \x07\x02Wild Veggie Pot\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x2BC)
    OP_31(0x1, 0xFD, 0x2BC)
    OP_31(0x2, 0xFD, 0x2BC)
    OP_31(0x3, 0xFD, 0x2BC)
    OP_31(0x4, 0xFD, 0x2BC)
    OP_31(0x5, 0xFD, 0x2BC)
    OP_31(0x6, 0xFD, 0x2BC)
    OP_31(0x7, 0xFD, 0x2BC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CE7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x4)"), scpexpr(EXPR_END)), "loc_1CB6")
    Jump("loc_1CE7")

    label("loc_1CB6")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #77
        "\x06\x07\x00Learned '\x07\x02Wild Veggie Pot\x07\x00' recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_1CE7")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_1D1D")

    label("loc_1CF5")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #78
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_1D1D")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xE)
    Return()

    label("loc_1D2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D40")
    TalkEnd(0xE)
    Return()

    label("loc_1D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1E45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1DBD")

    ChrTalk(    #79
        0xE,
        (
            "Let's get this cleaning out of\x01",
            "the way right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xE,
        (
            "We'll be full of customers before\x01",
            "we can blink.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E42")

    label("loc_1DBD")

    OP_A2(0x6)

    ChrTalk(    #81
        0xE,
        (
            "Hello!\x01",
            "Welcome to the Maple Leaf Inn!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xE,
        (
            "We welcome everyone, especially\x01",
            "those en route to the royal birthday\x01",
            "festivities!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E42")

    Jump("loc_2153")

    label("loc_1E45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1E4F")
    Jump("loc_2153")

    label("loc_1E4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1F02")

    ChrTalk(    #83
        0xE,
        (
            "All people wanted to talk about\x01",
            "today was that incident in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xE,
        (
            "Here they are in a great resort\x01",
            "and that's what they all want\x01",
            "to discuss...how sad for them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2153")

    label("loc_1F02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1F43")

    ChrTalk(    #85
        0xE,
        "What? Leaving so soon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xE,
        "Come back again soon!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2153")

    label("loc_1F43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1FCC")

    ChrTalk(    #87
        0xE,
        (
            "Our exotic Eastern cooking tastes\x01",
            "even better after a long, hot bath!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xE,
        (
            "Make sure you sweat yourselves\x01",
            "up an appetite!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2153")

    label("loc_1FCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_END)), "loc_202E")

    ChrTalk(    #89
        0xE,
        (
            "I need to go help prepare\x01",
            "dinner soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xE,
        (
            "We have many authentic\x01",
            "Eastern dishes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2153")

    label("loc_202E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_20B9")

    ChrTalk(    #91
        0xE,
        (
            "I heard little Tita is here to\x01",
            "fix the pump.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xE,
        "She's such an amazing girl!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xE,
        (
            "I can't even change an orbal\x01",
            "light bulb.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2153")

    label("loc_20B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_20C3")
    Jump("loc_2153")

    label("loc_20C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_20CD")
    Jump("loc_2153")

    label("loc_20CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2153")

    ChrTalk(    #94
        0xE,
        (
            "Hello, and welcome to the\x01",
            "Maple Leaf Inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xE,
        (
            "We also have authentic Eastern\x01",
            "cuisine. We hope you have a\x01",
            "wonderful time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2153")

    TalkEnd(0xE)
    Return()

    # Function_12_1BA4 end

    def Function_13_2157(): pass

    label("Function_13_2157")

    TalkBegin(0xFE)

    ChrTalk(    #96
        0xFE,
        (
            "#073FThis food is VERY authentic.\x02\x03",

            "#070FStill, I've come all this way.\x01",
            "I should like to try some\x01",
            "Liberl cooking.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_2157 end

    def Function_14_21D4(): pass

    label("Function_14_21D4")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_14_21D4 end

    def Function_15_21DB(): pass

    label("Function_15_21DB")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_15_21DB end

    def Function_16_21E2(): pass

    label("Function_16_21E2")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_16_21E2 end

    def Function_17_21E9(): pass

    label("Function_17_21E9")

    Call(0, 18)
    Return()

    # Function_17_21E9 end

    def Function_18_21EE(): pass

    label("Function_18_21EE")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_224E")
    OP_0D()
    OP_A9(0x45)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_224E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_225F")
    TalkEnd(0x8)
    Return()

    label("loc_225F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2928")
    EventBegin(0x0)
    OP_A2(0x525)
    OP_28(0x40, 0x1, 0x800)
    OP_28(0x40, 0x4, 0x10)
    Fade(1000)
    OP_8C(0x8, 180, 0)
    SetChrPos(0x101, 1810, 250, 3490, 45)
    SetChrPos(0x102, 2500, 250, 2380, 0)
    SetChrPos(0x107, 3160, 250, 3550, 0)
    OP_6D(2080, 250, 5120, 0)
    OP_0D()

    ChrTalk(    #97
        0x8,
        (
            "#680FThank you, Tita!\x02\x03",

            "The pump's pumping like it was\x01",
            "just installed yesterday!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x107,
        (
            "#067FHee hee. Really?\x02\x03",

            "Please think nothing of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        (
            "#681FWell, haven't you grown into such\x01",
            "a well mannered young lady?\x02\x03",

            "#680FAnd thank you two for helping us\x01",
            "out with that guest, as well.\x02\x03",

            "You guys know everyone,\x01",
            "it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#506F#3PHa ha, I guess we do...\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x107, 270, 400)

    ChrTalk(    #101
        0x107,
        "#064FWhat happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x102,
        "#010F#3PA little bracer business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        (
            "#681FYou two have my thanks.\x02\x03",

            "As a way to pay you back, I'd\x01",
            "like you to stay here free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#004F#3PNo way! Really?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 0, 400)

    ChrTalk(    #105
        0x107,
        (
            "#065FMa'am?\x02\x03",

            "We didn't tell my grandfather we\x01",
            "were going to stay here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        (
            "#680FNonsense. I heard from Russell\x01",
            "a little earlier.\x02\x03",

            "He said the job would take him\x01",
            "until tomorrow to finish, and he\x01",
            "asked if you could stay here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x107,
        "#064FGrandpa said that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#006F#3PWhat a sweet old guy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        (
            "#019F#3PWell, if he said that, then I'm\x01",
            "afraid we have no choice but\x01",
            "to impose for the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x8,
        (
            "#680FCome right in.\x02\x03",

            "You can put your things in the\x01",
            "Yuzu room on the second floor.\x02\x03",

            "It'll be some time before dinner,\x01",
            "so go take a dip in the hot springs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#505F#3PYou want us to take a bath\x01",
            "before dinner?\x02\x03",

            "I thought people took their baths\x01",
            "before they went to sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x8,
        (
            "#681FWhat are you talking about?\x01",
            "This is a HOT SPRINGS resort!\x02\x03",

            "People expect you to jump\x01",
            "in the bath in the morning,\x01",
            "at lunch...whenever!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)

    ChrTalk(    #113
        0x107,
        (
            "#061FI'd be okay with three baths\x01",
            "a day here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        (
            "#008F#3PR-Really?\x02\x03",

            "Well, I like baths as much as\x01",
            "anybody, but it sounds a little\x01",
            "bit much for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x102,
        (
            "#010F#3PHa ha. Shall we go put our bags\x01",
            "in our room, then?\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_33FE")

    label("loc_2928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2BDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2993")

    ChrTalk(    #116
        0x8,
        (
            "#680FCome back and stay with us\x01",
            "any time you want!\x02\x03",

            "Have a safe trip to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDB")

    label("loc_2993")

    OP_A2(0x0)

    ChrTalk(    #117
        0x8,
        (
            "#683FHello, you all. Any luck catching\x01",
            "your target?\x02\x03",

            "#680FIf so, why not take a break and\x01",
            "stay for a while?\x02\x03",

            "We have a reservation only\x01",
            "outdoor bath for customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#506FThat sounds so lovely, but...\x02\x03",

            "We've got to get to the\x01",
            "capital right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x102,
        (
            "#010FAs always, we appreciate\x01",
            "your hospitality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x8,
        (
            "#681FNo, no, don't worry! Think of it\x01",
            "as payback from before!\x02\x03",

            "#680FAnd Tita's off to help Russell\x01",
            "again, no doubt?\x02\x03",

            "You tell him I said not to\x01",
            "overwork that poor girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        (
            "#003FUh...\x02\x03",

            "#501F...Okay!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x102,
        "#010FWe'll tell him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        "#680FHave a safe trip to the capital!\x02",
    )

    CloseMessageWindow()

    label("loc_2BDB")

    Jump("loc_33FE")

    label("loc_2BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2C93")

    ChrTalk(    #124
        0x8,
        (
            "#680FHello again, everybody.\x02\x03",

            "Just running all over looking\x01",
            "for your criminals, aren't you?\x02\x03",

            "I'm sorry to say we haven't\x01",
            "got any clues or heard any\x01",
            "more information.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FE")

    label("loc_2C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2DEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2D37")

    ChrTalk(    #125
        0x8,
        (
            "#680FI heard about the burglary at\x01",
            "the central factory. It had\x01",
            "me a little bit worried.\x02\x03",

            "Still, these things do happen.\x01",
            "A shame, but still...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE8")

    label("loc_2D37")

    OP_A2(0x0)

    ChrTalk(    #126
        0x8,
        (
            "#682FHello! How have you been?\x02\x03",

            "I heard about the burglary at\x01",
            "the central factory. It had\x01",
            "me a little bit worried.\x02\x03",

            "Still, these things do happen.\x01",
            "A shame, but still...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DE8")

    Jump("loc_33FE")

    label("loc_2DEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2E48")

    ChrTalk(    #127
        0x8,
        (
            "#680FWhat's the matter?\x02\x03",

            "Did you want to have another\x01",
            "dip in the hot springs?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FE")

    label("loc_2E48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_2EDE")

    ChrTalk(    #128
        0x8,
        (
            "#680FThe bath is separate from the\x01",
            "hotel. Go through the restaurant\x01",
            "to get there.\x02\x03",

            "We're especially proud of that\x01",
            "outdoor bath. Enjoy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FE")

    label("loc_2EDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_327D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_END)), "loc_2F64")

    ChrTalk(    #129
        0x8,
        (
            "#680FYou're all in the Yuzu room,\x01",
            "on the second floor.\x02\x03",

            "Drop off your things and go enjoy\x01",
            "a bath before dinner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_327A")

    label("loc_2F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 5)), scpexpr(EXPR_END)), "loc_301D")

    ChrTalk(    #130
        0x8,
        (
            "#680FThat girl is just like Russell...\x01",
            "Put her in front of a machine\x01",
            "and she just won't stop.\x02\x03",

            "Sorry to be an imposition,\x01",
            "but could you go check\x01",
            "on the pump shed for me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_327A")

    label("loc_301D")

    OP_A2(0x58D)

    ChrTalk(    #131
        0x8,
        (
            "#680FGood work, you all.\x02\x03",

            "Did you know that guest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#506FAh...ha...ha...\x01",
            "Unfortunately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x102,
        (
            "#010FIt looks like the pump repairs\x01",
            "are complete.\x02\x03",

            "The front well should fill back up\x01",
            "with hot water soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x8,
        (
            "#680FIs that right, now?\x02\x03",

            "But Tita hasn't come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#000FAh, yeah. Guess we should've\x01",
            "gone to the pump shed first,\x01",
            "before reporting back here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x102,
        "#010FWell, let's go, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x8,
        (
            "#680FPlease do.\x02\x03",

            "That girl is just like Russell...\x01",
            "Put her in front of a machine\x01",
            "and she just won't stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        "#506FIsn't that the truth!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x102,
        "#010FWe'll go have a look.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x8,
        "#680FOkay. Thanks again.\x02",
    )

    CloseMessageWindow()

    label("loc_327A")

    Jump("loc_33FE")

    label("loc_327D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_32E6")

    ChrTalk(    #141
        0x8,
        (
            "#680FI'll trust you two to fix it.\x02\x03",

            "Head on out and see if you can\x01",
            "bring that guest back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FE")

    label("loc_32E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3366")

    ChrTalk(    #142
        0x8,
        (
            "#680FWhat, did you forget where the\x01",
            "pump is?\x02\x03",

            "It's in a shed up north past the\x01",
            "town square.\x02\x03",

            "Good luck, you all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FE")

    label("loc_3366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_33FE")

    ChrTalk(    #143
        0x8,
        (
            "#680FWelcome, everyone! This is the\x01",
            "famous Maple Leaf Inn.\x02\x03",

            "We have lots of fine springs,\x01",
            "including our famous Eastern-\x01",
            "style outdoor bath!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33FE")

    TalkEnd(0x8)
    Return()

    # Function_18_21EE end

    def Function_19_3402(): pass

    label("Function_19_3402")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(560, 250, 2580, 0)
    SetChrPos(0x101, 490, 0, -1490, 0)
    SetChrPos(0x102, 2040, 0, -1370, 0)
    SetChrPos(0x107, 1200, 0, -430, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #144
        0x107,
        "#061FHi, Mrs. Mao!\x02",
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #145
        0x8,
        (
            "#681FOh, hello, Tita.\x01",
            "I'm glad you're here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34C6():
        OP_6D(2050, 250, 4540, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_34C6)

    def lambda_34DE():
        OP_8E(0xFE, 0xA78, 0xFA, 0xDCA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_34DE)
    Sleep(500)

    def lambda_34FE():
        OP_8E(0xFE, 0xDF2, 0xFA, 0xA5A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_34FE)
    Sleep(300)

    def lambda_351E():
        OP_8E(0xFE, 0x8CA, 0xFA, 0x9D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_351E)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x8, 0)

    ChrTalk(    #146
        0x8,
        (
            "#680FMr. Murdock just got in touch\x01",
            "with me a little while ago.\x02\x03",

            "Is it true that the professor is\x01",
            "making you do the repairs while\x01",
            "he's off doing Aidios-knows-what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x107,
        (
            "#065FI-It's not like that...\x02\x03",

            "He was planning to come\x01",
            "here until I said some-\x01",
            "thing about it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        (
            "#680FAwww, well, bless your\x01",
            "heart, child!\x02\x03",

            "But you know you spoil that\x01",
            "old coot, don't you?\x02\x03",

            "He's always been the sort to\x01",
            "completely lose himself in his\x01",
            "research, given half the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x107,
        "#067FUm, ha ha ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#506F(Energetic old granny, isn't she?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x102,
        (
            "#010F(Well, she obviously knows\x01",
            "the professor.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x8,
        "#683FAnd who might you be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x107,
        (
            "#560FOh, let me introduce you...\x02\x03",

            "This is Estelle,\x01",
            "and this is Joshua...\x02\x03",

            "They're with the Bracer Guild,\x01",
            "and they're looking out for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        "#006FHello...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x102,
        "#010FIt's nice to meet you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x8,
        (
            "#681FWell, what do you know?\x01",
            "Please, do pardon me.\x02\x03",

            "#680FI'm the owner of the Maple Leaf Inn.\x01",
            "You can call me Mrs. Mao.\x02\x03",

            "Russell and I have been friends since we\x01",
            "were knee-high to a grasshopper. Tita\x01",
            "here is almost like my own granddaughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        "#501FOhh, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x107,
        (
            "#067FHee hee...\x02\x03",

            "#064FOh, right. Mrs. Mao...\x02\x03",

            "Is the orbal pump really broken?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x8,
        (
            "#682FI'm afraid so, dear.\x02\x03",

            "I think the forty-year-old beast\x01",
            "may finally be on its last legs...\x02\x03",

            "Ah, well. I wanted to replace\x01",
            "it at some point, anyway.\x02\x03",

            "Can you handle it, Tita?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x107,
        "#061FYou bet'cha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x8,
        "#680FOkay. Just a sec.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #162
        "\x07\x00Received \x07\x02Pump Shed Key\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x369, 1)

    ChrTalk(    #163
        0x8,
        (
            "#680FJust go north of the village\x01",
            "square, up the hill. The pump\x01",
            "shed's right there.\x02\x03",

            "I really appreciate it.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x40, 0x1, 0x4)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_19_3402 end

    def Function_20_3B86(): pass

    label("Function_20_3B86")

    EventBegin(0x0)
    OP_6D(560, 250, 2580, 0)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x101, 490, 0, -1490, 0)
    SetChrPos(0x102, 2040, 0, -1370, 0)
    FadeToBright(1000, 0)

    def lambda_3BCF():
        OP_6D(1770, 250, 5380, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3BCF)

    def lambda_3BE7():
        OP_8E(0xFE, 0x92E, 0xFA, 0xDA2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BE7)

    def lambda_3C02():
        OP_8E(0xFE, 0xE38, 0xFA, 0xD84, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C02)
    OP_0D()
    OP_4A(0x8, 255)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #164
        0x8,
        (
            "#683FHello again.\x01",
            "How's Tita doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        (
            "#000FShe's hard at work.\x02\x03",

            "We figured we'd probably\x01",
            "just get in the way, so\x01",
            "we'll stay here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x8,
        (
            "#681FHa ha ha. Well, you just\x01",
            "might be right, at that.\x02\x03",

            "She's almost as talented as\x01",
            "Russell himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        (
            "#501FHard to argue with that after\x01",
            "watching her at work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x102,
        (
            "#010FI'm just amazed that she's\x01",
            "working at the central factory\x01",
            "at her age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x8,
        (
            "#680FAnd no matter what, she's\x01",
            "always so sweet. Always has a\x01",
            "smile for everyone.\x02\x03",

            "But get her in front of a machine,\x01",
            "and she'll tinker with it for hours.\x01",
            "She loves it.\x02\x03",

            "She's just a fine girl.\x02\x03",

            "#682FBut still...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        "#004FWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x8,
        "#680FOh...it's nothing.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, 970, 0, -2050, 0)
    OP_4A(0x9, 255)

    ChrTalk(    #172
        0x9,
        "#2PHey! Missus Mao!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3F3E():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F3E)

    def lambda_3F4C():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F4C)

    def lambda_3F5A():
        OP_6D(1070, 250, 4930, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3F5A)

    def lambda_3F72():

        label("loc_3F72")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3F72")

    QueueWorkItem2(0x101, 1, lambda_3F72)

    def lambda_3F83():

        label("loc_3F83")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3F83")

    QueueWorkItem2(0x102, 1, lambda_3F83)

    def lambda_3F94():
        OP_8E(0xFE, 0xD02, 0xFA, 0xA1E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F94)
    ClearChrFlags(0x9, 0x80)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3FBF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3FBF)
    OP_8E(0x9, 0x7C6, 0xFA, 0xDC0, 0xBB8, 0x0)
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #173
        0x8,
        (
            "#683FWelcome back, Ed.\x02\x03",

            "What's gotten you all\x01",
            "frothing at the mouth?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x9,
        (
            "#1PI...umm...wanted to ask\x01",
            "you something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x9,
        "#1PDid that lady from Grancel leave?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x8,
        (
            "#680FHmm... A lady from Grancel...?\x01",
            "Oh, the guest from yesterday.\x02\x03",

            "She went out for a walk, but\x01",
            "she hasn't come back yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x9,
        "#1PI thought so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x9,
        "#1PUgh... This is awkward.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x8,
        "#683FWhat? Isn't she in the village?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x9,
        "#1PUmm...weeeell...actually...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x9,
        "#1PI saw her by the village gate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x9,
        (
            "#1PShe said she was going to\x01",
            "go and take in the scenery,\x01",
            "or something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x8,
        (
            "#682FOut on the plains? She'd have\x01",
            "to be a fool to go where all\x01",
            "the monsters are...\x02\x03",

            "#684FYou complete idiot!\x01",
            "Why didn't you stop her?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #184
        0x9,
        "#1PI did! I mean, I tried!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x9,
        "#1PShe just wouldn't listen!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x9,
        (
            "#1PI don't know how seriously\x01",
            "she took what I said, but\x01",
            "I'm worried.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0x102)

    ChrTalk(    #187
        0x101,
        "#002FUmmm...pardon me?\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 400)
    OP_8C(0x8, 135, 400)

    ChrTalk(    #188
        0x9,
        "#1PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x9,
        "#1PAre you new guests?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x102,
        (
            "#012F#2PDo you remember what time you\x01",
            "saw that lady by the gate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x9,
        (
            "#1PHmmm... I think it was\x01",
            "right around noon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x9,
        (
            "#1PAt least, that's about when\x01",
            "I got back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x101,
        (
            "#006FNoon... Yeah, I think we\x01",
            "can catch up with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x102,
        (
            "#010F#2PWe should get going, before\x01",
            "it's too late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x9,
        "#1PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        (
            "#006FWell, we're bracers, if you\x01",
            "couldn't tell by looking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x102,
        (
            "#010F#2PWe'll head out into the\x01",
            "plains and find this girl.\x01",
            "Don't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x9,
        "#1PNo kidding?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x9,
        (
            "#1PWhat a stroke of luck!\x01",
            "Yes, please!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    ChrTalk(    #200
        0x8,
        (
            "#684FYou've no right to even\x01",
            "ask for their help!\x02\x03",

            "#682FBut fine. The guest's safety\x01",
            "is paramount!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 135, 400)

    ChrTalk(    #201
        0x8,
        (
            "#682FI hate to impose on you two, but\x01",
            "please look after my guest.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #202
        0x101,
        "#006FWill do!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x102,
        "#010F#2PWe'll be going now.\x02",
    )

    CloseMessageWindow()
    OP_28(0x40, 0x1, 0x20)
    OP_28(0x40, 0x1, 0x40)
    ClearMapFlags(0x10000000)
    EventEnd(0x0)
    OP_8C(0x8, 180, 0)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    Return()

    # Function_20_3B86 end

    def Function_21_46E9(): pass

    label("Function_21_46E9")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(28000, 0, 40030, 0)
    SetChrPos(0x101, 33900, 0, 44790, 180)
    SetChrPos(0x102, 34550, 0, 44500, 180)
    SetChrPos(0x107, 33460, 0, 45000, 180)
    FadeToBright(1000, 0)

    def lambda_4743():
        OP_6D(32210, 0, 43130, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4743)
    OP_8E(0x101, 0x8476, 0x0, 0xA53C, 0x7D0, 0x0)
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8C(0x101, 90, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #204
        0x101,
        "#501F#1PWow... Nice room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x102,
        "#010F#4PIndeed. \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x107,
        (
            "#060FMrs. Mao told me that\x01",
            "she was born off to the east.\x02\x03",

            "She moved to Liberl with her\x01",
            "family when she was little.\x02\x03",

            "The village has a lot of\x01",
            "people from the same area.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #207
        0x101,
        (
            "#006F#1PI THOUGHT this village had\x01",
            "a kind of unusual vibe.\x02\x03",

            "I'll bet the food here\x01",
            "must be really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x102,
        (
            "#010F#4PYeah.\x02\x03",

            "But before that, why don't we\x01",
            "check out the spa we've been\x01",
            "hearing about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        (
            "#501F#1PHey, yeah!\x02\x03",

            "#001FDid you want to join us,\x01",
            "Tita?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x107,
        "#067FO-Okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x102,
        (
            "#010F#4PWe can go after we put\x01",
            "away our luggage.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_49C0():
        OP_8E(0xFE, 0x7C6A, 0x0, 0x9C0E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_49C0)
    Sleep(100)

    def lambda_49E0():
        OP_8E(0xFE, 0x8070, 0x0, 0x9EAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_49E0)
    Sleep(300)

    def lambda_4A00():
        OP_8E(0xFE, 0x8070, 0x0, 0x9EAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4A00)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3223   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_46E9 end

    def Function_22_4A32(): pass

    label("Function_22_4A32")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #212
        "\x07\x05Open-Air Bath ⇒\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_22_4A32 end

    def Function_23_4A75(): pass

    label("Function_23_4A75")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #213
        (
            "\x07\x05A card hangs on the door. It says,\x01",
            "'Sleeping. Do Not Disturb.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_23_4A75 end

    SaveToFile()

Try(main)
