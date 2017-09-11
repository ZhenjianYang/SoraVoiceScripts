from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3201   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3201.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Dorothy',                              # 9
        'Mrs. Mao',                             # 10
        'Percy',                                # 11
        'Ed',                                   # 12
        'Lynn',                                 # 13
        'Recia',                                # 14
        'Cyril',                                # 15
        'Addy',                                 # 16
        'Lucky',                                # 17
        'Sima',                                 # 18
        'Quantay',                              # 19
        'Seagaro',                              # 20
        'Edel',                                 # 21
        'Tratt Plains Road',                    # 22
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
        'ED6_DT07/CH02070 ._CH',             # 00
        'ED6_DT07/CH02430 ._CH',             # 01
        'ED6_DT07/CH02300 ._CH',             # 02
        'ED6_DT07/CH02310 ._CH',             # 03
        'ED6_DT07/CH02290 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01270 ._CH',             # 06
        'ED6_DT07/CH01030 ._CH',             # 07
        'ED6_DT07/CH01150 ._CH',             # 08
        'ED6_DT07/CH01120 ._CH',             # 09
        'ED6_DT07/CH01130 ._CH',             # 0A
        'ED6_DT07/CH01160 ._CH',             # 0B
        'ED6_DT07/CH01020 ._CH',             # 0C
        'ED6_DT07/CH01060 ._CH',             # 0D
        'ED6_DT07/CH01040 ._CH',             # 0E
        'ED6_DT07/CH01210 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH02070P._CP',             # 00
        'ED6_DT07/CH02430P._CP',             # 01
        'ED6_DT07/CH02300P._CP',             # 02
        'ED6_DT07/CH02310P._CP',             # 03
        'ED6_DT07/CH02290P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01270P._CP',             # 06
        'ED6_DT07/CH01030P._CP',             # 07
        'ED6_DT07/CH01150P._CP',             # 08
        'ED6_DT07/CH01120P._CP',             # 09
        'ED6_DT07/CH01130P._CP',             # 0A
        'ED6_DT07/CH01160P._CP',             # 0B
        'ED6_DT07/CH01020P._CP',             # 0C
        'ED6_DT07/CH01060P._CP',             # 0D
        'ED6_DT07/CH01040P._CP',             # 0E
        'ED6_DT07/CH01210P._CP',             # 0F
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 2590,
        Z                   = 250,
        Y                   = 5360,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -30790,
        Z                   = -2000,
        Y                   = 15330,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 28950,
        Y                   = 1000,
        Z                   = 4030,
        Range               = 2500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = 980,
        Y                   = -250,
        Z                   = 18420,
        Range               = 1250,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 20,
    )

    DeclEvent(
        X                   = 42330,
        Y                   = 5750,
        Z                   = 36020,
        Range               = 1250,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 21,
    )


    DeclActor(
        TriggerX            = 40000,
        TriggerZ            = 6000,
        TriggerY            = 49730,
        TriggerRange        = 800,
        ActorX              = 40000,
        ActorZ              = 7000,
        ActorY              = 49730,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 42130,
        TriggerZ            = 0,
        TriggerY            = -860,
        TriggerRange        = 1250,
        ActorX              = 44880,
        ActorZ              = 3000,
        ActorY              = 1020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_392",          # 00, 0
        "Function_1_614",          # 01, 1
        "Function_2_665",          # 02, 2
        "Function_3_67B",          # 03, 3
        "Function_4_8F2",          # 04, 4
        "Function_5_B1D",          # 05, 5
        "Function_6_C47",          # 06, 6
        "Function_7_C4E",          # 07, 7
        "Function_8_C55",          # 08, 8
        "Function_9_10E2",         # 09, 9
        "Function_10_10E9",        # 0A, 10
        "Function_11_10F0",        # 0B, 11
        "Function_12_14FE",        # 0C, 12
        "Function_13_1505",        # 0D, 13
        "Function_14_190C",        # 0E, 14
        "Function_15_1F70",        # 0F, 15
        "Function_16_3677",        # 10, 16
        "Function_17_36C6",        # 11, 17
        "Function_18_3803",        # 12, 18
        "Function_19_389C",        # 13, 19
        "Function_20_38A0",        # 14, 20
        "Function_21_38A4",        # 15, 21
    )


    def Function_0_392(): pass

    label("Function_0_392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3A0")
    OP_A3(0x3FA)
    Event(0, 15)

    label("loc_3A0")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_3AC"),
        (SWITCH_DEFAULT, "loc_3C2"),
    )


    label("loc_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BF")
    OP_A2(0x527)
    Event(0, 14)

    label("loc_3BF")

    Jump("loc_3C2")

    label("loc_3C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_40E")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 30590, 4500, 35260, 249)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 28630, 4000, 36530, 176)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 28800, 4000, 33220, 0)
    Jump("loc_613")

    label("loc_40E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_45A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 41610, 6000, 48020, 219)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 9750, 2000, 15450, 181)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 9820, 2000, 13580, 351)
    Jump("loc_613")

    label("loc_45A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4A6")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 39080, 6000, 47390, 7)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 40560, 6000, 47840, 342)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 39640, 6000, 44670, 353)
    Jump("loc_613")

    label("loc_4A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4B0")
    Jump("loc_613")

    label("loc_4B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4E6")
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 47620, 0, 7310, 180)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 48380, 0, 7130, 180)
    Jump("loc_613")

    label("loc_4E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_51C")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 16830, 2500, 13990, 11)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 39080, 6000, 47390, 7)
    Jump("loc_613")

    label("loc_51C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_568")
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 13770, 2500, 18660, 90)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 17190, 2500, 13960, 351)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 15890, 2500, 13840, 32)
    Jump("loc_613")

    label("loc_568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_5CA")
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 13770, 2500, 18660, 90)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 13780, 2500, 19720, 153)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 17190, 2500, 13960, 351)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 15890, 2500, 13840, 32)
    Jump("loc_613")

    label("loc_5CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_613")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 13400, 2500, 18050, 224)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 14390, 2500, 16520, 263)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 12490, 2000, 16460, 41)

    label("loc_613")

    Return()

    # Function_0_392 end

    def Function_1_614(): pass

    label("Function_1_614")

    OP_16(0x2, 0xFA0, 0xFFFE8130, 0xFFFE5E08, 0x30054)
    OP_72(0xB, 0x10)
    OP_1B(0x0, 0x0, 0x11)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x11C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_644")
    OP_28(0x2A, 0x1, 0x800)

    label("loc_644")

    OP_64(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_664")
    OP_65(0x1, 0x1)

    label("loc_664")

    Return()

    # Function_1_614 end

    def Function_2_665(): pass

    label("Function_2_665")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_67A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_665")

    label("loc_67A")

    Return()

    # Function_2_665 end

    def Function_3_67B(): pass

    label("Function_3_67B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_688")
    Jump("loc_8EE")

    label("loc_688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_692")
    Jump("loc_8EE")

    label("loc_692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_69C")
    Jump("loc_8EE")

    label("loc_69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_6A6")
    Jump("loc_8EE")

    label("loc_6A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_70E")

    ChrTalk(    #0
        0xFE,
        (
            "This garden is so mysterious\x01",
            "and beautiful under the moon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "...Don't you think so?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EE")

    label("loc_70E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_827")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_791")

    ChrTalk(    #2
        0xFE,
        (
            "I'd love to see the other side\x01",
            "of the mountain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "But there aren't any roads to\x01",
            "get there in the village.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_824")

    label("loc_791")

    OP_A2(0xA)

    ChrTalk(    #4
        0xFE,
        (
            "They say there's a giant natural\x01",
            "hot spring on the other side of\x01",
            "the mountain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I'd to love go see, but they said\x01",
            "nobody's allowed to.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_824")

    Jump("loc_8EE")

    label("loc_827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_831")
    Jump("loc_8EE")

    label("loc_831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_8E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_87E")

    ChrTalk(    #6
        0xFE,
        "Why, that's a gift shop!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "Let's have a quick peek!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E4")

    label("loc_87E")

    OP_A2(0xA)

    ChrTalk(    #8
        0xFE,
        "Mmm, what a quiet town...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "There's something so...idyllic...\x01",
            "about the Eastern lifestyle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E4")

    Jump("loc_8EE")

    label("loc_8E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8EE")

    label("loc_8EE")

    TalkEnd(0xFE)
    Return()

    # Function_3_67B end

    def Function_4_8F2(): pass

    label("Function_4_8F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_8FF")
    Jump("loc_B19")

    label("loc_8FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_909")
    Jump("loc_B19")

    label("loc_909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_913")
    Jump("loc_B19")

    label("loc_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_91D")
    Jump("loc_B19")

    label("loc_91D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_9F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_964")

    ChrTalk(    #10
        0xFE,
        (
            "Ah, this cool night air feels\x01",
            "so good right now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F4")

    label("loc_964")

    OP_A2(0x9)

    ChrTalk(    #11
        0xFE,
        (
            "Mmm, that bath was hot. It warms\x01",
            "you right down to your toes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Nothing like a slow, warm bath to\x01",
            "help you forget all your troubles.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F4")

    Jump("loc_B19")

    label("loc_9F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_A01")
    Jump("loc_B19")

    label("loc_A01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_A0B")
    Jump("loc_B19")

    label("loc_A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_A3F")

    ChrTalk(    #13
        0xFE,
        "Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "Where did Edel get off to?\x02",
    )

    CloseMessageWindow()
    Jump("loc_B19")

    label("loc_A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_A8A")

    ChrTalk(    #15
        0xFE,
        (
            "I'm so glad I came here.\x01",
            "This is just what I needed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B19")

    label("loc_A8A")

    OP_A2(0x9)

    ChrTalk(    #16
        0xFE,
        (
            "This cool night air feels so\x01",
            "great on my skin!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "Hopefully this trip will help\x01",
            "my wife kick that dreadful\x01",
            "shopping habit she's got.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B19")

    TalkEnd(0xFE)
    Return()

    # Function_4_8F2 end

    def Function_5_B1D(): pass

    label("Function_5_B1D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_B2A")
    Jump("loc_C43")

    label("loc_B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_B34")
    Jump("loc_C43")

    label("loc_B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_B3E")
    Jump("loc_C43")

    label("loc_B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B48")
    Jump("loc_C43")

    label("loc_B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_B52")
    Jump("loc_C43")

    label("loc_B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_C28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BA8")

    ChrTalk(    #18
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "This well would make a\x01",
            "great fishing pond.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C25")

    label("loc_BA8")

    OP_A2(0x0)

    ChrTalk(    #21
        0xFE,
        (
            "Sometimes it's nice to just\x01",
            "forget I'm fishing and relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I feel like I'm completely cleansed...\x01",
            "body and soul!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C25")

    Jump("loc_C43")

    label("loc_C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_C32")
    Jump("loc_C43")

    label("loc_C32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_C3C")
    Jump("loc_C43")

    label("loc_C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C43")

    label("loc_C43")

    TalkEnd(0xFE)
    Return()

    # Function_5_B1D end

    def Function_6_C47(): pass

    label("Function_6_C47")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_6_C47 end

    def Function_7_C4E(): pass

    label("Function_7_C4E")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_7_C4E end

    def Function_8_C55(): pass

    label("Function_8_C55")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_D96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_CD9")

    ChrTalk(    #23
        0xFE,
        "Hello, Quantay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "You were just practicing some\x01",
            "orbal arts, weren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "You should pace yourself.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D93")

    label("loc_CD9")

    OP_A2(0x3)

    ChrTalk(    #26
        0xFE,
        (
            "It's like you're pretending you're\x01",
            "at the Martial Arts Competition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "...right there in the middle of the\x01",
            "road. Don't you feel embarrassed\x01",
            "at all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "You're such a child.\x02",
    )

    CloseMessageWindow()

    label("loc_D93")

    Jump("loc_10DE")

    label("loc_D96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_EAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E32")

    ChrTalk(    #29
        0xFE,
        (
            "Figures the pumps here would\x01",
            "break right when some big\x01",
            "calamity hits Zeiss...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "'Elmo, the town of little rest\x01",
            "and no relaxation.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA7")

    label("loc_E32")

    OP_A2(0x3)

    ChrTalk(    #31
        0xFE,
        "Some news, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "That big attack in Zeiss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "It ought to make the front page\x01",
            "of the Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA7")

    Jump("loc_10DE")

    label("loc_EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_F9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_F1E")

    ChrTalk(    #34
        0xFE,
        (
            "Hey, Lucky! No going past\x01",
            "the fences!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Mrs. Mao'll have my hide if you\x01",
            "do, you know that!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F97")

    label("loc_F1E")

    OP_A2(0x3)

    ChrTalk(    #36
        0xFE,
        (
            "Why does everybody care so much\x01",
            "about the other side of the mountain?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "You guys act like such\x01",
            "little kids...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F97")

    Jump("loc_10DE")

    label("loc_F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_FA4")
    Jump("loc_10DE")

    label("loc_FA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_FAE")
    Jump("loc_10DE")

    label("loc_FAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_FB8")
    Jump("loc_10DE")

    label("loc_FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_FC2")
    Jump("loc_10DE")

    label("loc_FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_FCC")
    Jump("loc_10DE")

    label("loc_FCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_10DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1037")

    ChrTalk(    #38
        0xFE,
        "People from Zeiss are so cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "They're so...I don't know...\x01",
            "so...sophisticated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DE")

    label("loc_1037")

    OP_A2(0x3)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1060")

    ChrTalk(    #40
        0xFE,
        "Ooh, look at him!\x02",
    )

    CloseMessageWindow()
    Jump("loc_108E")

    label("loc_1060")


    ChrTalk(    #41
        0xFE,
        (
            "That boy over there is one\x01",
            "major hottie.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108E")


    ChrTalk(    #42
        0xFE,
        (
            "Hey! You guys are from Zeiss,\x01",
            "right? Right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "What's popular there now?\x02",
    )

    CloseMessageWindow()

    label("loc_10DE")

    TalkEnd(0xFE)
    Return()

    # Function_8_C55 end

    def Function_9_10E2(): pass

    label("Function_9_10E2")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_9_10E2 end

    def Function_10_10E9(): pass

    label("Function_10_10E9")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_10_10E9 end

    def Function_11_10F0(): pass

    label("Function_11_10F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1183")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1136")

    ChrTalk(    #44
        0xFE,
        "Taste my ORBAL ARTS!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "BOOM-SHAKKA-LAKKA!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1180")

    label("loc_1136")

    OP_A2(0x6)

    ChrTalk(    #46
        0xFE,
        "See, Recia?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xD, 400)

    ChrTalk(    #47
        0xFE,
        (
            "I'll really do it this time,\x01",
            "so watch me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1180")

    Jump("loc_14FA")

    label("loc_1183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1222")

    ChrTalk(    #48
        0xFE,
        (
            "Hey, did you hear? Some big\x01",
            "crazy thing happened in Zeiss!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "I heard some bracers came here\x01",
            "to investigate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "I wanna meet a bracer...\x02",
    )

    CloseMessageWindow()
    Jump("loc_14FA")

    label("loc_1222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_132D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1288")

    ChrTalk(    #51
        0xFE,
        (
            "Man, I wanna go to the other\x01",
            "side of the mountain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "I'm BORED playing here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_132A")

    label("loc_1288")

    OP_A2(0x6)

    ChrTalk(    #53
        0xFE,
        (
            "The hot spring there has got\x01",
            "to be GIGANTIC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "It's been giving us hot water for\x01",
            "years, and it still hasn't dried up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "I wish I could see it once.\x02",
    )

    CloseMessageWindow()

    label("loc_132A")

    Jump("loc_14FA")

    label("loc_132D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1337")
    Jump("loc_14FA")

    label("loc_1337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1341")
    Jump("loc_14FA")

    label("loc_1341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_134B")
    Jump("loc_14FA")

    label("loc_134B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_13A8")

    ChrTalk(    #56
        0xFE,
        "That's strange.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "I am NOT mistaken! I see\x01",
            "it every single day!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13F4")

    label("loc_13A8")

    OP_A2(0x6)

    ChrTalk(    #58
        0xFE,
        "That's weird.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "It seems like the hot water\x01",
            "pressure got weaker.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F4")

    Jump("loc_14FA")

    label("loc_13F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_14FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1491")

    ChrTalk(    #60
        0xFE,
        (
            "You guys are pretty young to\x01",
            "be visiting the hot springs. It's\x01",
            "like an old people hangout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "You must be real tired\x01",
            "or sumthin'.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14FA")

    label("loc_1491")

    OP_A2(0x6)

    ChrTalk(    #62
        0xFE,
        "Hey, it's new people!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "Wow, they're young. Or maybe\x01",
            "they just LOOK young but are\x01",
            "REALLY old!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14FA")

    TalkEnd(0xFE)
    Return()

    # Function_11_10F0 end

    def Function_12_14FE(): pass

    label("Function_12_14FE")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_12_14FE end

    def Function_13_1505(): pass

    label("Function_13_1505")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_15D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1561")

    ChrTalk(    #64
        0xFE,
        (
            "You can't defeat me! My orbal\x01",
            "arts are TOO STRONG!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "AAH-CHOOO!\x02",
    )

    CloseMessageWindow()
    Jump("loc_15CE")

    label("loc_1561")

    OP_A2(0x8)

    ChrTalk(    #66
        0xFE,
        (
            "Heh heh, the best part of the\x01",
            "birthday celebration stuff has gotta \x01",
            "be the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15CE")

    Jump("loc_1908")

    label("loc_15D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_169F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_163C")

    ChrTalk(    #67
        0xFE,
        "That was some incident...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "But it doesn't have anything\x01",
            "to do with this village.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_169C")

    label("loc_163C")

    OP_A2(0x8)

    ChrTalk(    #69
        0xFE,
        (
            "You hear about that big incident\x01",
            "that happened in Zeiss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "Cities sure can be scary.\x02",
    )

    CloseMessageWindow()

    label("loc_169C")

    Jump("loc_1908")

    label("loc_169F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_17CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1710")

    ChrTalk(    #71
        0xFE,
        "Wow, Recia sure looks bored.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "She ought to be helping out at\x01",
            "the inn, not watching us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C9")

    label("loc_1710")

    OP_A2(0x8)

    ChrTalk(    #73
        0xFE,
        (
            "You know the spring on the\x01",
            "other side of the mountain?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "I've heard all about it, but I've\x01",
            "never seen it for real.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "I'd go right now if it weren't for\x01",
            "this stupid fence.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C9")

    Jump("loc_1908")

    label("loc_17CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_17D6")
    Jump("loc_1908")

    label("loc_17D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_17E0")
    Jump("loc_1908")

    label("loc_17E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_17EA")
    Jump("loc_1908")

    label("loc_17EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_184C")

    ChrTalk(    #76
        0xFE,
        (
            "Lucky says the hot spring is\x01",
            "acting strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "I can't tell the difference.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1908")

    label("loc_184C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1908")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_18CA")

    ChrTalk(    #78
        0xFE,
        "Lucky's such a little kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "Doesn't he know that the best\x01",
            "place for a couple to go is a\x01",
            "hot spring?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1908")

    label("loc_18CA")

    OP_A2(0x8)

    ChrTalk(    #80
        0xFE,
        (
            "Heh. Nice. A little date vacation\x01",
            "to the hot springs?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1908")

    TalkEnd(0xFE)
    Return()

    # Function_13_1505 end

    def Function_14_190C(): pass

    label("Function_14_190C")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(53490, 2500, 9430, 0)
    OP_67(0, 5410, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 52820, 2500, -3040, 270)
    SetChrPos(0x101, 42000, 2500, -2430, 45)
    SetChrPos(0x102, 41080, 2500, -1680, 45)
    SetChrPos(0x107, 40890, 2500, -2710, 45)
    FadeToBright(1000, 0)
    OP_6D(40870, 2500, -2620, 5000)

    ChrTalk(    #81
        0x101,
        "#501FWow, it's already dark.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x102,
        (
            "#010FLook at the Eastern-style\x01",
            "garden. Very nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        "#2POh! Estelle and Joshua, hi!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(46060, 2500, -3350, 0)
    OP_67(0, 5850, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 41530, 2500, -2520, 90)
    SetChrPos(0x107, 41120, 2500, -3580, 90)
    SetChrPos(0x102, 40830, 2500, -1900, 90)
    SetChrFlags(0x107, 0x4)
    SetChrFlags(0x102, 0x4)

    def lambda_1ABA():
        OP_8E(0xFE, 0xB842, 0x9C4, 0xFFFFF498, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1ABA)
    OP_0D()
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #84
        0x101,
        "#501FDorothy...?\x02",
    )

    CloseMessageWindow()

    def lambda_1AF1():
        OP_8E(0xFE, 0xB068, 0x9C4, 0xFFFFF4DE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AF1)
    Sleep(300)

    def lambda_1B11():
        OP_8E(0xFE, 0xADA2, 0x9C4, 0xFFFFF1C8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1B11)
    Sleep(300)

    def lambda_1B31():
        OP_8E(0xFE, 0xADE8, 0x9C4, 0xFFFFF6FA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B31)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #85
        0x8,
        (
            "#151FDid you come here to soak in\x01",
            "these heavenly waters, too?\x02\x03",

            "I just love it here. It's so\x01",
            "spacious and comfortable.\x02\x03",

            "I just wish staying in the\x01",
            "hot water didn't make me\x01",
            "dizzy after a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#004FHave you been in here\x01",
            "this whole time?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        (
            "#151FOh, yeah.\x01",
            "It just feels sooooo good.\x02\x03",

            "#153FAnd who are you, little girl?\x01",
            "I don't think we've met before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x107,
        (
            "#560FI'm Tita.\x01",
            "It's nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "#150FTita, huh?\x02\x03",

            "You can call me Dorothy.\x02\x03",

            "I'm a photographer for\x01",
            "a magazine in Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x107,
        (
            "#061FReally? Wow, that must\x01",
            "be a great job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        (
            "#151FHee hee...\x01",
            "It is pretty awesome.\x02\x03",

            "#150FOh, right. Estelle, you guys\x01",
            "are staying at the inn, right?\x02\x03",

            "Why don't we have dinner together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#501FSure, sounds okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x102,
        (
            "#010FWould you mind waiting\x01",
            "for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "#151FSure. I'll have some fruity\x01",
            "milk in the meantime.\x02\x03",

            "I'll see you guys soon.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1EA1():

        label("loc_1EA1")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1EA1")

    QueueWorkItem2(0x101, 1, lambda_1EA1)

    def lambda_1EB2():

        label("loc_1EB2")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1EB2")

    QueueWorkItem2(0x102, 1, lambda_1EB2)

    def lambda_1EC3():

        label("loc_1EC3")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1EC3")

    QueueWorkItem2(0x107, 1, lambda_1EC3)
    OP_8F(0x102, 0xACE4, 0x9C4, 0xFFFFF510, 0x7D0, 0x0)
    SetChrFlags(0x8, 0x40)
    OP_8E(0x8, 0xB34C, 0x9C4, 0xFFFFF6FA, 0xBB8, 0x0)
    OP_8E(0x8, 0x9E98, 0x9C4, 0xFFFFF4DE, 0xBB8, 0x0)
    OP_70(0x5, 0x1D)
    OP_73(0x5)
    OP_8E(0x8, 0x9826, 0x9C4, 0xFFFFF51A, 0xBB8, 0x0)
    SetChrFlags(0x8, 0x80)
    Sleep(500)
    OP_72(0x5, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x5, 29)
    OP_70(0x5, 0x0)
    OP_73(0x5)
    OP_71(0x5, 0x800)
    OP_44(0x101, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x102, 0xFF)
    ClearChrFlags(0x107, 0x4)
    ClearChrFlags(0x102, 0x4)
    EventEnd(0x0)
    Return()

    # Function_14_190C end

    def Function_15_1F70(): pass

    label("Function_15_1F70")

    OP_22(0x1C7, 0x1, 0x64)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_11(0xEF, 0xEC, 0xF1, 0x8534, 0x99E8, 0x0)
    SetMapFlags(0x10)
    OP_6D(67020, 1000, 15120, 0)
    OP_67(0, 9190, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    SetChrChipByIndex(0x101, 2)
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x107, 3)
    SetChrFlags(0x107, 0x1000)
    SetChrChipByIndex(0x102, 4)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x107, 0x80)
    SetChrPos(0x101, 68840, 2000, 6530, 0)
    SetChrPos(0x102, 66060, 1000, 21730, 225)
    FadeToBright(1000, 0)
    OP_8E(0x101, 0x10496, 0x7D0, 0x2BB6, 0xBB8, 0x0)

    ChrTalk(    #95
        0x101,
        (
            "#441F(Whew... Okay, settle down,\x01",
            "heart... I hear you...)\x02\x03",

            "(What the hell was that all about?)\x02\x03",

            "(I've never even thought about\x01",
            "Joshua like that before...)\x02\x03",

            "#377F( ... )\x02\x03",

            "#376F(AARRGGHH, stop it, Estelle!\x01",
            "This isn't like you!)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2113():
        OP_6D(65160, 1000, 17980, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2113)

    def lambda_212B():
        OP_6C(11000, 3500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_212B)
    OP_8E(0x101, 0xF64A, 0x7D0, 0x2ABC, 0x7D0, 0x0)
    OP_8E(0x101, 0xF21C, 0x3E8, 0x3B42, 0x7D0, 0x0)
    OP_8E(0x101, 0xFE42, 0x3E8, 0x45EC, 0x3E8, 0x0)
    OP_8C(0x101, 225, 300)
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(    #96
        0x101,
        (
            "#371FAhhh, this feels great!\x02\x03",

            "I love that the bath is\x01",
            "open to the outside.\x02\x03",

            "#370FMmmm...and it's big enough\x01",
            "to stretch out and really\x01",
            "relax in...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #97
        0x102,
        "Boy's Voice",
        (
            "...You do know that you're not\x01",
            "meant to go swimming, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#444FYou see me doin' the butterfly\x01",
            "stroke, buddy?!\x02\x03",

            "...\x02\x03",

            "#374F...Uh.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22B5():
        OP_6D(65630, 1000, 20540, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_22B5)
    OP_67(0, 8970, -10000, 1000)
    TurnDirection(0x101, 0x102, 400)
    Fade(2500)
    ClearMapFlags(0x10)
    Sleep(2500)
    OP_6C(45000, 2500)

    ChrTalk(    #99
        0x102,
        (
            "#380FHi, Estelle. I got in a\x01",
            "little while before you.\x02\x03",

            "#389FHa ha... It's kind of awkward\x01",
            "to be around you like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#374F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x102,
        (
            "#389FB-But hey, the hot spring works\x01",
            "even better than I'd expected.\x02\x03",

            "It's good for injuries, and it\x01",
            "really helps work out any\x01",
            "muscle stiffness.\x02\x03",

            "Just the right idea for a\x01",
            "bracer, really...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#374F...\x01",
            ".....\x01",
            ".........\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x102,
        (
            "#388FUh... I...\x02\x03",

            "You staying silent like that is making this\x01",
            "a bit awkward, you know...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)

    ChrTalk(    #104
        0x101,
        "#373FAh... I... Uh...\x02",
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x3E8, 0xBB8)
    Sleep(1000)

    ChrTalk(    #105 op#A op#5
        0x101,
        "#375F#30A#5SEEEEEEEEEEEEEK!\x05\x02",
    )

    FadeToDark(3000, 0, -1)
    OP_6B(15700, 2000)
    Sleep(2000)
    OP_6D(67030, 2000, 13540, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 66930, 2000, 12000, 0)
    ClearChrFlags(0x107, 0x80)
    SetChrPos(0x101, 65690, 1000, 15170, 180)
    SetChrPos(0x107, 64620, 1000, 15010, 180)
    SetChrPos(0x102, 65430, 1000, 16430, 180)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_1E()
    OP_0D()

    ChrTalk(    #106
        0x9,
        (
            "#682FThat shriek startled me so badly\x01",
            "that I almost flew through the\x01",
            "ceiling.\x02\x03",

            "I almost suffer through a heart\x01",
            "attack, and all for what?\x01",
            "A false alarm!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#377FI'm... I'm sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x9,
        (
            "#682FListen.\x01",
            "The open-air bath is unisex.\x02\x03",

            "Is there not a sign, clearly saying\x01",
            "that, in the dressing room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#373FUm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x102,
        (
            "#387F...I think what she's trying to\x01",
            "say is that she didn't notice it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x9,
        (
            "#681FFirst of all, getting caught starkers once\x01",
            "or twice isn't such a big deal that you\x01",
            "need to go screaming your lungs out.\x02\x03",

            "And I've heard it said that a\x01",
            "woman's skin gets prettier\x01",
            "when you show it off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x107,
        "#393FR-Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#372FBUNCH. OF. CRAP.\x02\x03",

            "I wasn't out to show off\x01",
            "anything for anyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x9,
        (
            "#680FWell, whatever, then. Why not\x01",
            "make up and just try to enjoy\x01",
            "the baths?\x02\x03",

            "This place was intended for family\x01",
            "members to be able to bathe together,\x01",
            "from the get-go.\x02\x03",

            "Now, I'm off.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)

    def lambda_292F():
        OP_8E(0x9, 0x10C98, 0x7D0, 0x1982, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_292F)
    Sleep(1000)

    def lambda_294F():
        OP_6D(65269, 1000, 15580, 2000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_294F)
    WaitChrThread(0x9, 0x2)
    OP_6F(0x8, 29)
    OP_70(0x8, 0x1D)
    Sleep(1000)
    OP_72(0x8, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x8, 0x0)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #115
        0x101,
        (
            "#377F*sigh*\x01",
            "And suddenly, I'm exhausted.\x02\x03",

            "#444FGrrr...\x01",
            "Joshua, this is all your fault!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(    #116
        0x102,
        (
            "#387FHow do you figure THAT?\x02\x03",

            "#388FI mean, it wasn't ME who\x01",
            "shrieked like a banshee.\x02\x03",

            "Nor did I flake out and\x01",
            "completely miss the sign\x01",
            "in the dressing room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#379FY-You shut up!\x02\x03",

            "You think you're so cute!\x01",
            "Well, you're not!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x102,
        (
            "#382FOh, is that how it is?\x02\x03",

            "#385FWell, fine.\x02\x03",

            "It's not as if it means anything\x01",
            "to me whether or not you think\x01",
            "I'm cute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        "#372FWh-What did you say?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x102,
        (
            "#383FI'm making a point. Looking at me and\x01",
            "screaming the way you did...\x02\x03",

            "I never would have even dreamed that you'd\x01",
            "react like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        (
            "#441FUh... Well, I...just wasn't...\x01",
            "It was bad timing, okay?\x02\x03",

            "I didn't mean that I'm disgusted\x01",
            "at the thought of being in there\x01",
            "with you or anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x102,
        (
            "#385FNo, no. I wouldn't want\x01",
            "you to put yourself out.\x02\x03",

            "#380FI'll just be on my way,\x01",
            "so you two can be alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        (
            "#375F'Put myself out...'?!\x02\x03",

            "I can't believe you sometimes,\x01",
            "you JERK!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x102,
        (
            "#382FHeh...\x01",
            "Look who's talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x107,
        "#391F*giggle*\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 400)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #126
        0x101,
        (
            "#441FH-Hey!\x02\x03",

            "Don't you dare laugh, Tita!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x102,
        (
            "#388FI still don't get why I'M the\x01",
            "jerk...but whatever...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2E49():
        OP_69(0x107, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E49)

    def lambda_2E57():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E57)
    TurnDirection(0x102, 0x107, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #128
        0x102,
        (
            "#389FI... I'm sorry. I wasn't trying\x01",
            "to embarrass you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x107,
        (
            "#396FIt's okay...\x01",
            "I'm sorry for laughing.\x02\x03",

            "I just...well, I'm a little envious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        "#374F#3PE-Envious of what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x102,
        "#384F...Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x107,
        (
            "#390FI don't have any siblings...\x01",
            "so I don't have anyone to\x01",
            "fight with or make up with.\x02\x03",

            "Grandpa's always nice and\x01",
            "never mean to me...\x02\x03",

            "Mostly because my mom and\x01",
            "dad couldn't be there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        "#374F#3PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x102,
        (
            "#382FYou don't mean to say\x01",
            "that they're...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x107,
        (
            "#390FThey've been out of the country\x01",
            "working as orbal engineers for\x01",
            "a long time.\x02\x03",

            "I guess they're somewhere\x01",
            "that orbment technology\x01",
            "hasn't really hit, yet...\x02\x03",

            "I'm not even sure how many\x01",
            "years it's been since they\x01",
            "last came to Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        "#373F#3PI had no idea...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x102,
        "#383FYou must have been lonely...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x107,
        (
            "#396FNot really... I have my grandpa,\x01",
            "at least.\x02\x03",

            "And everyone at the central\x01",
            "factory is always super nice\x01",
            "to me.\x02\x03",

            "#395FBut...I still get a little jealous\x01",
            "when I look at you two.\x02\x03",

            "Heehee... I'm probably just\x01",
            "wishing for something that\x01",
            "I'll never have...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x102,
        "#382FTita...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        (
            "#440F#3P...\x02\x03",

            "#376FI've got an idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x107,
        "#393FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x102,
        "#384F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#371F#3PFrom now on,\x01",
            "I'll be your big sister!\x02\x03",

            "And Joshua can be your\x01",
            "big brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x107,
        "#394FWha--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x102,
        (
            "#387F*sigh* Always with the grand,\x01",
            "sweeping gestures...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#379F#3POh, come on.\x01",
            "Are you seriously complaining?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x102,
        (
            "#381FNo...\x01",
            "I feel the same way you do.\x02\x03",

            "I have no objections, as long\x01",
            "as Tita's okay with the idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x107,
        (
            "#396F...\x02\x03",

            "#395FTh-Thank you...both of you...\x02\x03",

            "I don't know what to say...\x01",
            "I can't stop smiling...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        (
            "#371F#3PWell, that settles it, then!\x02\x03",

            "#376FTreat us just like you would\x01",
            "a normal brother and sister!\x02\x03",

            "I give you permission to make fun\x01",
            "of Joshua as much as you like!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x102,
        (
            "#389FThat's right. Estelle is fair game\x01",
            "to make fun of, too, in that case.\x02\x03",

            "You can talk to us just like \x01",
            "when you talk to the professor,\x01",
            "like family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x107,
        (
            "#397FB-But...\x01",
            "Is that really okay...?\x02\x03",

            "...\x02\x03",

            "#396FI... I'll try. I promise.\x02\x03",

            "#395FOkay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        "#371F#3POkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x102,
        (
            "#389FSo this is a new beginning\x01",
            "for all of us.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T3223   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1F70 end

    def Function_16_3677(): pass

    label("Function_16_3677")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #154
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_3677 end

    def Function_17_36C6(): pass

    label("Function_17_36C6")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3768")
    TurnDirection(0x102, 0x1, 400)

    ChrTalk(    #155
        0x102,
        (
            "#010FThe fields are dangerous at night,\x01",
            "so we should probably turn back.\x02\x03",

            "There's always the village if\x01",
            "we feel like walking around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37E7")

    label("loc_3768")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(    #156
        0x102,
        (
            "#010FThe fields are dangerous at night.\x02\x03",

            "If we want to go out walking,\x01",
            "it's probably best to do it\x01",
            "in the village.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37E7")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_17_36C6 end

    def Function_18_3803(): pass

    label("Function_18_3803")

    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #157
        "\x07\x00Found a package wrapped in oiled-paper.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #158
        "\x07\x00Inside was \x07\x02The Erbe Woodpecker\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x343, 1)
    OP_64(0x1, 0x1)
    OP_28(0x2E, 0x1, 0x10)
    TalkEnd(0xFF)
    Return()

    # Function_18_3803 end

    def Function_19_389C(): pass

    label("Function_19_389C")

    SetPlaceName(0x88)
    Return()

    # Function_19_389C end

    def Function_20_38A0(): pass

    label("Function_20_38A0")

    SetPlaceName(0x87)
    Return()

    # Function_20_38A0 end

    def Function_21_38A4(): pass

    label("Function_21_38A4")

    SetPlaceName(0x89)
    Return()

    # Function_21_38A4 end

    SaveToFile()

Try(main)
