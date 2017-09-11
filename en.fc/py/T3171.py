from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3171   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3171.x',
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
        'Martina',                              # 9
        'Emma',                                 # 10
        'Dodge',                                # 11
        'Professor Alba',                       # 12
        'Dorothy',                              # 13
        'Radmira',                              # 14
        'Charles',                              # 15
        'Seagaro',                              # 16
        'Edel',                                 # 17
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
        'ED6_DT07/CH01210 ._CH',             # 00
        'ED6_DT07/CH01350 ._CH',             # 01
        'ED6_DT07/CH01140 ._CH',             # 02
        'ED6_DT07/CH02050 ._CH',             # 03
        'ED6_DT07/CH02070 ._CH',             # 04
        'ED6_DT07/CH01690 ._CH',             # 05
        'ED6_DT07/CH02640 ._CH',             # 06
        'ED6_DT07/CH01140 ._CH',             # 07
        'ED6_DT07/CH01130 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01210P._CP',             # 00
        'ED6_DT07/CH01350P._CP',             # 01
        'ED6_DT07/CH01140P._CP',             # 02
        'ED6_DT07/CH02050P._CP',             # 03
        'ED6_DT07/CH02070P._CP',             # 04
        'ED6_DT07/CH01690P._CP',             # 05
        'ED6_DT07/CH02640P._CP',             # 06
        'ED6_DT07/CH01140P._CP',             # 07
        'ED6_DT07/CH01130P._CP',             # 08
    )

    DeclNpc(
        X                   = -1700,
        Z                   = 0,
        Y                   = 2400,
        Direction           = 192,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -44500,
        Z                   = 0,
        Y                   = 7710,
        Direction           = 82,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
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
        TalkScenaIndex      = 17,
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
        TalkScenaIndex      = 16,
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
        TalkScenaIndex      = 15,
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
        TalkScenaIndex      = 13,
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
        TalkScenaIndex      = 14,
    )


    DeclActor(
        TriggerX            = -1290,
        TriggerZ            = 0,
        TriggerY            = 550,
        TriggerRange        = 400,
        ActorX              = -1700,
        ActorZ              = 1500,
        ActorY              = 2400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_236",          # 00, 0
        "Function_1_525",          # 01, 1
        "Function_2_526",          # 02, 2
        "Function_3_53C",          # 03, 3
        "Function_4_560",          # 04, 4
        "Function_5_584",          # 05, 5
        "Function_6_5A8",          # 06, 6
        "Function_7_5CC",          # 07, 7
        "Function_8_5F0",          # 08, 8
        "Function_9_614",          # 09, 9
        "Function_10_638",         # 0A, 10
        "Function_11_65C",         # 0B, 11
        "Function_12_680",         # 0C, 12
        "Function_13_6A4",         # 0D, 13
        "Function_14_904",         # 0E, 14
        "Function_15_A32",         # 0F, 15
        "Function_16_16F3",        # 10, 16
        "Function_17_1ADF",        # 11, 17
        "Function_18_1BB4",        # 12, 18
        "Function_19_1DF0",        # 13, 19
        "Function_20_284E",        # 14, 20
        "Function_21_2853",        # 15, 21
        "Function_22_3019",        # 16, 22
    )


    def Function_0_236(): pass

    label("Function_0_236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_258")
    SetChrPos(0x9, 34920, 0, 91540, 240)
    OP_43(0x9, 0x0, 0x0, 0x6)
    Jump("loc_524")

    label("loc_258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_28E")
    SetChrPos(0x9, 48750, 0, 137140, 170)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 650, 0, 3140, 280)
    SetChrFlags(0xC, 0x10)
    Jump("loc_524")

    label("loc_28E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2B0")
    SetChrPos(0x9, 53820, 0, 136060, 76)
    OP_43(0x9, 0x0, 0x0, 0x4)
    Jump("loc_524")

    label("loc_2B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_329")
    SetChrPos(0x9, 53820, 0, 136060, 76)
    OP_43(0x9, 0x0, 0x0, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 35060, 0, 51880, 175)
    OP_43(0xB, 0x0, 0x0, 0x8)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 35130, 0, 91450, 214)
    OP_43(0xD, 0x0, 0x0, 0x9)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 32420, 0, 95120, 302)
    OP_43(0xE, 0x0, 0x0, 0xA)
    Jump("loc_524")

    label("loc_329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_368")
    SetChrPos(0x9, 4750, 0, 1370, 265)
    OP_43(0x9, 0x0, 0x0, 0x5)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 68050, 0, 56260, 30)
    OP_43(0xA, 0x0, 0x0, 0x7)
    Jump("loc_524")

    label("loc_368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3DA")
    SetChrPos(0x9, 5810, 0, 3490, 194)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 68050, 0, 56260, 30)
    OP_43(0xA, 0x0, 0x0, 0x7)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 35130, 0, 91450, 214)
    OP_43(0xD, 0x0, 0x0, 0x9)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 2990, 0, 1550, 87)
    OP_43(0xE, 0x0, 0x0, 0xB)
    Jump("loc_524")

    label("loc_3DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_42F")
    SetChrPos(0x9, 64750, 0, 95500, 3)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 35130, 0, 91450, 214)
    OP_43(0xD, 0x0, 0x0, 0x9)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 32420, 0, 95120, 302)
    OP_43(0xE, 0x0, 0x0, 0xA)
    Jump("loc_524")

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_49A")
    SetChrPos(0x9, 53820, 0, 136060, 76)
    OP_43(0x9, 0x0, 0x0, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 66540, 0, 59500, 354)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 64450, 0, 95110, 275)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 68300, 0, 90910, 151)
    OP_43(0x10, 0x0, 0x0, 0xC)
    Jump("loc_524")

    label("loc_49A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_505")
    SetChrPos(0x9, 53820, 0, 136060, 76)
    OP_43(0x9, 0x0, 0x0, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 66540, 0, 59500, 354)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 64450, 0, 95110, 275)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 68300, 0, 90910, 151)
    OP_43(0x10, 0x0, 0x0, 0xC)
    Jump("loc_524")

    label("loc_505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_524")
    SetChrPos(0x9, 35090, 0, 51720, 32)
    OP_43(0x9, 0x0, 0x0, 0x3)

    label("loc_524")

    Return()

    # Function_0_236 end

    def Function_1_525(): pass

    label("Function_1_525")

    Return()

    # Function_1_525 end

    def Function_2_526(): pass

    label("Function_2_526")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_526")

    label("loc_53B")

    Return()

    # Function_2_526 end

    def Function_3_53C(): pass

    label("Function_3_53C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_55F")
    OP_8D(0xFE, 33590, 49640, 1108473283, 53470, 3000)
    Jump("Function_3_53C")

    label("loc_55F")

    Return()

    # Function_3_53C end

    def Function_4_560(): pass

    label("Function_4_560")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_583")
    OP_8D(0xFE, 44740, 134200, 62330, 137000, 3000)
    Jump("Function_4_560")

    label("loc_583")

    Return()

    # Function_4_560 end

    def Function_5_584(): pass

    label("Function_5_584")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A7")
    OP_8D(0xFE, 1650, -310, 7710, 1910, 3000)
    Jump("Function_5_584")

    label("loc_5A7")

    Return()

    # Function_5_584 end

    def Function_6_5A8(): pass

    label("Function_6_5A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5CB")
    OP_8D(0xFE, 4059, 88790, 36250, 93240, 3000)
    Jump("Function_6_5A8")

    label("loc_5CB")

    Return()

    # Function_6_5A8 end

    def Function_7_5CC(): pass

    label("Function_7_5CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EF")
    OP_8D(0xFE, 66680, 54350, 69610, 58920, 2000)
    Jump("Function_7_5CC")

    label("loc_5EF")

    Return()

    # Function_7_5CC end

    def Function_8_5F0(): pass

    label("Function_8_5F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_613")
    OP_8D(0xFE, 34200, 49490, 36490, 53440, 1500)
    Jump("Function_8_5F0")

    label("loc_613")

    Return()

    # Function_8_5F0 end

    def Function_9_614(): pass

    label("Function_9_614")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_637")
    OP_8D(0xFE, 33860, 89530, 36420, 93590, 2000)
    Jump("Function_9_614")

    label("loc_637")

    Return()

    # Function_9_614 end

    def Function_10_638(): pass

    label("Function_10_638")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_65B")
    OP_8D(0xFE, 31570, 94690, 33720, 95490, 3000)
    Jump("Function_10_638")

    label("loc_65B")

    Return()

    # Function_10_638 end

    def Function_11_65C(): pass

    label("Function_11_65C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_67F")
    OP_8D(0xFE, 1090, -290, 4450, 2920, 3000)
    Jump("Function_11_65C")

    label("loc_67F")

    Return()

    # Function_11_65C end

    def Function_12_680(): pass

    label("Function_12_680")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A3")
    OP_8D(0xFE, 67180, 88480, 69500, 93510, 2000)
    Jump("Function_12_680")

    label("loc_6A3")

    Return()

    # Function_12_680 end

    def Function_13_6A4(): pass

    label("Function_13_6A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_773")

    ChrTalk(    #0
        0xFE,
        (
            "I'm headed for a famous hot\x01",
            "springs resort near here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I've decided to stay there until\x01",
            "I leave for Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "With any luck, it'll keep my\x01",
            "wife from spending all her\x01",
            "time shopping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_900")

    label("loc_773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_900")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_846")

    ChrTalk(    #3
        0xFE,
        (
            "I'm headed for a famous hot\x01",
            "springs resort near here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I've decided to stay there until\x01",
            "I leave for Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "With any luck, it'll keep my\x01",
            "wife from spending all her\x01",
            "time shopping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_900")

    label("loc_846")

    OP_A2(0x7)

    ChrTalk(    #6
        0xFE,
        "What happened last night?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "I was dead to the world.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Uh oh, no time to chit-chat.\x01",
            "I've got to get ready to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I'm headed for a famous hot\x01",
            "springs resort near here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_900")

    TalkEnd(0xFE)
    Return()

    # Function_13_6A4 end

    def Function_14_904(): pass

    label("Function_14_904")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_99D")

    ChrTalk(    #10
        0xFE,
        (
            "Isn't it nice to have a real hot\x01",
            "spring so nearby?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "There'll be so many unusual \x01",
            "things for sale there! I'll have\x01",
            "a ball shopping!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2E")

    label("loc_99D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_A2E")

    ChrTalk(    #12
        0xFE,
        (
            "Just when I decided to go to\x01",
            "bed last night, all the lights\x01",
            "just went out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "I accidentally ended up getting\x01",
            "in my husband's bed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2E")

    TalkEnd(0xFE)
    Return()

    # Function_14_904 end

    def Function_15_A32(): pass

    label("Function_15_A32")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_E86")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC0")
    OP_A2(0x583)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #14
        0xFE,
        "Hey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "Hey. Long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#014F...?\x02\x03",

            "#010FAh, hey.\x01",
            "It HAS been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#501FWho's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        (
            "#010FYou remember that kid who was\x01",
            "looking for the quartz shard in\x01",
            "Rolent, don't you?\x02\x03",

            "Remember? We took a request\x01",
            "to find it a while back.\x02\x03",

            "Are you headed back to\x01",
            "the Republic?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #19
        0xFE,
        (
            "After we finish doing some shopping\x01",
            "at the central factory. We made\x01",
            "some cash in Grancel, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Mom said we're gonna take this\x01",
            "mira and stock up on orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "They say the eyes are the first\x01",
            "to go, but she can still spot a\x01",
            "good deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#506FI can see you're still an\x01",
            "obnoxious brat.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #23
        0xFE,
        (
            "What? I'm only saying what\x01",
            "everybody else is thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Anyway...do they really make\x01",
            "the airships here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "I heard the engineers are having\x01",
            "a big meeting right now about\x01",
            "orbal engines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "That's so cool. Making real\x01",
            "live airships...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "Just...cool.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E83")

    label("loc_DC0")


    ChrTalk(    #28
        0xFE,
        (
            "Do they really make the\x01",
            "airships here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "I heard the engineers are having\x01",
            "a big meeting right now about\x01",
            "orbal engines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "That's so cool. Making real\x01",
            "live airships...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "Just...cool.\x02",
    )

    CloseMessageWindow()

    label("loc_E83")

    Jump("loc_16EF")

    label("loc_E86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_130A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12B7")
    OP_A2(0x583)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #32
        0xFE,
        "Hey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "Hey. Long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        (
            "#014F...?\x02\x03",

            "#010FAh, hey.\x01",
            "It HAS been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#501FWho's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#010FYou remember that kid who was\x01",
            "looking for the quartz shard in\x01",
            "Rolent, don't you?\x02\x03",

            "Remember? We took a request\x01",
            "to find it a while back.\x02\x03",

            "Are you headed back to\x01",
            "the Republic?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #37
        0xFE,
        (
            "After we finish doing some shopping\x01",
            "at the central factory. We made\x01",
            "some cash in Grancel, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "Mom said we're gonna take this\x01",
            "mira and stock up on orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "They say the eyes are the first\x01",
            "to go, but she can still spot a\x01",
            "good deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#506FI can see you're still an\x01",
            "obnoxious brat.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #41
        0xFE,
        (
            "What? I'm only saying what\x01",
            "everybody else is thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Anyway...everybody sure seems\x01",
            "excited around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "Did something happen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#010FWe're on our way to find\x01",
            "out ourselves.\x02\x03",

            "It might be dangerous. You may\x01",
            "want to leave the town.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #45
        0xFE,
        (
            "What? I'm not leaving!\x01",
            "I'm not a kid, you know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#007FMore like an obnoxious brat.\x02\x03",

            "#002FBut we're not here to exchange\x01",
            "insults with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        "#012FLet's get going.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1307")

    label("loc_12B7")


    ChrTalk(    #48
        0xFE,
        "It sure got noisy outside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "If something happened, \x01",
            "come tell me, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1307")

    Jump("loc_16EF")

    label("loc_130A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_16EF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1656")
    OP_A2(0x583)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #50
        0xFE,
        "Hey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "Hey. Long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        (
            "#014F...?\x02\x03",

            "#010FAh, hey.\x01",
            "It HAS been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#501FWho's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        (
            "#010FYou remember that kid who was\x01",
            "looking for the quartz shard in\x01",
            "Rolent, don't you?\x02\x03",

            "Remember? We took a request\x01",
            "to find it a while back.\x02\x03",

            "Are you headed back to\x01",
            "the Republic?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #55
        0xFE,
        (
            "After we finish doing some shopping\x01",
            "at the central factory. We made\x01",
            "some cash in Grancel, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Mom said we're gonna take this\x01",
            "mira and stock up on orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "They say the eyes are the first\x01",
            "to go, but she can still spot a\x01",
            "good deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#506FI can see you're still an\x01",
            "obnoxious brat.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #59
        0xFE,
        (
            "What? I'm only saying what\x01",
            "everybody else is thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Anyway...this town is crazy. \x01",
            "It's all orbments!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "It's just what I imagined a city\x01",
            "that builds airships would be\x01",
            "like in real life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16EF")

    label("loc_1656")


    ChrTalk(    #62
        0xFE,
        "This place is so cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "Moving stairs, orbment clocks...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "It's just what I imagined a city\x01",
            "that builds airships would be\x01",
            "like in real life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16EF")

    TalkEnd(0xFE)
    Return()

    # Function_15_A32 end

    def Function_16_16F3(): pass

    label("Function_16_16F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_194E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1809")

    ChrTalk(    #65
        0xFE,
        (
            "Today I went to the factory and\x01",
            "bought some orbal cameras.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "After I pick them up tomorrow I'll\x01",
            "be finished, and we can finally go\x01",
            "back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "I hope Charles will lend me a\x01",
            "proper hand with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "...I probably shouldn't hope\x01",
            "too much, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_194B")

    label("loc_1809")

    OP_A2(0x5)

    ChrTalk(    #69
        0xFE,
        (
            "Today I went to the factory and\x01",
            "bought some orbal cameras.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "Some simple cameras ought to\x01",
            "sell well in the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "After I pick them up tomorrow I'll\x01",
            "be finished, and we can finally go\x01",
            "back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "I hope Charles will lend me a\x01",
            "proper hand with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "...I probably shouldn't hope\x01",
            "too much, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_194B")

    Jump("loc_1ADB")

    label("loc_194E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1A1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_19B5")

    ChrTalk(    #74
        0xFE,
        (
            "*sigh* That Charles has run off\x01",
            "somewhere again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "He simply can't calm down.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A17")

    label("loc_19B5")

    OP_A2(0x5)

    ChrTalk(    #76
        0xFE,
        (
            "*yaaaawn*\x01",
            "Oh my, I'm sleepy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "But I've still got to go to the\x01",
            "factory this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A17")

    Jump("loc_1ADB")

    label("loc_1A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1ADB")

    ChrTalk(    #78
        0xFE,
        (
            "This is such a nice,\x01",
            "spacious room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "It's definitely worth what we're\x01",
            "paying for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "I think I'll take things easy for\x01",
            "the rest of the day and finish\x01",
            "my business tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ADB")

    TalkEnd(0xFE)
    Return()

    # Function_16_16F3 end

    def Function_17_1ADF(): pass

    label("Function_17_1ADF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1BB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1B71")

    ChrTalk(    #81
        0x110,
        (
            "#150FThat's what Nial toooold meee...\x02\x03",

            "Yes, that's already finished.\x02\x03",

            "Oh, yes! I managed to get\x01",
            "just the CUTEST picture!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB0")

    label("loc_1B71")

    OP_A2(0x4)

    ChrTalk(    #82
        0x110,
        (
            "#150FUmmmm...\x02\x03",

            "No, I meaaaannt...\x02\x03",

            "What I meeean is...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB0")

    TalkEnd(0xFE)
    Return()

    # Function_17_1ADF end

    def Function_18_1BB4(): pass

    label("Function_18_1BB4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1DEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1C25")

    ChrTalk(    #83
        0xB,
        (
            "#130FYou bracers certainly have it\x01",
            "rough, having to work this late.\x02\x03",

            "Good luck with it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DEC")

    label("loc_1C25")

    OP_A2(0x3)

    ChrTalk(    #84
        0xB,
        (
            "#130FEstelle! Joshua!\x02\x03",

            "What a terrible, terrible mess.\x01",
            "Quite frightful, really. Did you\x01",
            "find out anything useful?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#000FYes, sort of...\x02\x03",

            "...Sorry, Professor. We're kind\x01",
            "of in a hurry right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xB,
        (
            "#130FOh. I see.\x02\x03",

            "Still working at this hour...\x01",
            "You bracers are quite busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        "#000FEspecially today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x102,
        (
            "#010FIndeed. Good bye, Professor.\x02\x03",

            "Thank you again for your\x01",
            "help last time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xB,
        (
            "#130FI'm glad I could help.\x02\x03",

            "Good luck with your work!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DEC")

    TalkEnd(0xFE)
    Return()

    # Function_18_1BB4 end

    def Function_19_1DF0(): pass

    label("Function_19_1DF0")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E50")
    OP_0D()
    OP_A9(0x3F)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_1E50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E61")
    TalkEnd(0x8)
    Return()

    label("loc_1E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1FA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F30")

    ChrTalk(    #90
        0x8,
        (
            "Today I plan to give Emma\x01",
            "some real work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        (
            "We've got to clean up all of\x01",
            "the rooms before our new\x01",
            "customers arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "Working at a hotel is nothing\x01",
            "but a big battle against time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FA0")

    label("loc_1F30")

    OP_A2(0x0)

    ChrTalk(    #93
        0x8,
        "Welcome to the Zahnrad Hotel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "Our rooms are open for\x01",
            "your patronage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x8,
        "We are at your disposal.\x02",
    )

    CloseMessageWindow()

    label("loc_1FA0")

    Jump("loc_284A")

    label("loc_1FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_20BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_201A")

    ChrTalk(    #96
        0x8,
        (
            "I always have problems dealing\x01",
            "with people from Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        (
            "Even though I'm from\x01",
            "Zeiss myself...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20B8")

    label("loc_201A")

    OP_A2(0x0)

    ChrTalk(    #98
        0x8,
        "I'm glad I talked to Emma.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        (
            "It looks like she didn't quite\x01",
            "get what I first told her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "I always have problems dealing\x01",
            "with people from Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20B8")

    Jump("loc_284A")

    label("loc_20BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_225F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2161")

    ChrTalk(    #101
        0x8,
        (
            "Even though I'm from\x01",
            "Zeiss myself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "Why is she shouting the greeting\x01",
            "at the customers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        (
            "Does she want to give them\x01",
            "all heart attacks?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_225C")

    label("loc_2161")

    OP_A2(0x0)

    ChrTalk(    #104
        0x8,
        (
            "I already talked to her about\x01",
            "that, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        (
            "Why does Emma insist on speaking\x01",
            "so loudly to the customers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        (
            "I know she just started and\x01",
            "is anxious to make a good\x01",
            "first impression...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x8,
        (
            "...but she'll give all the customers\x01",
            "heart attacks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_225C")

    Jump("loc_284A")

    label("loc_225F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_22A0")

    ChrTalk(    #108
        0x8,
        "Hello! Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x8,
        "Must have been a busy night.\x02",
    )

    CloseMessageWindow()
    Jump("loc_284A")

    label("loc_22A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2393")

    ChrTalk(    #110
        0x8,
        (
            "What a surprise, though...\x01",
            "that attack and everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "I was shocked myself, but we\x01",
            "staff have to keep calm so the\x01",
            "customers can relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x8,
        (
            "We have to go about doing our\x01",
            "jobs as normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x8,
        "For the sake of our customers.\x02",
    )

    CloseMessageWindow()
    Jump("loc_284A")

    label("loc_2393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_23FD")

    ChrTalk(    #114
        0x8,
        (
            "There was quite an uproar near\x01",
            "the factory district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        "Was there some kind of accident?\x02",
    )

    CloseMessageWindow()
    Jump("loc_284A")

    label("loc_23FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_25DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_24B0")

    ChrTalk(    #116
        0x8,
        (
            "People in Zeiss just don't understand\x01",
            "how to give casual service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        "They take things so seriously.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        (
            "...Of course, there are exceptions\x01",
            "to every rule.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D8")

    label("loc_24B0")

    OP_A2(0x0)

    ChrTalk(    #119
        0x8,
        (
            "It's important for us not to\x01",
            "make our customers feel\x01",
            "uncomfortable here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x8,
        (
            "But I'm not sure Zeissians know how to be\x01",
            "casual and friendly. Take our maid, for\x01",
            "example...she's a bit, er, overenthusiastic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x8,
        (
            "Everyone in Zeiss takes things\x01",
            "too seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x8,
        "It wears me out sometimes.\x02",
    )

    CloseMessageWindow()

    label("loc_25D8")

    Jump("loc_284A")

    label("loc_25DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_26B3")

    ChrTalk(    #123
        0x8,
        (
            "Last night was such a burden\x01",
            "on our customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x8,
        (
            "I'm glad things got fixed so\x01",
            "quickly, but still...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x8,
        (
            "...I don't know that we've had a\x01",
            "night without orbal lights since\x01",
            "before the Revolution.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_284A")

    label("loc_26B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_27C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_271B")

    ChrTalk(    #126
        0x8,
        "Also...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x8,
        (
            "This is the first hotel with orbal\x01",
            "lights in all of our guest rooms.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27C0")

    label("loc_271B")

    OP_A2(0x0)

    ChrTalk(    #128
        0x8,
        "Welcome to the Zahnrad Hotel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x8,
        (
            "It's one of the most storied hotels in the \x01",
            "history of Liberl. It has been run by my\x01",
            "family for over six generations now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C0")

    Jump("loc_284A")

    label("loc_27C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_284A")

    ChrTalk(    #130
        0x8,
        "Welcome to the Zahnrad Hotel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        (
            "We have every amenity to suit\x01",
            "your needs. I think you'll find\x01",
            "your stay a pleasant one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_284A")

    TalkEnd(0x8)
    Return()

    # Function_19_1DF0 end

    def Function_20_284E(): pass

    label("Function_20_284E")

    Call(0, 19)
    Return()

    # Function_20_284E end

    def Function_21_2853(): pass

    label("Function_21_2853")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_297B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_28C2")

    ChrTalk(    #132
        0xFE,
        "Okay. Let's clean this room!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "All right, Emma old girl.\x01",
            "Time to give it your all!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2978")

    label("loc_28C2")

    OP_A2(0x1)

    ChrTalk(    #134
        0xFE,
        (
            "Martina had a talk with\x01",
            "me today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "She said I can work off any extra\x01",
            "energy when the customers aren't\x01",
            "watching!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "I can finally let out some of this\x01",
            "pent-up energy!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2978")

    Jump("loc_3015")

    label("loc_297B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2AB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A06")

    ChrTalk(    #137
        0xFE,
        (
            "Martina talked to me today about\x01",
            "not overdoing things in front of the\x01",
            "hotel guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "TIME TO...calm things down.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AB4")

    label("loc_2A06")

    OP_A2(0x1)

    ChrTalk(    #139
        0xFE,
        (
            "This room...is CLEAN!\x01",
            "CLEEEEEEAAAAAAN!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "Now for the other rooms!\x01",
            "YOUR SOUL IS MINE, DUST!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        "Wait... I need to calm down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "Time to...bring it down a notch.\x02",
    )

    CloseMessageWindow()

    label("loc_2AB4")

    Jump("loc_3015")

    label("loc_2AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2C26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B6E")

    ChrTalk(    #143
        0xFE,
        (
            "Martina told me that I was\x01",
            "overdoing things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "I did just start working here though,\x01",
            "of course I'm going to give it my all!\x01",
            "I want to be a cleaning AVENGER!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C23")

    label("loc_2B6E")

    OP_A2(0x1)

    ChrTalk(    #145
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "Martina told me that I was\x01",
            "overdoing things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "I did just start working here though,\x01",
            "of course I'm going to give it my all!\x01",
            "I want to be a cleaning AVENGER!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C23")

    Jump("loc_3015")

    label("loc_2C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2CB1")

    ChrTalk(    #148
        0xFE,
        (
            "I just heard from one of\x01",
            "the guests...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "The central factory was attacked?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "Can you believe it?\x01",
            "I can't believe it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3015")

    label("loc_2CB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2DAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D28")

    ChrTalk(    #151
        0xFE,
        "Hmm...the town seems strange.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "Martina won't tell me a thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "I've got a bad feeling...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DA8")

    label("loc_2D28")

    OP_A2(0x1)

    ChrTalk(    #154
        0xFE,
        "Hmm...the town seems strange.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        "Martina won't tell me a thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "I know I shouldn't ask the\x01",
            "guests either, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DA8")

    Jump("loc_3015")

    label("loc_2DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2DEC")

    ChrTalk(    #157
        0xFE,
        "GREEEEEETINGS!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "WELCOME TO THE ZAHNRAD HOTEL!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3015")

    label("loc_2DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2E6C")

    ChrTalk(    #159
        0xFE,
        (
            "There. This room has been...SANITIZED!\x01",
            "AHAHAHAHAHAHA!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "What's next?! Hallway?! Closet?!\x01",
            "You are all UNCLEAN!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3015")

    label("loc_2E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2EBA")

    ChrTalk(    #161
        0xFE,
        "Oh! Oh, I'm so sorry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "Please come in and stay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F7A")

    label("loc_2EBA")

    OP_A2(0x1)

    ChrTalk(    #163
        0xFE,
        (
            "GOOD MORNING! My name is Emma,\x01",
            "and I'll be your maid today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "You just relax and you will\x01",
            "experience the GREATEST service\x01",
            "of your lives!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        "Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        "Aren't you guys guests here?\x02",
    )

    CloseMessageWindow()

    label("loc_2F7A")

    Jump("loc_3015")

    label("loc_2F7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3015")

    ChrTalk(    #167
        0xFE,
        (
            "Okay, sheets are done. Let's\x01",
            "stock the room amenities...\x01",
            "STOCK THEM, I SAY!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "Lots of stuff still to do!\x01",
            "Time to unleash the FURY, Emma!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3015")

    TalkEnd(0xFE)
    Return()

    # Function_21_2853 end

    def Function_22_3019(): pass

    label("Function_22_3019")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_30C6")

    ChrTalk(    #169
        0xFE,
        (
            "Seems like there was some kind\x01",
            "of accident or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "I came to observe and study the\x01",
            "airship boarding platform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        "Maybe I should reschedule...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3476")

    label("loc_30C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_32C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_315A")

    ChrTalk(    #172
        0xFE,
        (
            "Wow, the scale completely changes\x01",
            "when you're selling stuff like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "I've really got to step up my\x01",
            "game to keep going.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32C3")

    label("loc_315A")

    OP_A2(0x2)

    ChrTalk(    #174
        0xFE,
        (
            "Yesterday this guy at the factory\x01",
            "named Rutherford helped me out\x01",
            "big time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "Thanks to him I was able to\x01",
            "choose a heating orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "Rutherford says he worked more\x01",
            "in airship sales...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "Wow, the scale completely changes\x01",
            "when you're selling stuff like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "He just delegated it to his shop\x01",
            "staff and had the part for me in\x01",
            "no time at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32C3")

    Jump("loc_3476")

    label("loc_32C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3476")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3364")

    ChrTalk(    #179
        0xFE,
        (
            "You know, last night it seemed\x01",
            "like all the lights went off for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "I guess these orbal lights can\x01",
            "burn out sometimes, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3476")

    label("loc_3364")

    OP_A2(0x2)

    ChrTalk(    #181
        0xFE,
        (
            "Liberl is amazing. Everything, even\x01",
            "the lights, are orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "My village is in a rough corner of\x01",
            "the Republic and we don't have\x01",
            "many orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "I'm here in Zeiss to pick up a\x01",
            "new heating orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "After I rest up I'm going to go\x01",
            "to the central factory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3476")

    TalkEnd(0xFE)
    Return()

    # Function_22_3019 end

    SaveToFile()

Try(main)
