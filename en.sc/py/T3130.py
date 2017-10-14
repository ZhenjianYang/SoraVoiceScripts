from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3130   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3130.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        'Father Vixen',                         # 9
        'Sister Kiera',                         # 10
        'Lane',                                 # 11
        'Ada',                                  # 12
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
        'ED6_DT07/CH01410 ._CH',             # 01
        'ED6_DT07/CH01450 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH01410P._CP',             # 01
        'ED6_DT07/CH01450P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
    )

    DeclNpc(
        X                   = 59010,
        Z                   = 1000,
        Y                   = 52150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 56310,
        Z                   = 1000,
        Y                   = 50360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 59970,
        Z                   = 0,
        Y                   = 43850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 59010,
        Z                   = 1000,
        Y                   = 50160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    DeclActor(
        TriggerX            = 58950,
        TriggerZ            = 1000,
        TriggerY            = 50290,
        TriggerRange        = 400,
        ActorX              = 58800,
        ActorZ              = 2500,
        ActorY              = 52200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_16E",          # 00, 0
        "Function_1_1F1",          # 01, 1
        "Function_2_1F2",          # 02, 2
        "Function_3_1F7",          # 03, 3
        "Function_4_165D",         # 04, 4
        "Function_5_1E81",         # 05, 5
        "Function_6_2403",         # 06, 6
    )


    def Function_0_16E(): pass

    label("Function_0_16E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_17D")
    SetChrFlags(0xA, 0x80)
    Jump("loc_1F0")

    label("loc_17D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_198")
    SetChrPos(0xA, 62680, 0, 45050, 0)
    Jump("loc_1F0")

    label("loc_198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1D3")
    SetChrFlags(0x8, 0x10)
    SetChrPos(0xB, 56190, 0, 46550, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xA, 62680, 0, 45050, 0)
    Jump("loc_1F0")

    label("loc_1D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1F0")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, 62680, 0, 45050, 0)

    label("loc_1F0")

    Return()

    # Function_0_16E end

    def Function_1_1F1(): pass

    label("Function_1_1F1")

    Return()

    # Function_1_1F1 end

    def Function_2_1F2(): pass

    label("Function_2_1F2")

    Call(0, 3)
    Return()

    # Function_2_1F2 end

    def Function_3_1F7(): pass

    label("Function_3_1F7")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_3BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E")

    ChrTalk(    #0
        0x8,
        (
            "Being unable to use orbments is\x01",
            "a serious safety issue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "As you may be aware, orbal lighting\x01",
            "has an anti-monster effect, as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "Now, when monsters attacked before,\x01",
            "the Royal Army fought very well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "But one must remember, they could\x01",
            "still use orbments at that time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_3B9")

    label("loc_32E")


    ChrTalk(    #4
        0x8,
        (
            "Being unable to use orbments\x01",
            "is a serious safety issue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "As you may be aware, orbal lighting\x01",
            "has an anti-monster effect, as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B9")

    Jump("loc_1659")

    label("loc_3BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_521")

    ChrTalk(    #6
        0x8,
        (
            "Right after the orbments failed, chaos\x01",
            "ruled in the hearts of many.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "Fortunately, It seems the city has mostly\x01",
            "calmed itself now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "To these good people, however, orbments are\x01",
            "more than just machines, so it's no surprise\x01",
            "they were more distraught than most.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "After all, this city was built on their\x01",
            "trust in technology.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_5C2")

    label("loc_521")


    ChrTalk(    #10
        0x8,
        (
            "To the people of this city, orbments\x01",
            "are far more than just machines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "It's no surprise an incident of this\x01",
            "magnitude would disturb them to their\x01",
            "core.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C2")

    Jump("loc_1659")

    label("loc_5C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 0)), scpexpr(EXPR_END)), "loc_CF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_75E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_699")

    ChrTalk(    #12
        0x8,
        (
            "Accepting one's powerlessness is\x01",
            "perhaps the optimal road to a calmer,\x01",
            "more manageable existence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "Those who would look to the heavens\x01",
            "for help have taken the first step.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75B")

    label("loc_699")


    ChrTalk(    #14
        0x8,
        (
            "To pray to the Goddess because you\x01",
            "wish the earthquakes to stop...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "I think that such appeals are\x01",
            "perfectly acceptable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "It means acknowledging that\x01",
            "we are powerless, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_75B")

    Jump("loc_C76")

    label("loc_75E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_7BB")

    ChrTalk(    #17
        0x8,
        "Oh, Goddess of the Sky, Aidios...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "Grant your blessing to these people...\x02",
    )

    CloseMessageWindow()
    Jump("loc_C76")

    label("loc_7BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_9C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_82E")
    TurnDirection(0x8, 0x107, 0)

    ChrTalk(    #19
        0x8,
        "Best of luck to you in your work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "If you have need of answers,\x01",
            "come by any time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C6")

    label("loc_82E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_871")

    ChrTalk(    #21
        0x8,
        "Hello, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "Helping the professor again?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D0")

    label("loc_871")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x107, 0)

    ChrTalk(    #23
        0x8,
        "Well, if it isn't little Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        "Helping the professor again?\x02",
    )

    CloseMessageWindow()

    label("loc_8D0")


    ChrTalk(    #25
        0x107,
        (
            "#560FAhh, yes.\x02\x03",

            "I'm just placing a couple instruments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "Very good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        "Be sure you come to Sunday School, now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        "Everyone's more motivated when you're around.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x107,
        "#067FHeehee... Yeah, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        "Best of luck to you in your work.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_9C6")

    Jump("loc_C76")

    label("loc_9C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_B1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A59")

    ChrTalk(    #31
        0x8,
        (
            "Sister Kiera has been working quite\x01",
            "diligently lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "She's come to understand the importance\x01",
            "of social activities.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1B")

    label("loc_A59")


    ChrTalk(    #33
        0x8,
        (
            "Providence of medical care is an\x01",
            "important duty of the church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "Pain of the heart or pain of the body,\x01",
            "it matters not; pain is pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "Salvation is had only\x01",
            "when both are healed.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_B1B")

    Jump("loc_C76")

    label("loc_B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_C76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_BB5")

    ChrTalk(    #36
        0x8,
        (
            "It was a small earthquake, but there\x01",
            "still may have been injuries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "It would be wise to prepare\x01",
            "medicine, at the very least.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C76")

    label("loc_BB5")


    ChrTalk(    #38
        0x8,
        (
            "That shaking a bit ago was\x01",
            "an earthquake, it would seem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "It was a little one, but there still may\x01",
            "have been injuries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "It would be wise to prepare\x01",
            "medicine, at the very least.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_C76")

    Jump("loc_CF3")

    label("loc_C79")


    ChrTalk(    #41
        0x8,
        "If anything happens, please come by again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "If I can be of aid, I will happily\x01",
            "provide it. Come see me any time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF3")

    Jump("loc_1659")

    label("loc_CF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_10C4")

    ChrTalk(    #43
        0x8,
        "Oh, hello.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1025FAh, Father Vixen.\x02\x03",

            "#1007FUm... Thank you again for your help before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x106,
        "#552F...I owe ya.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x106, 400)

    ChrTalk(    #46
        0x8,
        "Ohh, you look to be doing well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "If you've recovered this much, then\x01",
            "my worries are for naught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "However, you mustn't overextend yourself,\x01",
            "no matter how much you've recovered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x106,
        (
            "#050FYeah, I get it.\x02\x03",

            "#555FI mean, I'm not a kid.\x01",
            "You don't need to fuss like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        "Well, as long as you understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "But remember, it was the will of the Goddess\x01",
            "that saved you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "It means you still have a duty that\x01",
            "you must perform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "Please, do not let the precious gift\x01",
            "that is your life go to waste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "...Though this is but my own wish\x01",
            "for you, mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x106,
        "#552F...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #56
        0x8,
        "My, pardon me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "That nearly became a lecture\x01",
            "all its own.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(    #58
        0x8,
        "Please, feel free to drop by any time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "If I can be of aid, I will\x01",
            "happily provide it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1000FAll right. Thank you!\x02\x03",

            "Your concern is appreciated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1653")

    label("loc_10C4")


    ChrTalk(    #61
        0x8,
        "Oh, hello.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1025FAh, Father Vixen!\x02\x03",

            "#1007FThank you soooo much for when Agate\x01",
            "was hurt before.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #63
        0x103,
        "#023FHurt...? Wait, when did this happen?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1241")

    ChrTalk(    #64
        0x107,
        "#561FY-Yeah...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #65
        0x101,
        (
            "#1003FHe got hit with a poisoned bullet by one\x01",
            "of those Intelligence goons a while back\x01",
            "and was in a pretty bad way.\x02\x03",

            "#1015FIt was a close call, but Father Vixen\x01",
            "saved him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D6")

    label("loc_1241")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_131E")

    def lambda_1255():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1255)
    TurnDirection(0x108, 0x103, 400)

    ChrTalk(    #66
        0x108,
        (
            "#072FHe was hit by a poisoned round,\x01",
            "I believe.\x02\x03",

            "From the sounds of it, he was in\x01",
            "a pretty serious state for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#1015FIt was a close call, but Father Vixen\x01",
            "saved him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D6")

    label("loc_131E")


    ChrTalk(    #68
        0x101,
        (
            "#1003FYeah, he got hit with a poisoned bullet by\x01",
            "one of those Intelligence goons a while back\x01",
            "and was in a pretty bad way.\x02\x03",

            "#1015FIt was a close call, but Father Vixen\x01",
            "saved him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D6")


    ChrTalk(    #69
        0x8,
        (
            "Well, I just helped a little at the\x01",
            "end, really.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #70
        0x8,
        "Incidentally, is he well?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_144E")

    def lambda_1446():
        TurnDirection(0x108, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1446)

    label("loc_144E")

    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #71
        0x101,
        (
            "#1006FAh, he's totally fine.\x02\x03",

            "He's working on some other cases at\x01",
            "the moment, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "I hope he isn't pushing himself\x01",
            "too hard again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        "He was saved by the will of the Goddess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "It means he still has an important\x01",
            "mission to perform...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #75
        0x8,
        "...Oh, pardon me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        "I fear that was about to turn into a lecture.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        "Please, feel free to drop by any time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        (
            "If I can be of aid, I will\x01",
            "happily provide it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1000FAll right. Thank you!\x02\x03",

            "Your concern is appreciated.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1653")

    OP_A2(0x1428)
    OP_A2(0x0)

    label("loc_1659")

    TalkEnd(0x8)
    Return()

    # Function_3_1F7 end

    def Function_4_165D(): pass

    label("Function_4_165D")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_16F5")

    ChrTalk(    #80
        0xFE,
        (
            "In order to prepare for emergencies,\x01",
            "we're making extra medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "I certainly hope these precautions\x01",
            "prove unnecessary, however.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E7D")

    label("loc_16F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_18A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_180F")

    ChrTalk(    #82
        0xFE,
        (
            "Citizens unnerved by the failure of the\x01",
            "orbments pushed their way into the central\x01",
            "factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "For a while, the whole city was in an uproar.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "Yet, there wasn't much we could do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "...I feel as if I have once again learned\x01",
            "of my own powerlessness.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_18A2")

    label("loc_180F")


    ChrTalk(    #86
        0xFE,
        (
            "Citizens unnerved by the failure of the\x01",
            "orbments pushed their way into the central\x01",
            "factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "For a while the whole city was in an uproar.\x02",
    )

    CloseMessageWindow()

    label("loc_18A2")

    Jump("loc_1E7D")

    label("loc_18A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1A57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1983")

    ChrTalk(    #88
        0xFE,
        (
            "Apparently, Father Vixen thinks that asking the\x01",
            "Goddess for help in these kinds of situations\x01",
            "is okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "*sigh* I rather feel bad for Goddess\x01",
            "Aidios now. So many demands placed\x01",
            "upon her shoulders!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A54")

    label("loc_1983")


    ChrTalk(    #90
        0xFE,
        (
            "Apparently, Father Vixen thinks that asking the\x01",
            "Goddess for help in these kinds of situations\x01",
            "is okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "His reasoning is sound...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "...yet I have difficulty coming to\x01",
            "terms with his conclusion.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1A54")

    Jump("loc_1E7D")

    label("loc_1A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1C28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1AC0")

    ChrTalk(    #93
        0xFE,
        "To only pray when you're in trouble...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "It just seems a bit overly convenient.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C25")

    label("loc_1AC0")


    ChrTalk(    #95
        0xFE,
        (
            "The number of people who worship\x01",
            "in the church has increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "Everyone's praying to the Goddess that\x01",
            "there will be no more earthquakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "Father Vixen can barely contain\x01",
            "his happiness at the growth of\x01",
            "the congregation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "But to me, it just seems a bit overly\x01",
            "convenient to believe that the Goddess\x01",
            "exists solely to save us from strife.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1C25")

    Jump("loc_1E7D")

    label("loc_1C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1D82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1CDB")

    ChrTalk(    #99
        0xFE,
        (
            "Personally, I do what I do solely for the\x01",
            "sake of the people. I do not seek to win\x01",
            "favors with the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        "I think Father Vixen's ideas are wonderful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D7F")

    label("loc_1CDB")


    ChrTalk(    #101
        0xFE,
        (
            "Dispensing medicine is an important\x01",
            "duty of the church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "At first I had some reservations, but\x01",
            "now I truly believe he is doing the\x01",
            "work of the Goddess.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1D7F")

    Jump("loc_1E7D")

    label("loc_1D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_1E7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1E00")

    ChrTalk(    #103
        0xFE,
        "I wonder if the city is all right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "...More importantly, I wonder if\x01",
            "the central factory is okay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E7D")

    label("loc_1E00")


    ChrTalk(    #105
        0xFE,
        (
            "Though small, that was an earthquake.\x01",
            "Without question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "I think it might be my first since\x01",
            "coming to this city.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1E7D")

    TalkEnd(0x9)
    Return()

    # Function_4_165D end

    def Function_5_1E81(): pass

    label("Function_5_1E81")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_203B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1F19")

    ChrTalk(    #107
        0xFE,
        "Ughhh! I'll be up all night working today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "*sigh* There really is no way to combine\x01",
            "religious passion with a social life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2038")

    label("loc_1F19")


    ChrTalk(    #109
        0xFE,
        (
            "Did you hear the announcement\x01",
            "from the central factory?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "We prayed night and day and now the\x01",
            "earthquakes have stopped! It's a miracle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "Though, the flip side of that is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "I was praying so hard, I didn't\x01",
            "get any work done!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "Ahh, what should I do about my job...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2038")

    Jump("loc_23FF")

    label("loc_203B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_218B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_20EC")

    ChrTalk(    #114
        0xFE,
        (
            "Seems like everyone's praying for the\x01",
            "earthquakes to stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "I've skipped a bit too much work, but I can't\x01",
            "go home yet. Not until my prayers are heard!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2188")

    label("loc_20EC")


    ChrTalk(    #116
        0xFE,
        (
            "Seems like everyone's praying for the\x01",
            "earthquakes to stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "I must admit, though, it's uplifting to have\x01",
            "everyone wishing for the same thing...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2188")

    Jump("loc_23FF")

    label("loc_218B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_22D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_225C")

    ChrTalk(    #118
        0xFE,
        (
            "Now, then, before I go back to work, I should\x01",
            "really pray EXTRA hard this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "Errr, may no more earthquakes come...\x01",
            "May no more earthquakes come...\x01",
            "May no more earthquakes come...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22CD")

    label("loc_225C")


    ChrTalk(    #120
        0xFE,
        (
            "Seems like there's a lot of people\x01",
            "in the church now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "Guess the earthquake was a shock\x01",
            "to everyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_22CD")

    Jump("loc_23FF")

    label("loc_22D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_23FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_237F")

    ChrTalk(    #122
        0xFE,
        (
            "Since I'm at the church, I should pray\x01",
            "before I go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "May no more earthquakes come...\x01",
            "May no more earthquakes come...\x01",
            "May no more earthquakes come...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23FF")

    label("loc_237F")


    ChrTalk(    #124
        0xFE,
        (
            "Phew! That earthquake a bit ago sure\x01",
            "was a shock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "I was on the job, and I ran to the\x01",
            "Church without even thinking!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_23FF")

    TalkEnd(0xA)
    Return()

    # Function_5_1E81 end

    def Function_6_2403(): pass

    label("Function_6_2403")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_246D")

    ChrTalk(    #126
        0xFE,
        "Great Aidios... Please, no more earthquakes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "Also, thank you for all the medicine.\x02",
    )

    CloseMessageWindow()
    Jump("loc_25C4")

    label("loc_246D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_25C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_24F1")

    ChrTalk(    #128
        0xFE,
        "I should pray with everything I've got today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "I've got to ask Aidios to put an end to these\x01",
            "earthquakes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C4")

    label("loc_24F1")


    ChrTalk(    #130
        0xFE,
        "Father Vixen's medicine is very effective.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "My shoulder pain's gotten a lot better.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        "I should pray with everything I've got today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "I've got to ask Aidios to put an end to these\x01",
            "earthquakes.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_25C4")

    TalkEnd(0xB)
    Return()

    # Function_6_2403 end

    SaveToFile()

Try(main)
