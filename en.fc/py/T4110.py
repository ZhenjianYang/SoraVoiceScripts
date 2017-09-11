from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4110   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Patty',                                # 9
        'Ralph',                                # 10
        'Bill',                                 # 11
        'Ilene',                                # 12
        'Phelio',                               # 13
        'Lakeisha',                             # 14
        'Duncan',                               # 15
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
        'ED6_DT07/CH01030 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT07/CH01490 ._CH',             # 02
        'ED6_DT07/CH01180 ._CH',             # 03
        'ED6_DT07/CH01040 ._CH',             # 04
        'ED6_DT07/CH01030 ._CH',             # 05
        'ED6_DT07/CH01460 ._CH',             # 06
        'ED6_DT07/CH01043 ._CH',             # 07
        'ED6_DT07/CH01210 ._CH',             # 08
        'ED6_DT07/CH01183 ._CH',             # 09
        'ED6_DT07/CH01033 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01030P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT07/CH01490P._CP',             # 02
        'ED6_DT07/CH01180P._CP',             # 03
        'ED6_DT07/CH01040P._CP',             # 04
        'ED6_DT07/CH01030P._CP',             # 05
        'ED6_DT07/CH01460P._CP',             # 06
        'ED6_DT07/CH01043P._CP',             # 07
        'ED6_DT07/CH01210P._CP',             # 08
        'ED6_DT07/CH01183P._CP',             # 09
        'ED6_DT07/CH01033P._CP',             # 0A
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 26550,
        Z                   = 0,
        Y                   = -2980,
        Direction           = 77,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 32860,
        Z                   = 100,
        Y                   = 1000,
        Direction           = 175,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x111,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 51890,
        Z                   = 0,
        Y                   = 56160,
        Direction           = 84,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 59860,
        Z                   = 0,
        Y                   = 58240,
        Direction           = 9,
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
        X                   = 90200,
        Z                   = 0,
        Y                   = -2190,
        Direction           = 169,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 7200,
        Z                   = 200,
        Y                   = 53270,
        Direction           = 254,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 10450,
        Z                   = 0,
        Y                   = 53510,
        Direction           = 106,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )


    ScpFunction(
        "Function_0_222",          # 00, 0
        "Function_1_4E5",          # 01, 1
        "Function_2_532",          # 02, 2
        "Function_3_548",          # 03, 3
        "Function_4_56C",          # 04, 4
        "Function_5_590",          # 05, 5
        "Function_6_5B4",          # 06, 6
        "Function_7_F6E",          # 07, 7
        "Function_8_153F",         # 08, 8
        "Function_9_2496",         # 09, 9
        "Function_10_2B8A",        # 0A, 10
        "Function_11_32AA",        # 0B, 11
        "Function_12_38D6",        # 0C, 12
        "Function_13_3E3E",        # 0D, 13
        "Function_14_45CF",        # 0E, 14
    )


    def Function_0_222(): pass

    label("Function_0_222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_27D")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -28640, 0, 1890, 183)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -32060, 0, -2000, 187)
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x10, 0x80)
    Jump("loc_4E4")

    label("loc_27D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2C6")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -27680, 0, -3510, 10)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -32060, 0, -2000, 187)
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrFlags(0x10, 0x80)
    Jump("loc_4E4")

    label("loc_2C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_30A")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -27310, 0, -4370, 81)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -32060, 0, -2000, 187)
    OP_43(0x9, 0x0, 0x0, 0x3)
    Jump("loc_4E4")

    label("loc_30A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_364")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -27680, 0, -3510, 10)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -31960, 0, -1490, 135)
    OP_43(0x9, 0x0, 0x0, 0x2)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0x10, 1950, 0, 56650, 90)
    Jump("loc_4E4")

    label("loc_364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_373")
    SetChrFlags(0x10, 0x80)
    Jump("loc_4E4")

    label("loc_373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3A2")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 10)
    SetChrPos(0x8, -28640, 150, 1890, 180)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    Jump("loc_4E4")

    label("loc_3A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3D3")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -32060, 0, -2000, 187)
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    Jump("loc_4E4")

    label("loc_3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_424")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 10)
    SetChrPos(0x8, -28640, 150, 1890, 180)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -30620, 0, -1960, 0)
    SetChrFlags(0x9, 0x10)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_4E4")

    label("loc_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_450")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -32060, 0, -2000, 187)
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrFlags(0x10, 0x80)
    Jump("loc_4E4")

    label("loc_450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4B4")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 10)
    SetChrPos(0x8, -28640, 150, 1890, 180)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -32060, 0, -2000, 187)
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xB, 9)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x4)
    OP_44(0xB, 0xFF)
    Jump("loc_4E4")

    label("loc_4B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4E4")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -32369, 0, 790, 0)
    SetChrChipByIndex(0xB, 9)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x4)
    OP_44(0xB, 0xFF)

    label("loc_4E4")

    Return()

    # Function_0_222 end

    def Function_1_4E5(): pass

    label("Function_1_4E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_518")
    OP_B1("t4110_y")
    Jump("loc_521")

    label("loc_518")

    OP_B1("t4110_n")

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_531")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_531")

    Return()

    # Function_1_4E5 end

    def Function_2_532(): pass

    label("Function_2_532")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_547")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_532")

    label("loc_547")

    Return()

    # Function_2_532 end

    def Function_3_548(): pass

    label("Function_3_548")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56B")
    OP_8D(0xFE, -33020, -920, -30290, -3790, 4000)
    Jump("Function_3_548")

    label("loc_56B")

    Return()

    # Function_3_548 end

    def Function_4_56C(): pass

    label("Function_4_56C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_58F")
    OP_8D(0xFE, 24820, -4110, 30930, -1350, 1800)
    Jump("Function_4_56C")

    label("loc_58F")

    Return()

    # Function_4_56C end

    def Function_5_590(): pass

    label("Function_5_590")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5B3")
    OP_8D(0xFE, 89790, -700, 91780, -4740, 2000)
    Jump("Function_5_590")

    label("loc_5B3")

    Return()

    # Function_5_590 end

    def Function_6_5B4(): pass

    label("Function_6_5B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_681")

    ChrTalk(    #0
        0xFE,
        (
            "I've been recognized by the\x01",
            "archbishop, so maybe I'll put\x01",
            "out a book about my trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "You'd be surprised how useful one's\x01",
            "life experience can be when one's\x01",
            "been on a world pilgrimage!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F6A")

    label("loc_681")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_6D1")

    ChrTalk(    #2
        0xFE,
        "Finally! The house is clean!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Time to head to the cathedral.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F6A")

    label("loc_6D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_791")

    ChrTalk(    #4
        0xFE,
        (
            "My wife always has to leave early\x01",
            "each morning, so I'm in charge of\x01",
            "making breakfast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Lunch is by our own means, and\x01",
            "whoever gets home earliest is \x01",
            "the one to make dinner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F6A")

    label("loc_791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_79B")
    Jump("loc_F6A")

    label("loc_79B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_821")

    ChrTalk(    #6
        0xFE,
        (
            "Today, I'm headed to the cathedral\x01",
            "for my prayers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I must finish all this cleaning\x01",
            "before the morning is through!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F6A")

    label("loc_821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_9BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_8D0")

    ChrTalk(    #8
        0xFE,
        (
            "Every now and again, I envy the\x01",
            "life my betrothed is living...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I believe it was her lack of\x01",
            "inhibition that attracted me\x01",
            "to her in the first place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BB")

    label("loc_8D0")

    OP_A2(0x7)

    ChrTalk(    #10
        0xFE,
        (
            "Honestly, there are times when\x01",
            "I envy my wife's lifestyle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "But I can't live my own life\x01",
            "that way, no matter how much\x01",
            "I may wish to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I believe it was her lack of\x01",
            "inhibition that attracted me\x01",
            "to her in the first place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BB")

    Jump("loc_F6A")

    label("loc_9BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_9C8")
    Jump("loc_F6A")

    label("loc_9C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_A10")

    ChrTalk(    #13
        0xFE,
        (
            "Having a working wife can be\x01",
            "difficult, at times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2B")

    label("loc_A10")

    OP_A2(0x7)

    ChrTalk(    #14
        0xFE,
        (
            "Religiously speaking, I wish\x01",
            "she'd moderate her shopping \x01",
            "vice and live more...simply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "But she DID pay for this\x01",
            "entire pilgrimage herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Or rather, her father did. And as his\x01",
            "son-in-law, I am the guest, and thus\x01",
            "obliged to keep my lectures to myself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "Heh...\x02",
    )

    CloseMessageWindow()

    label("loc_B2B")

    Jump("loc_F6A")

    label("loc_B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_BDB")

    ChrTalk(    #18
        0xFE,
        (
            "My wife inherited her father's\x01",
            "store from him, and she's really\x01",
            "quite adept at running it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "We just finished our trip, and\x01",
            "now it's back to work for her!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F6A")

    label("loc_BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_EC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_CE3")

    ChrTalk(    #20
        0xFE,
        (
            "The many Septian Churches dotting\x01",
            "this kingdom have stood for several\x01",
            "hundreds of years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "After the Great Collapse, traveling the country-\x01",
            "side became a meaningful act, allowing pilgrims\x01",
            "to better reflect on the teachings of the Goddess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC6")

    label("loc_CE3")

    OP_A2(0x7)

    ChrTalk(    #22
        0xFE,
        (
            "The many Septian Churches dotting\x01",
            "this kingdom have stood for several\x01",
            "hundreds of years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "After the Great Collapse, traveling the country-\x01",
            "side became a meaningful act, allowing pilgrims\x01",
            "to better reflect on the teachings of the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "For me, it was also a chance \x01",
            "to spend some time with my\x01",
            "otherwise very busy wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "I don't think she had any epiphanies, but she\x01",
            "did manage to get a lot of her beloved shopping\x01",
            "done, so I think she's pleased with the trip.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC6")

    Jump("loc_F6A")

    label("loc_EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_F6A")

    ChrTalk(    #26
        0xFE,
        (
            "It's good to be home after \x01",
            "such a long pilgrimage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "A new sister joined the cathedral in\x01",
            "my absence. I must familiarize myself\x01",
            "with her name...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6A")

    TalkEnd(0xFE)
    Return()

    # Function_6_5B4 end

    def Function_7_F6E(): pass

    label("Function_7_F6E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_F7B")
    Jump("loc_153B")

    label("loc_F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_F85")
    Jump("loc_153B")

    label("loc_F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_FC6")

    ChrTalk(    #28
        0xFE,
        (
            "Well, I guess I'd better get\x01",
            "over to the store...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_153B")

    label("loc_FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_102A")

    ChrTalk(    #29
        0xFE,
        "Hmm? Seagaro's not home yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "I guess that means making\x01",
            "dinner's my job today...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_153B")

    label("loc_102A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1034")
    Jump("loc_153B")

    label("loc_1034")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_11D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_10DD")

    ChrTalk(    #31
        0xFE,
        (
            "My husband needs to enjoy\x01",
            "life a bit more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "He's always all 'thou mustn't' this\x01",
            "and 'thou shan't' that. It's got to\x01",
            "be taking its toll on him!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11D4")

    label("loc_10DD")

    OP_A2(0x8)

    ChrTalk(    #33
        0xFE,
        (
            "My husband needs to enjoy\x01",
            "life a bit more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "He's always all 'thou mustn't' this\x01",
            "and 'thou shan't' that. It's got to\x01",
            "be taking its toll on him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "It shows how seriously he \x01",
            "takes life though. And that's\x01",
            "a very, very important trait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D4")

    Jump("loc_153B")

    label("loc_11D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_11E1")
    Jump("loc_153B")

    label("loc_11E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1320")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_127D")

    ChrTalk(    #36
        0xFE,
        (
            "Being back in the capital and\x01",
            "running a store means I have\x01",
            "no time to enjoy shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "*sigh* How I'd love to go on\x01",
            "another trip!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_131D")

    label("loc_127D")

    OP_A2(0x8)

    ChrTalk(    #38
        0xFE,
        "There we go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Being back in the capital and\x01",
            "running a store means I have\x01",
            "no time to enjoy shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "*sigh* How I'd love to go on\x01",
            "another trip!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_131D")

    Jump("loc_153B")

    label("loc_1320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_132A")
    Jump("loc_153B")

    label("loc_132A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_13B8")

    ChrTalk(    #41
        0xFE,
        (
            "Back to work again, first\x01",
            "thing tomorrow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "The Martial Arts Competition\x01",
            "and Birthday Celebration make \x01",
            "this profit season!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_153B")

    label("loc_13B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_153B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1447")

    ChrTalk(    #43
        0xFE,
        (
            "My husband got to enjoy his\x01",
            "churches, and I got to enjoy\x01",
            "my shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "It was win-win for us, both\x01",
            "husband AND wife!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_153B")

    label("loc_1447")

    OP_A2(0x8)

    ChrTalk(    #45
        0xFE,
        "Ahhhh, so busy again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "I did so much shopping that \x01",
            "getting it all sorted out is\x01",
            "going to take forever!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "My husband got to enjoy his\x01",
            "churches, and I got to enjoy\x01",
            "my shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "It was win-win for us, both\x01",
            "husband AND wife!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_153B")

    TalkEnd(0xFE)
    Return()

    # Function_7_F6E end

    def Function_8_153F(): pass

    label("Function_8_153F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_16BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_15E8")

    ChrTalk(    #49
        0xFE,
        (
            "So the ports were all closed \x01",
            "because of the coup, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "After the Birthday Celebration\x01",
            "I bet I'll have a mountain of\x01",
            "work waiting for me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16BA")

    label("loc_15E8")

    OP_A2(0x6)

    ChrTalk(    #51
        0xFE,
        (
            "So the ports were all closed \x01",
            "because of the coup, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Man... Thanks for the headache,\x01",
            "Royal Army bastards!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "After the Birthday Celebration\x01",
            "I bet I'll have a mountain of\x01",
            "work waiting for me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16BA")

    Jump("loc_2492")

    label("loc_16BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_185D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1773")

    ChrTalk(    #54
        0xFE,
        (
            "What is the deal with those\x01",
            "soldiers in black anyway?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "They've been walking around the\x01",
            "capital since sunrise. It ain't\x01",
            "natural! Something is surely afoot!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_185A")

    label("loc_1773")

    OP_A2(0x6)

    ChrTalk(    #56
        0xFE,
        (
            "What is the deal with those\x01",
            "soldiers in black anyway?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Their excess of arrogance is\x01",
            "really starting to annoy me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "They've been walking around the\x01",
            "capital since sunrise. It ain't\x01",
            "natural! Something is surely afoot!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_185A")

    Jump("loc_2492")

    label("loc_185D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1A6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_193B")

    ChrTalk(    #59
        0xFE,
        (
            "A lot of people came to the capital for the\x01",
            "Birthday Celebration, completely unaware\x01",
            "that Her Majesty had fallen ill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "It would be a disaster if they should\x01",
            "just up and cancel the festival now...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A68")

    label("loc_193B")

    OP_A2(0x6)

    ChrTalk(    #61
        0xFE,
        (
            "Now that the competition's done,\x01",
            "the Birthday Celebration should\x01",
            "be starting up soon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "A lot of people came to the capital for the\x01",
            "Birthday Celebration, completely unaware\x01",
            "that Her Majesty had fallen ill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "It would be a disaster if they should\x01",
            "just up and cancel the festival now...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A68")

    Jump("loc_2492")

    label("loc_1A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1B66")

    ChrTalk(    #64
        0xFE,
        (
            "The duke is inviting the winners of the tournament\x01",
            "to the castle for a banquet. If the queen is so\x01",
            "sick, how is that anything but a bad idea?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "Once again, the duke does an\x01",
            "exemplary job of making us \x01",
            "fear for our country's future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2492")

    label("loc_1B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1CE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1BA9")

    ChrTalk(    #66
        0xFE,
        (
            "I just want everything to go\x01",
            "back to normal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CE6")

    label("loc_1BA9")

    OP_A2(0x6)

    ChrTalk(    #67
        0xFE,
        (
            "Now it's not just the port, \x01",
            "but also the Erbe Royal Villa\x01",
            "that's closed to the public.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "It's been such a long time\x01",
            "since we've been allowed\x01",
            "to go into the castle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "The only real bright spot amidst\x01",
            "all of this has been the Martial\x01",
            "Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "I just want everything to go\x01",
            "back to normal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CE6")

    Jump("loc_2492")

    label("loc_1CE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1F48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1DDE")

    ChrTalk(    #71
        0xFE,
        (
            "I've got a ton of work that I should have\x01",
            "been able to finish before the festivities\x01",
            "that I'm still not even able to START yet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "And it's not like the army is \x01",
            "giving me any compensation for\x01",
            "all the work I'm not doing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F45")

    label("loc_1DDE")

    OP_A2(0x6)

    ChrTalk(    #73
        0xFE,
        (
            "And do you think they'll re-open the port \x01",
            "amidst all these extra regulations? Just a\x01",
            "hint, but I wouldn't hold my breath!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "I've got a ton of work that I should have\x01",
            "been able to finish before the festivities\x01",
            "that I'm still not even able to START yet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "And it's not like the army is \x01",
            "giving me any compensation for\x01",
            "all the work I'm not doing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F45")

    Jump("loc_2492")

    label("loc_1F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2103")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2008")

    ChrTalk(    #76
        0xFE,
        (
            "I get to sit here at home and\x01",
            "wait for the ports to re-open\x01",
            "so I can go back to work. Joy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "I can't even go watch the\x01",
            "Martial Arts Competition.\x01",
            "I'm going stir crazy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2100")

    label("loc_2008")

    OP_A2(0x6)

    ChrTalk(    #78
        0xFE,
        (
            "I get to sit here at home and\x01",
            "wait for the ports to re-open\x01",
            "so I can go back to work. Joy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "I can't even go watch the\x01",
            "Martial Arts Competition.\x01",
            "I'm going stir crazy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "Why can't I get the day off?\x01",
            "Nothing's going to get done\x01",
            "anyway!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2100")

    Jump("loc_2492")

    label("loc_2103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_22D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_21C1")

    ChrTalk(    #81
        0xFE,
        (
            "So the army's telling us that\x01",
            "the Royal Guardsmen were the\x01",
            "terrorists after all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "You know what I think? I think\x01",
            "those Special Ops guys from\x01",
            "the tournament did it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22D1")

    label("loc_21C1")

    OP_A2(0x6)

    ChrTalk(    #83
        0xFE,
        (
            "So the army's telling us that\x01",
            "the Royal Guardsmen were the\x01",
            "terrorists after all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "The Royal Guardsmen are a bit\x01",
            "formal and old-fashioned, but\x01",
            "they're not bad people at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "You know what I think? I think\x01",
            "those Special Ops guys from\x01",
            "the tournament did it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D1")

    Jump("loc_2492")

    label("loc_22D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2376")

    ChrTalk(    #86
        0xFE,
        (
            "I just want the Royal Army\x01",
            "to get out of the port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "A boat tried to come in from\x01",
            "Ruan, but was denied entry and\x01",
            "left to drift out in the lake.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2492")

    label("loc_2376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_244F")

    ChrTalk(    #88
        0xFE,
        (
            "There are lot of packages from\x01",
            "Ruan left in the Grancel port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "But thanks to the Royal Army's\x01",
            "anti-terror initiative, the\x01",
            "ports are all locked down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "And here I am, stuck at\x01",
            "home without a job!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2492")

    label("loc_244F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2492")

    ChrTalk(    #91
        0xFE,
        (
            "How long do they plan to keep\x01",
            "the port closed, anyway?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2492")

    TalkEnd(0xFE)
    Return()

    # Function_8_153F end

    def Function_9_2496(): pass

    label("Function_9_2496")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_24A3")
    Jump("loc_2B86")

    label("loc_24A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2503")

    ChrTalk(    #92
        0xFE,
        (
            "The port's closed, and nobody's\x01",
            "hiring now anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "Where should I try next?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B86")

    label("loc_2503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2646")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2580")

    ChrTalk(    #94
        0xFE,
        (
            "They just sold a house around\x01",
            "here recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "I wish I were living there;\x01",
            "this place is too small.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2643")

    label("loc_2580")

    OP_A2(0x4)

    ChrTalk(    #96
        0xFE,
        (
            "They just sold a house around\x01",
            "here recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "I wish I were living there;\x01",
            "this place is too small.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "If I worked hard enough, I \x01",
            "could take out a loan and\x01",
            "buy a place of my own...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2643")

    Jump("loc_2B86")

    label("loc_2646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_26DF")

    ChrTalk(    #99
        0xFE,
        (
            "That final match was pretty\x01",
            "amazing, wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "Yeah! Tomorrow, I'm rolling \x01",
            "up my sleeves and making \x01",
            "something new out of my life!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B86")

    label("loc_26DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2794")

    ChrTalk(    #101
        0xFE,
        (
            "Today I'm going to watch the\x01",
            "Martial Arts Competition \x01",
            "championship with my wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "Hopefully it'll inspire me\x01",
            "to get motivated! Or motivate\x01",
            "me to get inspired...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B86")

    label("loc_2794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_288F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_280D")

    ChrTalk(    #103
        0xFE,
        (
            "I promised I would quit\x01",
            "smoking and find a job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "Then my wife said we could\x01",
            "go see the finals.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_288C")

    label("loc_280D")

    OP_A2(0x4)

    ChrTalk(    #105
        0xFE,
        (
            "I promised I would quit\x01",
            "smoking and find a job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "Then my wife said we could\x01",
            "go see the finals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "I can do this!\x02",
    )

    CloseMessageWindow()

    label("loc_288C")

    Jump("loc_2B86")

    label("loc_288F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2938")

    ChrTalk(    #108
        0xFE,
        "I am a MAN!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "Time to shout it from the roof-\x01",
            "tops...uphill...both ways...in\x01",
            "HELL!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "With the Goddess as my witness,\x01",
            "I will never go jobless again!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B86")

    label("loc_2938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_29B5")

    ChrTalk(    #111
        0xFE,
        "We can't live like this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "I've been saying I'll go find\x01",
            "a job, but that's all I've been\x01",
            "doing: saying it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B86")

    label("loc_29B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2A63")

    ChrTalk(    #113
        0xFE,
        (
            "We didn't move here to the\x01",
            "capital to live this way...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "We ought to be able to have a little\x01",
            "fun during the Birthday Celebration,\x01",
            "at least, though, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B86")

    label("loc_2A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2B0F")

    ChrTalk(    #115
        0xFE,
        (
            "Wow, the tickets to the Martial Arts\x01",
            "Competition are CRAZY expensive!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "They usually discount them.\x01",
            "I can't believe Duke Dunan\x01",
            "is getting away with this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B86")

    label("loc_2B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2B86")

    ChrTalk(    #117
        0xFE,
        "We just moved here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "Ever since I was a child, it's\x01",
            "been a dream of mine to live\x01",
            "in the royal capital.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B86")

    TalkEnd(0xFE)
    Return()

    # Function_9_2496 end

    def Function_10_2B8A(): pass

    label("Function_10_2B8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2B97")
    Jump("loc_32A6")

    label("loc_2B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2BEF")

    ChrTalk(    #119
        0xFE,
        (
            "How long do these soldiers \x01",
            "plan on standing around\x01",
            "our streets, anyway?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A6")

    label("loc_2BEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2E77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2CF7")

    ChrTalk(    #120
        0xFE,
        (
            "Earlier he went out and bought\x01",
            "a stuffed doll--'for when we\x01",
            "have a little girl,' he said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "We don't even know if we'll\x01",
            "be having a girl, though!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "And if we don't...well, then\x01",
            "I guess we'll have a little boy\x01",
            "who enjoys dolls. OR ELSE.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E74")

    label("loc_2CF7")

    OP_A2(0x5)

    ChrTalk(    #123
        0xFE,
        (
            "Not two seconds after he left,\x01",
            "he runs back in raving about\x01",
            "us buying a house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "It's hard enough for us to pay rent\x01",
            "on THIS dump each month...so how are\x01",
            "we supposed to afford a mortgage?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "I finally told him, stop screwing\x01",
            "around and find yourself a job.\x01",
            "And THEN we'll talk!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "*sigh* For better or for worse,\x01",
            "for richer or poorer...till death\x01",
            "do us part...ugh!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E74")

    Jump("loc_32A6")

    label("loc_2E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2F48")

    ChrTalk(    #127
        0xFE,
        (
            "He said he would look for\x01",
            "work instead of going to\x01",
            "watch the tournament...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "But I knew he'd never keep that promise.\x01",
            "So...I broke it for him, and told him we'd\x01",
            "go. I'm a good wife, damn it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A6")

    label("loc_2F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2F9E")

    ChrTalk(    #129
        0xFE,
        (
            "Thinking about it, we haven't\x01",
            "been on a date for...who knows\x01",
            "how long!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A6")

    label("loc_2F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_304E")

    ChrTalk(    #130
        0xFE,
        (
            "So I was the one who said,\x01",
            "'Let's go watch the tournament\x01",
            "together!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "*sigh* Guess I don't have to\x01",
            "worry about him breaking his\x01",
            "promise. I broke it FOR him!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A6")

    label("loc_304E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_30B4")

    ChrTalk(    #132
        0xFE,
        "Okay, I've made up my mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "It's time for us to sit down\x01",
            "and have a serious talk.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A6")

    label("loc_30B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3119")

    ChrTalk(    #134
        0xFE,
        "My husband's a lazy man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "But I'm also responsible for\x01",
            "letting him stay that way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A6")

    label("loc_3119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_31F1")

    ChrTalk(    #136
        0xFE,
        (
            "What is this 'we should be able to have a little\x01",
            "fun now, at least' garbage?! The reason we can't\x01",
            "afford to is because HE doesn't have a job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "I never would have imagined \x01",
            "he was this kind of man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A6")

    label("loc_31F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3244")

    ChrTalk(    #138
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "We shouldn't even be going to\x01",
            "the tournament right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A6")

    label("loc_3244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_32A6")

    ChrTalk(    #140
        0xFE,
        (
            "I swear, ever since we moved\x01",
            "here to the capital all he's\x01",
            "done is piss his life away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32A6")

    TalkEnd(0xFE)
    Return()

    # Function_10_2B8A end

    def Function_11_32AA(): pass

    label("Function_11_32AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_32B7")
    Jump("loc_38D2")

    label("loc_32B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3308")

    ChrTalk(    #141
        0xFE,
        (
            "Look at all the soldiers\x01",
            "out there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "Trouble's a-brewin'...\x02",
    )

    CloseMessageWindow()
    Jump("loc_38D2")

    label("loc_3308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_338A")

    ChrTalk(    #143
        0xFE,
        (
            "Her Majesty the Queen is the\x01",
            "center of our kingdom and the\x01",
            "pride of our people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        "I want to see her well again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_38D2")

    label("loc_338A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_33F8")

    ChrTalk(    #145
        0xFE,
        (
            "I got so caught up in the \x01",
            "match I don't even remember\x01",
            "getting up on my feet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        "Oh, dear...\x02",
    )

    CloseMessageWindow()
    Jump("loc_38D2")

    label("loc_33F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3432")

    ChrTalk(    #147
        0xFE,
        "Grandpa, you devil!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "Hold on a moment.\x02",
    )

    CloseMessageWindow()
    Jump("loc_38D2")

    label("loc_3432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_349A")

    ChrTalk(    #149
        0xFE,
        "So, what shall I make for dinner?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "Baked potatoes and sauteed\x01",
            "mushrooms sounds good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D2")

    label("loc_349A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3697")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3588")

    ChrTalk(    #151
        0xFE,
        (
            "Hmm... Actually, come to\x01",
            "think of it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "...I think that kind young gentleman\x01",
            "who came to my aid earlier was part\x01",
            "of a team from the tournament...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "They're the ones who lost to\x01",
            "the Republican team, for sure!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3694")

    label("loc_3588")

    OP_A2(0x3)

    ChrTalk(    #154
        0xFE,
        (
            "Grandpa and I left the house\x01",
            "early this morning to go\x01",
            "shopping at the general store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "We ended up buying too much.\x01",
            "So there we were, with all \x01",
            "these heavy bags...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "...and along comes this kind\x01",
            "young man with a red bandana,\x01",
            "who carried them all for us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3694")

    Jump("loc_38D2")

    label("loc_3697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3748")

    ChrTalk(    #157
        0xFE,
        (
            "The castle actually gave us tickets\x01",
            "to the tournament...so, we went!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "Grandpa gets so excited during\x01",
            "each match. He acts almost\x01",
            "like a little boy with candy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D2")

    label("loc_3748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_37B3")

    ChrTalk(    #159
        0xFE,
        (
            "Well, if we're going out this\x01",
            "afternoon, I'd better get all\x01",
            "the cleaning done this morning!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D2")

    label("loc_37B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_386C")

    ChrTalk(    #160
        0xFE,
        (
            "There's so much more energy in\x01",
            "the air during the Martial Arts\x01",
            "Competition!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "It's like everyone's sharing\x01",
            "their youth with me. I could\x01",
            "go a few more years like this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D2")

    label("loc_386C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_38D2")

    ChrTalk(    #162
        0xFE,
        "...Just listen to me babble...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "You can still get excited, no\x01",
            "matter how old you are!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38D2")

    TalkEnd(0xFE)
    Return()

    # Function_11_32AA end

    def Function_12_38D6(): pass

    label("Function_12_38D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_38E3")
    Jump("loc_3E3A")

    label("loc_38E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3911")

    ChrTalk(    #164
        0xFE,
        "Something outside seems...off.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_3911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_39CE")

    ChrTalk(    #165
        0xFE,
        (
            "You know, the queen's illness\x01",
            "really has me worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "I'm worried about the terrorists too,\x01",
            "of course, but I'm more interested in\x01",
            "hearing news of Her Majesty's recovery.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_39CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3A57")

    ChrTalk(    #167
        0xFE,
        "Wow, what a match!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "I don't know martial arts very well,\x01",
            "but I know a spectacle of epic pro-\x01",
            "portions when I see one!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_3A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3AA7")

    ChrTalk(    #169
        0xFE,
        (
            "Hurry it up, Shorty, or we'll\x01",
            "be stuck in the nosebleed\x01",
            "section!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_3AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3B03")

    ChrTalk(    #170
        0xFE,
        (
            "I've been eating Shorty's\x01",
            "cooking for decades and I'm\x01",
            "still not tired of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_3B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3BC3")

    ChrTalk(    #171
        0xFE,
        (
            "I know we old people are \x01",
            "always complaining about \x01",
            "the kids these days...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "But really, we were the same way\x01",
            "when we were young. Always on\x01",
            "peoples' lawns, with our music...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_3BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3C4B")

    ChrTalk(    #173
        0xFE,
        "I feel so young again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "I really hope my grandkids, and\x01",
            "their kids too, get to grow up in\x01",
            "a time of peace like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_3C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3C8A")

    ChrTalk(    #175
        0xFE,
        (
            "Good morning! Fine weather we've\x01",
            "got, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_3C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3E3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3D1E")

    ChrTalk(    #176
        0xFE,
        (
            "The two of us have been living\x01",
            "here in Grancel since we were\x01",
            "just little bawling babies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "This is how the city should be.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_3D1E")

    OP_A2(0x2)

    ChrTalk(    #178
        0xFE,
        (
            "We were pretty depressed when we heard the news\x01",
            "about the queen, but now the status quo seems to\x01",
            "be returning...and all is right with the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "The two of us have been living\x01",
            "here in Grancel since we were\x01",
            "just little bawling babies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "This is how the city should be.\x02",
    )

    CloseMessageWindow()

    label("loc_3E3A")

    TalkEnd(0xFE)
    Return()

    # Function_12_38D6 end

    def Function_13_3E3E(): pass

    label("Function_13_3E3E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3ED3")

    ChrTalk(    #181
        0xFE,
        (
            "It's hard to imagine Colonel\x01",
            "Richard as the one who planned\x01",
            "this whole coup d'etat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "Every one of us was taken in\x01",
            "by his lies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CB")

    label("loc_3ED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3F3C")

    ChrTalk(    #183
        0xFE,
        (
            "Those black-clad soldiers make\x01",
            "me feel kind of...nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        "Maybe I'll just stay in...\x02",
    )

    CloseMessageWindow()
    Jump("loc_45CB")

    label("loc_3F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3FCB")

    ChrTalk(    #185
        0xFE,
        (
            "I can't believe the Royal\x01",
            "Guardsmen were behind the\x01",
            "terrorist attack...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "But, if Colonel Richard \x01",
            "said it, it must be true!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CB")

    label("loc_3FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4205")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_40D2")

    ChrTalk(    #187
        0xFE,
        (
            "The trick to winning the game is to subtly nudge\x01",
            "your spouse into doing something on her own as\x01",
            "if it were her idea, rather than directly asking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "Marriage is...a game. A strategy\x01",
            "role-playing game, with both sides\x01",
            "in constant struggle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4202")

    label("loc_40D2")

    OP_A2(0x1)

    ChrTalk(    #189
        0xFE,
        (
            "Today my wife is doing all of\x01",
            "the housework. Heh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "The trick to winning the game is to subtly nudge\x01",
            "your spouse into doing something on her own as\x01",
            "if it were her idea, rather than directly asking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "Marriage is...a game. A strategy\x01",
            "role-playing game, with both sides\x01",
            "in constant struggle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4202")

    Jump("loc_45CB")

    label("loc_4205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_420F")
    Jump("loc_45CB")

    label("loc_420F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4219")
    Jump("loc_45CB")

    label("loc_4219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_42FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_426B")

    ChrTalk(    #192
        0xFE,
        (
            "Better clean up the house, so\x01",
            "the wifey doesn't complain...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42F9")

    label("loc_426B")

    OP_A2(0x1)

    ChrTalk(    #193
        0xFE,
        "...I know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "I'm going to pull some top-rate hypnotic\x01",
            "suggestion techniques on her tomorrow.\x01",
            "Just you wait and see! Heh heh heh...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42F9")

    Jump("loc_45CB")

    label("loc_42FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4336")

    ChrTalk(    #195
        0xFE,
        (
            "Uh, so...wh-what's going on\x01",
            "with...dinner?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CB")

    label("loc_4336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_442B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4374")

    ChrTalk(    #196
        0xFE,
        (
            "*sigh* Guess I'd better get\x01",
            "cleaning...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4428")

    label("loc_4374")

    OP_A2(0x1)

    ChrTalk(    #197
        0xFE,
        (
            "When I woke up this morning,\x01",
            "my wife was already gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        "She'd already left for the arena.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "*sigh* Five years already...\x01",
            "Is this how married life is\x01",
            "supposed to be?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4428")

    Jump("loc_45CB")

    label("loc_442B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4578")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_44A9")

    ChrTalk(    #200
        0xFE,
        (
            "I don't mind her going to the\x01",
            "arena or anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "But would it kill her to do a\x01",
            "little housework?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4575")

    label("loc_44A9")

    OP_A2(0x1)

    ChrTalk(    #202
        0xFE,
        (
            "No, I don't mind her going\x01",
            "to the arena or anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "But would it kill her to do a\x01",
            "little housework?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "This isn't how things were\x01",
            "supposed to be. This isn't\x01",
            "what we promised each other!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4575")

    Jump("loc_45CB")

    label("loc_4578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_45CB")

    ChrTalk(    #205
        0xFE,
        (
            "At least if she's out, she\x01",
            "isn't nagging me while I do\x01",
            "HER cleaning...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45CB")

    TalkEnd(0xFE)
    Return()

    # Function_13_3E3E end

    def Function_14_45CF(): pass

    label("Function_14_45CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4667")

    ChrTalk(    #206
        0xFE,
        (
            "Princess Klaudia has really\x01",
            "grown up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "She's, like, ten billion times\x01",
            "more suitable for succession\x01",
            "than Duke Dunan could EVER be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BDC")

    label("loc_4667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_46D0")

    ChrTalk(    #208
        0xFE,
        (
            "All these soldiers are standing\x01",
            "around and staring at us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        "I don't like it one bit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BDC")

    label("loc_46D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4769")

    ChrTalk(    #210
        0xFE,
        (
            "Now that the tournament's over,\x01",
            "the Birthday Celebration should\x01",
            "be moments away from starting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "At least, that's usually how\x01",
            "it goes!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BDC")

    label("loc_4769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4889")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_47B1")

    ChrTalk(    #212
        0xFE,
        (
            "Wow, that final was a real\x01",
            "back-and-forth battle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4886")

    label("loc_47B1")

    OP_A2(0x0)

    ChrTalk(    #213
        0xFE,
        (
            "Wow, that final was a real\x01",
            "back-and-forth battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        "I had such great seats! And...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #215
        0xFE,
        (
            "I found out just how much my\x01",
            "husband really loves me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        "This is the best day ever!\x02",
    )

    CloseMessageWindow()

    label("loc_4886")

    Jump("loc_4BDC")

    label("loc_4889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4893")
    Jump("loc_4BDC")

    label("loc_4893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4A44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_494D")

    ChrTalk(    #217
        0xFE,
        (
            "I thought I was going to have\x01",
            "to camp out overnight to get\x01",
            "some good arena seats...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "But my husband lined up for\x01",
            "me. 'It's too dangerous for\x01",
            "a woman!' he said.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A41")

    label("loc_494D")

    OP_A2(0x0)

    ChrTalk(    #219
        0xFE,
        (
            "I thought I was going to have\x01",
            "to camp out overnight to get\x01",
            "some good arena seats...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "But my husband lined up for\x01",
            "me. 'It's too dangerous for\x01",
            "a woman!' he said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "...Well, that's men for you.\x01",
            "And husbands are doubly bad!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A41")

    Jump("loc_4BDC")

    label("loc_4A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4A4E")
    Jump("loc_4BDC")

    label("loc_4A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4B17")

    ChrTalk(    #223
        0xFE,
        (
            "What they need to do is wait for the right\x01",
            "moment, pin down the opponent with orbal gun\x01",
            "shots, then move in for the kill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "Their switch between offense\x01",
            "and defense is just terrible!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BDC")

    label("loc_4B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4B21")
    Jump("loc_4BDC")

    label("loc_4B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4BD5")

    ChrTalk(    #225
        0xFE,
        (
            "Today's matches were good, \x01",
            "even for preliminaries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "You've got to watch this all the way\x01",
            "through, though, if you want to really\x01",
            "get a feel for how things went.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BDC")

    label("loc_4BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4BDC")

    label("loc_4BDC")

    TalkEnd(0xFE)
    Return()

    # Function_14_45CF end

    SaveToFile()

Try(main)
