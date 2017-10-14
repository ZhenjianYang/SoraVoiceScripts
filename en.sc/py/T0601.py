from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0601   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0601.x',
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
        'Private Selbourne',                    # 9
        'Warrant Officer Graves',               # 10
        'Father Kevin',                         # 11
        'Port Seeker',                          # 12
        'Port Seeker',                          # 13
        'Warrant Officer Graves',               # 14
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
        'ED6_DT27/CH03080 ._CH',             # 01
        'ED6_DT29/CH12581 ._CH',             # 02
        'ED6_DT07/CH01310 ._CH',             # 03
        'ED6_DT27/CH04000 ._CH',             # 04
        'ED6_DT27/CH04080 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT27/CH03080P._CP',             # 01
        'ED6_DT29/CH12581P._CP',             # 02
        'ED6_DT07/CH01310P._CP',             # 03
        'ED6_DT27/CH04000P._CP',             # 04
        'ED6_DT27/CH04080P._CP',             # 05
    )

    DeclNpc(
        X                   = -940,
        Z                   = 7250,
        Y                   = -94770,
        Direction           = 180,
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
        X                   = -5540,
        Z                   = 7250,
        Y                   = -68220,
        Direction           = 266,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -5700,
        Y                   = -2000,
        Z                   = -21100,
        Range               = 3800,
        Unknown_10          = 0x2328,
        Unknown_14          = 0xFFFFBA14,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    ScpFunction(
        "Function_0_1BA",          # 00, 0
        "Function_1_240",          # 01, 1
        "Function_2_286",          # 02, 2
        "Function_3_29C",          # 03, 3
        "Function_4_2C0",          # 04, 4
        "Function_5_11A0",         # 05, 5
        "Function_6_128A",         # 06, 6
        "Function_7_1370",         # 07, 7
        "Function_8_2177",         # 08, 8
        "Function_9_30F7",         # 09, 9
        "Function_10_3113",        # 0A, 10
        "Function_11_313C",        # 0B, 11
    )


    def Function_0_1BA(): pass

    label("Function_0_1BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1DC")
    SetChrPos(0x8, -2980, 7250, -67430, 335)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Jump("loc_201")

    label("loc_1DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1E6")
    Jump("loc_201")

    label("loc_1E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_1F5")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_201")

    label("loc_1F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_201")
    SetChrFlags(0x8, 0x80)

    label("loc_201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_21D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_21D")

    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_1BA end

    def Function_1_240(): pass

    label("Function_1_240")

    OP_16(0x2, 0xFA0, 0xFFFE0818, 0xFFFD7790, 0x230012)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27C")
    OP_B1("t0601_y")
    OP_C4(0x0, 0x2)
    OP_7E(0xFC18, 0x1F4, 0x3E8, 0x96, 0x0)
    Jump("loc_285")

    label("loc_27C")

    OP_B1("t0601_n")

    label("loc_285")

    Return()

    # Function_1_240 end

    def Function_2_286(): pass

    label("Function_2_286")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_286")

    label("loc_29B")

    Return()

    # Function_2_286 end

    def Function_3_29C(): pass

    label("Function_3_29C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BF")
    OP_8D(0xFE, -3140, -97580, 1480, -73120, 3000)
    Jump("Function_3_29C")

    label("loc_2BF")

    Return()

    # Function_3_29C end

    def Function_4_2C0(): pass

    label("Function_4_2C0")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_465")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E9")

    ChrTalk(    #0
        0xFE,
        (
            "Looks like that floating island is\x01",
            "pretty high up there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "In which case, naturally you'd be able\x01",
            "to see it from the Empire, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "A mysterious giant structure appearing\x01",
            "in Liberl airspace... Huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "H-Hopefully this doesn't invite any\x01",
            "misunderstandings...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_462")

    label("loc_3E9")


    ChrTalk(    #4
        0xFE,
        (
            "I bet the Empire's keeping an eye\x01",
            "on that island too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "H-Hopefully this doesn't invite any\x01",
            "misunderstandings...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_462")

    Jump("loc_119C")

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_647")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C8")

    ChrTalk(    #6
        0xFE,
        (
            "I saw it on that night...\x01",
            "The moment the island appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "It suddenly got bright for a moment\x01",
            "like the sun had risen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Then, by the time I came to my senses,\x01",
            "that island was floating right there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I know it's hard to believe, but I swear\x01",
            "it just appeared out of nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Almost like it was there all along...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_644")

    label("loc_5C8")


    ChrTalk(    #11
        0xFE,
        (
            "That floating island just appeared\x01",
            "outta nowhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I couldn't believe it for a while until\x01",
            "my eyes got used to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_644")

    Jump("loc_119C")

    label("loc_647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_7B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6DD")

    ChrTalk(    #13
        0xFE,
        (
            "Clean blue skies and a deep forest\x01",
            "that seems to go on forever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "This contrast itself is the charm of\x01",
            "Rolent's landscape.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B3")

    label("loc_6DD")


    ChrTalk(    #15
        0xFE,
        (
            "Clean blue skies and a deep forest\x01",
            "that seems to go on forever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "Yep, this is what Rolent should be like.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "The contrast between the sky and the\x01",
            "land is the selling point of this place,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_7B3")

    Jump("loc_119C")

    label("loc_7B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_92D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_83C")

    ChrTalk(    #18
        0xFE,
        "That fog is so thick it's like a white wall.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "If you guys are going out onto the\x01",
            "highways, watch yourselves\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92A")

    label("loc_83C")


    ChrTalk(    #20
        0xFE,
        (
            "Nothing out of the ordinary to report\x01",
            "today...is what I told my commander,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "There's no real meaning in patrolling\x01",
            "when the Rolent side is pure white.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "You guys should be careful too if\x01",
            "you go out onto the highways.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_92A")

    Jump("loc_119C")

    label("loc_92D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_AC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9DA")

    ChrTalk(    #23
        0xFE,
        (
            "Feels like the fog's even thicker\x01",
            "than yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "I've been working here a long time,\x01",
            "but this is my first time experiencing\x01",
            "something like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC2")

    label("loc_9DA")


    ChrTalk(    #25
        0xFE,
        (
            "Feels like the fog's even thicker\x01",
            "than yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Even though the air on the Grancel side\x01",
            "is clear as always today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "I've been working here a long time,\x01",
            "but this is my first time experiencing\x01",
            "something like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_AC2")

    Jump("loc_119C")

    label("loc_AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_BED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B42")

    ChrTalk(    #28
        0xFE,
        (
            "Today the Rolent side's scenery is\x01",
            "clouded in white.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "Normally it's just bursting with green, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BEA")

    label("loc_B42")


    ChrTalk(    #30
        0xFE,
        (
            "The Grancel side is clear and the\x01",
            "weather's great, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "On the other hand, Rolent is clouded in white.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "Normally it's just bursting with green, too.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_BEA")

    Jump("loc_119C")

    label("loc_BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_C9E")

    ChrTalk(    #33
        0xFE,
        (
            "Ultimately, the society and the Special Ops\x01",
            "guys haven't shown up since then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "I heard some bracers and the Royal Guard\x01",
            "defended the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "Thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_119C")

    label("loc_C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_D00")

    ChrTalk(    #36
        0xFE,
        "We just heard about the society a bit ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "For now, you're in a hurry, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_119C")

    label("loc_D00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_DB1")

    ChrTalk(    #38
        0xFE,
        (
            "The Intelligence Division's Special Ops forces,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Now they're wanted people,\x01",
            "but they used to be an elite force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "Better be on our best guard, huh.\x02",
    )

    CloseMessageWindow()
    Jump("loc_119C")

    label("loc_DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_10F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1068")

    ChrTalk(    #41
        0xFE,
        "Hey, welcome to the Gurune Gate.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0x8, 400)

    ChrTalk(    #42
        0x12F,
        (
            "#264FHey, I remember seeing a building\x01",
            "like this south of the capital.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x12F, 400)

    ChrTalk(    #43
        0xFE,
        (
            "Haha, well, that building is a part of the\x01",
            "barrier encompassing this region,\x01",
            "the Ahnenburg Wall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "What you saw was the Sanktheim Gate\x01",
            "on the south part of the wall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x12F,
        "#260FOh, okay. So that's what it was.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0x101, 400)

    ChrTalk(    #46
        0x101,
        (
            "#1007F*yaaaaawn* The view's great here.\x01",
            "There's a nice breeze that comes\x01",
            "off the forest too.\x02\x03",

            "#1006FI really do like this place, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x12F,
        (
            "#261FHeeheehee.\x02\x03",

            "#265FBut, you know, I like this place too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Haha. Unlike the Sanktheim Gate, there's\x01",
            "not many people around here, so it's a\x01",
            "very calming place, I think.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1652)
    Jump("loc_10F1")

    label("loc_1068")


    ChrTalk(    #49
        0xFE,
        (
            "The Gurune Gate, unlike the Sanktheim Gate,\x01",
            "doesn't have a lot of people around, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "So, I think it's a very calming place.\x02",
    )

    CloseMessageWindow()

    label("loc_10F1")

    Jump("loc_119C")

    label("loc_10F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_119C")

    ChrTalk(    #51
        0xFE,
        (
            "As always, this place is huge,\x01",
            "and patrolling's a tough order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "The beauty of the scenery and the feel of\x01",
            "the wind are the silver lining to it, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_119C")

    TalkEnd(0x8)
    Return()

    # Function_4_2C0 end

    def Function_5_11A0(): pass

    label("Function_5_11A0")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_1286")

    ChrTalk(    #53
        0xFE,
        (
            "The machines that attacked us might\x01",
            "have been from the society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "They've appeared on the Erbe Scenic Route\x01",
            "and here too now, so we'll need to strengthen\x01",
            "our patrols.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "You should return to the guild quickly.\x02",
    )

    CloseMessageWindow()

    label("loc_1286")

    TalkEnd(0x9)
    Return()

    # Function_5_11A0 end

    def Function_6_128A(): pass

    label("Function_6_128A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1297")
    Return()

    label("loc_1297")

    EventBegin(0x0)
    Fade(1000)
    AddParty(0x8, 0xF7, 0xFF)
    SetChrPos(0x109, 3570, 7250, -68040, 90)
    SetChrPos(0x101, -780, 7250, -45000, 180)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    OP_69(0x101, 0x0)
    OP_6A(0x101)
    Sleep(100)
    OP_8E(0x101, 0xFFFFFDA8, 0x1C52, 0xFFFF2946, 0xBB8, 0x0)
    OP_6A(0xFF)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_6D(-1190, 7250, -61210, 2000)

    ChrTalk(    #56
        0x101,
        "#1025F#5PAh...!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4103   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_6_128A end

    def Function_7_1370(): pass

    label("Function_7_1370")

    EventBegin(0x0)
    AddParty(0x8, 0xF7, 0xFF)
    OP_31(0x8, 0x0, 0x37)
    OP_31(0x8, 0xFE, 0x0)
    OP_31(0x8, 0x5, 0x5A)
    OP_41(0x8, 0xE9, 0xFF)
    OP_41(0x8, 0x100, 0xFF)
    OP_41(0x8, 0x121, 0xFF)
    OP_41(0x8, 0x273, 0x0)
    OP_41(0x8, 0x25C, 0x1)
    OP_41(0x8, 0x259, 0x2)
    OP_41(0x8, 0x265, 0x3)
    OP_41(0x8, 0x262, 0x4)
    OP_35(0x8, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x109, 3570, 7250, -68040, 90)
    SetChrPos(0x101, -600, 7250, -54970, 180)
    OP_6D(-1190, 7250, -61210, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #57
        0x101,
        "#1018F#5PJOSHUA!\x02",
    )

    CloseMessageWindow()

    def lambda_143B():
        OP_8E(0x101, 0xFFFFFF74, 0x1C52, 0xFFFF15B4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_143B)

    def lambda_1456():
        OP_6D(500, 7250, -63380, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1456)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0x1)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #58
        0x101,
        "#1004F#5PHuh...?\x02",
    )

    CloseMessageWindow()
    OP_6D(1140, 7250, -65340, 1200)
    OP_62(0x109, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_14DB():

        label("loc_14DB")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_14DB")

    QueueWorkItem2(0x109, 0, lambda_14DB)
    Sleep(400)

    ChrTalk(    #59
        0x109,
        (
            "#1064F#6PWhat?\x02\x03",

            "Estelle? That you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1020F#5P...Kevin?\x02\x03",

            "Wh... Why are YOU here?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    def lambda_1556():
        OP_8E(0xFE, 0xFFFFFBF0, 0x1C52, 0xFFFEF700, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1556)

    def lambda_1571():
        OP_6D(160, 7250, -67940, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1571)

    def lambda_1589():
        OP_67(0, 8210, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1589)

    def lambda_15A1():
        OP_6B(2570, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_15A1)

    def lambda_15B1():
        OP_6E(334, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_15B1)
    OP_6C(134000, 3000)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8C(0x101, 90, 400)
    Sleep(500)
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #61
        0x101,
        "#1026F#6PHe...isn't here...\x02",
    )

    CloseMessageWindow()
    OP_44(0x109, 0x0)
    OP_8E(0x109, 0x244, 0x1C52, 0xFFFEF746, 0x7D0, 0x0)

    ChrTalk(    #62
        0x109,
        (
            "#1062F#6PWell, heeeeey! Been a while, hasn't it?\x02\x03",

            "#1061FHow's this for chances! You don't think\x01",
            "there might be a destiny 'thing' between\x01",
            "us, do--\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 600)

    ChrTalk(    #63
        0x101,
        (
            "#1002F#4PKevin, listen!\x02\x03",

            "Did you meet anyone else on\x01",
            "your way here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x109,
        (
            "#1064F#6PUh, someone else?\x02\x03",

            "Wait...you're here to meet someone too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1026F#4PYeah... Joshu--\x02\x03",

            "#1015FEr, hold on. You too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x109,
        "#1063F#6PYeah... I got called out here by a letter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#1011F#4PReally? Me too!\x02\x03",

            "#1016FHaha! What a crazy coincidence!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x109,
        (
            "#1061F#6PHaha. I know, right...?\x02\x03",

            "#1069FOr not! No way this is just coincidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1015F#4PYeah, that's kind of what I figured.\x02\x03",

            "So, then, Joshua called you out here too?\x01",
            "Huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x109,
        (
            "#1064F#6PEr, Joshua?\x02\x03",

            "Ain't that...that boyfriend you were\x01",
            "talkin' about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#1026F#4PU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x109,
        (
            "#1067F#6POh, um, I had no idea...\x02\x03",

            "Didn't think Joshua would be quite that,\x01",
            "ah, well-seasoned.\x02\x03",

            "#1068FI mean, hey, don't get me wrong,\x01",
            "love can fill in any gap in age...\x02\x03",

            "You'd think that'd mean I'd have a shot,\x01",
            "though. *sigh*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1007F#4PUmmmmm. I kinda get the sense we're having\x01",
            "two different conversations, here.\x02\x03",

            "#1015FYou said you got called here by a letter\x01",
            "from someone? Who?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x109,
        (
            "#1060F#6PYeah, a letter delivered, addressed to me,\x01",
            "at Grancel Cathedral.\x02\x03",

            "The man who delivered it was a fairly\x01",
            "handsome middle-aged guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1019F#4PBut Joshua's the same age I am!\x02\x03",

            "Why would you ever think he's some old dude!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x109,
        (
            "#1064F#6PReally?\x02\x03",

            "#1061FUh, haha! Of course! I was, uh, wondering\x01",
            "what was up with that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#1007F#4PThat's my line...\x02\x03",

            "#1002FBut then, what the heck is going on?\x02\x03",

            "Wait, this is...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Really Just A Coincidence\x01",                       # 0
            "A Trap\x01",                                          # 1
            "The Middle-aged Guy Was Joshua's Disguise!\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1CF9"),
        (1, "loc_1D51"),
        (2, "loc_1D88"),
        (SWITCH_DEFAULT, "loc_1E2A"),
    )


    label("loc_1CF9")


    ChrTalk(    #78
        0x109,
        "#1067F#6PI, uh, guess that isn't impossible, but...\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_1E2A")

    label("loc_1D51")

    OP_2B(0x8E, 0x3)

    ChrTalk(    #79
        0x109,
        "#1063F#6PHuh?\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_1E2A")

    label("loc_1D88")

    OP_2B(0x8E, 0x1)

    ChrTalk(    #80
        0x109,
        (
            "#1064F#6PUh... I guess that's...possible?\x02\x03",

            "#1063FSo your Joshua's a master of disguise?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        "#1015F#4PUm...kinda? Maybe?\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_1E2A")

    label("loc_1E2A")

    OP_20(0x3E8)

    def lambda_1E35():
        OP_6B(2850, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1E35)
    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrPos(0xB, 11930, 10500, -73000, 90)
    SetChrPos(0xC, -11930, 10500, -62000, 270)
    OP_22(0xCF, 0x1, 0xA)
    OP_43(0xB, 0x3, 0x0, 0x2)
    OP_43(0xC, 0x3, 0x0, 0x2)

    def lambda_1EA4():
        OP_8E(0xFE, 0xFFFFFB96, 0x2134, 0xFFFEE2D8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1EA4)

    def lambda_1EBF():
        OP_8E(0xFE, 0xFFFFFDDA, 0x2134, 0xFFFF0DD0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1EBF)
    Sleep(100)
    OP_24(0xCF, 0x1E)
    Sleep(100)
    OP_24(0xCF, 0x32)
    Sleep(100)
    OP_24(0xCF, 0x3C)
    Sleep(100)
    OP_24(0xCF, 0x46)
    Sleep(100)
    OP_24(0xCF, 0x50)
    Sleep(100)
    OP_24(0xCF, 0x5A)
    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_24(0xCF, 0x64)
    WaitChrThread(0xC, 0x1)

    def lambda_1F35():
        OP_97(0xFE, 0xFFFFFBF0, 0xFFFEF700, 0x57E40, 0x2AF8, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_1F35)
    WaitChrThread(0xB, 0x1)

    def lambda_1F56():
        OP_97(0xFE, 0xFFFFFBF0, 0xFFFEF700, 0x57E40, 0x2AF8, 0x1)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1F56)
    OP_1D(0x35)
    OP_8C(0x101, 0, 600)
    OP_8C(0x109, 180, 600)

    ChrTalk(    #82 op#A
        0x101,
        "#1020F#2P#12AWhat...?\x02",
    )

    Sleep(1200)

    ChrTalk(    #83 op#A
        0x109,
        "#1063F#3P#12AI was afraid of that.\x02",
    )

    Sleep(1200)

    def lambda_1FCD():
        OP_95(0xFE, 0x0, 0x0, 0x1F4, 0xFA, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FCD)
    SetChrChipByIndex(0x101, 4)
    SetChrSubChip(0x101, 0)
    OP_22(0xD5, 0x0, 0x64)
    Sleep(100)

    def lambda_1FFF():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0xFA, 0x1770)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1FFF)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 5)
    SetChrSubChip(0x109, 0)
    WaitChrThread(0xB, 0x0)
    OP_8C(0xB, 0, 400)
    WaitChrThread(0xC, 0x0)
    OP_8C(0xC, 180, 400)

    def lambda_2044():
        OP_91(0xFE, 0x0, 0xFFFFFA24, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2044)

    def lambda_205F():
        OP_91(0xFE, 0x0, 0xFFFFFA24, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_205F)
    Sleep(500)

    def lambda_207F():
        OP_91(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_207F)

    def lambda_209A():
        OP_91(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_209A)
    Sleep(1000)

    ChrTalk(    #84
        0x109,
        (
            "#1067F#6PAww, man.\x01",
            "So much for coincidences...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        "#1005F#6PHere they come!\x02",
    )

    CloseMessageWindow()

    def lambda_210C():
        OP_6B(2100, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_210C)

    def lambda_211C():
        OP_8E(0xFE, 0xFFFFFDA8, 0x1C52, 0xFFFEF278, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_211C)

    def lambda_2137():
        OP_8E(0xFE, 0xFFFFFE70, 0x1C52, 0xFFFEFDF4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2137)
    WaitChrThread(0xB, 0x1)
    OP_23(0xCF)
    Battle(0x45A, 0x0, 0x1, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_216D"),
        (SWITCH_DEFAULT, "loc_2172"),
    )


    label("loc_216D")

    OP_B4(0x0)
    Jump("loc_2172")

    label("loc_2172")

    Call(0, 8)
    Return()

    # Function_7_1370 end

    def Function_8_2177(): pass

    label("Function_8_2177")

    EventBegin(0x0)
    OP_7E(0xFC7C, 0x1F4, 0x384, 0x96, 0x0)
    FadeToDark(0, 0, -1)
    OP_1D(0x51)
    Sleep(500)
    OP_6D(-430, 7250, -70700, 0)
    OP_67(0, 8210, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(134000, 0)
    OP_6E(334, 0)
    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrPos(0x101, -2170, 7250, -68100, 180)
    SetChrPos(0x109, -180, 7250, -67940, 180)
    SetChrPos(0xB, -2080, 8500, -72570, 0)
    SetChrPos(0xC, 800, 8500, -72820, 0)
    OP_43(0xB, 0x3, 0x0, 0x2)
    OP_43(0xC, 0x3, 0x0, 0x2)
    OP_22(0xCF, 0x1, 0x64)
    OP_24(0xCF, 0x64)
    SetChrChipByIndex(0x101, 4)
    SetChrChipByIndex(0x109, 5)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x109, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #86
        0x101,
        "#1005F#5PThese're...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x109,
        "#1063FGah!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 400)
    OP_8C(0xC, 270, 400)

    def lambda_22BA():
        OP_6D(-6930, 7250, -69700, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_22BA)

    def lambda_22D2():
        OP_8E(0xFE, 0xFFFFB9CE, 0x280A, 0xFFFEE8DC, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_22D2)
    Sleep(200)

    def lambda_22F2():
        OP_8E(0xFE, 0xFFFFB9CE, 0x280A, 0xFFFEE8DC, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_22F2)

    def lambda_230D():

        label("loc_230D")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_230D")

    QueueWorkItem2(0x101, 2, lambda_230D)

    def lambda_231E():

        label("loc_231E")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_231E")

    QueueWorkItem2(0x109, 2, lambda_231E)
    OP_24(0xCF, 0x5A)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    OP_24(0xCF, 0x5A)
    Sleep(150)
    OP_24(0xCF, 0x50)
    Sleep(150)
    OP_24(0xCF, 0x46)
    Sleep(100)
    OP_24(0xCF, 0x3C)
    Sleep(100)
    OP_24(0xCF, 0x32)
    Sleep(100)
    OP_24(0xCF, 0x28)
    Sleep(100)
    OP_24(0xCF, 0x1E)
    Sleep(100)
    OP_24(0xCF, 0x14)
    Sleep(100)
    OP_24(0xCF, 0xA)
    Sleep(100)
    OP_23(0xCF)

    ChrTalk(    #88
        0x101,
        "#1004F#6PWaaah!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x2)
    OP_44(0x109, 0x2)
    SetChrChipByIndex(0x101, 65535)

    def lambda_23C5():
        OP_8E(0xFE, 0xFFFFEEB2, 0x1C52, 0xFFFEF58E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23C5)
    Sleep(200)
    SetChrChipByIndex(0x109, 65535)

    def lambda_23EA():
        OP_8E(0xFE, 0xFFFFEDEA, 0x1C52, 0xFFFEF066, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_23EA)
    WaitChrThread(0x109, 0x1)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x109, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_6D(-4350, 7250, -69080, 1500)
    OP_63(0x101)
    OP_63(0x109)

    ChrTalk(    #89
        0x101,
        (
            "#1020F#6PWhat the heck was THAT?\x02\x03",

            "And those things... They were\x01",
            "less like monsters and more like...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x109,
        (
            "#1063F#6PYeah, they were kind of like the\x01",
            "archaisms in Grancel Castle's sealed\x01",
            "ruins. Puppet weapons of some sort.\x02\x03",

            "#1065FTrick is, they looked like they were\x01",
            "built recently.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 400)

    ChrTalk(    #91
        0x101,
        "#1015F#6PWhat do you mean?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 400)

    ChrTalk(    #92
        0x109,
        (
            "#1060FWell, archaisms are ancient, and you\x01",
            "could tell by the wear, right?\x02\x03",

            "But looking at them, the way the\x01",
            "orbments were made... Those things\x01",
            "were modern.\x02\x03",

            "They're just about as good as the ones\x01",
            "from down below, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1007F#6POh, I see...\x02\x03",

            "...\x02\x03",

            "#1019FWait. A. Second.\x01",
            "How do YOU know about what's\x01",
            "beneath Grancel Castle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x109,
        "#1064FERK!\x02",
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)
    SetChrPos(0xD, -1180, 7250, -58700, 180)
    SetChrPos(0x8, -570, 7250, -57570, 180)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #95
        0x8,
        "Man's Voice",
        "#2PHey! Who goes there?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x109, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2783():

        label("loc_2783")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_2783")

    QueueWorkItem2(0x101, 2, lambda_2783)

    def lambda_2794():

        label("loc_2794")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_2794")

    QueueWorkItem2(0x109, 2, lambda_2794)
    Fade(1000)
    OP_6D(-2190, 7250, -67000, 0)
    OP_67(0, 7650, -10000, 0)
    OP_6B(2420, 0)
    OP_6C(89000, 0)
    OP_6E(334, 0)
    OP_6E(334, 0)

    def lambda_27F0():
        OP_8E(0xFE, 0xFFFFFAA6, 0x1C52, 0xFFFF031D, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_27F0)
    Sleep(300)

    def lambda_2810():
        OP_8E(0xFE, 0xFFFFFDE4, 0x1C52, 0xFFFF0614, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2810)
    WaitChrThread(0xD, 0x1)
    OP_8C(0xD, 225, 400)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 225, 400)
    OP_44(0x101, 0x2)
    OP_44(0x109, 0x2)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #96
        0x101,
        "#1004F#2PAh, a soldier!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xD,
        "#6PThought I heard something...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xD,
        "#6PYou two! What are you doing here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#1020F#2PW-Wait a moment, please!\x02\x03",

            "We were just attacked by strange machines...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xD,
        "#6PStrange what...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x109,
        (
            "#1062FSorry t'have caused such a disturbance, sir.\x02\x03",

            "Actually, the little lady here's a member\x01",
            "of the Bracer Guild, you see?\x02\x03",

            "We're in the middle of investigatin' something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#1004F#2PEr?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xD,
        "#6PA bracer? Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x109,
        (
            "#1060FEstelle, make with the notebook and badge,\x01",
            "why don'cha? Let the nice man know he\x01",
            "doesn't need to shoot us in the face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#1015F#2POh, uh, sure.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #106
        "\x07\x05Estelle showed Warrant Officer Graves her notebook and badge.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #107
        0xD,
        "#6PHmm... They look real, at least.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xD,
        "#6PSo what's this 'something' you're investigating?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x109,
        (
            "#1065FA terrorist group who call themselves the\x01",
            "Society of Ouroboros.\x02\x03",

            "They've been conducting 'experiments' and\x01",
            "causing trouble all over the country recently.\x02\x03",

            "#1063FWe were pursuing a lead on them when\x01",
            "we got attacked by these machines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        "#1026F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xD,
        (
            "#6PWait, come to think of it...HQ did tell\x01",
            "us to keep an ear open for things relating\x01",
            "to a 'society'...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xD,
        (
            "#6PSo are those guys out on the roads also\x01",
            "with this group, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1020F#2PWait, hold on!\x02\x03",

            "Someone showed up on the roads?\x01",
            "What do you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xD,
        (
            "#6PWe just got word from the squad guarding\x01",
            "the Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xD,
        "#6PThey were attacked by an armed group.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #116
        0x101,
        "#1005F#2PWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xD,
        (
            "#6PGood news is, Lieutenant Colonel Cid and company\x01",
            "managed to send 'em packing with no trouble!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xD,
        (
            "#6PAt the moment, they've got the roads closed\x01",
            "and they're hunting the attackers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x109,
        (
            "#1068FOhhhh, great.\x01",
            "Things really are getting serious.\x02\x03",

            "We should probably book it back to the\x01",
            "guildhouse, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        "#1026F#2PEr, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xD,
        (
            "#6PYeah, those guys might be the same ones\x01",
            "you're after.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xD,
        "#6PAll right! We'll keep an eye on this area.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xD,
        (
            "#6PYou two get back to the capital guildhouse,\x01",
            "go on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x109,
        (
            "#1061FThanks, sir!\x02\x03",

            "#1062FC'mon, Estelle. Let's get back.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_305C():

        label("loc_305C")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_305C")

    QueueWorkItem2(0x101, 2, lambda_305C)

    ChrTalk(    #125
        0x101,
        "#1020F#5PWait, hold on a...\x02",
    )

    CloseMessageWindow()

    def lambda_308E():

        label("loc_308E")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_308E")

    QueueWorkItem2(0xD, 2, lambda_308E)

    def lambda_309F():

        label("loc_309F")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_309F")

    QueueWorkItem2(0x8, 2, lambda_309F)
    OP_43(0x109, 0x0, 0x0, 0xA)
    Sleep(1500)
    OP_44(0x101, 0x2)
    OP_43(0x101, 0x0, 0x0, 0xB)
    OP_6D(-2110, 7250, -63810, 3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x1)
    OP_44(0x101, 0x1)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0610   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_8_2177 end

    def Function_9_30F7(): pass

    label("Function_9_30F7")

    OP_8E(0xFE, 0xFFFFFD3A, 0x1C52, 0xFFFEF9E4, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_9_30F7 end

    def Function_10_3113(): pass

    label("Function_10_3113")

    OP_8E(0xFE, 0xFFFFF51A, 0x1C52, 0xFFFEF84A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF8F8, 0x1C52, 0xFFFF30D0, 0xBB8, 0x0)
    Return()

    # Function_10_3113 end

    def Function_11_313C(): pass

    label("Function_11_313C")

    OP_8E(0xFE, 0xFFFFF4B6, 0x1C52, 0xFFFEFC82, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF8F8, 0x1C52, 0xFFFF30D0, 0xBB8, 0x0)
    Return()

    # Function_11_313C end

    SaveToFile()

Try(main)
