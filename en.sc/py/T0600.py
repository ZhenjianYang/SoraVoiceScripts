from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0600   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0600.x',
        MapIndex            = 17,
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Private Ethan',                        # 9
        'Private Logan',                        # 10
        'Private Thomas',                       # 11
        'Warrant Officer Graves',               # 12
        'Private Stoll',                        # 13
        'Private Barranco',                     # 14
        'Fog',                                  # 15
        'Elize Highway',                        # 16
        'Royal Avenue',                         # 17
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
    )

    DeclNpc(
        X                   = -10690,
        Z                   = 0,
        Y                   = -3640,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -10660,
        Z                   = 0,
        Y                   = 3600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -21590,
        Z                   = 11750,
        Y                   = 150,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -7840,
        Z                   = 0,
        Y                   = -4840,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -35300,
        Z                   = 0,
        Y                   = 3650,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -35300,
        Z                   = 0,
        Y                   = -3560,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x189,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 37180,
        Z                   = 0,
        Y                   = -1450,
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

    DeclNpc(
        X                   = -83430,
        Z                   = 0,
        Y                   = -1170,
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
        X                   = -75400,
        Y                   = -2000,
        Z                   = -8100,
        Range               = -74400,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x1FA4,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )


    ScpFunction(
        "Function_0_1FA",          # 00, 0
        "Function_1_249",          # 01, 1
        "Function_2_457",          # 02, 2
        "Function_3_5D4",          # 03, 3
        "Function_4_5F8",          # 04, 4
        "Function_5_68E",          # 05, 5
        "Function_6_D4D",          # 06, 6
        "Function_7_152B",         # 07, 7
        "Function_8_2117",         # 08, 8
        "Function_9_2357",         # 09, 9
        "Function_10_29AD",        # 0A, 10
        "Function_11_2FEC",        # 0B, 11
        "Function_12_3158",        # 0C, 12
        "Function_13_31DC",        # 0D, 13
    )


    def Function_0_1FA(): pass

    label("Function_0_1FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_213")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_224")

    label("loc_213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_224")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    label("loc_224")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (107, "loc_230"),
        (SWITCH_DEFAULT, "loc_248"),
    )


    label("loc_230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_245")
    SetMapFlags(0x10000000)
    Event(0, 11)

    label("loc_245")

    Jump("loc_248")

    label("loc_248")

    Return()

    # Function_0_1FA end

    def Function_1_249(): pass

    label("Function_1_249")

    OP_16(0x2, 0xFA0, 0xFFFDB610, 0xFFFE0430, 0x230006)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_273")
    OP_B1("t0600_y")
    Jump("loc_285")

    label("loc_273")

    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_B1("t0600_n")

    label("loc_285")

    OP_1C(0x2, 0x0, 0xD)
    OP_1C(0x3, 0x0, 0xD)
    OP_1C(0x4, 0x0, 0xD)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_40E")
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)
    OP_43(0xE, 0x0, 0x0, 0x4)

    label("loc_40E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43E")
    OP_6F(0x2, 100)
    OP_72(0x2, 0x10)
    OP_6F(0x3, 100)
    OP_72(0x3, 0x10)
    OP_6F(0x4, 100)
    OP_72(0x4, 0x10)

    label("loc_43E")

    OP_6F(0x0, 160)
    OP_6F(0x1, 160)
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    Return()

    # Function_1_249 end

    def Function_2_457(): pass

    label("Function_2_457")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47C")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5BE")

    label("loc_47C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_495")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_5BE")

    label("loc_495")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AE")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_5BE")

    label("loc_4AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C7")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_5BE")

    label("loc_4C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E0")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_5BE")

    label("loc_4E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F9")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_5BE")

    label("loc_4F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_512")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_5BE")

    label("loc_512")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52B")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_5BE")

    label("loc_52B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_544")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_5BE")

    label("loc_544")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55D")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_5BE")

    label("loc_55D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_576")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_5BE")

    label("loc_576")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58F")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_5BE")

    label("loc_58F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A8")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_5BE")

    label("loc_5A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BE")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_5BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D3")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5BE")

    label("loc_5D3")

    Return()

    # Function_2_457 end

    def Function_3_5D4(): pass

    label("Function_3_5D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F7")
    OP_8D(0xFE, -28070, -8920, -16500, 6400, 3000)
    Jump("Function_3_5D4")

    label("loc_5F7")

    Return()

    # Function_3_5D4 end

    def Function_4_5F8(): pass

    label("Function_4_5F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_68D")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x5DC0), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x37), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_62B")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_640")

    label("loc_62B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x37), scpexpr(EXPR_PUSH_LONG, 0x7D00), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_640")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x7D00), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_640")

    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x5DC0), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_IMUL), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x38), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_670")
    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_685")

    label("loc_670")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x38), scpexpr(EXPR_PUSH_LONG, 0x222E0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_685")
    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x222E0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_685")

    Sleep(10)
    Jump("Function_4_5F8")

    label("loc_68D")

    Return()

    # Function_4_5F8 end

    def Function_5_68E(): pass

    label("Function_5_68E")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_717")

    ChrTalk(    #0
        0xFE,
        (
            "Apparently the gate function's still\x01",
            "not fixed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Man, I don't want to spend the night with\x01",
            "it wide open like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_822")

    ChrTalk(    #2
        0xFE,
        "Right now this guard post is in a bit of a fix.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "The weapons are a problem for one thing,\x01",
            "but I'm really worried about supplies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "If both freight vehicles and airships are out\x01",
            "of commission, then getting food supplies\x01",
            "is going to be difficult.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_8F2")

    ChrTalk(    #5
        0xFE,
        (
            "The non-aggression pact signing ceremony\x01",
            "ended without incident, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "As a soldier of a guard post protecting the\x01",
            "capital, it feels like a weight off my shoulders,\x01",
            "let me tell you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_8F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_END)), "loc_9DE")

    ChrTalk(    #7
        0xFE,
        (
            "The bracer who went through here yesterday\x01",
            "came back a bit ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "Guy looked like he'd been through the wringer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Well, guess it makes sense to be beat after\x01",
            "traveling to the capital and then turning\x01",
            "right around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_9DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_B74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AA0")

    ChrTalk(    #10
        0xFE,
        (
            "This morning I saw a really weird-looking\x01",
            "priest. At least I think he was a priest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "The guy was packing, so I guess modern priests\x01",
            "carry weapons to defend themselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B71")

    label("loc_AA0")


    ChrTalk(    #12
        0xFE,
        (
            "This morning I saw a really weird-looking\x01",
            "priest. At least I think he was a priest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "He had a crossbow on his back of all things...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            " I guess modern priests carry weapons to\x01",
            "defend themselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B71")

    Jump("loc_D49")

    label("loc_B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_C33")

    ChrTalk(    #15
        0xFE,
        (
            "The bracer that came by the guard post\x01",
            "yesterday was off again early this morning\x01",
            "for the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Thanks to the night's rest, the travelers\x01",
            "seemed in a much better mood.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_D49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 1)), scpexpr(EXPR_END)), "loc_CB1")

    ChrTalk(    #17
        0xFE,
        (
            "Just a bit ago, some travelers escorted\x01",
            "by a bracer arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "Is the fog in Rolent really that bad?\x02",
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_CB1")


    ChrTalk(    #19
        0xFE,
        (
            "Tomorrow is the signing ceremony at\x01",
            "the royal villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Because of that, the customs procedures will\x01",
            "be stricter on all traffic passing through.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D49")

    TalkEnd(0x8)
    Return()

    # Function_5_68E end

    def Function_6_D4D(): pass

    label("Function_6_D4D")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_F49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAF")

    ChrTalk(    #21
        0xFE,
        (
            "It's a real blow to the Royal Army to have\x01",
            "our airships grounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "After all, they're our country's ace in the\x01",
            "hole when it comes to defense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "The Empire has an air force too, but their\x01",
            "main strength is their ground troops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Even if they're affected by this Orbal Shutdown\x01",
            "mess, it won't be as bad as we have it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_F46")

    label("loc_EAF")


    ChrTalk(    #25
        0xFE,
        (
            "It's a real blow to the Royal Army to have\x01",
            "our airships grounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "After all, they're our country's ace in the\x01",
            "hole when it comes to defense.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F46")

    Jump("loc_1527")

    label("loc_F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1005")

    ChrTalk(    #27
        0xFE,
        (
            "On top of the gate not closing,\x01",
            "our orbal guns don't work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "This is about the worst situation possible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "All we can do is pray it passes without\x01",
            "anything happening.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1527")

    label("loc_1005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_10A7")

    ChrTalk(    #30
        0xFE,
        "The fog's finally cleared, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Apparently the signing ceremony went well,\x01",
            "so this morning feels amazingly stress free\x01",
            "compared to yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1527")

    label("loc_10A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1201")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1150")

    ChrTalk(    #32
        0xFE,
        (
            "Apparently the Verte Bridge defense force\x01",
            "was dispatched to Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "You might think it's only a bit of fog,\x01",
            "but the power of nature is scary.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11FE")

    label("loc_1150")


    ChrTalk(    #34
        0xFE,
        (
            "Apparently the Verte Bridge defense force\x01",
            "was dispatched to Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "To think this'd happen over just some fog.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "The power of nature, man, it's pretty scary.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_11FE")

    Jump("loc_1527")

    label("loc_1201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1335")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_126E")

    ChrTalk(    #37
        0xFE,
        (
            "Finally, the non-aggression pact signing\x01",
            "is today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "At long last, it feels like.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1332")

    label("loc_126E")


    ChrTalk(    #39
        0xFE,
        (
            "Finally, the non-aggression pact signing\x01",
            "is today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "It'll be a day to remember. It's a new start\x01",
            "for the kingdom, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "All right! I'd better put myself into\x01",
            "my tasks too!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1332")

    Jump("loc_1527")

    label("loc_1335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1527")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_13F1")

    ChrTalk(    #42
        0xFE,
        (
            "All the important people are gathering\x01",
            "in the capital, of course, but so are the\x01",
            "media types.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Us soldiers are just hoping the whole thing\x01",
            "ends without incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1527")

    label("loc_13F1")


    ChrTalk(    #44
        0xFE,
        "Tomorrow's the pact signing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "All the important people are gathering\x01",
            "in the capital, of course, but so are the\x01",
            "media types.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "After all, it's a non-aggression pact signed\x01",
            "with the very country that invaded us just\x01",
            "ten years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "It'd be weirder if it didn't attract attention,\x01",
            "if anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1527")

    TalkEnd(0x9)
    Return()

    # Function_6_D4D end

    def Function_7_152B(): pass

    label("Function_7_152B")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_161A")

    ChrTalk(    #48
        0xFE,
        (
            "Apparently, right now the Haken Gate's\x01",
            "on high alert...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "I wonder how the Empire will react to\x01",
            "these events.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "We just signed a non-aggression pact with them,\x01",
            "so I doubt they'll do anything too crazy,\x01",
            "but still...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2113")

    label("loc_161A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1817")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176D")

    ChrTalk(    #51
        0xFE,
        (
            "You can see the floating island very clearly\x01",
            "from these walls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Even if you try not to think about it,\x01",
            "it's always in the corner of your vision,\x01",
            "just hovering there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "And before you realize what you're doing,\x01",
            "you're staring at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Hmm, I'm supposed to be on guard,\x01",
            "so it's bad to be so distracted.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1814")

    label("loc_176D")


    ChrTalk(    #55
        0xFE,
        (
            "Still, that island...\x01",
            "I really wish I knew what it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "It's nice enough to look at, but it makes me\x01",
            "feel more and more uncomfortable the longer\x01",
            "it's there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1814")

    Jump("loc_2113")

    label("loc_1817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1971")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_18BC")

    ChrTalk(    #57
        0xFE,
        "Things here have finally gotten back to normal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "I'd appreciate being spared more governmental\x01",
            "ceremonies or abnormal weather for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_196E")

    label("loc_18BC")


    ChrTalk(    #59
        0xFE,
        "Things here have finally gotten back to normal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "I'd appreciate being spared more governmental\x01",
            "ceremonies or abnormal weather for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "*sigh* Man, I'm beat.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_196E")

    Jump("loc_2113")

    label("loc_1971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1B2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A2F")

    ChrTalk(    #62
        0xFE,
        (
            "Lately Emily from the dining hall's been\x01",
            "obsessed with Eastern cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "When it's good it's good, but when\x01",
            "she messes up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "Seems today should be a good day.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B2C")

    label("loc_1A2F")


    ChrTalk(    #65
        0xFE,
        (
            "Just about time to change shifts...\x01",
            "I wonder what's for lunch today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Lately Emily from the dining hall's been\x01",
            "obsessed with Eastern cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "When it's good it's good, but when\x01",
            "she messes up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "*g-gulp* I wonder which today'll be.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1B2C")

    Jump("loc_2113")

    label("loc_1B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1C5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1BAF")

    ChrTalk(    #69
        0xFE,
        (
            "The signing ceremony's over, but now we\x01",
            "have a fog problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "*sigh* We just can't catch a break here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C5A")

    label("loc_1BAF")


    ChrTalk(    #71
        0xFE,
        (
            "The high alert status for the signing ceremony\x01",
            "ends today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "Or so I thought, but now we've got\x01",
            "this crazy fog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "*sigh* We just can't catch a break here.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1C5A")

    Jump("loc_2113")

    label("loc_1C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1CDC")

    ChrTalk(    #74
        0xFE,
        (
            "The Rolent side's hard to check\x01",
            "with this fog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "I have to be extra careful to make sure no\x01",
            "monsters get in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2113")

    label("loc_1CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1D4B")

    ChrTalk(    #76
        0xFE,
        (
            "Apparently damage to the capital was kept\x01",
            "to a minimum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "That's Julia and the gang for you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2113")

    label("loc_1D4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_1DE0")

    ChrTalk(    #78
        0xFE,
        "I-I was watching from here, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "Were you the ones who fought that\x01",
            "weird flying object?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "Wh-What the heck was that thing?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2113")

    label("loc_1DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_1F17")

    ChrTalk(    #81
        0xFE,
        (
            "...A black-haired boy?\x01",
            "No, no one like that here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "If there was anyone, he'd have to be on\x01",
            "the southern side of the wall, I'd guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "That's where most of the tourists are guided to.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "To get to the south side, go down the stairs and\x01",
            "head to the south door. That should get you there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2113")

    label("loc_1F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_1FB1")

    ChrTalk(    #85
        0xFE,
        (
            "Even with the signing ceremony coming up\x01",
            "our job's basically the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "Protect the Gurune Gate with everything we have...\x01",
            "That's all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2113")

    label("loc_1FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_20C6")

    ChrTalk(    #87
        0xFE,
        (
            "After the end of the coup d'etat, there's been a\x01",
            "reorganization of the military, so the brass\x01",
            "have been pretty busy, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "This is a fortress protecting the capital so\x01",
            "we've got a lot of veterans here, and that's\x01",
            "probably why not much has changed here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2113")

    label("loc_20C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2113")

    ChrTalk(    #89
        0xFE,
        "Nothing out of the ordinary!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "Hey, great weather today, huh.\x02",
    )

    CloseMessageWindow()

    label("loc_2113")

    TalkEnd(0xA)
    Return()

    # Function_7_152B end

    def Function_8_2117(): pass

    label("Function_8_2117")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_21BB")

    ChrTalk(    #91
        0xFE,
        (
            "The walls of the Ahnenburg haven't been\x01",
            "breached since our kingdom was founded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "On that glory and tradition, we swear to\x01",
            "protect this place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2353")

    label("loc_21BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2353")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_229F")

    ChrTalk(    #93
        0xFE,
        "Oh, you're bracers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "We, the Gurune Gate Defense Force,\x01",
            "are currently increasing our security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "We can't stop danger before it gets out of\x01",
            "hand when we can't even control the gate,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2353")

    label("loc_229F")


    ChrTalk(    #96
        0xFE,
        (
            "We, the Gurune Gate Defense Force,\x01",
            "are currently increasing our security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "We can't stop danger before it gets out of\x01",
            "hand when we can't even control the gate,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2353")

    TalkEnd(0xB)
    Return()

    # Function_8_2117 end

    def Function_9_2357(): pass

    label("Function_9_2357")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_24F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247A")

    ChrTalk(    #98
        0xFE,
        (
            "First a flying island appears,\x01",
            "then orbments conk out on us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "It's just been one crazy thing after another\x01",
            "in the kingdom lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "At this rate, I suppose the Goddess'll drop\x01",
            "in for lunch next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "...Oops, pardon me. Didn't mean to insult\x01",
            "She Above.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_24ED")

    label("loc_247A")


    ChrTalk(    #102
        0xFE,
        (
            "First a flying island appears,\x01",
            "then orbments conk out on us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "Feels like something out of a fairy tale.\x02",
    )

    CloseMessageWindow()

    label("loc_24ED")

    Jump("loc_29A9")

    label("loc_24F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2651")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25BF")

    ChrTalk(    #104
        0xFE,
        "Hello, welcome to the Gurune Gate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "We're on high alert at the moment,\x01",
            "so customs will be more strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "The only ones allowed to pass freely\x01",
            "are bracers and army personnel.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_264E")

    label("loc_25BF")


    ChrTalk(    #107
        0xFE,
        (
            "This is an emergency situation,\x01",
            "so customs will be more strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "The only ones allowed to pass freely\x01",
            "are bracers and army personnel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_264E")

    Jump("loc_29A9")

    label("loc_2651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_271B")

    ChrTalk(    #109
        0xFE,
        (
            "Apparently there was some crazy incident\x01",
            "in Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "I wonder if it had anything to do with the\x01",
            "Special Ops soldiers who appeared on\x01",
            "the scenic route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "I've got a bad feeling...\x02",
    )

    CloseMessageWindow()
    Jump("loc_29A9")

    label("loc_271B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_27AD")

    ChrTalk(    #112
        0xFE,
        (
            "Ah, just so you know, the scenic route is\x01",
            "currently closed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "If you're heading to Grancel, you should go\x01",
            "via the Royal Avenue.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A9")

    label("loc_27AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_2859")

    ChrTalk(    #114
        0xFE,
        "Welcome to the Gurune Gate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "You seem awfully worked up.\x01",
            "Everything all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "If you're here to have a look around,\x01",
            "you can stay for a bit longer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A9")

    label("loc_2859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_28DC")

    ChrTalk(    #117
        0xFE,
        "Welcome to the Gurune Gate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "It's almost time for the signing ceremony,\x01",
            "so we've been told to step up security.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A9")

    label("loc_28DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2937")

    ChrTalk(    #119
        0xFE,
        "A pact signing, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "Hopefully no one turns up to try and interfere.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29A9")

    label("loc_2937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_29A9")

    ChrTalk(    #121
        0xFE,
        "Welcome to the Gurune Gate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "This is the guard post that connects the\x01",
            "Grancel and Rolent regions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29A9")

    TalkEnd(0xC)
    Return()

    # Function_9_2357 end

    def Function_10_29AD(): pass

    label("Function_10_29AD")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_2A4D")

    ChrTalk(    #123
        0xFE,
        "Really, it's just one crazy event after the other.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "Compared to things these days, that coup d'etat\x01",
            "from before almost seems like a game.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE8")

    label("loc_2A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B67")

    ChrTalk(    #125
        0xFE,
        (
            "This guard post was a mess when the\x01",
            "orbments stopped working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "On top of all the lights suddenly going out,\x01",
            "the gate wouldn't close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "Apparently communications are working again,\x01",
            "but it doesn't change the fact that this is\x01",
            "a pretty dire situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_2C44")

    label("loc_2B67")


    ChrTalk(    #128
        0xFE,
        (
            "Apparently communications are working again,\x01",
            "but it doesn't change the fact that this is\x01",
            "a pretty dire situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "I don't really know what's going on,\x01",
            "but I'd better stay on my toes and be\x01",
            "ready for anything...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C44")

    Jump("loc_2FE8")

    label("loc_2C47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2D01")

    ChrTalk(    #130
        0xFE,
        (
            "With this, the Intelligence Division's\x01",
            "finally buried...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "That's a relief for now, but I still wonder what\x01",
            "that giant mechanical doll-looking thing that\x01",
            "flew off was.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE8")

    label("loc_2D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_2D7D")

    ChrTalk(    #132
        0xFE,
        (
            "The society, huh...\x01",
            "Wonder what kind of people they are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "I'd better attend to the security of the gate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FE8")

    label("loc_2D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_2E15")

    ChrTalk(    #134
        0xFE,
        (
            "We've got a meeting later, so the commander\x01",
            "told us to assemble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "It's gotta be about 'that'...\x01",
            "That incident that happened in Bose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE8")

    label("loc_2E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_2EB6")

    ChrTalk(    #136
        0xFE,
        (
            "There's a guard force placed in the villa,\x01",
            "I hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "Ever since General Cassius returned,\x01",
            "assignments like that have become a\x01",
            "lot more common.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE8")

    label("loc_2EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2F44")

    ChrTalk(    #138
        0xFE,
        "Not long now till the signing ceremony.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "There's gonna be a lot of VIPs going in\x01",
            "and out, so I bet we'll be on high alert.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE8")

    label("loc_2F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2FE8")

    ChrTalk(    #140
        0xFE,
        (
            "Apparently weird events happened over in\x01",
            "Ruan and Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "Grancel and Rolent over there on the other\x01",
            "side of the wall have been the image of peace.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FE8")

    TalkEnd(0xD)
    Return()

    # Function_10_29AD end

    def Function_11_2FEC(): pass

    label("Function_11_2FEC")

    EventBegin(0x0)
    OP_6D(-16830, 0, 1620, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(8000, 0)
    OP_6C(74000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -82890, 0, 20, 90)
    StopSound(0x7D00, 0x3D090, 0x0)
    FadeToBright(2000, 0)
    StopSound(0x7D00, 0x1FBD0, 0x2EE0)

    def lambda_3065():
        OP_6B(3250, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3065)

    def lambda_3075():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3075)

    def lambda_3085():
        OP_6D(-72030, 0, 20, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3085)
    Sleep(8000)
    OP_8E(0x101, 0xFFFEDED2, 0x0, 0xFFFFFFEC, 0x1388, 0x0)
    WaitChrThread(0x101, 0x3)
    Sleep(500)

    ChrTalk(    #142
        0x101,
        (
            "#1020F#5PIt's evening already! Crap!\x02\x03",

            "#1015FOkay, calm down... Above the Ahnenburg...\x01",
            "In other words, on top of the wall.\x02\x03",

            "#1002FI've gotta hurry!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1637)
    EventEnd(0x0)
    Return()

    # Function_11_2FEC end

    def Function_12_3158(): pass

    label("Function_12_3158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31DB")
    EventBegin(0x2)

    ChrTalk(    #143
        0x101,
        (
            "#1003F(What am I even doing?!)\x02\x03",

            "#1002F(Joshua's... Joshua's waiting for me, right?!)\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_31DB")

    Return()

    # Function_12_3158 end

    def Function_13_31DC(): pass

    label("Function_13_31DC")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_13_31DC end

    SaveToFile()

Try(main)
