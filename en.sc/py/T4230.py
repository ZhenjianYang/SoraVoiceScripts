from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4230   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4230.x',
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
        'Queen Alicia',                         # 9
        '紅茶',                                 # 10
        '紅茶',                                 # 11
        '紅茶',                                 # 12
        '紅茶',                                 # 13
        '紅茶',                                 # 14
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
        'ED6_DT07/CH02013 ._CH',             # 00
        'ED6_DT27/CH03003 ._CH',             # 01
        'ED6_DT07/CH00033 ._CH',             # 02
        'ED6_DT07/CH00043 ._CH',             # 03
        'ED6_DT07/CH00073 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02013P._CP',             # 00
        'ED6_DT27/CH03003P._CP',             # 01
        'ED6_DT07/CH00033P._CP',             # 02
        'ED6_DT07/CH00043P._CP',             # 03
        'ED6_DT07/CH00073P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_1D0",          # 01, 1
        "Function_2_207",          # 02, 2
        "Function_3_582",          # 03, 3
        "Function_4_215A",         # 04, 4
        "Function_5_2C7E",         # 05, 5
        "Function_6_2CCD",         # 06, 6
        "Function_7_2D30",         # 07, 7
        "Function_8_2D93",         # 08, 8
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BC")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -104230, 200, 9990, 225)

    label("loc_1BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1CF")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_1CF")

    Return()

    # Function_0_19A end

    def Function_1_1D0(): pass

    label("Function_1_1D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EC")
    OP_B1("t4230_y")
    Jump("loc_1F5")

    label("loc_1EC")

    OP_B1("t4230_n")

    label("loc_1F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_206")
    OP_72(0xB, 0x4)

    label("loc_206")

    Return()

    # Function_1_1D0 end

    def Function_2_207(): pass

    label("Function_2_207")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_297")
    Jump("loc_2D9")

    label("loc_297")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D9")

    label("loc_2B3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CF")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D9")

    label("loc_2CF")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D9")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE")

    ChrTalk(    #0
        0x8,
        (
            "#090FThanks to Cassius' tireless\x01",
            "service, the Royal Army is well\x01",
            "on its way to being rebuilt.\x02\x03",

            "#094F'Choose the best path, and then\x01",
            "walk it.'\x02\x03",

            "#090FTo put it into words is simple,\x01",
            "but nothing is harder than putting\x01",
            "it into practice.\x02\x03",

            "He is one of the few who knows\x01",
            "how to walk such paths.\x02\x03",

            "#093FI'm sure he'd dearly love to\x01",
            "spend his days living peacefully\x01",
            "with you, Estelle.\x02\x03",

            "#090FI must never lose sight of being\x01",
            "a queen worthy of loyalty like your\x01",
            "father's.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_579")

    label("loc_4DE")


    ChrTalk(    #1
        0x8,
        (
            "#090FI'm sure Cassius would rather live\x01",
            "peacefully with you, Estelle.\x02\x03",

            "I must never lose sight of being\x01",
            "a queen worthy of loyalty like your\x01",
            "father's.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_579")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_2_207 end

    def Function_3_582(): pass

    label("Function_3_582")

    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x105, 0x40)
    SetChrFlags(0x104, 0x40)
    SetChrFlags(0x108, 0x40)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x108, 0x4)
    SetChrPos(0x8, -104230, 200, 9990, 225)
    SetChrPos(0x101, -105330, 200, 10390, 180)
    SetChrPos(0x105, -103780, 200, 9000, 270)
    SetChrPos(0x108, -105330, 50, 7670, 0)
    SetChrPos(0x104, -106680, 200, 9000, 90)
    SetChrPos(0x9, -104750, 550, 9430, 0)
    SetChrPos(0xA, -105280, 550, 9460, 0)
    SetChrPos(0xB, -104730, 550, 8950, 0)
    SetChrPos(0xC, -105280, 550, 8400, 0)
    SetChrPos(0xD, -105830, 550, 8950, 0)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x104, 2)
    SetChrChipByIndex(0x105, 3)
    SetChrChipByIndex(0x108, 4)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x105, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0x105, 2)
    OP_6D(-104610, 200, 9480, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(253, 0)
    OP_72(0xB, 0x4)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #2
        0x8,
        (
            "#094FAh... So you've come about the letters.\x02\x03",

            "I wasn't aware they had been sent to the\x01",
            "cathedral and the embassies as well...\x02\x03",

            "#092FYour fears are not groundless.\x01",
            "It is difficult to think of such lengths\x01",
            "as a mere childish prank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1002F#6PYes, Your Highness.\x02\x03",

            "That's why we're trying to talk to people\x01",
            "affiliated to the case, to see if we can\x01",
            "find some clues...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x105,
        (
            "#043F#4PGrandmother, do you have any idea who\x01",
            "might be responsible?\x02\x03",

            "Especially someone...within Liberl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        "#094FHmm.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(300)

    ChrTalk(    #6
        0x8,
        "#090FKlaudia. What do you think?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x105,
        "#044F#4PMe...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#090FAs a possible heir, your thoughts should\x01",
            "daily be on the forces moving within our\x01",
            "nation.\x02\x03",

            "Would you share your opinion with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x105,
        (
            "#542F#4PV-Very well...\x02\x03",

            "#047F*deep breath*\x02\x03",

            "#042FI don't believe there is any force in the\x01",
            "country which is truly opposed to the\x01",
            "pact.\x02\x03",

            "I've heard in various places, however, that\x01",
            "following the coup, some of our extreme right-\x01",
            "wing citizens are feeling very concerned.\x02\x03",

            "Their frustrations might be at the root of\x01",
            "these letters...maybe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#094FHmm... Very good.\x02\x03",

            "#090FMy opinion is more or less the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1004F#6PSorry, but, uh, I don't quite follow...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    Sleep(300)

    ChrTalk(    #12
        0x8,
        (
            "#094FAlan...ah, Colonel Richard...was not the only\x01",
            "man who approved of the idea of expanding\x01",
            "and empowering our military.\x02\x03",

            "#092FIn the wake of the failed coup, however,\x01",
            "the matter is effectively untouchable.\x02\x03",

            "I can only imagine all who share his mindset are\x01",
            "quite dissatisfied, and worried, for our safety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#1002F#6POkay, so...\x02\x03",

            "You think the letters are from believers in\x01",
            "military control and expansion? Like the\x01",
            "Intelligence Division guys still on the run?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#090FThat would be the short of it, yes.\x02\x03",

            "#094FIf that is the case...then I would say\x01",
            "I bear the responsibility for this as\x01",
            "much as they.\x02\x03",

            "It was my beliefs that led them to take\x01",
            "such action in the first place, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x105,
        "#043F#4PGrandmother...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1015F#6PI dunno, I don't think they have the right to be\x01",
            "all 'blarrr, let's threaten people and be scary\x01",
            "because we're sore losers.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#092FNo. There are few things more precious\x01",
            "than the freedom to express one's self,\x01",
            "Estelle.\x02\x03",

            "Remember, even those who promote military\x01",
            "empowerment and a war footing do so out of\x01",
            "a love for Liberl and its people.\x02\x03",

            "They have as much right to express that\x01",
            "idea as any of us have ours.\x02\x03",

            "And listening to all such opinions and\x01",
            "choosing how to guide the country...\x01",
            "that is a ruler's responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x105,
        "#049F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x108,
        (
            "#070F#4PThough, in that case...\x02\x03",

            "I rather doubt they'll actually try to\x01",
            "stop the ceremony, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#090FAssuming the letter is from the\x01",
            "expansionists, yes, that's quite possible.\x02\x03",

            "With Colonel Richard under arrest, they\x01",
            "have little power with which to act.\x02\x03",

            "#094FThe problem lies with the idea that\x01",
            "someone else may be responsible.\x02\x03",

            "If that is the case, then I fear I can\x01",
            "offer you little advice or knowledge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1007F#6PAww, rats.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x104,
        "#030F#3PQueen Alicia, if I may broach a question?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(75)
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0x105, 0)

    ChrTalk(    #23
        0x8,
        (
            "#097FOf course...Olivier.\x01",
            "Whatever you wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x104,
        (
            "#032F#3PWhy are you so determined to act upon\x01",
            "this non-aggression pact NOW?\x02\x03",

            "Your own country is still deeply confused\x01",
            "and unsettled from the coup attempt.\x02\x03",

            "Most rulers would think this is a time to\x01",
            "focus solely on one's own country,\x01",
            "not the affairs of others.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #25
        0x101,
        (
            "#1019FOlivier, you ARE talking to a queen,\x01",
            "you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#094FIt's all right, Estelle.\x01",
            "Olivier has a point.\x02\x03",

            "#090FThe plans and proposals for the pact,\x01",
            "however, far predate the coup.\x02\x03",

            "Further delays would only harm the dignity\x01",
            "of the nation.\x02\x03",

            "The Crossbell issue is causing a great\x01",
            "deal of friction again as well, and I hope\x01",
            "this can help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x104,
        "#033F#3PHmm.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(300)

    ChrTalk(    #28
        0x101,
        (
            "#1004FCrossbell... That's where Renne's from,\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x105,
        (
            "#042FYes, it lies due northeast of here, over the\x01",
            "Krone Mountains and directly between Erebonia\x01",
            "and Calvard.\x02\x03",

            "Both the Republic and Empire claim it should be\x01",
            "part of their governments, and some Crossbellans\x01",
            "want total independence... It's quite a mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x108,
        (
            "#070F#4PCrossbell's basically a fishbone stuck in\x01",
            "two throats at once.\x02\x03",

            "All the issues surrounding it just get\x01",
            "called the 'Crossbell Problem.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1015FI see... Boy, no wonder people get\x01",
            "worked up about it, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x104,
        (
            "#035F#3PAh. So your aim is to pluck out the bone\x01",
            "with this pact, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "#090FTo continue the analogy...it is not a bone that\x01",
            "can be removed in one gesture, sadly.\x02\x03",

            "If I can open a way to resolve the issue,\x01",
            "however, yes.\x02\x03",

            "Laying the groundwork for resolving that issue\x01",
            "will strengthen peace across the entire region...\x01",
            "and people will remember Liberl spurred it on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x104,
        (
            "#035F#3PHeh... I have underestimated you even\x01",
            "more than I previously thought.\x02\x03",

            "Our invasion of Liberl was far more of a\x01",
            "fool's errand than I'd even imagined.\x02\x03",

            "That much, at least, is painfully obvious\x01",
            "to me now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#1007FWhat are you going on about...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #36
        0x101,
        (
            "#1004F#6POH! Wait, Crossbell, Renne, duh!\x01",
            "Sorry to change the subject,\x01",
            "Your Majesty, but...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x05Estelle asked Queen Alicia about Renne's parents.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #38
        0x8,
        (
            "#097FMy goodness... A child, abandoned at the Royal\x01",
            "Villa? I must instruct Raymond to keep me\x01",
            "better informed, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1008F#6PI know it's a shot in the dark, but I don't\x01",
            "suppose you have any idea where they\x01",
            "might be, Your Majesty?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C6B")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as talked to Hilda\x01",          # 0
            "Set as not talked to Hilda\x01",      # 1
            "No change\x01",                       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C5F"),
        (1, "loc_1C65"),
        (SWITCH_DEFAULT, "loc_1C6B"),
    )


    label("loc_1C5F")

    OP_A2(0x1626)
    Jump("loc_1C6B")

    label("loc_1C65")

    OP_A3(0x1626)
    Jump("loc_1C6B")

    label("loc_1C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_END)), "loc_1E2D")

    ChrTalk(    #40
        0x8,
        (
            "#093FNo, I am very sorry, but I do not.\x01",
            "However...\x02\x03",

            "#090FIf they visited the castle, especially\x01",
            "recently, Hilda would know of it.\x02\x03",

            "Have you spoken with her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#1015F#6PYeah, we did...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x105,
        (
            "#043F#4PHilda only said they were behaving a\x01",
            "little strangely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "#094FI see.\x02\x03",

            "#090FWell, should you wish, I can contact Mayor\x01",
            "MacDowell and the Crossbell government.\x02\x03",

            "If that would help, ask whenever you need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1018F#6POh, uh, thanks!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FB4")

    label("loc_1E2D")


    ChrTalk(    #45
        0x8,
        (
            "#093FNo, I am very sorry, but I do not.\x01",
            "However...\x02\x03",

            "#090FIf they visited the castle, especially\x01",
            "recently, Hilda would know of it.\x02\x03",

            "You should speak with her, if you have\x01",
            "not already done so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1006F#6POkay, we will!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "#090FShould you wish, I can also contact Mayor\x01",
            "MacDowell and the Crossbell government.\x02\x03",

            "If that would help, ask whenever you need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        "#1018F#6POh, uh, thanks!\x02",
    )

    CloseMessageWindow()

    label("loc_1FB4")


    ChrTalk(    #49
        0x105,
        (
            "#041F#4PGrandmother, thank you for all your help.\x02\x03",

            "#542FWe need to move on, unfortunately.\x02\x03",

            "#049FBut... Umm...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(300)

    ChrTalk(    #50
        0x8,
        (
            "#094FDon't be nervous.\x01",
            "I know what you wish to say, I think.\x02\x03",

            "#090FYou will be staying in the castle\x01",
            "tonight, yes?\x02\x03",

            "Let us speak then, once you are no\x01",
            "longer busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x105,
        "#047F#4PAll right...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x104, 65535)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 65535)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x105, 0x40)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x40)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x108, 0x40)
    ClearChrFlags(0x108, 0x4)
    Sleep(500)
    Call(0, 4)
    Return()

    # Function_3_582 end

    def Function_4_215A(): pass

    label("Function_4_215A")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x108, 0x80)
    SetChrFlags(0x104, 0x80)
    OP_6D(-1000, 8000, 35200, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3C)
    OP_72(0x1, 0x10)
    OP_0D()
    OP_43(0x101, 0x1, 0x0, 0x5)
    Sleep(800)
    OP_43(0x108, 0x1, 0x0, 0x6)
    Sleep(800)
    OP_43(0x104, 0x1, 0x0, 0x7)
    Sleep(800)
    OP_43(0x105, 0x1, 0x0, 0x8)
    OP_6D(-200, 8000, 27500, 4000)
    WaitChrThread(0x105, 0x1)
    OP_71(0x1, 0x10)
    Sleep(500)

    ChrTalk(    #52
        0x104,
        (
            "#031F#3PMy Goddess. Such...royalty!\x02\x03",

            "I would say she is the only person on the\x01",
            "continent with that sense of...balance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x108,
        (
            "#071FYeah. Sort of feels weird to say,\x01",
            "coming from a democracy,\x01",
            "but she's the perfect ruler.\x02\x03",

            "I kind of envy Liberl, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1006FHeh! Of course!\x02\x03",

            "She's the queen, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x105,
        "#049F#6P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #56
        0x101,
        "#1004FKloe? What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x105,
        (
            "#542F#6POh, it's nothing.\x02\x03",

            "#045FI was just struck again by how incredible\x01",
            "a woman Grandmother is.\x02\x03",

            "I...really doubt I can ever live up to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#1026FOh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x105, 400)
    Sleep(500)

    ChrTalk(    #59
        0x104,
        (
            "#035F#3PHm. Princess?\x02\x03",

            "When did Her Majesty the Queen\x01",
            "take the throne?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x104, 400)
    Sleep(300)

    ChrTalk(    #60
        0x105,
        (
            "#044F#6PHmm? Oh, she was...twenty,\x01",
            "if I recall correctly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x104,
        "#030F#3PAnd may I ask your age?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x105,
        (
            "#043F#6PI'm sixteen, but wh--\x02\x03",

            "#044F...Ah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x104,
        (
            "#031F#3PHeh. My point.\x02\x03",

            "I truly doubt Her Majesty was a master\x01",
            "politician the day she took the throne.\x02\x03",

            "And you are not yet even as old as she\x01",
            "was when she first donned the purple.\x02\x03",

            "I see little point in comparing yourself to\x01",
            "her as she is now. Wouldn't you agree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x108,
        (
            "#074FWe martial artists tend to say that only\x01",
            "those with the proper capacity can achieve\x01",
            "this thing called 'unity of purpose.'\x02\x03",

            "Even those with the greatest innate skill, like,\x01",
            "say, Walter, only reach their peak through a\x01",
            "journey of a thousand steps.\x02\x03",

            "#070FI think Her Majesty believes you have the\x01",
            "capacity to get there, Princess.\x02\x03",

            "Just take it one step at a time. Don't worry.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)
    Sleep(500)

    ChrTalk(    #65
        0x105,
        (
            "#542F#6POlivier...Zin...\x02\x03",

            "#041FThank you. Really...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1006FGood job, you two!\x01",
            "Kloe's going to be an awesome queen\x01",
            "someday.\x02\x03",

            "I guess you get good with pep talks as\x01",
            "you get older, huh?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)
    Sleep(300)

    ChrTalk(    #67
        0x104,
        (
            "#032F#3PHm? 'Get older'? How rude! I'm a fresh,\x01",
            "YOUTHFUL twenty five.\x02\x03",

            "Five years younger than Zin here,\x01",
            "even!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x108,
        (
            "#075FYou're one to call out someone\x01",
            "on being rude, Olivier...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A57")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as Haven't Talked to Hilda/Have asked maids' room\x01",         # 0
            "Set as Haven't Talked to Hilda/Haven't asked maids' room\x01",      # 1
            "Set as have talked to Hilda\x01",                                   # 2
            "No change\x01",                                                     # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A3F"),
        (1, "loc_2A48"),
        (2, "loc_2A51"),
        (SWITCH_DEFAULT, "loc_2A57"),
    )


    label("loc_2A3F")

    OP_A3(0x1626)
    OP_A2(0x1629)
    Jump("loc_2A57")

    label("loc_2A48")

    OP_A3(0x1626)
    OP_A3(0x1629)
    Jump("loc_2A57")

    label("loc_2A51")

    OP_A2(0x1626)
    Jump("loc_2A57")

    label("loc_2A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 1)), scpexpr(EXPR_END)), "loc_2B17")

    ChrTalk(    #69
        0x105,
        (
            "#045F#6PHeeheehee...\x02\x03",

            "#048FAnyway...shall we go speak with Hilda?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1006FYeah, that should be step two.\x02\x03",

            "She's in the Library in the left wing,\x01",
            "if I remember right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB6")

    label("loc_2B17")


    ChrTalk(    #71
        0x105,
        (
            "#045F#6PHeeheehee...\x02\x03",

            "#048FAnyway...shall we go speak with Hilda?\x02\x03",

            "We should be able to find her, or where\x01",
            "she is, in the maid quarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1006FSure!\x02",
    )

    CloseMessageWindow()

    label("loc_2BB6")

    Jump("loc_2C6D")

    label("loc_2BB9")


    ChrTalk(    #73
        0x105,
        (
            "#045F#6PHeeheehee...\x02\x03",

            "#048FWell, anyway...we've spoken to Hilda\x01",
            "and Grandmother both.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#1006FYep! Back to town, then, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x105,
        "#542F#6PYes, let's be off.\x02",
    )

    CloseMessageWindow()
    OP_28(0x8B, 0x2, 0x80)
    OP_28(0x8B, 0x1, 0x100)

    label("loc_2C6D")

    Sleep(100)
    OP_A2(0x1625)
    OP_28(0x8B, 0x1, 0x400)
    EventEnd(0x0)
    Return()

    # Function_4_215A end

    def Function_5_2C7E(): pass

    label("Function_5_2C7E")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -870, 8000, 37870, 180)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2CA5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2CA5)
    OP_8E(0xFE, 0xFFFFFC7C, 0x1F40, 0x6590, 0x7D0, 0x0)
    OP_8C(0xFE, 360, 400)
    Return()

    # Function_5_2C7E end

    def Function_6_2CCD(): pass

    label("Function_6_2CCD")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -870, 8000, 37870, 180)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2CF4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2CF4)
    OP_8E(0xFE, 0xFFFFFC18, 0x1F40, 0x6EE6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x46, 0x1F40, 0x6978, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_6_2CCD end

    def Function_7_2D30(): pass

    label("Function_7_2D30")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -870, 8000, 37870, 180)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2D57():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D57)
    OP_8E(0xFE, 0xFFFFFC18, 0x1F40, 0x6EE6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF862, 0x1F40, 0x6978, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_7_2D30 end

    def Function_8_2D93(): pass

    label("Function_8_2D93")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -870, 8000, 37870, 180)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2DBA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DBA)
    OP_8E(0xFE, 0xFFFFFC18, 0x1F40, 0x8980, 0x7D0, 0x0)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFFD44, 0x1F40, 0x6E28, 0x7D0, 0x0)
    Return()

    # Function_8_2D93 end

    SaveToFile()

Try(main)
