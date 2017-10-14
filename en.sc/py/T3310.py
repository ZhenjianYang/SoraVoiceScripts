from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3310   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3310.x',
        MapIndex            = 1,
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Private Brahm',                        # 9
        'Private Henning',                      # 10
        'CWO Pace',                             # 11
        'Corporal Gerwin',                      # 12
        'Rufus',                                # 13
        'Bruno',                                # 14
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
        'ED6_DT07/CH01310 ._CH',             # 02
        'ED6_DT07/CH01300 ._CH',             # 03
        'ED6_DT07/CH01270 ._CH',             # 04
        'ED6_DT07/CH01530 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
        'ED6_DT07/CH01310P._CP',             # 02
        'ED6_DT07/CH01300P._CP',             # 03
        'ED6_DT07/CH01270P._CP',             # 04
        'ED6_DT07/CH01530P._CP',             # 05
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
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
        InitFunctionIndex   = 6,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 5990,
        Z                   = 0,
        Y                   = 9340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclActor(
        TriggerX            = 7230,
        TriggerZ            = 0,
        TriggerY            = 9350,
        TriggerRange        = 400,
        ActorX              = 6990,
        ActorZ              = 1500,
        ActorY              = 11450,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -49710,
        TriggerZ            = 0,
        TriggerY            = 7160,
        TriggerRange        = 400,
        ActorX              = -51810,
        ActorZ              = 1500,
        ActorY              = 6820,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E2",          # 00, 0
        "Function_1_23E",          # 01, 1
        "Function_2_23F",          # 02, 2
        "Function_3_246",          # 03, 3
        "Function_4_35F",          # 04, 4
        "Function_5_EBE",          # 05, 5
        "Function_6_EC3",          # 06, 6
        "Function_7_187C",         # 07, 7
        "Function_8_1881",         # 08, 8
        "Function_9_1888",         # 09, 9
        "Function_10_188D",        # 0A, 10
        "Function_11_2821",        # 0B, 11
        "Function_12_31BC",        # 0C, 12
        "Function_13_4155",        # 0D, 13
        "Function_14_44A4",        # 0E, 14
    )


    def Function_0_1E2(): pass

    label("Function_0_1E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_200")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 3860, 0, 68230, 108)

    label("loc_200")

    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -51810, 0, 6820, 97)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 6990, 0, 11450, 189)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23D")
    ClearChrFlags(0xD, 0x80)

    label("loc_23D")

    Return()

    # Function_0_1E2 end

    def Function_1_23E(): pass

    label("Function_1_23E")

    Return()

    # Function_1_23E end

    def Function_2_23F(): pass

    label("Function_2_23F")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_2_23F end

    def Function_3_246(): pass

    label("Function_3_246")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_35B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2D4")

    ChrTalk(    #0
        0xFE,
        (
            "Apparently there was an earthquake\x01",
            "at the Sanktheim Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Heard there wasn't much damage, though.\x01",
            "Thank Aidios.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35B")

    label("loc_2D4")


    ChrTalk(    #2
        0xFE,
        (
            "Seems like even the Sanktheim Gate had\x01",
            "an earthquake not long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Gotta say, it's getting kinda creepy\x01",
            "having this many.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_35B")

    TalkEnd(0xD)
    Return()

    # Function_3_246 end

    def Function_4_35F(): pass

    label("Function_4_35F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_370")
    Call(0, 12)
    Return()

    label("loc_370")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_46A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3E8")

    ChrTalk(    #4
        0x9,
        (
            "Anyway, I'm just glad the earthquakes\x01",
            "have stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        "Now we can go back to taking it easy!\x02",
    )

    CloseMessageWindow()
    Jump("loc_467")

    label("loc_3E8")


    ChrTalk(    #6
        0x9,
        "It seems like the earthquakes have stopped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        (
            "An announcement from the central factory\x01",
            "said so, so it must be true!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_467")

    Jump("loc_EBA")

    label("loc_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_575")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_50F")

    ChrTalk(    #8
        0x9,
        "Apparently we got an emergency communication.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        (
            "I'd like to know what it said, but at the same\x01",
            "time, I kinda don't wanna know what it said.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_572")

    label("loc_50F")


    ChrTalk(    #10
        0x9,
        (
            "Seems the commander got an emergency\x01",
            "communication.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x9,
        "I-I wonder what's happened now...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_572")

    Jump("loc_EBA")

    label("loc_575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_6ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5F0")

    ChrTalk(    #12
        0x9,
        (
            "That suspicious guy I saw, and the constant\x01",
            "earthquakes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        "Feels like something's gonna happen.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EA")

    label("loc_5F0")


    ChrTalk(    #14
        0x9,
        (
            "Man, it's been crazy. Even the Sanktheim Gate\x01",
            "had an earthquake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        (
            "With them going on for this long, it can't\x01",
            "just be a coincidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        (
            "That suspicious guy I saw, and the constant\x01",
            "earthquakes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x9,
        "Feels like something's gonna happen.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_6EA")

    Jump("loc_EBA")

    label("loc_6ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 1)), scpexpr(EXPR_END)), "loc_782")

    ChrTalk(    #18
        0xFE,
        (
            "...Ahhh, just talking about it all makes\x01",
            "me feel better. Sometimes you just gotta\x01",
            "vent, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "Give my best to the commander.\x02",
    )

    CloseMessageWindow()
    Jump("loc_EBA")

    label("loc_782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 4)), scpexpr(EXPR_END)), "loc_D37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 5)), scpexpr(EXPR_END)), "loc_816")

    ChrTalk(    #20
        0xFE,
        (
            "The earthquake was so strong that everything\x01",
            "else was just chased right out of my head!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "Sorry I couldn't be of any help.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D34")

    label("loc_816")


    ChrTalk(    #22
        0xFE,
        "What, what is it?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8A0")

    ChrTalk(    #23
        0x106,
        (
            "#050FWe're with the Bracer Guild.\x02\x03",

            "We'd like to ask you about the earthquake\x01",
            "three days ago.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_905")

    label("loc_8A0")


    ChrTalk(    #24
        0x103,
        (
            "#020FWe're with the Bracer Guild.\x02\x03",

            "We'd like to ask about the earthquake\x01",
            "three days ago.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    label("loc_905")


    ChrTalk(    #25
        0xFE,
        "Ah, that... It was pretty scary!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "It was my first earthquake, so I didn't\x01",
            "really understand what was going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "So, are you guys here to investigate\x01",
            "the damage it caused or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1015FNo, not quite.\x02\x03",

            "Actually...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #29
        (
            "\x07\x05Estelle asked if anything odd had happened before or after\x01",
            "the earthquake.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #30
        0xFE,
        "Hmm... Odd events, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Really, the oddest thing was the\x01",
            "earthquake itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1016FW-Well, I'm sure that's true, but...\x02\x03",

            "...I'm asking if there was anything curious\x01",
            "ASIDE from the earthquake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "Mmm, sorry, there's nothing I really remember.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "The earthquake was so strong that everything\x01",
            "else just flew right out of my head!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#1007FAww... Okay.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C68")

    ChrTalk(    #36
        0x106,
        (
            "#053FIn that case, not much point in asking\x01",
            "anything else.\x02\x03",

            "#051FSorry to bother you.\x01",
            "You can get back to work.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_CE4")

    label("loc_C68")


    ChrTalk(    #37
        0x103,
        (
            "#026FGuess there's not much point\x01",
            "in asking anything else.\x02\x03",

            "#027FSorry to bother you.\x01",
            "You can get back to work.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    label("loc_CE4")


    ChrTalk(    #38
        0xFE,
        "Yeah, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "If you need anything else, though,\x01",
            "just say the word!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x140D)

    label("loc_D34")

    Jump("loc_EBA")

    label("loc_D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DEF")

    ChrTalk(    #40
        0xFE,
        (
            "If you want to pass through, they'll do the\x01",
            "processing in the building on the other side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Just ask the guy on duty inside and he should\x01",
            "stamp you guys right quick.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EBA")

    label("loc_DEF")


    ChrTalk(    #42
        0xFE,
        "Hey, how's it going?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "If you want to pass through, they'll do the\x01",
            "processing in the building on the other side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Just ask the guy on duty inside and he should\x01",
            "stamp you guys right quick.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_EBA")

    TalkEnd(0x9)
    Return()

    # Function_4_35F end

    def Function_5_EBE(): pass

    label("Function_5_EBE")

    Call(0, 6)
    Return()

    # Function_5_EBE end

    def Function_6_EC3(): pass

    label("Function_6_EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED0")
    Call(0, 11)
    Return()

    label("loc_ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE9")
    Call(0, 13)
    Return()

    label("loc_EE9")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_109D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 1)), scpexpr(EXPR_END)), "loc_F67")

    ChrTalk(    #45
        0xA,
        (
            "My soldiers are concerned over\x01",
            "the stuck gate, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xA,
        "Compared to Haken Gate, this is paradise!\x02",
    )

    CloseMessageWindow()
    Jump("loc_109A")

    label("loc_F67")


    ChrTalk(    #47
        0xA,
        (
            "My soldiers are concerned over\x01",
            "the stuck gate, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xA,
        "...compared to Haken Gate, this is paradise!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        (
            "I don't think there's anything to get so\x01",
            "worked up about, personally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xA,
        "Here, read a book or something and relax!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #51
        "\x07\x00Received #582i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x246, 1)
    OP_A2(0x10C1)

    label("loc_109A")

    Jump("loc_1878")

    label("loc_109D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_12D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11EA")

    ChrTalk(    #52
        0xA,
        "Hey, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        (
            "Thanks to that generator of yours,\x01",
            "communications are back up again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xA,
        (
            "It's not much, but we've had some\x01",
            "reinforcements sent from the fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        (
            "I've directed them over to Elmo Village\x01",
            "for patrols.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xA,
        (
            "That place is kind of far from Zeiss,\x01",
            "so the citizens must be pretty nervous.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_12CD")

    label("loc_11EA")


    ChrTalk(    #57
        0xA,
        (
            "I've sent the reinforcement soldiers\x01",
            "to Elmo Village for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xA,
        (
            "That place is kind of far from Zeiss,\x01",
            "so the citizens must be pretty nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xA,
        (
            "If they see us Royal Army soldiers,\x01",
            "they should be able to relax a bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12CD")

    Jump("loc_1878")

    label("loc_12D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1460")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_136E")

    ChrTalk(    #60
        0xA,
        (
            "We've got to go over our security in\x01",
            "preparation for the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xA,
        (
            "I imagine we'll be taking it\x01",
            "easy as ever here, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_145D")

    label("loc_136E")


    ChrTalk(    #62
        0xA,
        (
            "The whole earthquake thing seems\x01",
            "to have finally settled down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        (
            "What a strange, incomprehensible event.\x01",
            "We'll leave solving that one to the guild!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xA,
        (
            "We've got to go over our security in\x01",
            "preparation for the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_145D")

    Jump("loc_1878")

    label("loc_1460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1587")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_14CF")

    ChrTalk(    #65
        0xA,
        "As I recall, the general is at the fortress.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        "I'm sure he'll get through it somehow.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1584")

    label("loc_14CF")


    ChrTalk(    #67
        0xA,
        "So Leiston Fortress was attacked, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        "We just received word ourselves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xA,
        "I think the general's there...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xA,
        (
            "But I'm sure he'll get through it,\x01",
            "somehow or another.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1584")

    Jump("loc_1878")

    label("loc_1587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_16FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_162D")

    ChrTalk(    #71
        0xA,
        (
            "Doesn't seem like there was any severe\x01",
            "damage to the Sanktheim Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xA,
        (
            "Still, the fact that they've gone on\x01",
            "this long is kind of disturbing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F9")

    label("loc_162D")


    ChrTalk(    #73
        0xA,
        "Hey, bracers. Good work the other day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xA,
        (
            "It doesn't seem like there was any significant\x01",
            "damage to the Sanktheim Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "Still, the fact that they've gone on\x01",
            "this long is kind of disturbing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_16F9")

    Jump("loc_1878")

    label("loc_16FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 2)), scpexpr(EXPR_END)), "loc_17D2")

    ChrTalk(    #76
        0xA,
        (
            "I don't know if he's connected to\x01",
            "the earthquakes, but that suspicious\x01",
            "man is really bothering me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xA,
        "I'll have to report him to Leiston Fortress.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xA,
        (
            "You can handle reporting to the guild,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1878")

    label("loc_17D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 3)), scpexpr(EXPR_END)), "loc_1878")

    ChrTalk(    #79
        0xA,
        (
            "I haven't heard any particular reports\x01",
            "of suspicious persons or events, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xA,
        "...perhaps one of my men saw something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xA,
        "Feel free to ask around.\x02",
    )

    CloseMessageWindow()

    label("loc_1878")

    TalkEnd(0xA)
    Return()

    # Function_6_EC3 end

    def Function_7_187C(): pass

    label("Function_7_187C")

    Call(0, 8)
    Return()

    # Function_7_187C end

    def Function_8_1881(): pass

    label("Function_8_1881")

    TalkBegin(0xB)
    TalkEnd(0xB)
    Return()

    # Function_8_1881 end

    def Function_9_1888(): pass

    label("Function_9_1888")

    Call(0, 10)
    Return()

    # Function_9_1888 end

    def Function_10_188D(): pass

    label("Function_10_188D")

    TalkBegin(0xC)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Rest\x01",       # 2
            "Leave\x01",      # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F2")
    OP_0D()
    OP_A9(0xAB)
    OP_56(0x0)
    TalkEnd(0xC)
    Return()

    label("loc_18F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190B")
    OP_0D()
    OP_A9(0xAA)
    OP_56(0x0)
    TalkEnd(0xC)
    Return()

    label("loc_190B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_191C")
    TalkEnd(0xC)
    Return()

    label("loc_191C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1A68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19FE")

    ChrTalk(    #82
        0xC,
        (
            "The commander said something about\x01",
            "this whole incident while he was\x01",
            "eating...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xC,
        (
            "Thinking about it, I wonder what's\x01",
            "really happening at Haken Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xC,
        "Maybe it would be better if I didn't know...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1A65")

    label("loc_19FE")


    ChrTalk(    #85
        0xC,
        (
            "I wonder what's really happening\x01",
            "at Haken Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xC,
        "Maybe it would be better if I didn't know...\x02",
    )

    CloseMessageWindow()

    label("loc_1A65")

    Jump("loc_281D")

    label("loc_1A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1BB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B3E")

    ChrTalk(    #87
        0xC,
        "Really, doesn't this just beat all?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xC,
        (
            "When I went and looked, the bloody gate\x01",
            "was stuck open!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xC,
        (
            "I was wondering if we'd started permitting\x01",
            "free entry from the Republic or something.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1BB1")

    label("loc_1B3E")


    ChrTalk(    #90
        0xC,
        "Borders are created by people, in the end.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xC,
        (
            "There aren't any gates here or anything,\x01",
            "'cept what we build.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB1")

    Jump("loc_281D")

    label("loc_1BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1F7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x286, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1C71")

    ChrTalk(    #92
        0xC,
        (
            "Seems like there was an earthquake\x01",
            "over at Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xC,
        (
            "Wonder if that's some long-delayed punishment\x01",
            "for the coup d'etat...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D64")

    label("loc_1C71")


    ChrTalk(    #94
        0xC,
        (
            "Seems like there was an earthquake\x01",
            "over at Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xC,
        (
            "Earthquakes just hitting military facilities?\x01",
            "Real fishy, if you ask me. And...kind of\x01",
            "creepy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xC,
        (
            "Wonder if that's some long-delayed punishment\x01",
            "for the coup d'etat...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1D64")

    Jump("loc_1DDB")

    label("loc_1D67")


    ChrTalk(    #97
        0xC,
        "*sigh* No meals today, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xC,
        (
            "On one hand it's kind of a relief,\x01",
            "and on the other hand it's kind of\x01",
            "a pity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDB")

    Jump("loc_1F7C")

    label("loc_1DDE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E24")
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xC)

    ChrTalk(    #99
        0xC,
        "Ahhh, a customer?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E79")

    label("loc_1E24")


    ChrTalk(    #100
        0xC,
        "Yes...?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x108, 500)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xC)

    ChrTalk(    #101
        0xC,
        "Ah, you there, are you...?!\x02",
    )

    CloseMessageWindow()

    label("loc_1E79")


    ChrTalk(    #102
        0x108,
        (
            "#071FHaha, it's been a while.\x02\x03",

            "I was in the area, so I dropped by for a visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xC,
        "W-Would you like a meal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x108,
        (
            "#070FNo, I'll just have a snack, thanks.\x02\x03",

            "I can't stay long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xC,
        (
            "Ah, I see... Well, make yourself\x01",
            "at home!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x108,
        "#070FYou bet I will.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1640)
    OP_A2(0x2)

    label("loc_1F7C")

    Jump("loc_281D")

    label("loc_1F7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2108")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2021")

    ChrTalk(    #107
        0xC,
        (
            "Seems like that really big guest\x01",
            "was from the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xC,
        (
            "I'm from there too, so I can tell\x01",
            "with just a glance. It's all in the\x01",
            "clothes!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2105")

    label("loc_2021")


    ChrTalk(    #109
        0xC,
        (
            "When was it that that really\x01",
            "big guy came around here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xC,
        (
            "He ate just as much as you'd expect\x01",
            "for someone his size.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xC,
        (
            "He cleaned me right out of a bunch\x01",
            "of ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xC,
        "Hahaha. I wonder if he'll come again.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1431)
    OP_A2(0x3)

    label("loc_2105")

    Jump("loc_281D")

    label("loc_2108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_224E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_21DD")

    ChrTalk(    #113
        0xC,
        (
            "As it is, we don't get many guests\x01",
            "these days...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xC,
        (
            "If rumors of this earthquake spread, we might\x01",
            "really charge headfirst into an age of winter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xC,
        "Hahaha. Maybe I should just hibernate!\x02",
    )

    CloseMessageWindow()
    Jump("loc_224B")

    label("loc_21DD")


    ChrTalk(    #116
        0xC,
        "The commander had a real scary look on his face.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xC,
        "I wonder if there's something going on again...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_224B")

    Jump("loc_281D")

    label("loc_224E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 4)), scpexpr(EXPR_END)), "loc_273A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_268D")
    OP_A2(0x3)
    OP_A2(0x140F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2277")
    OP_28(0x85, 0x1, 0x800)
    Jump("loc_2277")

    label("loc_2277")


    ChrTalk(    #118
        0xC,
        (
            "Hey, welcome.\x01",
            "Welcome to this totally ordinary bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        "#1000FUm, may I have a moment?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #120
        0xC,
        "Sure. What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        (
            "#1011FEr, so we're with the Bracer Guild.\x02\x03",

            "We'd like you to help with our\x01",
            "investigation a little. If you\x01",
            "can, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xC,
        (
            "No problem. Not like I have any\x01",
            "customers anyway!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #123
        (
            "\x07\x05Estelle asked if anything odd had happened before or after\x01",
            "the earthquake.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #124
        0xC,
        (
            "Hmm, sorry. I can only remember the\x01",
            "earthquake itself. Heck of a surprise,\x01",
            "that was!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xC,
        (
            "When it suddenly hit, I was like, GRAAAAH!\x01",
            "I was shocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x105,
        (
            "#044FSo was there nothing that caught your\x01",
            "attention before or after the earthquake?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x105, 400)

    ChrTalk(    #127
        0xC,
        (
            "Nothing particularly different from\x01",
            "the norm, no.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xC,
        (
            "I mean, I was in this bar the whole time,\x01",
            "so there wouldn't be a whole lot that\x01",
            "COULD happen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        "#1015FAh, yeah, of course.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #130
        0x105,
        (
            "#043FDoesn't seem like there are any leads\x01",
            "to follow here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xC,
        "Sorry I couldn't be of more help!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1016FNo, don't worry about it.\x02\x03",

            "#1000FThanks for your cooperation!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2737")

    label("loc_268D")


    ChrTalk(    #133
        0xC,
        (
            "I don't think there was anything unusual\x01",
            "to report, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xC,
        (
            "I mean, I was in this bar the whole time,\x01",
            "so there wouldn't be a whole lot that\x01",
            "COULD happen...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2737")

    Jump("loc_281D")

    label("loc_273A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27BE")
    OP_A2(0x3)

    ChrTalk(    #135
        0xC,
        "Well, well, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xC,
        "As you can see, we're a completely ordinary bar.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xC,
        "Please, make yourselves at home!\x02",
    )

    CloseMessageWindow()
    Jump("loc_281D")

    label("loc_27BE")


    ChrTalk(    #138
        0xC,
        (
            "Hey, welcome.\x01",
            "Welcome to this totally ordinary bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xC,
        "Please, make yourselves at home!\x02",
    )

    CloseMessageWindow()

    label("loc_281D")

    TalkEnd(0xC)
    Return()

    # Function_10_188D end

    def Function_11_2821(): pass

    label("Function_11_2821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2832")
    Call(0, 14)

    label("loc_2832")

    EventBegin(0x0)
    OP_4A(0xA, 255)
    Fade(1000)
    SetChrPos(0x101, -49720, 0, 6390, 270)
    SetChrPos(0xF7, -49720, 0, 7460, 270)
    SetChrPos(0x104, -48400, 0, 7020, 270)
    SetChrPos(0x105, -49010, 0, 5660, 270)
    OP_6D(-50310, 0, 6810, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #140
        0xA,
        (
            "#6PAh, you're the bracers the guild\x01",
            "called ahead about, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xA,
        (
            "#6PHere to investigate the earthquake,\x01",
            "from what Ms. Kilika said on the phone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1004FAh, yeah, that's right.\x02\x03",

            "#1016FWow, I keep forgetting how,\x01",
            "uh, thorough Kilika is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xA,
        (
            "#6PHahah! She even keeps US on\x01",
            "our toes every now and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xA,
        "#6PAnyway, we'll do everything we can to help.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2A8A")

    ChrTalk(    #145
        0x106,
        (
            "#051FCheers.\x02\x03",

            "To start with, how about you explain\x01",
            "how the earthquake went down?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B00")

    label("loc_2A8A")


    ChrTalk(    #146
        0x103,
        (
            "#020FWe appreciate that, thank you.\x02\x03",

            "Let's start with your account\x01",
            "of what happened during the\x01",
            "earthquake, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B00")


    ChrTalk(    #147
        0xA,
        "#6PWell, let's see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xA,
        (
            "#6PThe earthquake happened three\x01",
            "days ago, at roughly 1700 hours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xA,
        (
            "#6PThe quake itself wasn't all that strong,\x01",
            "and it only lasted ten seconds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xA,
        (
            "#6PStill, though, earthquakes rarely ever\x01",
            "happen around here. Some of my\x01",
            "men are spooked, let me tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xA,
        "#6PThe part that spooked me, though...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xA,
        (
            "#6POnce I contacted Command\x01",
            "at Leiston Fortress to report...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x105,
        (
            "#043F...They told you that no other part\x01",
            "of the region had experienced an\x01",
            "earthquake, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xA,
        "#6PExactly right, miss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xA,
        (
            "#6PAnd it wasn't just Leiston. Even Sanktheim\x01",
            "Gate didn't feel anything. And they're\x01",
            "practically up the damn road!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xA,
        (
            "#6PI called in to Zeiss and Elmo, and\x01",
            "learned they'd felt nothing either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        (
            "#1002FIt's like Kilika said...\x02\x03",

            "Speaking of which, did you hear there\x01",
            "was an earthquake in Zeiss today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xA,
        "#6PYeah, I heard about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xA,
        (
            "#6PAnd that's the thing. We didn't feel\x01",
            "so much as a wobble here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x104,
        (
            "#035F#4PLocalized earthquakes that only\x01",
            "strike small, specific areas?\x02\x03",

            "#030FNot what I would call the most\x01",
            "natural thing in the world.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2FD0")

    ChrTalk(    #161
        0x106,
        (
            "#053FWell, that covers the quake.\x02\x03",

            "#050FAnything else happen that caught\x01",
            "your attention aside from that?\x02\x03",

            "Like, did you see anyone strange?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3063")

    label("loc_2FD0")


    ChrTalk(    #162
        0x103,
        (
            "#026FSo that's the earthquake, then.\x02\x03",

            "#022FDid anything else...'out of place'\x01",
            "happen around that time?\x02\x03",

            "Was anyone strange seen, for example?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3063")


    ChrTalk(    #163
        0xA,
        (
            "#6PHm. No, I've heard no meaningful\x01",
            "reports from my men...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xA,
        (
            "#6PIt's possible they saw something so\x01",
            "minor they didn't feel the need to\x01",
            "report it to me immediately, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xA,
        (
            "#6PFeel free to ask them some questions,\x01",
            "maybe jog their memories a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        (
            "#1006FSure! Thanks, sir!\x02\x03",

            "Let's go talk to the gate guards!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x140C)
    OP_28(0x85, 0x1, 0x40)
    OP_28(0x85, 0x1, 0x80)
    OP_4B(0xA, 255)
    EventEnd(0x0)
    Return()

    # Function_11_2821 end

    def Function_12_31BC(): pass

    label("Function_12_31BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31CD")
    Call(0, 14)

    label("loc_31CD")

    EventBegin(0x0)
    OP_4A(0x9, 255)
    Fade(1000)
    SetChrPos(0x105, 6250, 0, 69020, 270)
    SetChrPos(0x101, 5250, 0, 68630, 270)
    SetChrPos(0xF7, 5320, 0, 67540, 270)
    SetChrPos(0x104, 6400, 0, 67950, 270)
    OP_6D(4490, 0, 68450, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 5)), scpexpr(EXPR_END)), "loc_32BE")

    ChrTalk(    #167
        0x9,
        "#6POh, hey! Need something else?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        "#1002F#4PActually, yeah. We talked to Brahm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_34CF")

    label("loc_32BE")


    ChrTalk(    #169
        0x9,
        "#6POh, hello. What is it?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_335B")

    ChrTalk(    #170
        0x106,
        (
            "#051FHey, we're from the Bracer Guild.\x02\x03",

            "We've got a couple of questions about\x01",
            "that earthquake a few days back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E8")

    label("loc_335B")


    ChrTalk(    #171
        0x103,
        (
            "#020FHello, we're from the Bracer Guild.\x02\x03",

            "We have a few questions about\x01",
            "the earthquake that happened\x01",
            "three days ago, if you don't mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33E8")


    ChrTalk(    #172
        0x9,
        "#6POh, yeah... Gotta say, it was a surprise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x9,
        (
            "#6PFirst time I've ever been in an earthquake.\x01",
            "I had no idea what was going on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x9,
        "#6PSo what did you want to know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        (
            "#1002F#4PSo the thing is, we talked to Brahm,\x01",
            "and...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34CF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #176
        "\x07\x05Estelle explained what they heard from Brahm.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #177
        0x9,
        "#6POh, right, that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x9,
        "#6PYeah, I did ask him that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x105,
        (
            "#040FYou asked if someone had\x01",
            "passed through the gate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x9,
        "#6PYeah. Let me explain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x9,
        (
            "#6PSo four days ago, I'd just finished\x01",
            "my watch and was going off-duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x9,
        (
            "#6PJust as I was leaving, though, I saw\x01",
            "a weird man coming up the road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        "#1004F#4PA weird man?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x104,
        (
            "#030F#4PWas it a man garbed in white\x01",
            "with a mask, perchance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x9,
        "#6PA...mask?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x9,
        "#6PNo, no, he wasn't THAT weird.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x9,
        "#6PIt was a tall guy wearing a black suit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x9,
        "#6PHe also had these black glasses on.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37DB")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as heard Walter's info in Zeiss\x01",      # 0
            "Set as not heard\x01",                         # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_37C6"),
        (1, "loc_37CC"),
        (SWITCH_DEFAULT, "loc_37D2"),
    )


    label("loc_37C6")

    OP_A2(0x1480)
    Jump("loc_37D2")

    label("loc_37CC")

    OP_A3(0x1480)
    Jump("loc_37D2")

    label("loc_37D2")

    FadeToBright(300, 0)

    label("loc_37DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 0)), scpexpr(EXPR_END)), "loc_38D1")

    ChrTalk(    #189
        0x101,
        (
            "#1004F#4PBlack glasses!\x02\x03",

            "Those could be sunglasses, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x85, 0x1, 0x200)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_387C")

    ChrTalk(    #190
        0x106,
        (
            "#555FYeah.\x02\x03",

            "They're pretty rare, still, so\x01",
            "it's likely the same guy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38CE")

    label("loc_387C")


    ChrTalk(    #191
        0x103,
        (
            "#022FYes...\x02\x03",

            "Such glasses are fairly rare, so\x01",
            "it's very likely the same man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38CE")

    Jump("loc_3C8B")

    label("loc_38D1")


    ChrTalk(    #192
        0x101,
        (
            "#1015F#4PBlack...glasses?\x02\x03",

            "Like black frames or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x9,
        "#6PNo, that's the thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x9,
        "#6PThe lenses were stained dark.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        (
            "#1004F#4PUh. Wouldn't that mean you\x01",
            "couldn't see in front of you?\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x85, 0x1, 0x400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3A47")

    ChrTalk(    #196
        0x106,
        (
            "#555FWait, I've heard of those.\x01",
            "Called 'sunglasses,' I think.\x02\x03",

            "They're made to block strong sunlight.\x02\x03",

            "And you can still see through 'em,\x01",
            "apparently.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AFB")

    label("loc_3A47")


    ChrTalk(    #197
        0x103,
        (
            "#020FAh, wait, no. Those would be 'sunglasses.'\x02\x03",

            "They're designed to block strong sunlight.\x02\x03",

            "They ARE a little harder to see out of,\x01",
            "but it isn't impossible, as I understand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AFB")


    ChrTalk(    #198
        0x104,
        (
            "#035F#4PI have heard of them, but I rarely see them.\x02\x03",

            "#030FThe only prominent user of them I know of\x01",
            "is the leader of the greatest criminal cartel\x01",
            "in the capital of the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        "#1007F#4PWell, that sounds cheery.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #200
        0x101,
        (
            "#1019F#6PMore to the point... How, exactly,\x01",
            "do you know someone like that,\x01",
            "Olivier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x104,
        (
            "#031F#4PHeh... As they say, it takes a monster\x01",
            "to best understand a monster.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C8B")


    ChrTalk(    #202
        0x9,
        "#6PSunglasses, huh...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #203
        0x9,
        (
            "#6PAnyway. Just before I went on break,\x01",
            "I saw him coming up the road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x9,
        (
            "#6PMost of the travelers who pass\x01",
            "by here stop in at the bar, so\x01",
            "I figured I'd see him inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x105,
        "#043FI take it...he didn't?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x9,
        "#6PYeah, that's the thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x9,
        (
            "#6PHe didn't show, so I asked Brahm and\x01",
            "he said nobody'd passed through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x9,
        (
            "#6PAnd he's a lazy slob, but he ain't so bad\x01",
            "at his job that he'd just let a stranger\x01",
            "pass through without checking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x104,
        (
            "#030F#4PHmm. Perhaps he had business\x01",
            "at your barracks?\x02\x03",

            "He may have spoken to your\x01",
            "commander, for example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x9,
        (
            "#6PSee, I was pretty curious at that\x01",
            "point and asked the commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x9,
        (
            "#6PAnd he said nobody'd been in there\x01",
            "during that time period, either!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x9,
        (
            "#6PSo I have to wonder what\x01",
            "happened to that guy I saw.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x9,
        "#6PDoesn't seem like he came through...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x101,
        (
            "#1002F#4POkay, this IS really suspicious.\x02\x03",

            "We should tell Kilika about this.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4079")

    ChrTalk(    #215
        0x106,
        (
            "#053FYeah, no question.\x02\x03",

            "#051FThanks for sharing all this with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40E4")

    label("loc_4079")


    ChrTalk(    #216
        0x103,
        (
            "#020FYes, this seems like a good lead.\x02\x03",

            "#021FThank you for sharing all this\x01",
            "with us, Private Henning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40E4")


    ChrTalk(    #217
        0x9,
        "#6PHey, my pleasure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x9,
        "#6PI feel better having gotten it all off my chest!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1411)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_414E")
    OP_28(0x85, 0x1, 0x800)
    Jump("loc_414E")

    label("loc_414E")

    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    # Function_12_31BC end

    def Function_13_4155(): pass

    label("Function_13_4155")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4166")
    Call(0, 14)

    label("loc_4166")

    EventBegin(0x0)
    OP_4A(0xA, 255)
    Fade(1000)
    SetChrPos(0x101, -49720, 0, 6390, 270)
    SetChrPos(0xF7, -49720, 0, 7460, 270)
    SetChrPos(0x104, -48400, 0, 7020, 270)
    SetChrPos(0x105, -49010, 0, 5660, 270)
    OP_6D(-50310, 0, 6810, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #219
        0xA,
        "#6PHello again! Were my men helpful?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        "#1002FActually, yeah.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #221
        "\x07\x05Estelle told Pace about the man in sunglasses.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #222
        0xA,
        "#6PSo Henning saw a suspicious man?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xA,
        (
            "#6PHard to think he has something to do\x01",
            "with the earthquakes, but he sounds\x01",
            "suspicious regardless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xA,
        (
            "#6PI'll report this to Command at Leiston,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_43F1")

    ChrTalk(    #225
        0x106,
        "#050FYeah, thanks.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #226
        0x106,
        (
            "#051FAll right. Think that about wraps it up.\x02\x03",

            "Let's get back to Kilika and\x01",
            "tell her what we know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4474")

    label("loc_43F1")


    ChrTalk(    #227
        0x103,
        "#020FPlease do.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #228
        0x103,
        (
            "#526FAll right, I think we've learned\x01",
            "all we can here.\x02\x03",

            "Let's return to Kilika with what we know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4474")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #229
        0x101,
        "#1006F#4PAll right.\x02",
    )

    CloseMessageWindow()
    OP_4B(0xA, 255)
    OP_A2(0x1412)
    OP_28(0x85, 0x1, 0x1000)
    EventEnd(0x0)
    Return()

    # Function_13_4155 end

    def Function_14_44A4(): pass

    label("Function_14_44A4")

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
        (0, "loc_451D"),
        (1, "loc_4523"),
        (SWITCH_DEFAULT, "loc_4529"),
    )


    label("loc_451D")

    OP_A2(0x1200)
    Jump("loc_4529")

    label("loc_4523")

    OP_A2(0x1201)
    Jump("loc_4529")

    label("loc_4529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4537")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_453B")

    label("loc_4537")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_453B")

    Return()

    # Function_14_44A4 end

    SaveToFile()

Try(main)
