from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4222   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4222.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Mayor Klaus',                          # 9
        'Lila',                                 # 10
        'Mayor Maybelle',                       # 11
        'Dean Collins',                         # 12
        'Shea',                                 # 13
        'Zin',                                  # 14
        'Libra',                                # 15
        'Primrose',                             # 16
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
        'ED6_DT07/CH02350 ._CH',             # 00
        'ED6_DT07/CH02370 ._CH',             # 01
        'ED6_DT07/CH02360 ._CH',             # 02
        'ED6_DT07/CH02600 ._CH',             # 03
        'ED6_DT07/CH02620 ._CH',             # 04
        'ED6_DT07/CH02540 ._CH',             # 05
        'ED6_DT07/CH00070 ._CH',             # 06
        'ED6_DT07/CH02460 ._CH',             # 07
        'ED6_DT07/CH02230 ._CH',             # 08
        'ED6_DT07/CH02240 ._CH',             # 09
        'ED6_DT07/CH01100 ._CH',             # 0A
        'ED6_DT07/CH01350 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH02350P._CP',             # 00
        'ED6_DT07/CH02370P._CP',             # 01
        'ED6_DT07/CH02360P._CP',             # 02
        'ED6_DT07/CH02600P._CP',             # 03
        'ED6_DT07/CH02620P._CP',             # 04
        'ED6_DT07/CH02540P._CP',             # 05
        'ED6_DT07/CH00070P._CP',             # 06
        'ED6_DT07/CH02460P._CP',             # 07
        'ED6_DT07/CH02230P._CP',             # 08
        'ED6_DT07/CH02240P._CP',             # 09
        'ED6_DT07/CH01100P._CP',             # 0A
        'ED6_DT07/CH01350P._CP',             # 0B
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
        TalkScenaIndex      = 6,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        TalkScenaIndex      = 5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -139550,
        Z                   = 4000,
        Y                   = 9480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -78950,
        Z                   = 0,
        Y                   = 5960,
        Direction           = 359,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_358",          # 01, 1
        "Function_2_362",          # 02, 2
        "Function_3_378",          # 03, 3
        "Function_4_3D9",          # 04, 4
        "Function_5_59A",          # 05, 5
        "Function_6_5A7",          # 06, 6
        "Function_7_EE3",          # 07, 7
        "Function_8_EF0",          # 08, 8
        "Function_9_187E",         # 09, 9
        "Function_10_2537",        # 0A, 10
        "Function_11_2572",        # 0B, 11
        "Function_12_2FAE",        # 0C, 12
        "Function_13_3588",        # 0D, 13
        "Function_14_3735",        # 0E, 14
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_218")
    OP_A3(0x3FA)
    Event(0, 9)

    label("loc_218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_226")
    OP_A3(0x3FB)
    Event(0, 12)

    label("loc_226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_234")
    OP_A3(0x3FC)
    Event(0, 14)

    label("loc_234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_298")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, -28870, 0, 53540, 270)
    SetChrPos(0x9, -28040, 0, 54950, 211)
    SetChrPos(0xB, -83970, 0, -52980, 270)
    SetChrPos(0x8, -86020, 0, -52980, 90)

    label("loc_298")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (106, "loc_2A8"),
        (101, "loc_2CA"),
        (SWITCH_DEFAULT, "loc_2E0"),
    )


    label("loc_2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C7")
    OP_A2(0x63F)
    Event(0, 11)

    label("loc_2C7")

    Jump("loc_2E0")

    label("loc_2CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DD")
    OP_A2(0x640)
    Event(0, 13)

    label("loc_2DD")

    Jump("loc_2E0")

    label("loc_2E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30A")
    SetChrChipByIndex(0x0, 7)
    SetChrChipByIndex(0x1, 8)
    SetChrChipByIndex(0x138, 9)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_30A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_319")
    SetChrFlags(0xE, 0x80)
    Jump("loc_357")

    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_328")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_357")

    label("loc_328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_337")
    SetChrFlags(0xE, 0x80)
    Jump("loc_357")

    label("loc_337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_346")
    SetChrFlags(0xE, 0x80)
    Jump("loc_357")

    label("loc_346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_350")
    Jump("loc_357")

    label("loc_350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_357")

    label("loc_357")

    Return()

    # Function_0_20A end

    def Function_1_358(): pass

    label("Function_1_358")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_358 end

    def Function_2_362(): pass

    label("Function_2_362")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_377")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_362")

    label("loc_377")

    Return()

    # Function_2_362 end

    def Function_3_378(): pass

    label("Function_3_378")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "Time to clean the rooms.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "It's been hectic preparing\x01",
            "for so many guests tonight!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_378 end

    def Function_4_3D9(): pass

    label("Function_4_3D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_3E6")
    Jump("loc_596")

    label("loc_3E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_495")

    ChrTalk(    #2
        0xFE,
        (
            "Castle Blueprints... The\x01",
            "Seven Treasures... Chronicles\x01",
            "of the Hundred Days War...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "The Intelligence Division\x01",
            "finally sent back all the\x01",
            "books they borrowed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_596")

    label("loc_495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_49F")
    Jump("loc_596")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_4A9")
    Jump("loc_596")

    label("loc_4A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_510")

    ChrTalk(    #4
        0xFE,
        (
            "Hmm? Seems the castle blueprints\x01",
            "are missing too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "What do they need with those?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_596")

    label("loc_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_596")

    ChrTalk(    #6
        0xFE,
        (
            "What are those people at the \x01",
            "Intelligence Division up to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Taking important documents\x01",
            "without official permission...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_596")

    TalkEnd(0xFE)
    Return()

    # Function_4_3D9 end

    def Function_5_59A(): pass

    label("Function_5_59A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A6")
    Call(0, 6)

    label("loc_5A6")

    Return()

    # Function_5_59A end

    def Function_6_5A7(): pass

    label("Function_6_5A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE2")
    OP_A2(0x63B)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -85860, 0, -55170, 0)
    SetChrPos(0x102, -84960, 0, -55250, 0)
    OP_6D(-85030, 450, -53200, 1000)

    ChrTalk(    #8
        0x8,
        (
            "#600FAh, Joshua. Estelle. You made\x01",
            "it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xB,
        "#780FIt's been quite a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#000F...Dean Collins?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        (
            "#010FYou were invited to the banquet\x01",
            "as well, sir?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xB,
        (
            "#780FI just arrived today via\x01",
            "airship from Ruan.\x02\x03",

            "...A little mayoral birdie told\x01",
            "me you two won the tournament.\x02\x03",

            "Jill and everyone else will be\x01",
            "so happy to hear it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#000FHeh heh...thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        (
            "#010FWe couldn't have done it by\x01",
            "ourselves, though.\x02\x03",

            "At any rate, I had no idea\x01",
            "we'd be seeing you here,\x01",
            "Dean Collins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#600FDean Collins is a member of the\x01",
            "Royal Assembly, and a man of\x01",
            "great respect in Liberl.\x02\x03",

            "It's only fitting he be given\x01",
            "a seat at this banquet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xB,
        (
            "#780FA man of great respect, he says...\x01",
            "You flatter me, Mayor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#000F...What's the Royal Assembly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        (
            "#010FIt's a meeting held once per year\x01",
            "to address matters affecting the\x01",
            "kingdom.\x02\x03",

            "The queen, mayors of every city and other \x01",
            "representatives all come together to try\x01",
            "solving various problems of state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#000FWow. Sounds big.\x02\x03",

            "So all of those guys have been\x01",
            "invited here tonight, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xB,
        (
            "#780FNo... I'd say only about half.\x02\x03",

            "Her Majesty is still ill and\x01",
            "General Morgan is away on\x01",
            "official military business.\x02\x03",

            "And Mayor Dalmore of Ruan was\x01",
            "arrested in that nasty affair.\x02\x03",

            "And Professor Russell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#600FHe is a bit too entrenched in\x01",
            "too many unknowns right now.\x02\x03",

            "We don't know how true all this talk is of\x01",
            "the Royal Guardsmen being involved in some\x01",
            "underground terrorist organization.\x02\x03",

            "...It's hardly the time to be\x01",
            "holding a feast at all, if you\x01",
            "ask me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#000F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        "#010F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xB,
        (
            "#780FWell, we can use this chance\x01",
            "to see where Duke Dunan stands\x01",
            "on all of these issues.\x02\x03",

            "We need his permission to have\x01",
            "an audience with Her Majesty,\x01",
            "regardless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "#600FYes. That's the biggest issue\x01",
            "here, without a doubt.\x02\x03",

            "Barring us from seeing Her Majesty\x01",
            "is the height of idiocy and mis-\x01",
            "management!\x02\x03",

            "I would like to pay my respects\x01",
            "to Princess Klaudia, as well,\x01",
            "but it's the same story...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#000FPrincess Klaudia's...the queen's\x01",
            "granddaughter...right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        "#010FDoes she live here in the castle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#600FNo, it's my understanding her\x01",
            "actual residence is elsewhere.\x02\x03",

            "But I'm told she's come to the\x01",
            "capital, as of a few days ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#000FShe's...here, then?\x02\x03",

            "I'd really love to meet her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xB,
        "#780FI'm sure you'll have a chance.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_EE2")

    Return()

    # Function_6_5A7 end

    def Function_7_EE3(): pass

    label("Function_7_EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EEF")
    Call(0, 8)

    label("loc_EEF")

    Return()

    # Function_7_EE3 end

    def Function_8_EF0(): pass

    label("Function_8_EF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187D")
    OP_A2(0x63A)
    EventBegin(0x0)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -29280, 0, 55240, 135)
    SetChrPos(0x102, -30310, 0, 54780, 135)
    OP_6D(-28840, 0, 54560, 1000)

    ChrTalk(    #31
        0x101,
        "#000FMayor Maybelle?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x102,
        "#010FAnd Lila!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x9,
        "#620FJoshua! Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xA,
        (
            "#610FAh, here at last!\x02\x03",

            "I kept wondering when you'd get\x01",
            "here. I was practically counting\x01",
            "the seconds...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#000FSo you were invited here too, Mayor?\x02\x03",

            "...H-Hey, wait... You were waiting\x01",
            "for us? How did you know we were\x01",
            "coming?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xA,
        (
            "#610FI heard from Mayor Klaus.\x02\x03",

            "I heard about a pair of children who entered the\x01",
            "tournament, won its championship, and were \x01",
            "invited to a grand royal banquet in the castle.\x02\x03",

            "If I'd known, I would have\x01",
            "canceled my appointments and\x01",
            "come to cheer you on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        (
            "#620FBegging your pardon, ma'am...\x02\x03",

            "But that would have been quite\x01",
            "impossible, given the circum-\x01",
            "stances...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xA,
        (
            "#610FYes, yes, I'm aware. I'm trying\x01",
            "to be polite!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#000FHa ha ha! Don't worry. I know\x01",
            "how busy you must be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xA,
        (
            "#610FI'm sure the queen has no time to waste\x01",
            "at a banquet, what with everything else\x01",
            "going on. What is Duke Dunan thinking?!\x02\x03",

            "That captain was so stubborn about\x01",
            "inviting me, too... I had no real\x01",
            "choice but to accept!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        "#010FDo you mean Captain Amalthea?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        (
            "#610FYes, that's her.\x02\x03",

            "Her words were polite enough, but she\x01",
            "gave me an evil eye while she spoke\x01",
            "them. I dared not refuse her request!\x02\x03",

            "I haven't heard from General\x01",
            "Morgan in quite some time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#000FWait, does that mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#010F...You haven't heard any word\x01",
            "from the Haken Gate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        (
            "#610F'The general is unavailable'\x01",
            "is the longest message I've\x01",
            "been able to wring from them.\x02\x03",

            "It would seem he's busy with \x01",
            "these 'anti-terrorist counter-\x01",
            "measures,' or what-have-you.\x02\x03",

            "I had hoped he'd be in attendance\x01",
            "at this banquet tonight...\x02\x03",

            "But I guess he couldn't pull\x01",
            "himself away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#000FHmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        (
            "#010FWhat do you think about all of\x01",
            "this, Mayor?\x02\x03",

            "Putting mayors from every city\x01",
            "in the same place, at a time\x01",
            "like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xA,
        (
            "#610FWell...\x02\x03",

            "If the queen were to be in attendance,\x01",
            "I would expect some announcement of no\x01",
            "small importance...\x02\x03",

            "But as it is, this feels like\x01",
            "the duke has too much time\x01",
            "on his greasy, chubby hands.\x02\x03",

            "He's letting this position of\x01",
            "royal proxy go to his head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#000FThat sounds about right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x102,
        (
            "#010FBut there might still be some\x01",
            "kind of official announcement,\x01",
            "don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        (
            "#610FWell, whatever may come of the\x01",
            "night, the grand chef here is\x01",
            "the best in all the kingdom.\x02\x03",

            "I plan to enjoy the dinner, pay\x01",
            "my respects to Her Majesty, and\x01",
            "return to Bose post-haste.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_187D")

    Return()

    # Function_8_EF0 end

    def Function_9_187E(): pass

    label("Function_9_187E")

    EventBegin(0x0)
    SetChrPos(0x101, -52050, 0, 2040, 0)
    SetChrPos(0x102, -52050, 0, 2040, 0)
    SetChrPos(0x108, -52050, 0, 2040, 0)
    SetChrPos(0xC, -52050, 0, 2040, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x40)
    OP_69(0x102, 0x0)
    OP_6A(0x102)

    def lambda_18DE():
        OP_8E(0xFE, 0xFFFECE9C, 0x0, 0x884, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_18DE)
    Sleep(500)

    def lambda_18FE():
        OP_8E(0xFE, 0xFFFECE9C, 0x0, 0x884, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18FE)
    Sleep(500)

    def lambda_191E():
        OP_8E(0xFE, 0xFFFECE9C, 0x0, 0x884, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_191E)
    Sleep(500)

    def lambda_193E():
        OP_8E(0xFE, 0xFFFECE9C, 0x0, 0x884, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_193E)
    WaitChrThread(0xC, 0x1)

    def lambda_195E():
        OP_8E(0xFE, 0xFFFECB86, 0x0, 0x1CDE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_195E)
    WaitChrThread(0x102, 0x1)

    def lambda_197E():
        OP_8E(0xFE, 0xFFFEC7F8, 0x0, 0x159A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_197E)
    WaitChrThread(0x101, 0x1)

    def lambda_199E():
        OP_8E(0xFE, 0xFFFECD2A, 0x0, 0x1554, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_199E)
    WaitChrThread(0x108, 0x1)

    def lambda_19BE():
        OP_8E(0xFE, 0xFFFECA50, 0x0, 0x1162, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_19BE)
    WaitChrThread(0xC, 0x1)
    Sleep(200)
    OP_8E(0xC, 0xFFFEC668, 0x0, 0x1C52, 0x7D0, 0x0)
    TurnDirection(0xC, 0x102, 0)

    ChrTalk(    #52
        0xC,
        (
            "This is the room where\x01",
            "you'll be staying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xC,
        "Please, go on in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#000FO-Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        "#010FHoly Stregas!\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0xA)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0xA)
    Sleep(500)
    OP_43(0x108, 0x1, 0x0, 0xA)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    ClearMapFlags(0x1)
    Fade(1000)
    OP_6D(-79120, 0, 55910, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x108, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xC, -80040, 0, 50510, 0)
    SetChrPos(0x101, -80880, 0, 53000, 315)
    SetChrPos(0x102, -79650, 0, 53710, 270)
    SetChrPos(0x108, -78830, 0, 52390, 0)
    Sleep(1000)

    ChrTalk(    #56
        0x101,
        "#000FOh, WOW...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x102,
        (
            "#010FI never imagined we'd ever stay\x01",
            "in a place like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x108,
        (
            "#070FNiiiice. This will make a good\x01",
            "story for later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xC,
        (
            "I believe there is still some\x01",
            "time before the party.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1C1C():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C1C)

    def lambda_1C2A():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C2A)

    def lambda_1C38():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1C38)
    OP_6D(-79790, 0, 52600, 1000)

    ChrTalk(    #60
        0xC,
        (
            "You are free to explore the\x01",
            "castle, but the security areas\x01",
            "are off limits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xC,
        (
            "I ask that you refrain from\x01",
            "entering those areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#000FUmm...can you be a little\x01",
            "more specific?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xC,
        (
            "Most significantly, the Royal\x01",
            "Keep, where the queen resides.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xC,
        (
            "It is a small palace of sorts,\x01",
            "built on the Garden Terrace\x01",
            "on the roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#000FGarden Terrace...?\x01",
            "That sounds nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xC,
        (
            "Ha ha... The terrace is where Her\x01",
            "Majesty greets the people of Grancel\x01",
            "from during the birthday festivities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xC,
        (
            "So, you cannot go into the Royal\x01",
            "Keep itself, but you may visit the\x01",
            "Garden Terrace if you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xC,
        "As for the other restricted areas...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xC,
        (
            "There's the Royal Guard Room\x01",
            "and also the Treasury, I believe.\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0x108, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    ChrTalk(    #70
        0x102,
        "#010FThe Royal Guard Room...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x108,
        (
            "#070FI guess they're still wanted\x01",
            "for questioning about all that\x01",
            "terrorist stuff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xC,
        "Y-Yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xC,
        (
            "The Intelligence Division is\x01",
            "currently occupying it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xC,
        (
            "Entrance is restricted, so\x01",
            "please abide by the rules.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        (
            "#010FUnderstood.\x02\x03",

            "By the way, what are the others\x01",
            "who were invited doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xC,
        "They've already arrived.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xC,
        (
            "I imagine they're relaxing\x01",
            "in their respective rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        "#010FAll right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#000FSo Mayor Klaus is here, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xC,
        (
            "Oh, yes.\x01",
            "He arrived some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xC,
        (
            "Now, if you'll excuse me,\x01",
            "I'll be off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xC,
        (
            "If you need anything else, please\x01",
            "contact the first floor waiting room.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)

    def lambda_21AF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_21AF)
    OP_8E(0xC, 0xFFFEC6F4, 0x0, 0xBC3E, 0x3E8, 0x0)
    SetChrFlags(0xC, 0x4)

    ChrTalk(    #83
        0x101,
        "#000FNow, then...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    TurnDirection(0x102, 0x101, 400)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #84
        "\x07\x05Estelle and Joshua exchanged a look that went unnoticed by Zin.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    def lambda_2259():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2259)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #85
        0x101,
        (
            "#000F...Hey, Zin?\x02\x03",

            "We want to go and walk around\x01",
            "the castle for a little bit...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22C3():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_22C3)

    ChrTalk(    #86
        0x102,
        (
            "#010FWe'll be back in time for\x01",
            "the party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x108,
        (
            "#070FHuh... It must be nice to be so young.\x01",
            "I'm worn out after the tournament.\x02\x03",

            "No problem. Have fun.\x02\x03",

            "Me, I'm going to kick back and relax\x01",
            "in this oh-so-luxurious room.\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(-79060, 0, 5580, 0)
    RemoveParty(0x7, 0xFF)
    SetChrPos(0x101, -79060, 0, 9840, 0)
    SetChrPos(0x102, -79060, 0, 9840, 0)

    def lambda_23EA():
        OP_8E(0xFE, 0xFFFECE2E, 0x0, 0x15B8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23EA)
    Sleep(600)

    def lambda_240A():
        OP_8E(0xFE, 0xFFFECA5A, 0x0, 0x190A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_240A)
    WaitChrThread(0x101, 0x1)

    def lambda_242A():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_242A)
    WaitChrThread(0x102, 0x1)

    def lambda_243D():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_243D)

    ChrTalk(    #88
        0x101,
        (
            "#000FWe need to get as much done as\x01",
            "we can before the party starts.\x02\x03",

            "First, Julia told us that we have\x01",
            "to talk to the head maid, Hilda.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x102,
        (
            "#010FI'd like to say hello to the\x01",
            "other invitees, too.\x02\x03",

            "We likely know most of them.\x02",
        )
    )

    CloseMessageWindow()
    OP_6A(0x0)
    ClearMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_9_187E end

    def Function_10_2537(): pass

    label("Function_10_2537")

    OP_8E(0xFE, 0xFFFECB5E, 0x0, 0x1CA2, 0xBB8, 0x0)

    def lambda_2551():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2551)
    OP_8E(0xFE, 0xFFFECB68, 0x0, 0x2602, 0xBB8, 0x0)
    Return()

    # Function_10_2537 end

    def Function_11_2572(): pass

    label("Function_11_2572")

    EventBegin(0x0)
    OP_6D(-80130, 0, 51090, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    AddParty(0x7, 0xFF)
    SetChrPos(0x101, -80670, 0, 51310, 270)
    SetChrPos(0x102, -79770, 0, 50560, 270)
    SetChrPos(0x108, -87580, 0, 52200, 90)
    OP_6D(-83020, 0, 52310, 2000)

    ChrTalk(    #90
        0x108,
        (
            "#070FHey, guys.\x01",
            "Talk about being late.\x02\x03",

            "The party's about to start,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2651():
        OP_8E(0xFE, 0xFFFEBD4E, 0x0, 0xCDA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2651)
    Sleep(300)

    def lambda_2671():
        OP_6D(-86640, 0, 52720, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2671)

    def lambda_2689():
        OP_8E(0xFE, 0xFFFEBD4E, 0x0, 0xCDA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2689)
    WaitChrThread(0x101, 0x1)

    def lambda_26A9():
        OP_8E(0xFE, 0xFFFEB042, 0x0, 0xD0D4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26A9)
    WaitChrThread(0x102, 0x1)

    def lambda_26C9():
        OP_8E(0xFE, 0xFFFEAFF2, 0x0, 0xCB48, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_26C9)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x108, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #91
        0x101,
        (
            "#000FSorry...\x02\x03",

            "We got so caught up in sightseeing\x01",
            "that we lost track of time.\x02\x03",

            "Plus, we also talked to all\x01",
            "of the mayors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x108,
        (
            "#070FHuh...\x01",
            "Well, aren't we well-connected?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x102,
        (
            "#010FWe're close friends with the\x01",
            "mayor of Rolent.\x02\x03",

            "Plus, we've met the other mayors\x01",
            "in the course of our travels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x108,
        (
            "#070FAhh, I see.\x02\x03",

            "I guess your work as bracers has\x01",
            "caused you to meet quite a few\x01",
            "big shots.\x02\x03",

            "You two sure get around\x01",
            "for Junior Bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#000FHeh heh...\x01",
            "Yeah, you might say that.\x02\x03",

            "Have you done any bracer assignments\x01",
            "since we came to Grancel?\x02\x03",

            "I guess it's not all that different\x01",
            "in other countries, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x108,
        (
            "#070FRight. For a full-fledged bracer,\x01",
            "nationality isn't an issue when\x01",
            "it comes to your work.\x02\x03",

            "The prelim fights and legal procedures\x01",
            "at the embassy kept me too busy to get\x01",
            "any actual work done, though.\x02\x03",

            "But hey, there are four other bracers\x01",
            "on duty, too, which isn't so bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        (
            "#010FNormally, that would be enough\x01",
            "to handle most cases, I'd imagine.\x02\x03",

            "But with all of them concentrated in\x01",
            "Grancel, that must make it tough to\x01",
            "handle any cases in other regions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x108,
        (
            "#070FHa ha ha...\x01",
            "Yeah, could be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#000FUgh... I feel like a goose just\x01",
            "walked over my grave...\x02\x03",

            "I wonder what's going on with\x01",
            "Schera, back in Rolent...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x108,
        (
            "#070F'Schera'?\x01",
            "You talking about Scherazard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#000F...You know her?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x102,
        (
            "#010FShe's our mentor, and she's\x01",
            "been a close friend for ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x108,
        (
            "#070FOhh, okay. Makes sense.\x02\x03",

            "I met her a long time ago, when a\x01",
            "case brought her to the Republic.\x02\x03",

            "She was fortunate to have a good\x01",
            "master working with her from such\x01",
            "a young age.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D18():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D18)

    def lambda_2D26():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D26)
    Sleep(1000)

    ChrTalk(    #104
        0x101,
        "#000F(Her master...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        "#010F(Yeah, probably Dad.)\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0xC, -80120, 0, 48440, 315)

    def lambda_2DCF():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2DCF)

    def lambda_2DDD():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2DDD)

    def lambda_2DEB():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2DEB)

    ChrTalk(    #106
        0xC,
        (
            "...Please, pardon me. The table\x01",
            "for the dinner party has been set.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xC,
        "May I show you the way?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x108,
        (
            "#070FSure. I was getting bored\x01",
            "with waiting anyhow.\x02\x03",

            "All right...\x01",
            "Wanna go and eat fancy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#000FSure.\x01",
            "That fight left me starving.\x02\x03",

            "Let's go dig in! ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_8C(0x102, 315, 400)
    Sleep(1000)

    ChrTalk(    #110
        0x102,
        (
            "#010FCome on, you two...\x02\x03",

            "For once, I think it would be best if\x01",
            "you tried to keep up some appearance\x01",
            "of having table manners...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4251   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_2572 end

    def Function_12_2FAE(): pass

    label("Function_12_2FAE")

    EventBegin(0x0)
    OP_6D(-79320, 0, 55910, 0)
    RemoveParty(0x7, 0xFF)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -79660, 0, 56600, 192)
    SetChrPos(0x101, -80390, 0, 55080, 23)
    SetChrPos(0x102, -78690, 0, 55240, 315)

    ChrTalk(    #111
        0xD,
        (
            "#070FMan, I've heard some pretty unbelievable\x01",
            "conversations in my time, but that was\x01",
            "something else.\x02\x03",

            "I mean, I'm a foreigner after all so\x01",
            "it's not that big of a deal for me, but\x01",
            "for you guys, I bet that was huge news.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#000FO-Of course it was!\x02\x03",

            "I can't believe things have\x01",
            "gone this far already...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xD,
        "#070FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        (
            "#000FErr...n-never mind.\x02\x03",

            "But really...what a shame.\x02\x03",

            "That food was so amazing, and it practically\x01",
            "melted in the mouth... Couldn't tell what\x01",
            "that last flavor was, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x102,
        (
            "#010FHa ha... Understandable enough.\x02\x03",

            "But anyway... Did you want to go\x01",
            "for a walk to work off some of\x01",
            "that rich food, Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#000F...?\x02\x03",

            "Oh! Yeah, sure!\x02\x03",

            "Yeah, I could go for a little\x01",
            "bit of fresh air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xD,
        (
            "#070F*sigh* You just played tourist a\x01",
            "little while ago, and now you want\x01",
            "to take an after-dinner walk...?\x02\x03",

            "I sure don't get it.\x01",
            "Must be a local thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#000FHa ha... I think you're exaggerating\x01",
            "a little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x102,
        (
            "#010FYou haven't gone out to\x01",
            "take in the sights?\x02\x03",

            "There is a lot of historic architecture\x01",
            "around here, you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xD,
        (
            "#070FIf the mood hits me, I may\x01",
            "still give it a shot.\x02\x03",

            "On the other hand, the kitchen may\x01",
            "still have some food left over...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        (
            "#000FYou've gotta be kidding.\x01",
            "You're still hungry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xD,
        (
            "#070FIf you had a blade to my throat,\x01",
            "my dying wish would be for some\x01",
            "liquor and a snack.\x02\x03",

            "I might go and hunt up a bar\x01",
            "or something in a little bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4A, 0x4, 0x2)
    OP_28(0x4A, 0x4, 0x4)
    OP_28(0x4A, 0x1, 0x1)
    OP_28(0x4A, 0x1, 0x2)
    OP_28(0x4A, 0x1, 0x4)
    EventEnd(0x0)
    Return()

    # Function_12_2FAE end

    def Function_13_3588(): pass

    label("Function_13_3588")

    EventBegin(0x0)
    OP_6D(-79060, 0, 5580, 0)
    SetChrPos(0x101, -79060, 0, 9840, 0)
    SetChrPos(0x102, -79060, 0, 9840, 0)

    def lambda_35C3():
        OP_8E(0xFE, 0xFFFECE2E, 0x0, 0x15B8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35C3)
    Sleep(600)

    def lambda_35E3():
        OP_8E(0xFE, 0xFFFECA5A, 0x0, 0x190A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_35E3)
    WaitChrThread(0x101, 0x1)

    def lambda_3603():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3603)
    WaitChrThread(0x102, 0x1)

    def lambda_3616():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3616)

    ChrTalk(    #123
        0x101,
        (
            "#000F*sigh*\x01",
            "Things have gotten serious.\x02\x03",

            "We really have to find a way to\x01",
            "get in to see Her Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x102,
        (
            "#010FFirst things first: We go talk to the\x01",
            "head maid, Hilda, like we promised.\x02\x03",

            "She probably knows a way for us\x01",
            "to speak directly to the queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        "#000FFine by me.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_13_3588 end

    def Function_14_3735(): pass

    label("Function_14_3735")

    EventBegin(0x0)
    OP_6D(-79860, 0, 50720, 0)
    SetChrPos(0x101, -80040, 0, 48610, 0)
    SetChrPos(0x102, -80040, 0, 48610, 0)
    SetChrPos(0x108, -80040, 0, 48610, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x108, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_37A2():
        OP_6D(-79660, 0, 55360, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_37A2)

    def lambda_37BA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_37BA)

    def lambda_37CC():
        OP_8E(0xFE, 0xFFFEC762, 0x0, 0xDA52, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_37CC)
    Sleep(500)

    def lambda_37EC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37EC)

    def lambda_37FE():
        OP_8E(0xFE, 0xFFFEC640, 0x0, 0xD426, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37FE)
    Sleep(500)

    def lambda_381E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_381E)

    def lambda_3830():
        OP_8E(0xFE, 0xFFFECAC8, 0x0, 0xD3CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3830)
    WaitChrThread(0x108, 0x1)
    OP_8C(0x108, 180, 400)

    ChrTalk(    #126
        0x108,
        (
            "#070F*sigh*...\x02\x03",

            "Looks like we managed to convince her,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #127
        0x101,
        (
            "#000FWha...!\x02\x03",

            "Zin, aren't you drunk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x108,
        (
            "#070FI was ACTING drunk...\x02\x03",

            "I haven't had a single drop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#000FNo way! Your face had\x01",
            "even gone all red...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x102,
        (
            "#010FHe focused on making his blood \x01",
            "circulate better, which made it\x01",
            "look like he was intoxicated...\x02\x03",

            "It's done with some kind of \x01",
            "Eastern martial arts breathing\x01",
            "exercise, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x108,
        (
            "#070FHuh! I'm surprised you're\x01",
            "familiar with it.\x02\x03",

            "But hey, you seemed to be in a\x01",
            "tight spot, so I figured I'd\x01",
            "distract everyone.\x02\x03",

            "Nice, huh? Saved your bacon,\x01",
            "as the saying goes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#000FHmph...\x01",
            "You are an evil, evil man, Zin.\x02\x03",

            "Okay, sure, you did help us out,\x01",
            "but you also surprised the hell\x01",
            "out of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x108,
        (
            "#070FHa ha... Sorry about that.\x02\x03",

            "So, what's the story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        (
            "#000F???\x02\x03",

            "What story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x108,
        (
            "#070FI would've thought it'd be obvious.\x02\x03",

            "The 'story' of you meeting\x01",
            "with the queen.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #136
        0x101,
        (
            "#000FWhoa, wait, WHAT?!\x02\x03",

            "H-H-How did you--?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x102,
        (
            "#010FDid Elnan tell you something\x01",
            "about this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x108,
        (
            "#070FActually, I couldn't get him\x01",
            "to tell me anything.\x02\x03",

            "But now I know anyway,\x01",
            "don't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        "#000F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x102,
        (
            "#010FWithout prior knowledge, there's no\x01",
            "way you could have just guessed...\x02\x03",

            "So how much do you really know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x108,
        (
            "#070FHa ha...\x02\x03",

            "I guess it's finally time to\x01",
            "show you this.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x108, 0xFFFEC6D6, 0x0, 0xD6B0, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #142
        "\x07\x05Zin produced a letter from his pocket and handed it to Estelle and Joshua.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x108, 0xFFFEC762, 0x0, 0xDA52, 0x7D0, 0x0)

    ChrTalk(    #143
        0x101,
        "#000FWhat's this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x102,
        "#010FI know this handwriting...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x108,
        (
            "#070FWell, don't just stand there.\x01",
            "Read it.\x02\x03",

            "It'll explain a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        "#000FO-Okay...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #147
        (
            "\x07\x05Estelle and Joshua began to\x01",
            "read the letter's contents.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #148
        (
            "\x07\x05'Dear Zin Vathek,\x01",
            "I hope this letter finds you well.\x01",
            "I know I've been out of touch.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #149
        (
            "\x07\x05'I'm in a hurry, so I hope you'll\x01",
            "pardon my bluntness.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #150
        (
            "\x07\x05'My work concerning the jaegers\x01",
            "is leading me into Imperial territory.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #151
        (
            "\x07\x05'However, due to the fact that unusual forces\x01",
            "seem to be influencing matters inside Liberl,\x01",
            "I feel uneasy being absent for so long.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #152
        "\x07\x05'This is why I must ask a favor of you.'\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #153
        (
            "\x07\x05'Could I persuade you to come to Liberl\x01",
            "and help out, if they need it?'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #154
        (
            "\x07\x05'Since you haven't been to Liberl before, perhaps\x01",
            "you could think of it as recreational trip.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #155
        (
            "\x07\x05'There is a Martial Arts Competition before the\x01",
            "Queen's Birthday Celebration, and foreigners\x01",
            "can participate. It would make fine camouflage.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #156
        (
            "\x07\x05'I realize that this is sudden, but if you can\x01",
            "do it, I would be most grateful.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #157
        (
            "\x07\x05'I'm intending to return to Liberl before the\x01",
            "festival, so hopefully we'll be able to have\x01",
            "a drink together when I return.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #158
        "\x07\x05                 ' -Cassius Bright '\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #159
        (
            "\x07\x05'P.S. You may have the chance to meet\x01",
            "my son and daughter!'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #160
        (
            "\x07\x05'They're currently apprentices at the guild,\x01",
            "so if you happen to meet them, feel free to\x01",
            "test the extent of their training.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #161
        (
            "\x07\x05'Try not to bail them out too much, unless it\x01",
            "seems like they really need it.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #162
        0x101,
        "#000FI...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x102,
        (
            "#010FSo, Dad actually asked you to\x01",
            "come to Liberl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x108,
        "#070FThat's the long and short of it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        (
            "#000F'The long and short of it'...?\x02\x03",

            "What it means is that you were\x01",
            "in cahoots with him all along!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x108,
        (
            "#070FThat's kind of a nasty way to\x01",
            "put it, don't you think?\x02\x03",

            "I owed Master Cassius a favor, from\x01",
            "the time he spent in Calvard.\x02\x03",

            "This letter just gave me the\x01",
            "chance to make us square again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        "#000FI suppose...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x102,
        (
            "#010FWhen did you realize that\x01",
            "we were his kids?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x108,
        (
            "#070FI had a feeling from the outset, \x01",
            "once I saw Estelle's techniques\x01",
            "with a bo staff.\x02\x03",

            "I asked Kilika about it,\x01",
            "and that confirmed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        (
            "#000FEvil.\x02\x03",

            "It would have been nice if you'd\x01",
            "said something about it at ALL...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x108,
        (
            "#070FHa ha... Well, the letter did\x01",
            "say not to spoil you.\x02\x03",

            "So I helped out only as much as was\x01",
            "needed, and tried mostly to observe.\x02\x03",

            "Do you really think you could\x01",
            "have handled something this\x01",
            "major, all on your own?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        (
            "#000FI guess not...\x02\x03",

            "Joshua...? Aren't you going\x01",
            "to say something...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x102,
        (
            "#010FYes. I think I should explain\x01",
            "where we're coming from.\x02\x03",

            "It is a bit far-fetched to say that\x01",
            "we could put an end to this whole\x01",
            "situation on our own, after all.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #174
        (
            "\x07\x05Estelle and Joshua told of how they had managed to speak directly with the\x01",
            "queen...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #175
        "\x07\x05...as well as the queen's request to safely rescue Princess Klaudia.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #176
        0x108,
        (
            "#070FI see...\x02\x03",

            "I thought something seemed a\x01",
            "little 'off' when everyone was\x01",
            "talking at the party...\x02\x03",

            "All right, then. I'll help you\x01",
            "out with that little request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        "#000FWha... You will?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x108,
        (
            "#070FYep. I think this is the ideal\x01",
            "opportunity to settle my debt\x01",
            "to Master Cassius.\x02\x03",

            "Please, let me help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        "#000FWe... We'd be glad to!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x102,
        "#010FThank you, once again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x108,
        (
            "#070FNot a problem, guys.\x01",
            "Glad I can help out.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_3735 end

    SaveToFile()

Try(main)
