from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3231   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3231.x',
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
        'Percy',                                # 9
        'Ed',                                   # 10
        'Lynn',                                 # 11
        'Recia',                                # 12
        'Cyril',                                # 13
        'Addy',                                 # 14
        'Lucky',                                # 15
        'Sima',                                 # 16
        'Quantay',                              # 17
        'Seagaro',                              # 18
        'Edel',                                 # 19
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
        'ED6_DT07/CH01460 ._CH',             # 00
        'ED6_DT07/CH01270 ._CH',             # 01
        'ED6_DT07/CH01030 ._CH',             # 02
        'ED6_DT07/CH01150 ._CH',             # 03
        'ED6_DT07/CH01120 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
        'ED6_DT07/CH01160 ._CH',             # 06
        'ED6_DT07/CH01020 ._CH',             # 07
        'ED6_DT07/CH01060 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01210 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01460P._CP',             # 00
        'ED6_DT07/CH01270P._CP',             # 01
        'ED6_DT07/CH01030P._CP',             # 02
        'ED6_DT07/CH01150P._CP',             # 03
        'ED6_DT07/CH01120P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
        'ED6_DT07/CH01160P._CP',             # 06
        'ED6_DT07/CH01020P._CP',             # 07
        'ED6_DT07/CH01060P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01210P._CP',             # 0A
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
        TalkScenaIndex      = 11,
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
        TalkScenaIndex      = 12,
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
        TalkScenaIndex      = 13,
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
        TalkScenaIndex      = 4,
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
        TalkScenaIndex      = 3,
    )


    DeclActor(
        TriggerX            = -1900,
        TriggerZ            = 0,
        TriggerY            = 5070,
        TriggerRange        = 800,
        ActorX              = -1900,
        ActorZ              = 1000,
        ActorY              = 5070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1890,
        TriggerZ            = 0,
        TriggerY            = -4990,
        TriggerRange        = 800,
        ActorX              = -1890,
        ActorZ              = 1000,
        ActorY              = -4990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AA",          # 00, 0
        "Function_1_370",          # 01, 1
        "Function_2_3B0",          # 02, 2
        "Function_3_3C6",          # 03, 3
        "Function_4_424",          # 04, 4
        "Function_5_568",          # 05, 5
        "Function_6_8E4",          # 06, 6
        "Function_7_8EB",          # 07, 7
        "Function_8_8F2",          # 08, 8
        "Function_9_8F9",          # 09, 9
        "Function_10_900",         # 0A, 10
        "Function_11_907",         # 0B, 11
        "Function_12_90E",         # 0C, 12
        "Function_13_915",         # 0D, 13
        "Function_14_91C",         # 0E, 14
        "Function_15_BCF",         # 0F, 15
        "Function_16_E81",         # 10, 16
    )


    def Function_0_2AA(): pass

    label("Function_0_2AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2B4")
    Jump("loc_36F")

    label("loc_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2BE")
    Jump("loc_36F")

    label("loc_2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2DE")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1080, 0, 440, 85)
    Jump("loc_36F")

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2FE")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1090, 0, -900, 82)
    Jump("loc_36F")

    label("loc_2FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_31E")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1080, 0, 440, 85)
    Jump("loc_36F")

    label("loc_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_328")
    Jump("loc_36F")

    label("loc_328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_332")
    Jump("loc_36F")

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_352")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -990, 0, 10, 90)
    Jump("loc_36F")

    label("loc_352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_36F")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -990, 0, 10, 90)

    label("loc_36F")

    Return()

    # Function_0_2AA end

    def Function_1_370(): pass

    label("Function_1_370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_388")
    OP_B1("t3231_y")
    Jump("loc_391")

    label("loc_388")

    OP_B1("t3231_n")

    label("loc_391")

    OP_72(0x8, 0x10)
    OP_72(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AF")
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)

    label("loc_3AF")

    Return()

    # Function_1_370 end

    def Function_2_3B0(): pass

    label("Function_2_3B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3B0")

    label("loc_3C5")

    Return()

    # Function_2_3B0 end

    def Function_3_3C6(): pass

    label("Function_3_3C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3D3")
    Jump("loc_420")

    label("loc_3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3DD")
    Jump("loc_420")

    label("loc_3DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3E7")
    Jump("loc_420")

    label("loc_3E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3F1")
    Jump("loc_420")

    label("loc_3F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_3FB")
    Jump("loc_420")

    label("loc_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_405")
    Jump("loc_420")

    label("loc_405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_40F")
    Jump("loc_420")

    label("loc_40F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_419")
    Jump("loc_420")

    label("loc_419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_420")

    label("loc_420")

    TalkEnd(0xFE)
    Return()

    # Function_3_3C6 end

    def Function_4_424(): pass

    label("Function_4_424")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_431")
    Jump("loc_564")

    label("loc_431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_43B")
    Jump("loc_564")

    label("loc_43B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4B7")

    ChrTalk(    #0
        0xFE,
        (
            "I heard there was quite a\x01",
            "dangerous incident in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "It's a good thing we decided\x01",
            "to come here early.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_564")

    label("loc_4B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4C1")
    Jump("loc_564")

    label("loc_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_53F")

    ChrTalk(    #2
        0xFE,
        (
            "That was a wonderful bath!\x01",
            "It really warms you up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I feel like I can forget everything\x01",
            "when I'm in there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_564")

    label("loc_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_549")
    Jump("loc_564")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_553")
    Jump("loc_564")

    label("loc_553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_55D")
    Jump("loc_564")

    label("loc_55D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_564")

    label("loc_564")

    TalkEnd(0xFE)
    Return()

    # Function_4_424 end

    def Function_5_568(): pass

    label("Function_5_568")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_575")
    Jump("loc_8E0")

    label("loc_575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_57F")
    Jump("loc_8E0")

    label("loc_57F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_589")
    Jump("loc_8E0")

    label("loc_589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_6B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5F9")

    ChrTalk(    #4
        0xFE,
        "I see...lake fishing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "When I get back to the Fisherman's\x01",
            "Guild, I'll check it out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AF")

    label("loc_5F9")

    OP_A2(0x1)

    ChrTalk(    #6
        0xFE,
        (
            "Nothing like an early morning\x01",
            "bath, is there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "This bath is huge.\x01",
            "It's almost like a lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "Hmm... A lake...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Yeah. Lake fishing...\x01",
            "That sounds like it'd be fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AF")

    Jump("loc_8E0")

    label("loc_6B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_6BC")
    Jump("loc_8E0")

    label("loc_6BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_6C6")
    Jump("loc_8E0")

    label("loc_6C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_6D0")
    Jump("loc_8E0")

    label("loc_6D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_82B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_774")

    ChrTalk(    #10
        0xFE,
        (
            "I heard there aren't many good\x01",
            "places to fish in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "But I'm thinking there might be\x01",
            "some secret fishing hole that's\x01",
            "just incredible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_828")

    label("loc_774")

    OP_A2(0x1)

    ChrTalk(    #12
        0xFE,
        (
            "They said since the pump's broken\x01",
            "the springs are closed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "That lady from the capital sure\x01",
            "seemed disappointed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Might as well go fishing while\x01",
            "they fix the pumps.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_828")

    Jump("loc_8E0")

    label("loc_82B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8E0")

    ChrTalk(    #15
        0xFE,
        (
            "'Cuz there's nothing like a hot\x01",
            "bath after fishing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "For that matter, there's nothing like\x01",
            "a hot bath after just about anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "What a luxurious idea that is.\x02",
    )

    CloseMessageWindow()

    label("loc_8E0")

    TalkEnd(0xFE)
    Return()

    # Function_5_568 end

    def Function_6_8E4(): pass

    label("Function_6_8E4")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_6_8E4 end

    def Function_7_8EB(): pass

    label("Function_7_8EB")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_7_8EB end

    def Function_8_8F2(): pass

    label("Function_8_8F2")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_8_8F2 end

    def Function_9_8F9(): pass

    label("Function_9_8F9")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_9_8F9 end

    def Function_10_900(): pass

    label("Function_10_900")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_10_900 end

    def Function_11_907(): pass

    label("Function_11_907")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_11_907 end

    def Function_12_90E(): pass

    label("Function_12_90E")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_12_90E end

    def Function_13_915(): pass

    label("Function_13_915")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_13_915 end

    def Function_14_91C(): pass

    label("Function_14_91C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_92A")
    Call(0, 16)
    Jump("loc_BCB")

    label("loc_92A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_END)), "loc_AE0")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #18
        (
            "\x07\x05-Women's Bath-\x01",
            "If you would like to use this service,\x01",
            "please let the front desk know.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A68")
    OP_A2(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D4")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_9DB")

    label("loc_9D4")

    TurnDirection(0x102, 0x0, 400)

    label("loc_9DB")


    ChrTalk(    #19
        0x102,
        (
            "#010FThis must be the spa.\x02\x03",

            "Let's put our stuff in the\x01",
            "room and then check it out.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A39():
        TurnDirection(0x107, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A39)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #20
        0x101,
        "#001FSounds good to me!\x02",
    )

    CloseMessageWindow()
    Jump("loc_ADD")

    label("loc_A68")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7E")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_A85")

    label("loc_A7E")

    TurnDirection(0x102, 0x0, 400)

    label("loc_A85")


    ChrTalk(    #21
        0x102,
        (
            "#010FThis must be the spa.\x02\x03",

            "Let's put our stuff in the\x01",
            "room and then check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADD")

    Jump("loc_BCB")

    label("loc_AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_END)), "loc_B6C")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #22
        (
            "\x07\x05-Women's Bath-\x01",
            "If you would like to use this service,\x01",
            "please let the front desk know.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_BCB")

    label("loc_B6C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #23
        (
            "\x07\x05A card hangs from the door.\x01",
            "'Cleaning in Progress'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_BCB")

    TalkEnd(0xFF)
    Return()

    # Function_14_91C end

    def Function_15_BCF(): pass

    label("Function_15_BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_BE0")
    OP_A2(0xC)
    Call(0, 16)
    Jump("loc_E7D")

    label("loc_BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_END)), "loc_D94")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #24
        (
            "\x07\x05-Men's Bath-\x01",
            "If you would like to use this service,\x01",
            "please let the front desk know.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D1C")
    OP_A2(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C88")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_C8F")

    label("loc_C88")

    TurnDirection(0x102, 0x0, 400)

    label("loc_C8F")


    ChrTalk(    #25
        0x102,
        (
            "#010FThis must be the spa.\x02\x03",

            "Let's put our stuff in the\x01",
            "room and then check it out.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CED():
        TurnDirection(0x107, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_CED)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #26
        0x101,
        "#001FSounds good to me!\x02",
    )

    CloseMessageWindow()
    Jump("loc_D91")

    label("loc_D1C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D32")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_D39")

    label("loc_D32")

    TurnDirection(0x102, 0x0, 400)

    label("loc_D39")


    ChrTalk(    #27
        0x102,
        (
            "#010FThis must be the spa.\x02\x03",

            "Let's put our stuff in the\x01",
            "room and then check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D91")

    Jump("loc_E7D")

    label("loc_D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_END)), "loc_E1E")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #28
        (
            "\x07\x05-Men's Bath-\x01",
            "If you would like to use this service,\x01",
            "please let the front desk know.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_E7D")

    label("loc_E1E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #29
        (
            "\x07\x05A card hangs from the door.\x01",
            "'Cleaning in Progress'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_E7D")

    TalkEnd(0xFF)
    Return()

    # Function_15_BCF end

    def Function_16_E81(): pass

    label("Function_16_E81")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "[Bathe]\x01",      # 0
            "[Leave]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EE2"),
        (1, "loc_110C"),
        (SWITCH_DEFAULT, "loc_110F"),
    )


    label("loc_EE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_EFF")
    OP_6F(0x9, 0)
    OP_70(0x9, 0x1D)
    Sleep(200)
    Jump("loc_F12")

    label("loc_EFF")

    OP_6F(0x8, 0)
    OP_70(0x8, 0x1D)
    Sleep(200)

    label("loc_F12")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x8, 0)
    OP_6F(0x9, 0)
    Sleep(600)
    OP_22(0xA2, 0x0, 0x64)
    Sleep(1500)
    OP_22(0xB, 0x0, 0x64)
    Sleep(800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_FD6")
    SetChrPos(0x0, -1000, 0, -5090, 90)
    SetChrPos(0x1, -1000, 0, -5090, 90)
    SetChrPos(0x2, -1000, 0, -5090, 90)
    SetChrPos(0x3, -1000, 0, -5090, 90)
    SetChrPos(0x4, -1000, 0, -5090, 90)
    SetChrPos(0x5, -1000, 0, -5090, 90)
    SetChrPos(0x6, -1000, 0, -5090, 90)
    SetChrPos(0x7, -1000, 0, -5090, 90)
    Jump("loc_105E")

    label("loc_FD6")

    SetChrPos(0x0, -1000, 0, 4900, 90)
    SetChrPos(0x1, -1000, 0, 4900, 90)
    SetChrPos(0x2, -1000, 0, 4900, 90)
    SetChrPos(0x3, -1000, 0, 4900, 90)
    SetChrPos(0x4, -1000, 0, 4900, 90)
    SetChrPos(0x5, -1000, 0, 4900, 90)
    SetChrPos(0x6, -1000, 0, 4900, 90)
    SetChrPos(0x7, -1000, 0, 4900, 90)

    label("loc_105E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1071")
    OP_31(0x0, 0xFB, 0x0)

    label("loc_1071")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1084")
    OP_31(0x1, 0xFB, 0x0)

    label("loc_1084")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1097")
    OP_31(0x2, 0xFB, 0x0)

    label("loc_1097")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10AA")
    OP_31(0x3, 0xFB, 0x0)

    label("loc_10AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BD")
    OP_31(0x5, 0xFB, 0x0)

    label("loc_10BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D0")
    OP_31(0x4, 0xFB, 0x0)

    label("loc_10D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E3")
    OP_31(0x6, 0xFB, 0x0)

    label("loc_10E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F6")
    OP_31(0x7, 0xFB, 0x0)

    label("loc_10F6")

    OP_69(0x0, 0x0)
    OP_30(0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_1112")

    label("loc_110C")

    Jump("loc_1112")

    label("loc_110F")

    Jump("loc_1112")

    label("loc_1112")

    OP_A3(0xC)
    TalkEnd(0xFF)
    Return()

    # Function_16_E81 end

    SaveToFile()

Try(main)
