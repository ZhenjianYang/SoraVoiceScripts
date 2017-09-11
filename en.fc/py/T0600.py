from ED6ScenarioHelper import *

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
        'Private Stoll',                        # 9
        'Private Barranco',                     # 10
        'Private Thomas',                       # 11
        'Private Ethan',                        # 12
        'Private Logan',                        # 13
        'Elize Highway',                        # 14
        'Royal Avenue',                         # 15
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
        Unknown_3A              = 17,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
        'ED6_DT07/CH01300P._CP',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
        'ED6_DT07/CH01300P._CP',             # 02
    )

    DeclNpc(
        X                   = -35300,
        Z                   = 0,
        Y                   = 3650,
        Direction           = 261,
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
        X                   = -35300,
        Z                   = 0,
        Y                   = -3560,
        Direction           = 265,
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
        Direction           = 101,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        TalkScenaIndex      = 8,
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
        TalkScenaIndex      = 7,
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


    ScpFunction(
        "Function_0_1A2",          # 00, 0
        "Function_1_1A3",          # 01, 1
        "Function_2_216",          # 02, 2
        "Function_3_22C",          # 03, 3
        "Function_4_250",          # 04, 4
        "Function_5_DE1",          # 05, 5
        "Function_6_11CE",         # 06, 6
        "Function_7_178A",         # 07, 7
        "Function_8_1D18",         # 08, 8
        "Function_9_20DF",         # 09, 9
    )


    def Function_0_1A2(): pass

    label("Function_0_1A2")

    Return()

    # Function_0_1A2 end

    def Function_1_1A3(): pass

    label("Function_1_1A3")

    OP_16(0x2, 0xFA0, 0xFFFDB610, 0xFFFE0430, 0x30006)
    OP_6F(0x0, 160)
    OP_6F(0x1, 160)
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    OP_1C(0x2, 0x0, 0x9)
    OP_1C(0x3, 0x0, 0x9)
    OP_1C(0x4, 0x0, 0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1E6")
    Jump("loc_215")

    label("loc_1E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1F0")
    Jump("loc_215")

    label("loc_1F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1FA")
    Jump("loc_215")

    label("loc_1FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_204")
    Jump("loc_215")

    label("loc_204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_20E")
    Jump("loc_215")

    label("loc_20E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_215")

    label("loc_215")

    Return()

    # Function_1_1A3 end

    def Function_2_216(): pass

    label("Function_2_216")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_216")

    label("loc_22B")

    Return()

    # Function_2_216 end

    def Function_3_22C(): pass

    label("Function_3_22C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24F")
    OP_8D(0xFE, -28070, -8920, -16500, 6400, 3000)
    Jump("Function_3_22C")

    label("loc_24F")

    Return()

    # Function_3_22C end

    def Function_4_250(): pass

    label("Function_4_250")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2FD")

    ChrTalk(    #0
        0xFE,
        (
            "Selbourne said he saw a little girl\x01",
            "on the wall while he was on duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I'm sure he's just seeing things\x01",
            "since he hasn't seen his daughter\x01",
            "for so long.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3AF")

    ChrTalk(    #2
        0xFE,
        "It's pretty tranquil around here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Gazing out on this peaceful scenery makes it\x01",
            "hard to believe that any terrorist incidents\x01",
            "are happening within our borders.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_3AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_47C")

    ChrTalk(    #4
        0xFE,
        (
            "Yesterday, I saw a military aircraft\x01",
            "fly from Rolent to the Royal City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "That's usually the time we'd see an\x01",
            "airliner pass by, so I wonder if there\x01",
            "was some sort of emergency situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_682")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_54A")

    ChrTalk(    #6
        0xFE,
        (
            "That reminds me, I saw a white\x01",
            "falcon flying above the Scenic\x01",
            "Route earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "The white falcon is on the emblem\x01",
            "of the Liberl Kingdom and seeing\x01",
            "one is sure to bring good fortune.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67F")

    label("loc_54A")

    OP_A2(0x2)

    ChrTalk(    #8
        0xFE,
        (
            "That reminds me, I saw a white\x01",
            "falcon flying above the Scenic\x01",
            "Route earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "The white falcon is on the emblem\x01",
            "of the Liberl Kingdom and seeing\x01",
            "one is sure to bring good fortune.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I pray that both the Martial Arts\x01",
            "Competition and the queen's birthday\x01",
            "celebration will end without incident...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67F")

    Jump("loc_DDD")

    label("loc_682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_733")

    ChrTalk(    #11
        0xFE,
        (
            "Not that long ago, an airliner\x01",
            "passed through the airspace\x01",
            "above here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "It looks like it was inspected for\x01",
            "terrorists, but I guess the flight\x01",
            "resumed course.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_832")

    ChrTalk(    #13
        0xFE,
        (
            "The weather is so clear today.\x01",
            "I can even see the Krone Range\x01",
            "across the lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "In the center of the Liberl Kingdom\x01",
            "sits Valleria Lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "And surrounding it are mountains and\x01",
            "sea which make for an outstanding\x01",
            "view wherever you look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_8E5")

    ChrTalk(    #16
        0xFE,
        (
            "I saw a suspicious aircraft land and\x01",
            "take off somewhere in Mistwald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "When I reported it to the chief\x01",
            "he seemed a little perturbed, but\x01",
            "he didn't say anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_8E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_9A9")

    ChrTalk(    #18
        0xFE,
        (
            "All right, it looks like nothing out\x01",
            "of the ordinary has happened today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "Even though it's been ten years\x01",
            "since the war ended, when I think\x01",
            "about it, I can't let down my guard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_9A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_AB1")

    ChrTalk(    #20
        0xFE,
        (
            "I think the chief is an extremely\x01",
            "serious person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "But I sometimes wonder if he gets tired\x01",
            "of fretting over every little thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I'm sure it's difficult to rally the troops,\x01",
            "so at least I need to try not to make\x01",
            "things any more difficult.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_BF6")

    ChrTalk(    #23
        0xFE,
        (
            "At each checkpoint there is a\x01",
            "garrison for security stationed\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "The number of people going through the checkpoint\x01",
            "has been decreasing every year, but that's been\x01",
            "the case ever since the Hundred Days War ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Just because the war is over, it\x01",
            "doesn't mean that the Empire is\x01",
            "no longer a threat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_D41")

    ChrTalk(    #26
        0xFE,
        (
            "Good, it looks like nothing out of\x01",
            "the ordinary has happened today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "I'm starting to get hungry so after\x01",
            "I report in, maybe I'll get a bite to\x01",
            "eat at the mess hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "The owner of the mess hall loves\x01",
            "new things and is always changing\x01",
            "the menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "The only downside is that not\x01",
            "everything she makes is good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_D41")


    ChrTalk(    #30
        0xFE,
        (
            "I'm surprised that you made it up\x01",
            "here. Didn't you get lost inside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "The inside of this structure is\x01",
            "a little more complex than it\x01",
            "actually looks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDD")

    TalkEnd(0xFE)
    Return()

    # Function_4_250 end

    def Function_5_DE1(): pass

    label("Function_5_DE1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_F5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E85")

    ChrTalk(    #32
        0xFE,
        (
            "Starting yesterday, all checkpoints\x01",
            "in the kingdom have been put on\x01",
            "lockdown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "We are not conducting any pass\x01",
            "procedures at this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5A")

    label("loc_E85")

    OP_A2(0x0)

    ChrTalk(    #34
        0xFE,
        "Welcome to the Gurune Gate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "...is what I'd like to say, but starting\x01",
            "yesterday all checkpoints in the\x01",
            "kingdom have been put on lockdown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "We are not conducting any pass\x01",
            "procedures at this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F5A")

    Jump("loc_11CA")

    label("loc_F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_FD8")

    ChrTalk(    #37
        0xFE,
        (
            "The Martial Arts Competition ends\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "But until the terrorists are found\x01",
            "we won't be able to relax.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CA")

    label("loc_FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_105D")

    ChrTalk(    #39
        0xFE,
        (
            "We have received an order to beef\x01",
            "up security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "The issue of passes will be much\x01",
            "stricter starting today as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CA")

    label("loc_105D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_10D0")

    ChrTalk(    #41
        0xFE,
        (
            "If I remember right, the Martial Arts\x01",
            "Competition begins today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "I wonder who'll win this year.\x02",
    )

    CloseMessageWindow()
    Jump("loc_11CA")

    label("loc_10D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1167")

    ChrTalk(    #43
        0xFE,
        (
            "The central factory being attacked\x01",
            "is no laughing matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Not to mention we just barely dealt\x01",
            "with the incidents in Bose and Ruan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CA")

    label("loc_1167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_11CA")

    ChrTalk(    #45
        0xFE,
        "This is the Gurune Gate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "This checkpoint connects the Grancel\x01",
            "and Rolent regions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CA")

    TalkEnd(0xFE)
    Return()

    # Function_5_DE1 end

    def Function_6_11CE(): pass

    label("Function_6_11CE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_12B2")

    ChrTalk(    #47
        0xFE,
        (
            "I heard a royal banquet was held\x01",
            "at the castle, but did Her Majesty\x01",
            "attend?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "It would great if we could get an official\x01",
            "announcement about the queen's condition\x01",
            "and her birthday celebration some time soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1786")

    label("loc_12B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1391")

    ChrTalk(    #49
        0xFE,
        (
            "We've been seeing a lot of the Intelligence\x01",
            "Division's Special Ops Unit in the area over\x01",
            "the past several days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "If they don't find the terrorists\x01",
            "by the queen's birthday, I'm going\x01",
            "to be really worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1786")

    label("loc_1391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1410")

    ChrTalk(    #51
        0xFE,
        "All is well!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "No members of the Royal Guard or\x01",
            "other such suspicious individuals\x01",
            "have appeared around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1786")

    label("loc_1410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_14B7")

    ChrTalk(    #53
        0xFE,
        (
            "I was shocked to hear that the\x01",
            "Royal Guard had been charged\x01",
            "with treason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "But my mission is clear.\x01",
            "If I come across them,\x01",
            "I'll be forced to fight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1786")

    label("loc_14B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_159D")

    ChrTalk(    #55
        0xFE,
        (
            "It seems that even General Morgan\x01",
            "finally made a move regarding\x01",
            "anti-terrorist measures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "With Colonel Richard and General Morgan\x01",
            "at the forefront it's only a matter of time\x01",
            "before these incidents are resolved.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1786")

    label("loc_159D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_1786")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1692")

    ChrTalk(    #57
        0xFE,
        (
            "Come from the Erbe Scenic Route,\x01",
            "did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "The Royal Avenue and Erbe Scenic\x01",
            "Route basically run a loop around\x01",
            "this region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "This is why many travelers headed\x01",
            "to the castle miss the turnoff and\x01",
            "walk the entire loop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1786")

    label("loc_1692")

    OP_A2(0x1)

    ChrTalk(    #60
        0xFE,
        (
            "The Royal Avenue and Erbe Scenic\x01",
            "Route basically run a loop around\x01",
            "this region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "This is why many travelers headed\x01",
            "to the castle miss the turnoff and\x01",
            "walk the entire loop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "I saw a strange girl with glasses\x01",
            "on the loop earlier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1786")

    TalkEnd(0xFE)
    Return()

    # Function_6_11CE end

    def Function_7_178A(): pass

    label("Function_7_178A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_187D")

    ChrTalk(    #63
        0xFE,
        (
            "What? You're headed for the Bose\x01",
            "region? Then you're in the wrong\x01",
            "place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "You'll need to head back to Rolent\x01",
            "and aim for the Verte Bridge through\x01",
            "the west gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "It's in the same general direction\x01",
            "as the Perzel Farm.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D14")

    label("loc_187D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1930")

    ChrTalk(    #66
        0xFE,
        (
            "There have recently been reports of\x01",
            "seeing a number of suspicious figures\x01",
            "near the forest of Mistwald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "Make sure to be cautious as you\x01",
            "walk along the highway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D14")

    label("loc_1930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_19FA")

    ChrTalk(    #68
        0xFE,
        (
            "Ever since airliner flights began,\x01",
            "the number of people passing\x01",
            "through here has decreased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Basically, the only people coming\x01",
            "here these days are the ones who\x01",
            "want to view the wall.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D14")

    label("loc_19FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1A7B")

    ChrTalk(    #70
        0xFE,
        (
            "Right now, there's a young, hot-shot\x01",
            "colonel in the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "He's even pretty popular among\x01",
            "the soldiers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D14")

    label("loc_1A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1B76")

    ChrTalk(    #72
        0xFE,
        (
            "During the Hundred Days War, the Royal\x01",
            "City escaped from falling into enemy\x01",
            "hands because of the Ahnenburg Wall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "It seems that even the Imperial Army,\x01",
            "which overpowered the other four major\x01",
            "cities, ran into trouble with this wall.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D14")

    label("loc_1B76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1C08")

    ChrTalk(    #74
        0xFE,
        (
            "This massive structure is called\x01",
            "the Ahnenburg Wall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "It was built so that it surrounds the\x01",
            "entire neighboring Grancel region.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D14")

    label("loc_1C08")

    OP_A2(0x4)

    ChrTalk(    #76
        0xFE,
        (
            "This massive structure is called\x01",
            "the Ahnenburg Wall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "It was built so that is surrounds the\x01",
            "entire neighboring Grancel region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "It seems that this wall existed\x01",
            "even before the Liberl Kingdom\x01",
            "was founded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "I wonder who made it and for\x01",
            "what purpose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D14")

    TalkEnd(0xFE)
    Return()

    # Function_7_178A end

    def Function_8_1D18(): pass

    label("Function_8_1D18")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1DA5")

    ChrTalk(    #80
        0xFE,
        "Welcome to the Gurune Gate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "If you're headed to the Grancel\x01",
            "region, then you'll need to pass\x01",
            "through this checkpoint.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DB")

    label("loc_1DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1E1F")

    ChrTalk(    #82
        0xFE,
        (
            "Well there, it appears that you're\x01",
            "all bracers if I'm not mistaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "Did something happen around\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DB")

    label("loc_1E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1ECB")

    ChrTalk(    #84
        0xFE,
        (
            "We recently had a reporter\x01",
            "from the Liberl News come\x01",
            "to do a story on the Ahnenburg Wall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "He said something about writing\x01",
            "a story related to old ruins.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DB")

    label("loc_1ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1FE0")

    ChrTalk(    #86
        0xFE,
        (
            "Beyond here lies not only the Royal\x01",
            "City but the Erbe Royal Villa as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "The villa is open to all citizens of\x01",
            "Grancel except during times of\x01",
            "official business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "Ever since Queen Alicia took the throne,\x01",
            "the royal house has changed in a number\x01",
            "of ways.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DB")

    label("loc_1FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_2086")

    ChrTalk(    #89
        0xFE,
        (
            "Grancel Castle is an elegant structure\x01",
            "which sits on the shore of Valleria Lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "The bustle of the city just outside\x01",
            "the castle is pretty hectic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DB")

    label("loc_2086")


    ChrTalk(    #91
        0xFE,
        (
            "The Grancel region is just beyond\x01",
            "here. Do you have business in the\x01",
            "Royal City?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20DB")

    TalkEnd(0xFE)
    Return()

    # Function_8_1D18 end

    def Function_9_20DF(): pass

    label("Function_9_20DF")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_9_20DF end

    SaveToFile()

Try(main)
