from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0134   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0134.x',
        MapIndex            = 3,
        MapDefaultBGM       = "ed60084",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0134_1 ._SN',
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
        'Father Divine',                        # 9
        'Mayor Klaus',                          # 10
        'Sister May',                           # 11
        'Miner Pierre',                         # 12
        'Miner Heinrich',                       # 13
        'Armand',                               # 14
        'Ellie',                                # 15
        'Targeting Camera',                     # 16
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
        'ED6_DT07/CH01400 ._CH',             # 00
        'ED6_DT07/CH02350 ._CH',             # 01
        'ED6_DT07/CH01410 ._CH',             # 02
        'ED6_DT07/CH01500 ._CH',             # 03
        'ED6_DT07/CH01140 ._CH',             # 04
        'ED6_DT07/CH01150 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH02350P._CP',             # 01
        'ED6_DT07/CH01410P._CP',             # 02
        'ED6_DT07/CH01500P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
        'ED6_DT07/CH01150P._CP',             # 05
    )

    DeclNpc(
        X                   = -14740,
        Z                   = 0,
        Y                   = 43530,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        X                   = -16830,
        Z                   = 0,
        Y                   = 42890,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 55350,
        Z                   = 0,
        Y                   = 46550,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 56050,
        Z                   = 0,
        Y                   = 40700,
        Direction           = 358,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 64000,
        Z                   = 0,
        Y                   = 47270,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 64000,
        Z                   = 0,
        Y                   = 48170,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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


    ScpFunction(
        "Function_0_1DA",          # 00, 0
        "Function_1_234",          # 01, 1
        "Function_2_235",          # 02, 2
        "Function_3_3B2",          # 03, 3
        "Function_4_67E",          # 04, 4
        "Function_5_6E2",          # 05, 5
        "Function_6_7B6",          # 06, 6
        "Function_7_95C",          # 07, 7
        "Function_8_C50",          # 08, 8
        "Function_9_D27",          # 09, 9
        "Function_10_1785",        # 0A, 10
        "Function_11_1820",        # 0B, 11
    )


    def Function_0_1DA(): pass

    label("Function_0_1DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x234, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20D")
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x10)
    Jump("loc_21C")

    label("loc_20D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_21C")
    ClearChrFlags(0xE, 0x10)

    label("loc_21C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_233")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 9)

    label("loc_233")

    Return()

    # Function_0_1DA end

    def Function_1_234(): pass

    label("Function_1_234")

    Return()

    # Function_1_234 end

    def Function_2_235(): pass

    label("Function_2_235")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25A")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_39C")

    label("loc_25A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_273")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_39C")

    label("loc_273")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_39C")

    label("loc_28C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A5")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_39C")

    label("loc_2A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BE")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_39C")

    label("loc_2BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_39C")

    label("loc_2D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F0")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_39C")

    label("loc_2F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_309")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_39C")

    label("loc_309")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_322")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_39C")

    label("loc_322")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33B")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_39C")

    label("loc_33B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_354")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_39C")

    label("loc_354")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36D")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_39C")

    label("loc_36D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_386")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_39C")

    label("loc_386")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39C")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_39C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_39C")

    label("loc_3B1")

    Return()

    # Function_2_235 end

    def Function_3_3B2(): pass

    label("Function_3_3B2")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_67A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4A1")

    ChrTalk(    #0
        0x8,
        (
            "I intend to contact Grancel Cathedral\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "They have an abundance of texts, and\x01",
            "their priests are acquainted with diseases\x01",
            "from all respective regions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "They may know how to treat this affliction.\x02",
    )

    CloseMessageWindow()
    Jump("loc_67A")

    label("loc_4A1")


    ChrTalk(    #3
        0x8,
        (
            "If the secret stimulant of the church\x01",
            "hasn't worked, then I'm afraid I'm at\x01",
            "a loss as to what to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "The coma cases here differ from the\x01",
            "ones caused by drugs or disease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "For now, I intend to scour all the medical\x01",
            "texts I have on hand, but I have my doubts\x01",
            "about how much we can expect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "Perhaps I should contact Grancel Cathedral\x01",
            "and see what they have to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "Once I have a full report on the symptoms,\x01",
            "I'll have the results posted immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_67A")

    TalkEnd(0x8)
    Return()

    # Function_3_3B2 end

    def Function_4_67E(): pass

    label("Function_4_67E")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_6DE")

    ChrTalk(    #8
        0xFE,
        "Oh, Goddess Above, Aidios...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "May the people lured into this\x01",
            "sleep awaken...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DE")

    TalkEnd(0xA)
    Return()

    # Function_4_67E end

    def Function_5_6E2(): pass

    label("Function_5_6E2")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_7B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_733")

    ChrTalk(    #10
        0xFE,
        (
            "I am deeply thankful for the Goddess'\x01",
            "daily protection.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B2")

    label("loc_733")


    ChrTalk(    #11
        0xFE,
        (
            "Thanks to the Goddess, there were\x01",
            "no accidents of any kind today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I shall pray for Her protection again\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_7B2")

    TalkEnd(0xB)
    Return()

    # Function_5_6E2 end

    def Function_6_7B6(): pass

    label("Function_6_7B6")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_958")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_858")

    ChrTalk(    #13
        0xFE,
        (
            "Geez, how long is Pierre gonna keep\x01",
            "praying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "I wish he'd think for a second about me,\x01",
            "the guy who's been waitin' for, like, ever...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_958")

    label("loc_858")


    ChrTalk(    #15
        0xFE,
        (
            "Geez, how long is Pierre gonna keep\x01",
            "praying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "I wish he'd think for a second about me,\x01",
            "the guy who's been waitin' for, like, ever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "Ahhh, if he takes much longer, the bar'll\x01",
            "close!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Maybe I should just go and get\x01",
            "something on my own.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_958")

    TalkEnd(0xC)
    Return()

    # Function_6_7B6 end

    def Function_7_95C(): pass

    label("Function_7_95C")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x234, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_9A7")

    ChrTalk(    #19
        0xFE,
        "Ah, Ellie...\x02",
    )

    CloseMessageWindow()
    Jump("loc_C21")

    label("loc_9A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_A24")

    ChrTalk(    #20
        0xFE,
        "I'm counting on you to recover that ring.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "If you find anything out, come here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B4F")

    label("loc_A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_A87")

    ChrTalk(    #22
        0xFE,
        "I'm counting on you to recover that ring.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "If you find anything out, come here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B4F")

    label("loc_A87")

    OP_A2(0x4)

    ChrTalk(    #24
        0xFE,
        "Heya, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "H-How about it?\x01",
            "How's the investigation going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1015FWe're working on it.\x02\x03",

            "It won't be much longer, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "I-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "Okay, I understand. I'll be patient.\x02",
    )

    CloseMessageWindow()

    label("loc_B4F")

    Jump("loc_C21")

    label("loc_B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_C21")

    ChrTalk(    #29
        0xFE,
        (
            "The night sky may be veiled in\x01",
            "darkness tonight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "...but, as long as you're by my side,\x01",
            "I've no need for its dismal glow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Our love burns brighter than all the\x01",
            "stars in the sky, Ellie.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C21")

    Jump("loc_C4C")

    label("loc_C24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C48")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_C41")
    Call(1, 1)
    Jump("loc_C45")

    label("loc_C41")

    Call(1, 0)

    label("loc_C45")

    Jump("loc_C4C")

    label("loc_C48")

    Call(1, 3)

    label("loc_C4C")

    TalkEnd(0xD)
    Return()

    # Function_7_95C end

    def Function_8_C50(): pass

    label("Function_8_C50")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_C70")

    ChrTalk(    #32
        0xFE,
        "Oh, Armand...\x02",
    )

    CloseMessageWindow()
    Jump("loc_D23")

    label("loc_C70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEB")

    ChrTalk(    #33
        0xFE,
        "We'll be waiting here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "It may be a hard mission, but please,\x01",
            "do everything you can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D23")

    label("loc_CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_D23")

    ChrTalk(    #35
        0xFE,
        "Teehee. Oh, Armand, you're such a romantic!\x02",
    )

    CloseMessageWindow()

    label("loc_D23")

    TalkEnd(0xE)
    Return()

    # Function_8_C50 end

    def Function_9_D27(): pass

    label("Function_9_D27")

    EventBegin(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D48")
    Call(0, 10)
    FadeToBright(0, 0)
    Call(0, 11)

    label("loc_D48")

    OP_44(0x8, 0x0)
    SetChrPos(0x8, -17390, 0, 42890, 90)
    SetChrPos(0x101, -15830, 0, 42280, 270)
    SetChrPos(0x103, -15950, 0, 43470, 270)
    SetChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC7")
    SetChrPos(0x9, -15850, 0, 45570, 180)
    SetChrPos(0xF8, -14610, 0, 43470, 270)
    SetChrPos(0xF9, -14600, 0, 42200, 270)
    Jump("loc_DFA")

    label("loc_DC7")

    SetChrPos(0x9, -16020, 0, 45150, 180)
    SetChrPos(0xF8, -14600, 0, 42200, 270)
    SetChrPos(0xF9, -14610, 0, 43470, 270)

    label("loc_DFA")

    TurnDirection(0xF8, 0x8, 0)
    TurnDirection(0xF9, 0x8, 0)
    ClearChrFlags(0x9, 0x80)
    OP_6D(-16630, 3000, 43560, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_6D(-16630, 0, 43560, 2000)
    OP_0D()
    Sleep(500)
    OP_DC()

    ChrTalk(    #36
        0x8,
        (
            "#6PI've been to all the houses, and it seems\x01",
            "the symptoms are the same in every\x01",
            "case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#6PTheir breathing is stable, and their pupils\x01",
            "look fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "#6PThey seem to be asleep, so they shouldn't\x01",
            "sicken further, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        "#603FI see... It's a small mercy, at least.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "#6PIf we cannot rouse them, however...\x01",
            "I doubt I need to elaborate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "#6PMayor, we have to find a solution,\x01",
            "as fast as we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        "#602FHmmmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1003F#6P...\x02",
    )

    CloseMessageWindow()

    def lambda_1034():
        TurnDirection(0xF8, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1034)
    Sleep(100)

    def lambda_1047():
        TurnDirection(0xF9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1047)
    Sleep(100)
    TurnDirection(0x103, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A8")

    ChrTalk(    #44
        0x107,
        (
            "#065F#2PEstelle! Are you okay?\x02\x03",

            "You don't look so good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1202")

    label("loc_10A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10FA")

    ChrTalk(    #45
        0x106,
        (
            "#552F#2PEstelle, you all right?\x02\x03",

            "You're lookin'...kinda bad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1202")

    label("loc_10FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_114C")

    ChrTalk(    #46
        0x104,
        (
            "#032F#2PEstelle. Are you well?\x02\x03",

            "Your color is...distressing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1202")

    label("loc_114C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A0")

    ChrTalk(    #47
        0x105,
        (
            "#043F#2PEstelle, are you feeling all right?\x02\x03",

            "You're so pale...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1202")

    label("loc_11A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1202")

    ChrTalk(    #48
        0x108,
        (
            "#572F#4PBe strong, Estelle.\x02\x03",

            "There would be no shame in needing\x01",
            "to take a seat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1202")

    TurnDirection(0x101, 0xF8, 400)

    ChrTalk(    #49
        0x101,
        (
            "#1026F#6PI'm okay...\x02\x03",

            "#1007FIt's just, even Elissa's mom and\x01",
            "Luke collapsed...\x02\x03",

            "It's...kind of a shock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x103,
        (
            "#524F#4PEstelle...\x02\x03",

            "If you're not feeling well, you can go\x01",
            "back to the guildhouse, you know.\x02\x03",

            "Or you could rest at home.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(500)

    ChrTalk(    #51
        0x101,
        (
            "#1025F#6P...No. Can't let myself get\x01",
            "all mopey, you know?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    def lambda_134C():
        TurnDirection(0x103, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_134C)

    def lambda_135A():
        TurnDirection(0xF9, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_135A)
    TurnDirection(0xF8, 0x8, 400)
    Sleep(500)

    ChrTalk(    #52
        0x101,
        (
            "#1002F#6PFather, you really have no idea\x01",
            "why they're comatose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "#6PI'm afraid I don't.\x01",
            "I desperately wish I did!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "#6PThe traditional Church remedies for\x01",
            "awakening the sleeping aren't working,\x01",
            "so I don't think it is poison or illness...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "#6PIt's more like... Aidios preserve us,\x01",
            "but it's like their souls are trapped by\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#1002F#6PTheir...souls?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x103,
        "#522F#4P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    Sleep(500)

    ChrTalk(    #58
        0x103,
        (
            "#022F#4PFor the moment, it seems the best course\x01",
            "of action would be to visit the homes of\x01",
            "the afflicted.\x02\x03",

            "We need to find out what, exactly, the\x01",
            "situation was like when they fell into\x01",
            "these...comas.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #59
        0x101,
        (
            "#1004F#6PAh!\x02\x03",

            "#1002FRight, let's go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        "#603FEstelle. Scherazard.\x02",
    )

    CloseMessageWindow()

    def lambda_1625():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1625)
    Sleep(100)

    def lambda_1638():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1638)
    Sleep(100)
    OP_8C(0xF9, 0, 400)

    ChrTalk(    #61
        0x9,
        (
            "#602FAs of now, in my capacity as mayor of Rolent,\x01",
            "I am formally requesting guild assistance.\x02\x03",

            "Please...discover what has caused this,\x01",
            "and assuage the fears of our people!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1006F#6PJust leave it to us, Mayor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x103,
        (
            "#020F#6PWe'll do everything in our power, sir.\x01",
            "I swear it.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T0101   ._SN", 117, 0, 0)
    IdleLoop()
    Return()

    # Function_9_D27 end

    def Function_10_1785(): pass

    label("Function_10_1785")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_1801"),
        (1, "loc_1807"),
        (SWITCH_DEFAULT, "loc_180D"),
    )


    label("loc_1801")

    OP_A2(0x1200)
    Jump("loc_180D")

    label("loc_1807")

    OP_A2(0x1201)
    Jump("loc_180D")

    label("loc_180D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_181B")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_181F")

    label("loc_181B")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_181F")

    Return()

    # Function_10_1785 end

    def Function_11_1820(): pass

    label("Function_11_1820")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_11_1820 end

    SaveToFile()

Try(main)
