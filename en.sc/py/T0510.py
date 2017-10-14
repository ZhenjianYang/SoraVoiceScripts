from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0510   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0510.x',
        MapIndex            = 18,
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
        'Warrant Officer Dyne',                 # 9
        'CWO Ashton',                           # 10
        'CWO Irvine',                           # 11
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
        'ED6_DT07/CH01300 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01300P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
    )

    DeclNpc(
        X                   = 26800,
        Z                   = 0,
        Y                   = 29900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 29800,
        Z                   = 0,
        Y                   = -73400,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 29800,
        Z                   = 0,
        Y                   = -73400,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )


    DeclActor(
        TriggerX            = 28250,
        TriggerZ            = 0,
        TriggerY            = 29800,
        TriggerRange        = 500,
        ActorX              = 26800,
        ActorZ              = 1500,
        ActorY              = 29900,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28310,
        TriggerZ            = 0,
        TriggerY            = -73420,
        TriggerRange        = 500,
        ActorX              = 29850,
        ActorZ              = 1500,
        ActorY              = -73420,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 20640,
        TriggerZ            = 0,
        TriggerY            = 33000,
        TriggerRange        = 1000,
        ActorX              = 20640,
        ActorZ              = 1000,
        ActorY              = 33000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_186",          # 00, 0
        "Function_1_1A7",          # 01, 1
        "Function_2_1FD",          # 02, 2
        "Function_3_213",          # 03, 3
        "Function_4_218",          # 04, 4
        "Function_5_93E",          # 05, 5
        "Function_6_956",          # 06, 6
        "Function_7_1CBE",         # 07, 7
        "Function_8_1EA8",         # 08, 8
    )


    def Function_0_186(): pass

    label("Function_0_186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_190")
    Jump("loc_1A6")

    label("loc_190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A6")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_1A6")

    Return()

    # Function_0_186 end

    def Function_1_1A7(): pass

    label("Function_1_1A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FC")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 20640, 1000, 33000, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)

    label("loc_1FC")

    Return()

    # Function_1_1A7 end

    def Function_2_1FD(): pass

    label("Function_2_1FD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_212")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_1FD")

    label("loc_212")

    Return()

    # Function_2_1FD end

    def Function_3_213(): pass

    label("Function_3_213")

    Call(0, 4)
    Return()

    # Function_3_213 end

    def Function_4_218(): pass

    label("Function_4_218")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_381")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_309")

    ChrTalk(    #0
        0x8,
        (
            "Things are pretty tense at the Haken Gate,\x01",
            "too, it seems...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "Every time word comes in, they're all\x01",
            "on edge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "Even though we just signed a\x01",
            "non-aggression pact, we can't let\x01",
            "our guard down with the Empire.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_37E")

    label("loc_309")


    ChrTalk(    #3
        0x8,
        (
            "Things are pretty tense at the Haken Gate,\x01",
            "too, it seems...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "Every time word comes in, they're all\x01",
            "on edge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37E")

    Jump("loc_93A")

    label("loc_381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_449")

    ChrTalk(    #5
        0x8,
        (
            "Oh, it's the bracers. Thanks for all\x01",
            "your hard work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "Right now all the street lights are out, so\x01",
            "it's pretty dangerous on the highways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        "Be careful in your travels.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_4C2")

    label("loc_449")


    ChrTalk(    #8
        0x8,
        (
            "Right now all the street lights are out, so\x01",
            "it's pretty dangerous on the highways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        "Be careful in your travels.\x02",
    )

    CloseMessageWindow()

    label("loc_4C2")

    Jump("loc_93A")

    label("loc_4C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_600")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_551")

    ChrTalk(    #10
        0x8,
        (
            "I don't know all the details, but apparently\x01",
            "the dragon panic's over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        "Whatever the solution was, thank goodness!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FD")

    label("loc_551")


    ChrTalk(    #12
        0x8,
        (
            "I don't know all the details, but apparently\x01",
            "the dragon panic's over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        "Not much news makes it out here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "Ultimately, we don't know what was\x01",
            "settled or how.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_5FD")

    Jump("loc_93A")

    label("loc_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_78F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6B5")

    ChrTalk(    #15
        0x8,
        (
            "They can't even capture the dragon after\x01",
            "mobilizing half the damned air force...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "Looks like this isn't going to be resolved\x01",
            "unless Cassius takes command.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78C")

    label("loc_6B5")


    ChrTalk(    #17
        0x8,
        (
            "I hear even the airship forces were\x01",
            "fielded on the last mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "And with all that, they still couldn't\x01",
            "capture the dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "Looks like this isn't going to be resolved\x01",
            "unless Cassius takes command.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_78C")

    Jump("loc_93A")

    label("loc_78F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_93A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_82A")

    ChrTalk(    #20
        0x8,
        (
            "That deep fog really caused us\x01",
            "some serious headaches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "You wouldn't think something as simple\x01",
            "as fog could mess us up so bad...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93A")

    label("loc_82A")


    ChrTalk(    #22
        0x8,
        (
            "That deep fog really caused us\x01",
            "some serious headaches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "We didn't have sufficient troops\x01",
            "to patrol Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "We barely managed to respond with\x01",
            "reinforcements from the Haken Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "You wouldn't think something as simple\x01",
            "as fog could mess us up so bad...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_93A")

    TalkEnd(0x8)
    Return()

    # Function_4_218 end

    def Function_5_93E(): pass

    label("Function_5_93E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_951")
    Call(0, 7)
    Jump("loc_955")

    label("loc_951")

    Call(0, 6)

    label("loc_955")

    Return()

    # Function_5_93E end

    def Function_6_956(): pass

    label("Function_6_956")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1404")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x415, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1082")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E1")

    ChrTalk(    #26
        0x9,
        "Hey, you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x9,
        (
            "Thanks for your help during the fog incident.\x01",
            "Seriously, you were a huge help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A50")

    label("loc_9E1")


    ChrTalk(    #28
        0x9,
        "Hey, Estelle, Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        (
            "Thanks for your help during the fog incident.\x01",
            "Seriously, you were a huge help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A50")


    ChrTalk(    #30
        0x9,
        (
            "You in the middle of some kind of mission\x01",
            "today too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1000FYeah, we are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x102,
        (
            "#1040FHow are things here?\x02\x03",

            "From the looks of it, the guard post gate's\x01",
            "been left open...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #33
        0x9,
        (
            "Well, the gate's orbal-driven, so opening\x01",
            "and closing it's kind of difficult at the\x01",
            "moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "So in the interest of keeping traffic\x01",
            "flowing, we're leaving it open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#1007FI see... Not much of a choice, huh?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE3")

    ChrTalk(    #36
        0x103,
        (
            "#022FCircumstances certainly don't make this\x01",
            "easy, but I hope you're able to keep the\x01",
            "place secure until this blows over.\x02\x03",

            "I could definitely see some less scrupulous\x01",
            "people taking advantage of the situation to\x01",
            "sneak through.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x103, 400)
    Jump("loc_E7D")

    label("loc_CE3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D92")

    ChrTalk(    #37
        0x106,
        (
            "#057FCan't be easy to keep up with security, huh?\x02\x03",

            "You never know what kind of dangerous\x01",
            "guys might walk right on through without\x01",
            "you knowin' it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x106, 400)
    Jump("loc_E7D")

    label("loc_D92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E7D")

    ChrTalk(    #38
        0x108,
        (
            "#072FI hope you're able to keep the place\x01",
            "secure until the orbal mechanisms are\x01",
            "working again.\x02\x03",

            "Given the situation, it's easy to think\x01",
            "that some...less savory people might try\x01",
            "to take advantage and sneak in.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x108, 400)

    label("loc_E7D")


    ChrTalk(    #39
        0x9,
        (
            "Yeah, we got orders along those lines\x01",
            "from up above too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "It'll be a backbreaker of a job, but nothing\x01",
            "comes before the safety of the region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "We'll do our best to make sure everybody\x01",
            "here's as safe as they've ever been.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#1042FPlease do. We'll be counting on it.\x02\x03",

            "And in the meantime, we'll do what we can\x01",
            "to get this case closed and your gate up\x01",
            "and running.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #43
        0x9,
        (
            "Without your help, I fear we won't be\x01",
            "able to put an end to this mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        "So thank you for looking into the matter.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x20AE)
    Jump("loc_1401")

    label("loc_1082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1331")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1163")

    ChrTalk(    #45
        0x9,
        (
            "We've been tightening security at\x01",
            "our guard posts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        (
            "However, you bracers are free to\x01",
            "come and go as you please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "Without your help, I fear we won't be\x01",
            "able to put an end to this mess, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_132E")

    label("loc_1163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1293")

    ChrTalk(    #48
        0x9,
        (
            "The airship on the Milch Main Road was\x01",
            "apparently forced to make an emergency\x01",
            "landing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "Under normal circumstances,\x01",
            "a rescue force would be dispatched\x01",
            "from Leiston Fortress immediately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        "But regrettably, mobility is limited right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        "Their retrieval will have to wait.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_132E")

    label("loc_1293")


    ChrTalk(    #52
        0x9,
        (
            "I feel bad for the airship crew, but they're\x01",
            "going to have to hang in there a little longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "Mobility of any kind is severely limited\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_132E")

    Jump("loc_1401")

    label("loc_1331")


    ChrTalk(    #54
        0x9,
        (
            "We've been tightening security at\x01",
            "our guard posts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "However, you bracers are free to\x01",
            "come and go as you please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "Without your help, I fear we won't be\x01",
            "able to put an end to this mess, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1401")

    Jump("loc_1CBA")

    label("loc_1404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_170F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 1)), scpexpr(EXPR_END)), "loc_14B4")

    ChrTalk(    #57
        0x9,
        (
            "I'll be expecting more good things from you\x01",
            "in the future, bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x9,
        (
            "If we all join hands and act in unison,\x01",
            "this peace should be stronger than ever.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_170C")

    label("loc_14B4")

    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x101, 0)
    Sleep(400)

    ChrTalk(    #59
        0x9,
        "Hey, Estelle and Scherazard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "Sounds like all the credit goes\x01",
            "to you guys again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x9,
        (
            "With your help, Luke's even regained\x01",
            "consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1017FAhaha, nah, we didn't do anything.\x02\x03",

            "It's all because you were there to\x01",
            "keep the city safe, Mr. Ashton.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x9,
        "Thank you. Your words are a credit to my men.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        (
            "I'll be expecting more good things from you\x01",
            "in the future, bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "If we all join hands and act in unison,\x01",
            "this peace should be stronger than ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1006FWe'll...be sure to do that. After we leave.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x103,
        "#020FKeep up the good work, Ashton.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A69)

    label("loc_170C")

    Jump("loc_1CBA")

    label("loc_170F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1CBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 7)), scpexpr(EXPR_END)), "loc_1811")

    ChrTalk(    #68
        0x9,
        (
            "If it's even stopping the scheduled liners,\x01",
            "this fog must be really bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x9,
        (
            "Whatever happened, the army is prepared\x01",
            "to respond with all its capabilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "Let's work together to get this situation\x01",
            "resolved as quickly as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CBA")

    label("loc_1811")

    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x101, 0)
    Sleep(400)

    ChrTalk(    #71
        0x9,
        "Hey, Estelle, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1001FHey, Mr. Ashton. Long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        "On some job from the guild, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        (
            "If you want to pass right now,\x01",
            "it may take some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1015FNo, we're not passing through today.\x02\x03",

            "#1011FDid something happen to jam you guys up,\x01",
            "though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        (
            "Not exactly. Security's just been upped\x01",
            "since the sky bandit ship got taken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        (
            "So for safety's sake, orders came down\x01",
            "to strengthen our watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        "#1004FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x103,
        "#022FHmm... So the army's raising security, huh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x103, 400)

    ChrTalk(    #80
        0x9,
        (
            "Yes, but it's more just standard procedure.\x01",
            "A safety precaution, nothing more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x9,
        (
            "I'm more concerned with Rolent's fog\x01",
            "problem, to be perfectly honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        (
            "If it's even stopping the scheduled liners,\x01",
            "it must be pretty crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#1002FYeah, actually that's why we're here.\x01",
            "To investigate the cause of it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #84
        0x9,
        (
            "I see. That explains why you've come\x01",
            "this far, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x9,
        (
            "If you figure anything out, please\x01",
            "contact the army right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x9,
        (
            "This is exactly the sort of situation where\x01",
            "cooperation is paramount.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x103,
        "#020FUnderstood. And no problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x9,
        "Well, good luck with your investigation!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#1006FThanks. See you later.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1887)

    label("loc_1CBA")

    TalkEnd(0x9)
    Return()

    # Function_6_956 end

    def Function_7_1CBE(): pass

    label("Function_7_1CBE")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_1EA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1D9C")

    ChrTalk(    #90
        0xA,
        (
            "We will guard this location until\x01",
            "Mr. Ashton returns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        (
            "We've been assigned to guard this important\x01",
            "location until the return of those in charge,\x01",
            "and will apply ourselves dutifully to the task.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EA4")

    label("loc_1D9C")


    ChrTalk(    #92
        0xA,
        (
            "I was dispatched from the Haken Gate to act\x01",
            "in place of Mr. Ashton.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xA,
        (
            "I will be taking command here until his\x01",
            "patrol of Rolent ends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        (
            "It seems like anything could happen\x01",
            "in that fog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xA,
        (
            "I should order my troops to keep on full\x01",
            "guard at all times.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1EA4")

    TalkEnd(0xA)
    Return()

    # Function_7_1CBE end

    def Function_8_1EA8(): pass

    label("Function_8_1EA8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F0E")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #96
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_20C9")

    label("loc_1F0E")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #97
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20AE")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 20640, 1000, 33000, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x32)
    OP_73(0x1)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 20640, 1000, 33000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 20640, 1000, 33000, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_20AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20C8")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_20C8")

    Return()

    label("loc_20C9")

    Return()

    # Function_8_1EA8 end

    SaveToFile()

Try(main)
