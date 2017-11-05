from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1110   ._SN',
        MapName             = 'Bose',
        Location            = 'T1110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 1,
        EntryFunctionIndex  = 3,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1110_1 ._SN',
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
        'Rionne',                               # 9
        'Alvelle',                              # 10
        'Borden',                               # 11
        'Luana',                                # 12
        'Elke',                                 # 13
        'Paul',                                 # 14
        'Cecile',                               # 15
        'Kuwano',                               # 16
        'Modena',                               # 17
        'Mirano',                               # 18
        'Trino',                                # 19
        'Simon',                                # 20
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
        'ED6_DT07/CH01690 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT07/CH01680 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01480 ._CH',             # 04
        'ED6_DT07/CH01220 ._CH',             # 05
        'ED6_DT07/CH01010 ._CH',             # 06
        'ED6_DT07/CH01000 ._CH',             # 07
        'ED6_DT07/CH01183 ._CH',             # 08
        'ED6_DT07/CH01230 ._CH',             # 09
        'ED6_DT07/CH01200 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01143 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH01690P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT07/CH01680P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01480P._CP',             # 04
        'ED6_DT07/CH01220P._CP',             # 05
        'ED6_DT07/CH01010P._CP',             # 06
        'ED6_DT07/CH01000P._CP',             # 07
        'ED6_DT07/CH01183P._CP',             # 08
        'ED6_DT07/CH01230P._CP',             # 09
        'ED6_DT07/CH01200P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01143P._CP',             # 0C
    )

    DeclNpc(
        X                   = -21340,
        Z                   = 0,
        Y                   = 72520,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -11200,
        Z                   = 5250,
        Y                   = 72600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -22100,
        Z                   = 0,
        Y                   = 69250,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 20970,
        Z                   = 0,
        Y                   = 67860,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 27100,
        Z                   = 4000,
        Y                   = 72200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 20100,
        Z                   = 0,
        Y                   = 68410,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -16400,
        Z                   = 0,
        Y                   = -1700,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -22530,
        Z                   = 0,
        Y                   = -410,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -18730,
        Z                   = 70,
        Y                   = 33060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 16329,
        Z                   = 0,
        Y                   = 31480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -21100,
        Z                   = 0,
        Y                   = 33600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20200,
        Z                   = 0,
        Y                   = 30680,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )


    ScpFunction(
        "Function_0_292",          # 00, 0
        "Function_1_3E7",          # 01, 1
        "Function_2_3E8",          # 02, 2
        "Function_3_41F",          # 03, 3
        "Function_4_475",          # 04, 4
        "Function_5_4CB",          # 05, 5
        "Function_6_568",          # 06, 6
        "Function_7_E23",          # 07, 7
        "Function_8_1552",         # 08, 8
        "Function_9_2076",         # 09, 9
        "Function_10_282F",        # 0A, 10
        "Function_11_2C3E",        # 0B, 11
        "Function_12_3063",        # 0C, 12
        "Function_13_3D41",        # 0D, 13
        "Function_14_3EE4",        # 0E, 14
        "Function_15_46D3",        # 0F, 15
        "Function_16_5226",        # 10, 16
        "Function_17_5B2C",        # 11, 17
    )


    def Function_0_292(): pass

    label("Function_0_292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2A1")
    SetChrFlags(0x9, 0x80)
    Jump("loc_3C5")

    label("loc_2A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2BA")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_3C5")

    label("loc_2BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2F0")
    ClearChrFlags(0x13, 0x80)
    OP_43(0x13, 0x0, 0x6, 0x2)
    SetChrFlags(0xE, 0x10)
    SetChrPos(0xE, -22530, 0, 1020, 180)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    Jump("loc_3C5")

    label("loc_2F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_343")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xB, 12900, 0, 69780, 0)
    SetChrPos(0xC, 22510, 0, 68280, 270)
    ClearChrFlags(0x13, 0x80)
    OP_43(0x13, 0x0, 0x6, 0x2)
    SetChrPos(0xE, -22530, 0, 1020, 180)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_3C5")

    label("loc_343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_3BE")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xB, 12900, 0, 69780, 0)
    SetChrPos(0xC, 22510, 0, 68280, 270)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 12)
    SetChrPos(0x13, -20800, 0, 34930, 225)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, -21830, 0, 35100, 90)
    Jump("loc_3C5")

    label("loc_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_3C5")

    label("loc_3C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3CF")
    Jump("loc_3E6")

    label("loc_3CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E6")
    SetChrFlags(0x11, 0x80)

    label("loc_3E6")

    Return()

    # Function_0_292 end

    def Function_1_3E7(): pass

    label("Function_1_3E7")

    Return()

    # Function_1_3E7 end

    def Function_2_3E8(): pass

    label("Function_2_3E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_41A")

    label("loc_3F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_417")
    OP_8D(0xFE, 20900, 30000, 15300, 31700, 2000)
    Jump("loc_3F4")

    label("loc_417")

    Jump("loc_41E")

    label("loc_41A")

    Call(6, 2)

    label("loc_41E")

    Return()

    # Function_2_3E8 end

    def Function_3_41F(): pass

    label("Function_3_41F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_451")

    label("loc_42B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44E")
    OP_8D(0xFE, 21600, 67480, 22890, 69030, 2000)
    Jump("loc_42B")

    label("loc_44E")

    Jump("loc_474")

    label("loc_451")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_474")
    OP_8D(0xFE, 26200, 71400, 28400, 72600, 2000)
    Jump("loc_451")

    label("loc_474")

    Return()

    # Function_3_41F end

    def Function_4_475(): pass

    label("Function_4_475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A7")

    label("loc_481")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A4")
    OP_8D(0xFE, 12210, 70500, 14370, 68720, 1500)
    Jump("loc_481")

    label("loc_4A4")

    Jump("loc_4CA")

    label("loc_4A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4CA")
    OP_8D(0xFE, 17430, 68790, 23880, 64870, 1500)
    Jump("loc_4A7")

    label("loc_4CA")

    Return()

    # Function_4_475 end

    def Function_5_4CB(): pass

    label("Function_5_4CB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_567")
    OP_8E(0xFE, 0xFFFFA6F0, 0x0, 0x11B34, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFAB8C, 0x0, 0x11B34, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFADE4, 0x0, 0x11C60, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFAEC0, 0x0, 0x11C60, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFADE4, 0x0, 0x11C60, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFAB8C, 0x0, 0x11B34, 0x7D0, 0x0)
    Jump("Function_5_4CB")

    label("loc_567")

    Return()

    # Function_5_4CB end

    def Function_6_568(): pass

    label("Function_6_568")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_782")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E8")

    ChrTalk(    #0
        0xFE,
        (
            "Speaking very broadly, my husband's\x01",
            "viewpoint is correct.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Most citizens are simply going to care about\x01",
            "maintaining their daily lives, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "I really doubt anyone, even the mayor, cares\x01",
            "much about international relations right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Of course, the fact that nobody seems\x01",
            "to be able to focus on it is half the\x01",
            "reason it's really concerning.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_77F")

    label("loc_6E8")


    ChrTalk(    #4
        0xFE,
        (
            "Everyone has enough to worry about\x01",
            "with their lights and heat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I doubt anyone will spare a thought for\x01",
            "international geo-politics right now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77F")

    Jump("loc_E1F")

    label("loc_782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_8CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84F")

    ChrTalk(    #6
        0xFE,
        (
            "All the orbments in our home have\x01",
            "stopped working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I sent my son Alvelle down to the\x01",
            "factory, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I'm afraid this might not be the sort of\x01",
            "problem that they can fix.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_8CB")

    label("loc_84F")


    ChrTalk(    #9
        0xFE,
        (
            "All the orbments in our home have\x01",
            "stopped working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "If they can't be repaired...\x01",
            "No, I shouldn't think about that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CB")

    Jump("loc_E1F")

    label("loc_8CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_8D8")
    Jump("loc_E1F")

    label("loc_8D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_A77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_958")

    ChrTalk(    #11
        0xFE,
        (
            "Even Ms. Mirano exudes the atmosphere of\x01",
            "a merchant now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "I wish my Alvelle had a spirit like hers...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A74")

    label("loc_958")


    ChrTalk(    #13
        0xFE,
        (
            "Even Ms. Mirano exudes the atmosphere of\x01",
            "a merchant now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "I wish my Alvelle had a spirit like hers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Well, I'll keep my eye on him and hope\x01",
            "that his talent comes in eventually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "It's because I believe in him that I'm\x01",
            "sending him to the royal academy,\x01",
            "after all!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A74")

    Jump("loc_E1F")

    label("loc_A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_BBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AFA")

    ChrTalk(    #17
        0xFE,
        (
            "The core of our business is in that\x01",
            "market, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "It's only natural we'd help each other\x01",
            "for once!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBB")

    label("loc_AFA")


    ChrTalk(    #19
        0xFE,
        (
            "We're cooperating with Trino's family\x01",
            "to support repairing the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "The core of our business is in that\x01",
            "market, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "It's only natural we'd help each other\x01",
            "for once!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_BBB")

    Jump("loc_E1F")

    label("loc_BBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_C25")

    ChrTalk(    #22
        0xFE,
        (
            "It seems something terrible happened at\x01",
            "the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "My husband ran out in a panic!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E1F")

    label("loc_C25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_E1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CDD")

    ChrTalk(    #24
        0xFE,
        (
            "Borden and Trino come from two of\x01",
            "Bose's preeminent merchant houses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "We may be friendly neighbors, but we're also\x01",
            "rivals in trade who'll never admit defeat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1F")

    label("loc_CDD")


    ChrTalk(    #26
        0xFE,
        (
            "Borden and Trino come from two of\x01",
            "Bose's preeminent merchant houses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "We may be friendly neighbors, but we're also\x01",
            "rivals in trade who'll never admit defeat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "We're been pushed around by Trino\x01",
            "a bit lately, but we have a plan!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Hopefully all this new trade with Erebonia\x01",
            "will more than make up for it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_E1F")

    TalkEnd(0x8)
    Return()

    # Function_6_568 end

    def Function_7_E23(): pass

    label("Function_7_E23")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_FA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EBE")

    ChrTalk(    #30
        0xFE,
        (
            "Time to really start studying for the\x01",
            "entrance exams!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "I'm pretty confident, but I still try\x01",
            "to be cautious about everything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA0")

    label("loc_EBE")


    ChrTalk(    #32
        0xFE,
        (
            "Seems like the city's getting back\x01",
            "to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Time to start studying for the Jenis\x01",
            "entrance exams, then!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "After all, I'd look like kind of a doofus\x01",
            "if I botched them now, with my parents\x01",
            "finally accepting it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_FA0")

    Jump("loc_154E")

    label("loc_FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_10FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_101E")

    ChrTalk(    #35
        0xFE,
        (
            "I don't really like being compared\x01",
            "to Mirano.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "I mean, we're entirely different types\x01",
            "of people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F9")

    label("loc_101E")


    ChrTalk(    #37
        0xFE,
        "Mirano's an incredible woman, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "I just don't like being compared to her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "I mean, we're entirely different types\x01",
            "of people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "If I'm an herbivore, she's a carnivore.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "You know, in that sense.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_10F9")

    Jump("loc_154E")

    label("loc_10FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_12F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_119B")

    ChrTalk(    #42
        0xFE,
        (
            "Yesterday, Father was talking over repair\x01",
            "plans with Mr. Trino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Thanks to that, the repair work's going\x01",
            "to begin TODAY, apparently.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F3")

    label("loc_119B")


    ChrTalk(    #44
        0xFE,
        (
            "Yesterday, Father was talking over repair\x01",
            "plans with Mr. Trino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "Thanks to that, the repair work's going\x01",
            "to begin TODAY, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "Seeing them like that, I admit I don't find\x01",
            "the idea of being a merchant bad.\x01",
            "It's just...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I just don't think there's any way\x01",
            "I could do it. It's in my blood but\x01",
            "not in my heart, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_12F3")

    Jump("loc_154E")

    label("loc_12F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1379")

    ChrTalk(    #48
        0xFE,
        "Father ran out a bit ago in a panic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "It's rare to see him get so worked up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "Did something serious happen?\x02",
    )

    CloseMessageWindow()
    Jump("loc_154E")

    label("loc_1379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_154E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_141D")

    ChrTalk(    #51
        0xFE,
        (
            "My family seems set on the idea that\x01",
            "I'll be a merchant when I graduate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "But I personally have no real intention\x01",
            "of following that path.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_154E")

    label("loc_141D")


    ChrTalk(    #53
        0xFE,
        (
            "The main reason I'm still at the royal academy,\x01",
            "though, is because I told them I'd study\x01",
            "economics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "My family seems set on the idea that I'll\x01",
            "be a merchant when I graduate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "But I personally have no real intention\x01",
            "of following that path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "I just somehow don't think it'd work for me.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_154E")

    TalkEnd(0x9)
    Return()

    # Function_7_E23 end

    def Function_8_1552(): pass

    label("Function_8_1552")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_179D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16DD")

    ChrTalk(    #57
        0xFE,
        (
            "For the moment, our worries are little\x01",
            "more than lights or heating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "If this keeps up, however, we're going to\x01",
            "be facing international repercussions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "From a military perspective, the idea that\x01",
            "the Royal air force has been neutralized\x01",
            "is terrifying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "The Empire of old would leap, two-footed,\x01",
            "at this sort of chance to invade us while\x01",
            "we're defenseless.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_179A")

    label("loc_16DD")


    ChrTalk(    #61
        0xFE,
        (
            "This problem with the orbments is going to\x01",
            "end up being international, mark my words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "If it was just a problem with being dark\x01",
            "and cold at night, I wouldn't be nearly\x01",
            "so worried.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179A")

    Jump("loc_2072")

    label("loc_179D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1950")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18B7")

    ChrTalk(    #63
        0xFE,
        (
            "To be completely incapable of using\x01",
            "orbments is quite the problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Orbal technology can honestly be called\x01",
            "the lifeblood of our country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "If it ceases to work, then that affects\x01",
            "us on every imaginable level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "I fear hard times await us ahead.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_194D")

    label("loc_18B7")


    ChrTalk(    #67
        0xFE,
        (
            "Orbal technology can honestly be called\x01",
            "the lifeblood of our country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "If it ceases to work, then that affects\x01",
            "us on every imaginable level.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_194D")

    Jump("loc_2072")

    label("loc_1950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1B1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A25")

    ChrTalk(    #69
        0xFE,
        (
            "With flights resumed, we've begun trade\x01",
            "with the Empire once again. But...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "The results haven't been quite what\x01",
            "we hoped for, thanks to Mirano.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "We'll have to call it a draw for now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B1B")

    label("loc_1A25")


    ChrTalk(    #72
        0xFE,
        (
            "With flights resumed, we've begun trade\x01",
            "with the Empire once again. But...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "The results haven't been quite what\x01",
            "we hoped for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "Due, in no small part, to Mirano's efforts.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "Hmph. Now it seems I have TWO rivals\x01",
            "to contend with.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1B1B")

    Jump("loc_2072")

    label("loc_1B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1D35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1BB0")

    ChrTalk(    #76
        0xFE,
        (
            "I'm certain Mirano is finding a way\x01",
            "around the cessation of flights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "Hmm... I may need to think of\x01",
            "a plan of my own...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D32")

    label("loc_1BB0")


    ChrTalk(    #78
        0xFE,
        (
            "The total stop of all flights in or out\x01",
            "of the city is a problem even for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "It happened just as I was setting up a\x01",
            "healthy trade with Erebonia, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "Trino and I are busy providing support\x01",
            "for the market's reconstruction, but\x01",
            "there's more going on here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Trino has Mirano. I'm sure she's going\x01",
            "to act in some way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "I envy him having such a reliable daughter.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1D32")

    Jump("loc_2072")

    label("loc_1D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1EC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1DC1")

    ChrTalk(    #83
        0xFE,
        (
            "For the moment, repair work has begun,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "I'll need to consider further support\x01",
            "as the project continues.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EBE")

    label("loc_1DC1")


    ChrTalk(    #85
        0xFE,
        (
            "For the moment, repair work has begun,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "Trino and I provided all the crucial supplies.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "I fear, however, that they'll run out\x01",
            "as work begins to get serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "I may need to consider further support\x01",
            "as the project continues.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1EBE")

    Jump("loc_2072")

    label("loc_1EC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2072")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1F90")

    ChrTalk(    #89
        0xFE,
        (
            "With the signing of the non-aggression pact,\x01",
            "trade with the Empire's picked up substantially.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "Trino has pushed us around for a while now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "This is our chance to close the gap!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2072")

    label("loc_1F90")


    ChrTalk(    #92
        0xFE,
        (
            "With the signing of the non-aggression pact,\x01",
            "trade with the Empire's picked up substantially.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "I've dealt with Erebonians for years\x01",
            "and years, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "This will be a good opportunity to\x01",
            "expand my reach there.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2072")

    TalkEnd(0xA)
    Return()

    # Function_8_1552 end

    def Function_9_2076(): pass

    label("Function_9_2076")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_21D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2145")

    ChrTalk(    #95
        0xFE,
        (
            "I was at the orbal workshop a little\x01",
            "while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "It was so crowded that I just gave\x01",
            "up and went home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "It seems like every single house in\x01",
            "the city has the same problem!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_21D1")

    label("loc_2145")


    ChrTalk(    #98
        0xFE,
        (
            "The workshop was so chaotic that\x01",
            "I just gave up and went home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "It seems like every single house in\x01",
            "the city has the same problem!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21D1")

    Jump("loc_282B")

    label("loc_21D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_237B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22ED")

    ChrTalk(    #100
        0xFE,
        (
            "I didn't realize the lights had stopped\x01",
            "working until night fell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "I was panicking, looking for a lamp,\x01",
            "but it was hard to find.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "And Elke was bawling her eyes out\x01",
            "because she was so afraid of the dark...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "I hope things return to normal soon.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2378")

    label("loc_22ED")


    ChrTalk(    #104
        0xFE,
        (
            "I didn't realize the lights had stopped\x01",
            "working until night fell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "After all, it's hard to even imagine\x01",
            "orbments would just fail.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2378")

    Jump("loc_282B")

    label("loc_237B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_24C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_23EF")

    ChrTalk(    #106
        0xFE,
        "Oh, Paul took Elke off to work today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "He said he wanted to show her the\x01",
            "reopened market.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24C0")

    label("loc_23EF")


    ChrTalk(    #108
        0xFE,
        "Oh, Paul took Elke off to work today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "He said he wanted to show her the\x01",
            "reopened market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "I do hope she's not being a bother to\x01",
            "the other stores or customers.\x01",
            "She can be a bit...rambunctious.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_24C0")

    Jump("loc_282B")

    label("loc_24C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_258A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2517")

    ChrTalk(    #111
        0xFE,
        (
            "My husband went off to check up\x01",
            "on the repairs to the market.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2587")

    label("loc_2517")


    ChrTalk(    #112
        0xFE,
        (
            "My husband went off to check up\x01",
            "on the repairs to the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "That man really does love his trade!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2587")

    Jump("loc_282B")

    label("loc_258A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_260D")

    ChrTalk(    #114
        0xFE,
        (
            "It's been a while since my husband was\x01",
            "home this much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "Heehee, it's like we're back to before\x01",
            "we were married!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_282B")

    label("loc_260D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2682")

    ChrTalk(    #116
        0xFE,
        (
            "I never, ever thought the market would\x01",
            "be attacked by a monster...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        "Why does peace never last...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_282B")

    label("loc_2682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_282B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2737")

    ChrTalk(    #118
        0xFE,
        (
            "My husband runs a boutique in the market,\x01",
            "if you're interested in getting more clothes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "It's called Paul & Elke's Outlet,\x01",
            "after himself and our daughter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_282B")

    label("loc_2737")

    TurnDirection(0xFE, 0x101, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)

    ChrTalk(    #120
        0xFE,
        "Oh! Your clothes are lovely!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "My husband runs a boutique in the market,\x01",
            "if you're interested in getting more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "I'm sure even you'll find something\x01",
            "you like!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        "Please, go visit some time!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_282B")

    TalkEnd(0xB)
    Return()

    # Function_9_2076 end

    def Function_10_282F(): pass

    label("Function_10_282F")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_28DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28A7")

    ChrTalk(    #124
        0xFE,
        "The orbie workshop was fuuull of customers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "I hope Dad gets that many customers, too!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_28D8")

    label("loc_28A7")


    ChrTalk(    #126
        0xFE,
        "The orbie workshop was fuuull of customers.\x02",
    )

    CloseMessageWindow()

    label("loc_28D8")

    Jump("loc_2C3A")

    label("loc_28DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_29E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298D")

    ChrTalk(    #127
        0xFE,
        "It was dark and scary last night!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "And the stove or nothing wouldn't\x01",
            "turn on, so it was real cold, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "*sniffle* Why aren't orbies working?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_29DE")

    label("loc_298D")


    ChrTalk(    #130
        0xFE,
        "It was dark and scary last night!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "*sniffle* Why aren't orbies working?\x02",
    )

    CloseMessageWindow()

    label("loc_29DE")

    Jump("loc_2C3A")

    label("loc_29E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2A7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2A27")

    ChrTalk(    #132
        0xFE,
        (
            "Dad's out, so it's me watching the\x01",
            "house today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A77")

    label("loc_2A27")


    ChrTalk(    #133
        0xFE,
        (
            "Dad's out, so it's me watching the\x01",
            "house today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "It's so booooring!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2A77")

    Jump("loc_2C3A")

    label("loc_2A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2B32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2ACF")

    ChrTalk(    #135
        0xFE,
        "The market's reeeal big, you know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "I wonder who broke it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B2F")

    label("loc_2ACF")


    ChrTalk(    #137
        0xFE,
        (
            "The market is broken, so Dad's taking\x01",
            "a break from his job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "I wonder who broke it?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2B2F")

    Jump("loc_2C3A")

    label("loc_2B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2BAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2B63")

    ChrTalk(    #139
        0xFE,
        "Dad came home early today!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BA9")

    label("loc_2B63")


    ChrTalk(    #140
        0xFE,
        "Dad came home early today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        "Yay! I'm gonna play with him!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2BA9")

    Jump("loc_2C3A")

    label("loc_2BAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2C3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2BE3")

    ChrTalk(    #142
        0xFE,
        "Dad sells clothes at the market!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C3A")

    label("loc_2BE3")


    ChrTalk(    #143
        0xFE,
        "Dad sells clothes at the market!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        "I'm gonna help out at Dad's store today!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2C3A")

    TalkEnd(0xC)
    Return()

    # Function_10_282F end

    def Function_11_2C3E(): pass

    label("Function_11_2C3E")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2E21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2D10")

    ChrTalk(    #145
        0xFE,
        (
            "You know, I'm taking this whole thing as\x01",
            "a sign from the Goddess and taking\x01",
            "some time off from the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "Just gonna spend time with my daughter\x01",
            "and wait for the market to reopen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E1E")

    label("loc_2D10")


    ChrTalk(    #147
        0xFE,
        (
            "Some of the other merchants have\x01",
            "set up shop in the hotel, but I've\x01",
            "decided to stay closed for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "People don't need clothes every day\x01",
            "the way they need food, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "I'm taking this whole thing as a sign\x01",
            "from the Goddess and taking some\x01",
            "time off.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2E1E")

    Jump("loc_305F")

    label("loc_2E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_305F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x348, 4)), scpexpr(EXPR_END)), "loc_2E89")

    ChrTalk(    #150
        0xFE,
        "Thanks to you guys, everyone got out safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        "I hope Miss Lila recovers soon...\x02",
    )

    CloseMessageWindow()
    Jump("loc_305F")

    label("loc_2E89")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #152
        0xFE,
        (
            "You guys! You really helped us out at\x01",
            "the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "If you hadn't been there, we might not\x01",
            "have rescued everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "I'm sure Aidios guided you to us.\x01",
            "Thank you so much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        (
            "#1007FBelieve me, I'm just glad we made it in time.\x02\x03",

            "#1002FDid everyone make it out all right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #156
        0xFE,
        (
            "Yes, somehow, except for poor Lila.\x01",
            "Thank you for asking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "All the merchants have settled down\x01",
            "in the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "I hope Miss Lila recovers soon...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A44)

    label("loc_305F")

    TalkEnd(0xD)
    Return()

    # Function_11_2C3E end

    def Function_12_3063(): pass

    label("Function_12_3063")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_31DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_314E")

    ChrTalk(    #159
        0xFE,
        (
            "Kuwano went off to the factory and\x01",
            "hasn't come back yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        "I'm sure he's off wasting time somewhere.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "If he's off fishing at a time like this,\x01",
            "I'm really not letting him back in the\x01",
            "house this time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_31D7")

    label("loc_314E")


    ChrTalk(    #162
        0xFE,
        (
            "I mean, how long does it take to go on\x01",
            "an errand and come back? Hmph.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "Really, that old lump just isn't useful\x01",
            "when it matters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31D7")

    Jump("loc_3D3D")

    label("loc_31DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_335F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32C6")

    ChrTalk(    #164
        0xFE,
        (
            "The orbments aren't working over at\x01",
            "Trino's next door, either, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "Seems like the problem is affecting\x01",
            "the entire town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "I thought it was just us, and had Kuwano\x01",
            "go down to the orbal workshop.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_335C")

    label("loc_32C6")


    ChrTalk(    #167
        0xFE,
        (
            "I thought the problem was just with our\x01",
            "orbments and had Kuwano go down to\x01",
            "the orbal workshop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "Well, it's a short trip.\x01",
            "He'll be back soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_335C")

    Jump("loc_3D3D")

    label("loc_335F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_3947")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x386, 3)), scpexpr(EXPR_END)), "loc_34A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_33F9")

    ChrTalk(    #169
        0xFE,
        "Don't worry about the fishing rod, dearies.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "It'll be a good shock for that old\x01",
            "trout-head to have it missing, I'm sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A2")

    label("loc_33F9")


    ChrTalk(    #171
        0xFE,
        "Ah, hello again, dearies.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "You can do whatever you like with\x01",
            "that fishing rod.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "It'll be a good shock for that old\x01",
            "trout-head to have it missing, I'm sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A2")

    Jump("loc_3944")

    label("loc_34A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3537")

    ChrTalk(    #174
        0xFE,
        (
            "I was going to ask him to do some shopping,\x01",
            "but Kuwano's nowhere to be found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "If you see him anywhere, do tell me,\x01",
            "won't you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3944")

    label("loc_3537")


    ChrTalk(    #176
        0xFE,
        "How ridiculous!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "I was going to ask him to do some shopping,\x01",
            "but Kuwano's nowhere to be found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "I may have to tie a leash, or at least\x01",
            "a fishing line, to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "If you see him anywhere, do tell me,\x01",
            "won't you?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x386, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x386, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3941")

    ChrTalk(    #180
        0x101,
        (
            "#1011FOh, if you're looking for Kuwano,\x01",
            "we saw him at the Kingfisher Inn.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #181
        0xFE,
        (
            "What?! You aren't pulling an old\x01",
            "woman's leg, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        (
            "#1015FN-No, we really did see him.\x01",
            "Seemed like he wanted to do some fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        "*siiiigh* I knew it. Just like I thought.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "Thank you for telling me, dearie.\x01",
            "It's what I expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        "Here. Take this.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #186
        "\x07\x00Received #593i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x251, 1)

    ChrTalk(    #187
        0x101,
        "#1004FWait a minute! Isn't this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        "Yep. Kuwano's treasured fishing pole.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "I never want to have fishing equipment\x01",
            "in our house again until Doomsday!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "Don't worry, just take it.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #191
        0x101,
        "#1016FUmmmm, but, uhhhhhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "Oh, it's fine, trust me. It'll be a good\x01",
            "shock for that old fart, I'm sure.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    OP_A2(0x1C33)

    label("loc_3941")

    OP_A2(0x6)

    label("loc_3944")

    Jump("loc_3D3D")

    label("loc_3947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3A3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_39C8")

    ChrTalk(    #193
        0xFE,
        (
            "He's just coming up with a nice excuse\x01",
            "to cover the fact that he wants to go\x01",
            "fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        "I'm not fooled!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A3B")

    label("loc_39C8")


    ChrTalk(    #195
        0xFE,
        (
            "Why should I have to go out to\x01",
            "the lakeshore?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "I'm not interested in going along on\x01",
            "your fishing trip!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3A3B")

    Jump("loc_3D3D")

    label("loc_3A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_3B79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3ADC")

    ChrTalk(    #197
        0xFE,
        (
            "I honestly can't believe it. Kuwano\x01",
            "doesn't know what happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "Talk about being free from worldly\x01",
            "cares. TOO free, if you ask me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B76")

    label("loc_3ADC")


    ChrTalk(    #199
        0xFE,
        (
            "I honestly can't believe it. Kuwano\x01",
            "doesn't know what happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "That's what I get for thinking he came\x01",
            "back because he was worried about me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3B76")

    Jump("loc_3D3D")

    label("loc_3B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_3CC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3C2B")

    ChrTalk(    #201
        0xFE,
        (
            "I'm sure he was off fishing somewhere\x01",
            "without a care in the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "Hmph, really! I swear it's the LEAST\x01",
            "dedicated people who get the most\x01",
            "out of life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CC1")

    label("loc_3C2B")


    ChrTalk(    #203
        0xFE,
        "Everything's gone straight to Gehenna here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "And where's that old lunk?\x01",
            "Off fishing somewhere, I bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "Such a devoted husband!\x01",
            "Mrrgh.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3CC1")

    Jump("loc_3D3D")

    label("loc_3CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_3D3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3CF6")

    ChrTalk(    #206
        0xFE,
        "Kuwano's off fishing again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D3D")

    label("loc_3CF6")


    ChrTalk(    #207
        0xFE,
        "Kuwano's off fishing again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        "It's a disease at this point.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3D3D")

    TalkEnd(0xE)
    Return()

    # Function_12_3063 end

    def Function_13_3D41(): pass

    label("Function_13_3D41")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3E3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3DA4")

    ChrTalk(    #209
        0xFE,
        "The Kingfisher Inn sure is nice!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        "I'm sure Cecile would love it, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E38")

    label("loc_3DA4")


    ChrTalk(    #211
        0xFE,
        "Hey, Cecile.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "Why don't we go out to the Kingfisher\x01",
            "Inn sometime?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "I think you should take a break from\x01",
            "chores and relax sometimes!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_3E38")

    Jump("loc_3EE0")

    label("loc_3E3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_3EE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3E6E")

    ChrTalk(    #214
        0xFE,
        "What happened to the market?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EE0")

    label("loc_3E6E")


    ChrTalk(    #215
        0xFE,
        "What happened to the market?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "I just got back, so I'm completely\x01",
            "lost on what's going on, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_3EE0")

    TalkEnd(0xF)
    Return()

    # Function_13_3D41 end

    def Function_14_3EE4(): pass

    label("Function_14_3EE4")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_4045")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F9D")

    ChrTalk(    #217
        0xFE,
        (
            "Liberl's goods distribution networks have\x01",
            "become all but inoperable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "Moving anything anywhere's become very\x01",
            "difficult, so my husband's been very busy.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_4042")

    label("loc_3F9D")


    ChrTalk(    #219
        0xFE,
        (
            "Liberl's goods distribution networks have\x01",
            "become all but inoperable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "It's a scary thing, when you think about\x01",
            "the need to move food and other\x01",
            "necessities.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4042")

    Jump("loc_46CF")

    label("loc_4045")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_41A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_412E")

    ChrTalk(    #221
        0xFE,
        (
            "Every orbment in the city seems to\x01",
            "have stopped working, all at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        "And nobody has any idea why, either.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "Though I can hardly condone it, I can\x01",
            "understand why some people would\x01",
            "be driven to riot.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_41A3")

    label("loc_412E")


    ChrTalk(    #224
        0xFE,
        (
            "Every orbment in the city seems to have\x01",
            "stopped working, all at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        "And nobody has any idea why, either.\x02",
    )

    CloseMessageWindow()

    label("loc_41A3")

    Jump("loc_46CF")

    label("loc_41A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_4238")

    ChrTalk(    #226
        0xFE,
        (
            "I think I'll go out shopping at the\x01",
            "market today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "They're open for business again, after\x01",
            "all, so I should go show my support!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46CF")

    label("loc_4238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_43B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_42DB")

    ChrTalk(    #228
        0xFE,
        (
            "My husband is very busy with managing\x01",
            "repairs to the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "And Mirano's doing a fantastic job\x01",
            "substituting for him in business deals.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43B4")

    label("loc_42DB")


    ChrTalk(    #230
        0xFE,
        (
            "My husband is very busy with managing\x01",
            "repairs to the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "And Mirano's doing a fantastic job\x01",
            "substituting for him in business deals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "We're doing everything we can to\x01",
            "keep up with Borden's family!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_43B4")

    Jump("loc_46CF")

    label("loc_43B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_4506")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_444F")

    ChrTalk(    #233
        0xFE,
        (
            "My husband's working with Borden to\x01",
            "save the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "Working with our worst rivals...\x01",
            "THIS is what has made Bose what it is!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4503")

    label("loc_444F")


    ChrTalk(    #235
        0xFE,
        (
            "My husband's working with Borden to\x01",
            "save the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "In the face of a crisis, we can work\x01",
            "with even our worst rivals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "Now THIS is the strength\x01",
            "of Bose merchants!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_4503")

    Jump("loc_46CF")

    label("loc_4506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_462A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_457E")

    ChrTalk(    #238
        0xFE,
        (
            "Our Simon was hurt in the market\x01",
            "chaos as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        "We're very lucky it was just a minor injury.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4627")

    label("loc_457E")


    ChrTalk(    #240
        0xFE,
        (
            "Our Simon was also injured during\x01",
            "the attack on the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "Thankfully, it's minor, but I heard\x01",
            "someone was buried under the rubble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        "How terrifying...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_4627")

    Jump("loc_46CF")

    label("loc_462A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_46CF")

    ChrTalk(    #243
        0xFE,
        (
            "Right now, the vision of the merchants\x01",
            "of Bose is filled with the markets of\x01",
            "the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "Everyone's busy trying to create trade\x01",
            "routes to Erebonia.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46CF")

    TalkEnd(0x10)
    Return()

    # Function_14_3EE4 end

    def Function_15_46D3(): pass

    label("Function_15_46D3")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4709")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_4702")
    Call(1, 1)
    Jump("loc_4706")

    label("loc_4702")

    Call(1, 0)

    label("loc_4706")

    Jump("loc_5222")

    label("loc_4709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_4930")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4847")

    ChrTalk(    #245
        0xFE,
        (
            "Even if I wanted to look for alternate\x01",
            "shipping routes, everything, ab-so-lute-ly\x01",
            "everything, is blocked right now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        (
            "At this point, my only option is to get down\x01",
            "to the warehouse and get things out by\x01",
            "sheer muscle power!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "When Simon gets back, I'll have him\x01",
            "put together an estimate.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_492D")

    label("loc_4847")


    ChrTalk(    #248
        0xFE,
        (
            "Even if I wanted to look for alternate\x01",
            "shipping routes, everything, ab-so-lute-ly\x01",
            "everything, is blocked right now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "At this point, my only option is to get down\x01",
            "to the warehouse and get things out by\x01",
            "sheer muscle power!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_492D")

    Jump("loc_5222")

    label("loc_4930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4A7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A08")

    ChrTalk(    #250
        0xFE,
        (
            "With all this strangeness in the city,\x01",
            "and all the trouble with the flights...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        "I declare, it's enough to unsettle anyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "We'll need to be careful, or things\x01",
            "might get really bad.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_4A7C")

    label("loc_4A08")


    ChrTalk(    #253
        0xFE,
        (
            "That reminds me! There's talk about the\x01",
            "floating island in the sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        "As if things weren't sinister enough.\x02",
    )

    CloseMessageWindow()

    label("loc_4A7C")

    Jump("loc_5222")

    label("loc_4A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_4BF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4B29")

    ChrTalk(    #255
        0xFE,
        (
            "Just like I thought! Once the airships\x01",
            "were back in the sky, our trade with\x01",
            "the Empire was a huge success!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        "I bet old Borden is just mortified.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BF4")

    label("loc_4B29")


    ChrTalk(    #257
        0xFE,
        "Ahaha! Everything went perfect this time!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "Just like I thought! Once the airships\x01",
            "were back in the sky, our trade with\x01",
            "the Empire was a huge success!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        "I bet old Borden is just mortified.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_4BF4")

    Jump("loc_5222")

    label("loc_4BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_4E02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4C93")

    ChrTalk(    #260
        0xFE,
        (
            "When will the airship service be\x01",
            "restored... That's the crucial point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "I'm NOT going to let old Borden run\x01",
            "away with everything!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DFF")

    label("loc_4C93")


    ChrTalk(    #262
        0xFE,
        (
            "If possible, I want to beat him to the\x01",
            "punch and make a contract with the\x01",
            "Empire folks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "Ah, but, if the trade resumes too late,\x01",
            "I'll be sitting on warehouses of merchandise\x01",
            "until Aidios comes down!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        (
            "But if I just sit on my tuffet, Borden\x01",
            "will run away with everything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "When will the airship service be\x01",
            "restored... That's the crucial point.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_4DFF")

    Jump("loc_5222")

    label("loc_4E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_5075")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4F21")

    ChrTalk(    #266
        0xFE,
        (
            "I declare, Mayor Maybelle is an inspiration\x01",
            "to young ladies of business everywhere!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        (
            "I'd better learn a thing or two from her\x01",
            "example myself and get back to business!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        (
            "If I let myself get distracted, old Borden\x01",
            "might just pull everything out from under\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5072")

    label("loc_4F21")


    ChrTalk(    #269
        0xFE,
        (
            "Repair work started on the market just\x01",
            "this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "Mayor Maybelle is something else.\x01",
            "She's a spitfire like no other!\x01",
            "Nothing holds her back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        (
            "I'd better learn a thing or two from her\x01",
            "example myself and get back to business!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        (
            "If I let myself get distracted, old Borden\x01",
            "might just pull everything out from under\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_5072")

    Jump("loc_5222")

    label("loc_5075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_50F0")

    ChrTalk(    #273
        0xFE,
        "Oh, Simon, put up with it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "I don't want to hear a grown adult crying\x01",
            "like a child. Aren't you ashamed?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5222")

    label("loc_50F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_5222")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_515E")

    ChrTalk(    #275
        0xFE,
        "Trade with Erebonia's our family's weak point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        "I should talk with Father about it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5222")

    label("loc_515E")


    ChrTalk(    #277
        0xFE,
        "Trade with Erebonia's our family's weak point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "And it's also been something Borden\x01",
            "has been able to do easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        (
            "I should leave the market to Simon for now.\x01",
            "I think I have a plan.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_5222")

    TalkEnd(0x11)
    Return()

    # Function_15_46D3 end

    def Function_16_5226(): pass

    label("Function_16_5226")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_53E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_535B")

    ChrTalk(    #280
        0xFE,
        (
            "Right now the biggest problem is distribution.\x01",
            "We've no way to move our goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        (
            "With carrier trucks and airships down,\x01",
            "we simply can't move a damned thing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "I thought I was ready for any problem,\x01",
            "but apparently not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        (
            "This could end up being even worse\x01",
            "than I thought.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_53E0")

    label("loc_535B")


    ChrTalk(    #284
        0xFE,
        "Right now the biggest problem is distribution.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        (
            "With carrier trucks and airships down,\x01",
            "we simply can't move a damned thing!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53E0")

    Jump("loc_5B28")

    label("loc_53E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_553A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54A6")

    ChrTalk(    #286
        0xFE,
        (
            "It's not just the orbments in town, the\x01",
            "scheduled flights are down too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        (
            "JUST as we made a deal with that\x01",
            "Imperial, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        "Aidios seems to enjoy terrible timing.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_5537")

    label("loc_54A6")


    ChrTalk(    #289
        0xFE,
        (
            "It's not just the orbments in town, the\x01",
            "scheduled flights are down, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "It looks like it could be a while before\x01",
            "it's all sorted out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5537")

    Jump("loc_5B28")

    label("loc_553A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_56C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_55E7")

    ChrTalk(    #291
        0xFE,
        (
            "Ghahaha! My girl Mirano did better than\x01",
            "I expected, getting an Imperial merchant\x01",
            "right in our pocket!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "That's my daughter!\x01",
            "Couldn't be more proud!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56C0")

    label("loc_55E7")


    ChrTalk(    #293
        0xFE,
        (
            "Ghahaha! My girl Mirano did better than\x01",
            "I expected, getting an Imperial merchant\x01",
            "right in our pocket!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        (
            "That's my daughter!\x01",
            "Couldn't be more proud!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "And Borden must be spitting teeth!\x01",
            "What a great day!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_56C0")

    Jump("loc_5B28")

    label("loc_56C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_5850")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_5760")

    ChrTalk(    #296
        0xFE,
        (
            "I've decided to leave the business side\x01",
            "of things entirely to Mirano.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "I can only hope she finds a way to strike\x01",
            "a blow to Borden.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_584D")

    label("loc_5760")


    ChrTalk(    #298
        0xFE,
        (
            "I've been so busy with the repairs lately,\x01",
            "I can't find any time to run the business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "So I've decided to leave the business side\x01",
            "of things entirely to Mirano.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        (
            "I can only hope she finds a way to strike\x01",
            "a blow to Borden.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_584D")

    Jump("loc_5B28")

    label("loc_5850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_5999")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_58CD")

    ChrTalk(    #301
        0xFE,
        (
            "I've worked with Borden to get the\x01",
            "repairs started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        "We need to arrange for more materials soon...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5996")

    label("loc_58CD")


    ChrTalk(    #303
        0xFE,
        (
            "I've worked with Borden to get the\x01",
            "repairs started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        (
            "We could only get together enough\x01",
            "materials for the moment, so they'll\x01",
            "run out soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        "We need to arrange for more materials soon...\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_5996")

    Jump("loc_5B28")

    label("loc_5999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_5B28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_5A1D")

    ChrTalk(    #306
        0xFE,
        (
            "Trade with the Empire will be key from\x01",
            "here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        (
            "I've got to come up with some way to\x01",
            "counter Borden!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B28")

    label("loc_5A1D")


    ChrTalk(    #308
        0xFE,
        (
            "With the non-aggression pact all done\x01",
            "and dusted, trade with the Empire will\x01",
            "be key from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "But Borden's had acquaintances in Erebonia\x01",
            "since Aidios gave Man the Treasures!\x01",
            "It's his best business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xFE,
        "We need to figure out a way around that...\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_5B28")

    TalkEnd(0x12)
    Return()

    # Function_16_5226 end

    def Function_17_5B2C(): pass

    label("Function_17_5B2C")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_5D6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_5BCE")

    ChrTalk(    #311
        0xFE,
        (
            "The question of when the airships will run\x01",
            "again is a real problem for business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xFE,
        (
            "Even Miss Mirano's worrying, which\x01",
            "is pretty rare.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D67")

    label("loc_5BCE")


    ChrTalk(    #313
        0xFE,
        (
            "The question of when the airships will run\x01",
            "again is a real problem for business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xFE,
        (
            "If it takes too long, we'll be left with a\x01",
            "lot of goods which we won't be able to\x01",
            "sell off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xFE,
        (
            "On the other hand, though, this MIGHT be\x01",
            "our chance to shine while everyone else\x01",
            "plays it safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        (
            "Take the risk and the potential reward,\x01",
            "or avoid the risk...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xFE,
        (
            "Even Miss Mirano's worrying, which\x01",
            "is pretty rare.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_5D67")

    Jump("loc_5F06")

    label("loc_5D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_5E58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_5D9D")

    ChrTalk(    #318
        0xFE,
        "Gyah! My neck is KILLING me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E55")

    label("loc_5D9D")


    ChrTalk(    #319
        0xFE,
        (
            "Ouch! The injury I got during the\x01",
            "market attack still smarts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xFE,
        (
            "Honestly, I should be thankful I got\x01",
            "away with only this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xFE,
        (
            "...but what am I supposed to say?\x01",
            "It hurts!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_5E55")

    Jump("loc_5F06")

    label("loc_5E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_5F06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_5E77")

    ChrTalk(    #322
        0xFE,
        "O-Owwww!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F06")

    label("loc_5E77")


    ChrTalk(    #323
        0xFE,
        "At-cha-cha...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xFE,
        (
            "M-Miss Mirano. I appreciate you treating\x01",
            "me, but, uh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0xFE,
        "Could you, um, maybe be a bit more gen--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xFE,
        "OW OW OW!\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_5F06")

    TalkEnd(0x13)
    Return()

    # Function_17_5B2C end

    SaveToFile()

Try(main)
