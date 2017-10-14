from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4210   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        'Sorella',                              # 9
        'Royal Guardsman',                      # 10
        'Royal Guardsman',                      # 11
        'Head Maid Hilda',                      # 12
        'Duke Dunan',                           # 13
        'Princess Klaudia',                     # 14
        'Queen Alicia',                         # 15
        'Butler Phillip',                       # 16
        'Luciola',                              # 17
        'Walter',                               # 18
        'Bleublanc',                            # 19
        'Renne',                                # 20
        'Royal Guardsman',                      # 21
        'Royal Guardsman',                      # 22
        'Royal Guardsman',                      # 23
        'Royal Guardsman',                      # 24
        'Royal Guardsman',                      # 25
        'Royal Guardsman',                      # 26
        'Royal Guardsman',                      # 27
        'Royal Guardsman',                      # 28
        'Royal Guardsman',                      # 29
        'Royal Guardsman',                      # 30
        'Royal Guardsman',                      # 31
        'Royal Guardsman',                      # 32
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
        'ED6_DT26/CH20447 ._CH',             # 00
        'ED6_DT26/CH20448 ._CH',             # 01
        'ED6_DT26/CH20449 ._CH',             # 02
        'ED6_DT07/CH01350 ._CH',             # 03
        'ED6_DT07/CH01320 ._CH',             # 04
        'ED6_DT07/CH02460 ._CH',             # 05
        'ED6_DT26/CH20421 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT26/CH20447P._CP',             # 00
        'ED6_DT26/CH20448P._CP',             # 01
        'ED6_DT26/CH20449P._CP',             # 02
        'ED6_DT07/CH01350P._CP',             # 03
        'ED6_DT07/CH01320P._CP',             # 04
        'ED6_DT07/CH02460P._CP',             # 05
        'ED6_DT26/CH20421P._CP',             # 06
    )

    DeclNpc(
        X                   = -170,
        Z                   = 1000,
        Y                   = 4390,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 5000,
        Z                   = 0,
        Y                   = -5000,
        Direction           = 182,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -5000,
        Z                   = 0,
        Y                   = -5000,
        Direction           = 182,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 20,
        Z                   = 9000,
        Y                   = 29200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -1880,
        Y                   = 8000,
        Z                   = 29100,
        Range               = 1580,
        Unknown_10          = 0x2AF8,
        Unknown_14          = 0x760C,
        Unknown_18          = 0x0,
        Unknown_1C          = 20,
    )


    ScpFunction(
        "Function_0_402",          # 00, 0
        "Function_1_49A",          # 01, 1
        "Function_2_51C",          # 02, 2
        "Function_3_540",          # 03, 3
        "Function_4_77F",          # 04, 4
        "Function_5_8BB",          # 05, 5
        "Function_6_9E4",          # 06, 6
        "Function_7_D5D",          # 07, 7
        "Function_8_131D",         # 08, 8
        "Function_9_24F0",         # 09, 9
        "Function_10_251E",        # 0A, 10
        "Function_11_254C",        # 0B, 11
        "Function_12_257A",        # 0C, 12
        "Function_13_2745",        # 0D, 13
        "Function_14_3059",        # 0E, 14
        "Function_15_30EC",        # 0F, 15
        "Function_16_3172",        # 10, 16
        "Function_17_31CB",        # 11, 17
        "Function_18_33B0",        # 12, 18
        "Function_19_3595",        # 13, 19
        "Function_20_377A",        # 14, 20
    )


    def Function_0_402(): pass

    label("Function_0_402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_41B")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_427")

    label("loc_41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_427")
    ClearChrFlags(0xB, 0x80)

    label("loc_427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 5)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43B")
    Call(0, 12)

    label("loc_43B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_44C")
    OP_A3(0x10F0)
    Event(0, 8)
    Jump("loc_499")

    label("loc_44C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_45D")
    OP_A3(0x10F1)
    Event(0, 14)
    Jump("loc_499")

    label("loc_45D")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_469"),
        (SWITCH_DEFAULT, "loc_499"),
    )


    label("loc_469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_481")
    SetMapFlags(0x10000000)
    Event(0, 13)
    Jump("loc_496")

    label("loc_481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_496")
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_496")

    Jump("loc_499")

    label("loc_499")

    Return()

    # Function_0_402 end

    def Function_1_49A(): pass

    label("Function_1_49A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B6")
    OP_B1("t4210_y")
    Jump("loc_4BF")

    label("loc_4B6")

    OP_B1("t4210_n")

    label("loc_4BF")

    OP_71(0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_4F1")
    OP_22(0x87, 0x1, 0x1E)
    OP_22(0xAE, 0x1, 0x1E)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_77(0xFF, 0xBF, 0xB7, 0x0, 0x0)
    OP_72(0x6, 0x4)

    label("loc_4F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 6)), scpexpr(EXPR_END)), "loc_51B")
    OP_1B(0x1, 0x0, 0x11)
    OP_1B(0x2, 0x0, 0x12)
    OP_1B(0x8, 0x0, 0x12)
    OP_1B(0x3, 0x0, 0x13)
    OP_1B(0x4, 0x0, 0x13)
    OP_1B(0x5, 0x0, 0x13)
    OP_1B(0x6, 0x0, 0x13)

    label("loc_51B")

    Return()

    # Function_1_49A end

    def Function_2_51C(): pass

    label("Function_2_51C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53F")
    OP_8D(0xFE, -1790, 6330, 1580, 2190, 2000)
    Jump("Function_2_51C")

    label("loc_53F")

    Return()

    # Function_2_51C end

    def Function_3_540(): pass

    label("Function_3_540")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5BE")

    ChrTalk(    #0
        0xFE,
        (
            "Never thought I'd see the day where\x01",
            "the duke would behave so well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "The world works in mysterious ways.\x02",
    )

    CloseMessageWindow()
    Jump("loc_77B")

    label("loc_5BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_697")

    ChrTalk(    #2
        0xFE,
        (
            "Apparently, Kanone was captured\x01",
            "during yesterday's events.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "The politicians were overjoyed,\x01",
            "calling it a big roundup, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Huh, isn't there still the captain of\x01",
            "the Special Ops on the loose?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77B")

    label("loc_697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 1)), scpexpr(EXPR_END)), "loc_6BE")

    ChrTalk(    #5
        0xFE,
        "Phew! Busy, busy, busy!\x02",
    )

    CloseMessageWindow()
    Jump("loc_77B")

    label("loc_6BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_77B")

    ChrTalk(    #6
        0xFE,
        "Oh, the maid quarters?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)

    ChrTalk(    #7
        0xFE,
        (
            "Go straight ahead for a while,\x01",
            "and you'll see a big entrance.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 45, 400)

    ChrTalk(    #8
        0xFE,
        (
            "The door to the right of that is the\x01",
            "entrance to the maid quarters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77B")

    TalkEnd(0xFE)
    Return()

    # Function_3_540 end

    def Function_4_77F(): pass

    label("Function_4_77F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_81B")

    ChrTalk(    #9
        0xFE,
        (
            "Captain Schwarz is not currently in\x01",
            "the castle. She is aboard the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "While the captain is away,\x01",
            "we will keep this place safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B7")

    label("loc_81B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_890")

    ChrTalk(    #11
        0xFE,
        "Oww, my wounds still hurt...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "But, I'm glad we could stop that\x01",
            "tank from getting into the city...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B7")

    label("loc_890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_8B7")

    ChrTalk(    #13
        0xFE,
        "Welcome to Grancel Castle!\x02",
    )

    CloseMessageWindow()

    label("loc_8B7")

    TalkEnd(0xFE)
    Return()

    # Function_4_77F end

    def Function_5_8BB(): pass

    label("Function_5_8BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_950")

    ChrTalk(    #14
        0xFE,
        (
            "The other day, Princess Klaudia came\x01",
            "back with a strange look on her face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "She has been speaking much\x01",
            "to the queen of late...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E0")

    label("loc_950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_999")

    ChrTalk(    #16
        0xFE,
        (
            "The Intelligence Division invented\x01",
            "something truly mad...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E0")

    label("loc_999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_9E0")

    ChrTalk(    #17
        0xFE,
        (
            "At the moment, Captain Schwarz of the\x01",
            "Royal Guard is away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E0")

    TalkEnd(0xFE)
    Return()

    # Function_5_8BB end

    def Function_6_9E4(): pass

    label("Function_6_9E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_D59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8C")

    ChrTalk(    #18
        0xFE,
        "#712FEstelle, and Joshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        "#1040FIt's been a while, Hilda.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "#711FYes, welcome back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1011FHilda, is Kloe around?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "#710F...Miss Klaudia is in the audience room\x01",
            "ahead.\x02\x03",

            "However, she is currently speaking about\x01",
            "important matters with the queen, so I am\x01",
            "afraid I must ask you to refrain from entering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1004FAh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "#710FYes, I'm afraid I can't say\x01",
            "when they will be done.\x02\x03",

            "#713FI'm very sorry. I know you went\x01",
            "out of your way to visit, too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1006FNo, don't worry about it.\x02\x03",

            "I just came to see her since I was\x01",
            "in the capital.\x02\x03",

            "#1001FI don't want to get in the way,\x01",
            "so I'll take my leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        "#1040FPardon us.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20DC)
    Jump("loc_D59")

    label("loc_C8C")


    ChrTalk(    #27
        0xFE,
        (
            "#710FMiss Klaudia is in the audience room ahead.\x02\x03",

            "However, she is currently speaking about\x01",
            "important matters with the queen.\x02\x03",

            "I am very sorry, but I am afraid I must\x01",
            "ask you to refrain from entering.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D59")

    TalkEnd(0xFE)
    Return()

    # Function_6_9E4 end

    def Function_7_D5D(): pass

    label("Function_7_D5D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C8(0x200, 0x46, "C_PLAC00._CH", 0x0, 0x7D0)
    OP_DE("Grancel Castle")
    OP_6D(350, 500, -3260, 0)
    OP_67(0, 7380, -10000, 0)
    OP_6B(4350, 0)
    OP_6C(45000, 0)
    OP_6E(513, 0)
    SetChrPos(0x101, 500, 0, -23600, 360)
    SetChrPos(0x105, -500, 0, -23650, 360)
    SetChrPos(0x104, -610, 0, -24600, 360)
    SetChrPos(0x108, 650, 0, -24680, 360)
    Sleep(500)
    FadeToBright(2000, 0)

    def lambda_E23():
        OP_8E(0xFE, 0x258, 0x0, 0xFFFFB884, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E23)
    Sleep(300)

    def lambda_E43():
        OP_8E(0xFE, 0xFFFFFDA8, 0x0, 0xFFFFB884, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E43)

    def lambda_E5E():
        OP_8E(0xFE, 0x258, 0x0, 0xFFFFB370, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_E5E)
    Sleep(300)

    def lambda_E7E():
        OP_8E(0xFE, 0xFFFFFDA8, 0x0, 0xFFFFB370, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E7E)
    WaitChrThread(0x108, 0x1)
    Fade(1000)
    OP_6D(500, 0, -18600, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    TurnDirection(0x101, 0x104, 400)

    def lambda_EE8():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EE8)
    Sleep(50)

    def lambda_EFB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EFB)
    Sleep(50)

    def lambda_F0E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_F0E)
    Sleep(400)

    ChrTalk(    #28
        0x101,
        (
            "#1006FOkay! Time to nose around the castle a bit.\x02\x03",

            "So, obviously we should talk to Queen Alicia,\x01",
            "both to ask about the letter and just say hi,\x01",
            "but...\x02\x03",

            "#1015FLesse... Who else... Julia's gone, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x105,
        (
            "#542FYes, she's currently at Leiston Fortress\x01",
            "overseeing the refitting of the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x108,
        (
            "#073FWell, that's going to make things a bit\x01",
            "harder on us.\x02\x03",

            "She probably could've given us a lot of\x01",
            "help with this mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x104,
        "#030F#5PWho else could we confer with, I wonder?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x105,
        (
            "#040FWith Julia absent, I think our best bet\x01",
            "is Hilda, at least concerning Renne's\x01",
            "parents.\x02\x03",

            "If the Hayworths have ever visited the\x01",
            "castle, she would know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1006FYeah, Hilda kinda seems to have some sort\x01",
            "of 'castle sense' about these things.\x02\x03",

            "So where would we find them, you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x105,
        (
            "#040FGrandmother should be in her\x01",
            "chambers at this hour.\x02\x03",

            "#047FAnd Hilda... Hmm.\x02\x03",

            "#542FIf she isn't in the maids' room,\x01",
            "they can tell us where she is,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1001FGood idea.\x02\x03",

            "#1011FMaids' room and the queen's chambers.\x01",
            "Off we go!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1624)
    OP_28(0x8B, 0x1, 0x200)
    EventEnd(0x0)
    Return()

    # Function_7_D5D end

    def Function_8_131D(): pass

    label("Function_8_131D")

    EventBegin(0x0)
    OP_D2(0x600E8, 0x600ED, 0x7)
    OP_D2(0x2701C8, 0x2701CD, 0x8)
    OP_D2(0x2701C6, 0x2701CB, 0x9)
    OP_D2(0x2701C9, 0x2701CE, 0xA)
    OP_D2(0x260003, 0x260008, 0xB)
    OP_D2(0x7035B, 0x70360, 0xC)
    OP_D2(0x7015A, 0x7015E, 0xD)
    OP_D2(0x6011B, 0x60120, 0xE)
    OP_D2(0x70141, 0x70145, 0xF)
    OP_D2(0x7035C, 0x70361, 0x10)
    OP_D2(0x2601BB, 0x2601C0, 0x11)
    OP_D2(0x2600A0, 0x2600A5, 0x12)
    OP_4A(0xB, 255)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x14, -5310, 0, -18490, 135)
    SetChrPos(0x15, -4080, 0, -17010, 180)
    SetChrPos(0x16, -5390, 0, -16770, 135)
    SetChrPos(0x17, -3760, 0, -15580, 180)
    SetChrPos(0x18, -2220, 0, -15380, 180)
    SetChrPos(0x19, -850, 0, -14430, 180)
    SetChrPos(0x1A, 1210, 0, -14490, 180)
    SetChrPos(0x1B, 2410, 0, -15390, 180)
    SetChrPos(0x1C, 3840, 0, -15090, 225)
    SetChrPos(0x1D, 4030, 0, -16540, 225)
    SetChrPos(0x1E, 5190, 0, -16930, 225)
    SetChrPos(0x1F, 5180, 0, -18310, 225)
    SetChrSubChip(0x14, 1)
    SetChrSubChip(0x15, 1)
    SetChrSubChip(0x16, 1)
    SetChrSubChip(0x17, 1)
    SetChrSubChip(0x18, 1)
    SetChrSubChip(0x19, 1)
    SetChrSubChip(0x1A, 1)
    SetChrSubChip(0x1B, 1)
    SetChrSubChip(0x1C, 1)
    SetChrSubChip(0x1D, 1)
    SetChrSubChip(0x1E, 1)
    SetChrSubChip(0x1F, 1)
    SetChrChipByIndex(0x14, 7)
    SetChrChipByIndex(0x15, 7)
    SetChrChipByIndex(0x16, 7)
    SetChrChipByIndex(0x17, 7)
    SetChrChipByIndex(0x18, 7)
    SetChrChipByIndex(0x19, 7)
    SetChrChipByIndex(0x1A, 7)
    SetChrChipByIndex(0x1B, 7)
    SetChrChipByIndex(0x1C, 7)
    SetChrChipByIndex(0x1D, 7)
    SetChrChipByIndex(0x1E, 7)
    SetChrChipByIndex(0x1F, 7)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0xC, -590, 9000, 10940, 180)
    SetChrPos(0xF, 810, 9000, 10940, 180)
    SetChrPos(0xD, -790, 9000, 12400, 180)
    SetChrPos(0xE, 350, 9000, 12440, 180)
    SetChrPos(0xB, 1460, 9000, 12700, 180)
    SetChrChipByIndex(0xC, 13)
    SetChrChipByIndex(0xF, 16)
    SetChrChipByIndex(0xB, 12)
    SetChrChipByIndex(0xE, 15)
    SetChrChipByIndex(0xD, 14)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_6D(660, 0, -17440, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(312, 0)
    OP_71(0x6, 0x4)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_23(0x87)
    OP_23(0xAE)
    FadeToBright(1000, 0)

    def lambda_1616():
        OP_6D(540, 9000, 12460, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1616)

    def lambda_162E():
        OP_67(0, 7060, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_162E)

    def lambda_1646():
        OP_6B(2670, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1646)

    def lambda_1656():
        OP_6C(31000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1656)
    OP_6E(280, 5000)
    Sleep(500)

    ChrTalk(    #36
        0xB,
        "#712F#6PTo think they'd breach the castle gates...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xC,
        "#226F#5PGrh... They won't hold much longer.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 0, 600)
    Sleep(300)

    ChrTalk(    #38
        0xC,
        (
            "#222F#2PKlaudia! Hilda!\x02\x03",

            "Hurry and get Alicia to her\x01",
            "private chambers!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1735():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1735)
    Sleep(50)

    def lambda_1748():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1748)
    Sleep(50)

    def lambda_175B():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_175B)
    Sleep(50)

    def lambda_176E():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_176E)
    Sleep(500)

    ChrTalk(    #39
        0xD,
        "#409F#6PBut, Uncle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xE,
        "#093F#6PDunan...are you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xC,
        (
            "#226F#2PI... I am a scion of the von Auslese family!\x02\x03",

            "I will not stand quietly and watch as BRIGANDS\x01",
            "try to tear our land and authority to pieces!\x02\x03",

            "With Julia absent, I shall take command!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xD,
        "#403F#6PB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xC,
        (
            "#224F#2PAGH! Stop wasting time!\x02\x03",

            "Their goal is to abduct the queen\x01",
            "and her heir!\x02\x03",

            "Her heir being YOU, remember!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xD,
        "#402F#6PUncle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xC,
        (
            "#224F#2PYour priority must be the safety\x01",
            "of yourself and the queen!\x02\x03",

            "This is what it means to be heir,\x01",
            "Klaudia! Fulfill your duty!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xD,
        "#406F#6PUncle... I understand.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 90, 400)

    def lambda_19D1():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_19D1)

    def lambda_19DF():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_19DF)
    Sleep(300)

    ChrTalk(    #47
        0xD,
        (
            "#402F#6PGrandmother, Hilda! Come, we need\x01",
            "to get up to the chambers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xE,
        (
            "#094F#6PYes...it would be best.\x02\x03",

            "#092FDunan...please, be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xC,
        (
            "#221F#2PHah! You just watch as I cast these\x01",
            "cursed bandits from the walls!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xB,
        (
            "#713F#6P...I pray for your victory.\x02\x03",

            "#714FPhillip, you be careful, too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xB, 400)
    Sleep(300)

    ChrTalk(    #51
        0xF,
        "#720F#6PI will do my best, Mistress Hilda.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 45, 600)

    def lambda_1B63():
        OP_6D(2750, 9000, 17440, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B63)
    OP_43(0xE, 0x0, 0x0, 0x9)
    Sleep(200)
    OP_8C(0xD, 45, 600)
    OP_43(0xD, 0x0, 0x0, 0xA)
    Sleep(300)
    OP_8C(0xB, 45, 600)
    OP_43(0xB, 0x0, 0x0, 0xB)

    def lambda_1BA8():

        label("loc_1BA8")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_1BA8")

    QueueWorkItem2(0xF, 1, lambda_1BA8)

    def lambda_1BB9():

        label("loc_1BB9")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_1BB9")

    QueueWorkItem2(0xC, 1, lambda_1BB9)
    WaitChrThread(0x101, 0x1)
    Sleep(1500)
    OP_44(0xF, 0x1)
    OP_44(0xC, 0x1)

    def lambda_1BDC():
        OP_6D(430, 9000, 11240, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BDC)
    OP_6B(2550, 1500)
    TurnDirection(0xF, 0xC, 400)
    Sleep(300)

    ChrTalk(    #52
        0xF,
        (
            "#720F#4PI am...deeply impressed, Your Lordship.\x02\x03",

            "I have never been happier to\x01",
            "serve you than at this moment.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xF, 400)
    Sleep(300)

    ChrTalk(    #53
        0xC,
        (
            "#222F#6PH-Hmph! There's no need to make\x01",
            "such a show out of it, Phillip.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x88, 0x0, 0x50)
    OP_7C(0x0, 0x64, 0xBB8, 0x1F4)
    OP_72(0x6, 0x4)
    Sleep(500)
    OP_77(0xFF, 0xBF, 0xB7, 0x0, 0x1388)
    OP_22(0x87, 0x1, 0xA)
    OP_22(0xAE, 0x1, 0xA)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_22(0x13C, 0x0, 0x50)
    Sleep(1000)
    OP_22(0xF6, 0x0, 0x50)
    OP_24(0x87, 0x14)
    OP_24(0xAE, 0x14)

    def lambda_1D56():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1D56)
    Sleep(50)

    def lambda_1D69():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1D69)
    Sleep(2000)
    SetChrChipByIndex(0x10, 8)
    SetChrChipByIndex(0x11, 9)
    SetChrChipByIndex(0x12, 10)
    SetChrChipByIndex(0x13, 11)
    SetChrPos(0x12, -100, 0, -32200, 0)
    SetChrPos(0x11, -160, 0, -34300, 0)
    SetChrPos(0x13, -1250, 0, -32860, 0)
    SetChrPos(0x10, 1220, 0, -33660, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Fade(1000)
    OP_6D(410, 0, -21270, 0)
    OP_67(0, 5250, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(148000, 0)
    OP_6E(331, 0)
    OP_24(0x87, 0x1E)
    OP_24(0xAE, 0x1E)

    def lambda_1E32():
        OP_8E(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFACF4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1E32)
    Sleep(120)

    def lambda_1E52():
        OP_8E(0xFE, 0xFFFFFB1E, 0x0, 0xFFFFA6B4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1E52)
    Sleep(180)

    def lambda_1E72():
        OP_8E(0xFE, 0x4C4, 0x0, 0xFFFFA844, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1E72)
    Sleep(100)

    def lambda_1E92():
        OP_8E(0xFE, 0xFFFFFF60, 0x0, 0xFFFFA3BC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1E92)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 18)
    SetChrSubChip(0x11, 0)
    Fade(500)
    OP_6D(130, 9000, 11060, 0)
    OP_67(0, 7350, -10000, 0)
    OP_6B(2610, 0)
    OP_6C(31000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #54
        0xC,
        "#226F#6PAh! Here they are!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xF,
        (
            "#720F#6PMmm. Such ghastly appearances.\x01",
            "Rather more like demons than men.\x02\x03",

            "Your Lordship...should I fall,\x01",
            "do not hesitate to flee.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1FAB():

        label("loc_1FAB")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_1FAB")

    QueueWorkItem2(0xC, 1, lambda_1FAB)

    ChrTalk(    #56
        0xC,
        "#223F#6PWhat? But...\x02",
    )

    CloseMessageWindow()
    OP_8F(0xF, 0x410, 0x2328, 0x3516, 0x7D0, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0xF, 0x2)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0xF, 0x20)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xF, 17)
    OP_0D()
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_201C():
        OP_99(0xFE, 0x1, 0x8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_201C)
    OP_8F(0xF, 0x410, 0x2328, 0x2C88, 0x1B58, 0x0)
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    SetChrSubChip(0xF, 10)

    def lambda_2055():
        OP_6D(980, 1000, 3340, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2055)

    def lambda_206D():
        OP_67(0, 5250, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_206D)

    def lambda_2085():
        OP_6B(2560, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2085)

    def lambda_2095():
        OP_6C(33000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2095)

    def lambda_20A5():
        OP_6E(331, 1000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_20A5)
    OP_22(0x23B, 0x0, 0x64)
    OP_96(0xF, 0xD2, 0x3E8, 0xB04, 0x3E8, 0xFA0)
    OP_22(0xA4, 0x0, 0x64)
    OP_99(0xF, 0xB, 0xF, 0x5DC)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    def lambda_20ED():
        OP_6D(1040, 0, -17600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_20ED)

    def lambda_2105():
        OP_67(0, 4560, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2105)

    def lambda_211D():
        OP_6B(2590, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_211D)

    def lambda_212D():
        OP_6E(390, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_212D)

    def lambda_213D():

        label("loc_213D")

        OP_99(0xFE, 0x1, 0x8, 0x9C4)
        OP_48()
        Jump("loc_213D")

    QueueWorkItem2(0xF, 2, lambda_213D)
    OP_8F(0xF, 0xBE, 0x0, 0xFFFFC1EE, 0x1F40, 0x0)
    OP_44(0xF, 0x2)
    SetChrSubChip(0xF, 0)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrFlags(0x1A, 0x20)
    SetChrFlags(0x1B, 0x20)

    def lambda_229F():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_229F)
    Sleep(100)

    def lambda_22B2():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_22B2)
    WaitChrThread(0x1A, 0x1)

    ChrTalk(    #57
        0x1A,
        "#4PSir Phillip!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x13,
        "#264F#2POhhh, it's the old man with the closed eyes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x11,
        "#254F#2PWho the hell is this old lump?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xF,
        (
            "#720F#6PI am Phillip Runall. Butler to His Royal\x01",
            "Highness Dunan von Auslese...and\x01",
            "former captain of the Royal Guard.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x1F5, 0x0, 0x64)
    OP_99(0xF, 0x10, 0x17, 0x4B0)
    Sleep(500)

    ChrTalk(    #61
        0xF,
        (
            "#721F#6PThis blade I once held in days long past...\x02\x03",

            "I do not know how far it will carry me,\x01",
            "but it shall now cross with yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x11,
        "#252F#2POoooh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x12,
        "#231F#2PAh! Ever is this country full of surprises!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10,
        (
            "#241F#2PHeehee...\x01",
            "Let's see how skilled you are, then.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x203C)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4200   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_8_131D end

    def Function_9_24F0(): pass

    label("Function_9_24F0")

    OP_8E(0xFE, 0x143C, 0x2328, 0x6266, 0xFA0, 0x0)
    OP_8E(0xFE, 0x343A, 0x2328, 0x69C8, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_9_24F0 end

    def Function_10_251E(): pass

    label("Function_10_251E")

    OP_8E(0xFE, 0x143C, 0x2328, 0x6266, 0xFA0, 0x0)
    OP_8E(0xFE, 0x343A, 0x2328, 0x69C8, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_10_251E end

    def Function_11_254C(): pass

    label("Function_11_254C")

    OP_8E(0xFE, 0x1360, 0x2328, 0x5CC6, 0xFA0, 0x0)
    OP_8E(0xFE, 0x343A, 0x2328, 0x69C8, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_11_254C end

    def Function_12_257A(): pass

    label("Function_12_257A")

    SetChrPos(0x14, 4280, 0, -19910, 45)
    SetChrPos(0x15, 5060, 0, -18690, 315)
    SetChrPos(0x16, 3940, 0, -17900, 225)
    SetChrPos(0x17, 3150, 0, -16390, 315)
    SetChrPos(0x18, 5220, 0, -14920, 180)
    SetChrPos(0x19, 3700, 0, -13350, 135)
    SetChrPos(0x1A, -3770, 0, -14210, 45)
    SetChrPos(0x1B, -5950, 0, -16070, 315)
    SetChrPos(0x1C, -4320, 0, -21290, 225)
    SetChrPos(0x1D, -5730, 0, -18970, 180)
    SetChrPos(0x1E, -3430, 0, -18480, 90)
    SetChrPos(0x1F, -4480, 0, -17140, 45)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x14, 0x1)
    ClearChrFlags(0x15, 0x1)
    ClearChrFlags(0x16, 0x1)
    ClearChrFlags(0x17, 0x1)
    ClearChrFlags(0x18, 0x1)
    ClearChrFlags(0x19, 0x1)
    ClearChrFlags(0x1A, 0x1)
    ClearChrFlags(0x1B, 0x1)
    ClearChrFlags(0x1C, 0x1)
    ClearChrFlags(0x1D, 0x1)
    ClearChrFlags(0x1E, 0x1)
    ClearChrFlags(0x1F, 0x1)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x15, 0x20)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x17, 0x20)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x19, 0x20)
    SetChrFlags(0x1A, 0x20)
    SetChrFlags(0x1B, 0x20)
    SetChrFlags(0x1C, 0x20)
    SetChrFlags(0x1D, 0x20)
    SetChrFlags(0x1E, 0x20)
    SetChrFlags(0x1F, 0x20)
    SetChrPos(0xF, -1100, 0, -7300, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x2)
    ClearChrFlags(0xF, 0x1)
    SetChrChipByIndex(0xF, 6)
    SetChrSubChip(0xF, 5)
    SetChrPos(0xC, 940, 0, -6690, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x1)
    SetChrFlags(0xC, 0x20)
    Return()

    # Function_12_257A end

    def Function_13_2745(): pass

    label("Function_13_2745")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2766")
    Call(0, 15)
    Call(0, 16)

    label("loc_2766")

    SetChrPos(0x101, -380, 0, -33500, 0)
    SetChrPos(0x102, 480, 0, -33500, 0)
    SetChrPos(0xF8, -1190, 0, -34000, 0)
    SetChrPos(0xF9, 1290, 0, -34000, 0)
    SetChrPos(0xF, -750, 0, -6900, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 1)
    SetChrSubChip(0xF, 7)
    SetChrFlags(0xF, 0x1)
    OP_6D(400, 0, -28320, 0)
    OP_67(0, 7130, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_72(0x6, 0x4)

    def lambda_281C():
        OP_8E(0xFE, 0xFFFFFE84, 0x0, 0xFFFFAB3C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_281C)
    Sleep(80)

    def lambda_283C():
        OP_8E(0xFE, 0x370, 0x0, 0xFFFFAACE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_283C)
    Sleep(80)

    def lambda_285C():
        OP_8E(0xFE, 0xFFFFFC72, 0x0, 0xFFFFA560, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_285C)
    Sleep(80)

    def lambda_287C():
        OP_8E(0xFE, 0x384, 0x0, 0xFFFFA54C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_287C)
    FadeToBright(1000, 0)

    def lambda_28A0():
        OP_6D(810, 0, -20120, 2200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_28A0)

    def lambda_28B8():
        OP_6E(293, 2200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_28B8)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_292B")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2969")

    label("loc_292B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2952")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2969")

    label("loc_2952")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2969")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2995")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_29D3")

    label("loc_2995")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29BC")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_29D3")

    label("loc_29BC")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_29D3")

    Sleep(1000)

    ChrTalk(    #65
        0x101,
        "#1020F#5PNo, no...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A21")

    ChrTalk(    #66
        0x107,
        "#065FThey got...everybody...!\x02",
    )

    CloseMessageWindow()

    label("loc_2A21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A6D")

    ChrTalk(    #67
        0x106,
        (
            "#057F#2PNot even the Royal Guard\x01",
            "can stop 'em, huh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF9")

    label("loc_2A6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AAF")

    ChrTalk(    #68
        0x103,
        "#022F#2PEven the Royal Guard is no match...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AF9")

    label("loc_2AAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AF9")

    ChrTalk(    #69
        0x108,
        (
            "#072F#2PNot even the Royal Guard\x01",
            "can hold them back...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AF9")


    NpcTalk(    #70
        0xF,
        "Man's Voice",
        "#4PM-Miss...Estelle...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B7B")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2BB9")

    label("loc_2B7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BA2")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2BB9")

    label("loc_2BA2")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2BB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BE0")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2C1E")

    label("loc_2BE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C07")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2C1E")

    label("loc_2C07")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2C1E")

    Sleep(1000)

    def lambda_2C29():
        OP_6B(2830, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C29)
    OP_6D(280, 0, -6850, 2000)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1B, 0x40)

    def lambda_2C5E():
        OP_6D(640, 0, -7360, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C5E)

    def lambda_2C76():
        OP_67(0, 6310, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2C76)

    def lambda_2C8E():
        OP_8E(0xFE, 0xFFFFFD80, 0x0, 0xFFFFDE40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C8E)
    Sleep(80)

    def lambda_2CAE():
        OP_8E(0xFE, 0x1F4, 0x0, 0xFFFFDE2C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2CAE)
    Sleep(80)

    def lambda_2CCE():
        OP_8E(0xFE, 0xFFFFFBE6, 0x0, 0xFFFFD800, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2CCE)
    Sleep(80)

    def lambda_2CEE():
        OP_8E(0xFE, 0x190, 0x0, 0xFFFFD800, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2CEE)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 0, 400)
    WaitChrThread(0xF8, 0x1)
    OP_8C(0xF8, 0, 400)
    WaitChrThread(0xF9, 0x1)
    OP_8C(0xF9, 0, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #71
        0x101,
        "#1020F#2PPh-Phillip! And even Dunan...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x102,
        "#1042FDid you try to stop them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xF,
        (
            "#722F#6PTo my shame, I could not...\x02\x03",

            "I suppose age has...caught up to\x01",
            "me. I could not hold them for long...\x02\x03",

            "#721FIs...the duke...?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E5F")

    ChrTalk(    #74
        0x108,
        (
            "#070F#2PHe's fine. I believe he was\x01",
            "just knocked down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F0D")

    label("loc_2E5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EBB")

    ChrTalk(    #75
        0x103,
        (
            "#524F#2PDon't worry... I think he was just\x01",
            "knocked away or something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F0D")

    label("loc_2EBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F0D")

    ChrTalk(    #76
        0x106,
        (
            "#051F#2PAh, he's fine. Just got tackled\x01",
            "or something, I think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F0D")


    ChrTalk(    #77
        0xF,
        (
            "#722F#6PThat is...a relief...\x02\x03",

            "Her Majesty has...retreated to the\x01",
            "royal chambers... Please...hurry...!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    OP_22(0x20C, 0x0, 0x64)
    ClearChrFlags(0xF, 0x1)
    SetChrChipByIndex(0xF, 6)
    SetChrSubChip(0xF, 5)
    SetChrPos(0xF, -1100, 0, -7300, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #78
        0x101,
        "#1020F#2PPHILLIP!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x102,
        "#1035FHe's just unconscious.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(300)

    ChrTalk(    #80
        0x102,
        "#1042F#4PLet's hurry... Kloe is in danger!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 500)

    ChrTalk(    #81
        0x101,
        "#1002F#1PR-Right!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_2745 end

    def Function_14_3059(): pass

    label("Function_14_3059")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrPos(0x0, 50, 0, -8940, 0)
    SetChrPos(0x1, 50, 0, -8940, 0)
    SetChrPos(0x2, 50, 0, -8940, 0)
    SetChrPos(0x3, 50, 0, -8940, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x203E)
    Sleep(200)
    FadeToBright(1000, 0)
    OP_1B(0x1, 0x0, 0x11)
    OP_1B(0x2, 0x0, 0x12)
    OP_1B(0x8, 0x0, 0x12)
    OP_1B(0x3, 0x0, 0x13)
    OP_1B(0x4, 0x0, 0x13)
    OP_1B(0x5, 0x0, 0x13)
    OP_1B(0x6, 0x0, 0x13)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_14_3059 end

    def Function_15_30EC(): pass

    label("Function_15_30EC")

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
        (0, "loc_3165"),
        (1, "loc_316B"),
        (SWITCH_DEFAULT, "loc_3171"),
    )


    label("loc_3165")

    OP_A2(0x1200)
    Jump("loc_3171")

    label("loc_316B")

    OP_A2(0x1201)
    Jump("loc_3171")

    label("loc_3171")

    Return()

    # Function_15_30EC end

    def Function_16_3172(): pass

    label("Function_16_3172")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_16_3172 end

    def Function_17_31CB(): pass

    label("Function_17_31CB")

    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_31ED"),
        (1, "loc_3233"),
        (2, "loc_3274"),
        (5, "loc_32C0"),
        (7, "loc_32FE"),
        (6, "loc_3346"),
        (SWITCH_DEFAULT, "loc_338F"),
    )


    label("loc_31ED")


    ChrTalk(    #82
        0x101,
        (
            "#1002FNo, not this way. We need to hurry\x01",
            "to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_338F")

    label("loc_3233")


    ChrTalk(    #83
        0x102,
        (
            "#1042FNo, not this way. Let's hurry\x01",
            "to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_338F")

    label("loc_3274")


    ChrTalk(    #84
        0x103,
        (
            "#022FWe have no business this way.\x01",
            "Let's hurry to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_338F")

    label("loc_32C0")


    ChrTalk(    #85
        0x106,
        (
            "#057FCan't waste time.\x01",
            "Let's get to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_338F")

    label("loc_32FE")


    ChrTalk(    #86
        0x108,
        (
            "#072FNo time for side trips.\x01",
            "We must hurry to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_338F")

    label("loc_3346")


    ChrTalk(    #87
        0x107,
        (
            "#062FUm, um, not this way. We need to hurry\x01",
            "to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_338F")

    label("loc_338F")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_17_31CB end

    def Function_18_33B0(): pass

    label("Function_18_33B0")

    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_33D2"),
        (1, "loc_3418"),
        (2, "loc_3459"),
        (5, "loc_34A5"),
        (7, "loc_34E3"),
        (6, "loc_352B"),
        (SWITCH_DEFAULT, "loc_3574"),
    )


    label("loc_33D2")


    ChrTalk(    #88
        0x101,
        (
            "#1002FNo, not this way. We need to hurry\x01",
            "to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3574")

    label("loc_3418")


    ChrTalk(    #89
        0x102,
        (
            "#1042FNo, not this way. Let's hurry\x01",
            "to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3574")

    label("loc_3459")


    ChrTalk(    #90
        0x103,
        (
            "#022FWe have no business this way.\x01",
            "Let's hurry to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3574")

    label("loc_34A5")


    ChrTalk(    #91
        0x106,
        (
            "#057FCan't waste time.\x01",
            "Let's get to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3574")

    label("loc_34E3")


    ChrTalk(    #92
        0x108,
        (
            "#072FNo time for side trips.\x01",
            "We must hurry to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3574")

    label("loc_352B")


    ChrTalk(    #93
        0x107,
        (
            "#062FUm, um, not this way. We need to hurry\x01",
            "to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3574")

    label("loc_3574")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_18_33B0 end

    def Function_19_3595(): pass

    label("Function_19_3595")

    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_35B7"),
        (1, "loc_35FD"),
        (2, "loc_363E"),
        (5, "loc_368A"),
        (7, "loc_36C8"),
        (6, "loc_3710"),
        (SWITCH_DEFAULT, "loc_3759"),
    )


    label("loc_35B7")


    ChrTalk(    #94
        0x101,
        (
            "#1002FNo, not this way. We need to hurry\x01",
            "to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3759")

    label("loc_35FD")


    ChrTalk(    #95
        0x102,
        (
            "#1042FNo, not this way. Let's hurry\x01",
            "to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3759")

    label("loc_363E")


    ChrTalk(    #96
        0x103,
        (
            "#022FWe have no business this way.\x01",
            "Let's hurry to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3759")

    label("loc_368A")


    ChrTalk(    #97
        0x106,
        (
            "#057FCan't waste time.\x01",
            "Let's get to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3759")

    label("loc_36C8")


    ChrTalk(    #98
        0x108,
        (
            "#072FNo time for side trips.\x01",
            "We must hurry to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3759")

    label("loc_3710")


    ChrTalk(    #99
        0x107,
        (
            "#062FUm, um, not this way. We need to hurry\x01",
            "to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3759")

    label("loc_3759")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_19_3595 end

    def Function_20_377A(): pass

    label("Function_20_377A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B4D")
    EventBegin(0x1)
    TurnDirection(0xB, 0x0, 400)
    TurnDirection(0x0, 0xB, 0)
    TurnDirection(0x1, 0xB, 0)
    TurnDirection(0x2, 0xB, 0)
    TurnDirection(0x3, 0xB, 0)
    OP_4A(0xB, 255)
    SetChrFlags(0xB, 0x40)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A52")

    ChrTalk(    #100
        0xB,
        "#712FEstelle, and Joshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x102,
        "#1040FIt's been a while, Hilda.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xB,
        "#711FYes, welcome back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#1011FHilda, is Kloe around?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xB,
        (
            "#710F...Miss Klaudia is in the audience room ahead.\x02\x03",

            "However, she is currently speaking about important\x01",
            "matters with the queen, so I am afraid I must ask\x01",
            "you to refrain from entering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#1004FAh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xB,
        (
            "#710FYes, I'm afraid I can't say\x01",
            "when they will be done.\x02\x03",

            "#713FI'm very sorry. I know you went\x01",
            "out of your way to visit, too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#1006FNo, don't worry about it.\x02\x03",

            "I just came to see her since I was\x01",
            "in the capital.\x02\x03",

            "#1001FI don't want to get in the way,\x01",
            "so I'll take my leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x102,
        "#1040FPardon us.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20DC)
    Jump("loc_3B1F")

    label("loc_3A52")


    ChrTalk(    #109
        0xB,
        (
            "#710FMiss Klaudia is in the audience room ahead.\x02\x03",

            "However, she is currently speaking about\x01",
            "important matters with the queen.\x02\x03",

            "I am very sorry, but I am afraid I must\x01",
            "ask you to refrain from entering.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B1F")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8C(0xB, 180, 400)
    Sleep(50)
    EventEnd(0x4)
    OP_4B(0xB, 255)
    ClearChrFlags(0xB, 0x40)
    Jump("loc_3B4D")

    label("loc_3B4D")

    Return()

    # Function_20_377A end

    SaveToFile()

Try(main)
