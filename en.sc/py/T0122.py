from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0122   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0122.x',
        MapIndex            = 4,
        MapDefaultBGM       = "ed60084",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0122   ._SN',
            'ED6_DT21/T0122_1 ._SN',
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
        'Freddy',                               # 9
        'Melders',                              # 10
        'Elger',                                # 11
        'Stella',                               # 12
        'Crew Mem. Quint',                      # 13
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
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT07/CH01000 ._CH',             # 01
        'ED6_DT07/CH01680 ._CH',             # 02
        'ED6_DT07/CH01690 ._CH',             # 03
        'ED6_DT07/CH01290 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT07/CH01000P._CP',             # 01
        'ED6_DT07/CH01680P._CP',             # 02
        'ED6_DT07/CH01690P._CP',             # 03
        'ED6_DT07/CH01290P._CP',             # 04
    )

    DeclNpc(
        X                   = -38180,
        Z                   = 0,
        Y                   = -500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -36560,
        Z                   = 0,
        Y                   = 1550,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -36680,
        Z                   = 0,
        Y                   = 73750,
        Direction           = 180,
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
        X                   = -86130,
        Z                   = 0,
        Y                   = 71210,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -42050,
        Z                   = 0,
        Y                   = -4160,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )


    DeclActor(
        TriggerX            = -38537,
        TriggerZ            = 0,
        TriggerY            = -1845,
        TriggerRange        = 400,
        ActorX              = -38180,
        ActorZ              = 1500,
        ActorY              = -497,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36170,
        TriggerZ            = 0,
        TriggerY            = 71651,
        TriggerRange        = 1000,
        ActorX              = -36678,
        ActorZ              = 1500,
        ActorY              = 73751,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1BA",          # 00, 0
        "Function_1_1BB",          # 01, 1
        "Function_2_1BC",          # 02, 2
        "Function_3_1C1",          # 03, 3
        "Function_4_1C6",          # 04, 4
        "Function_5_97C",          # 05, 5
        "Function_6_1607",         # 06, 6
        "Function_7_22B1",         # 07, 7
    )


    def Function_0_1BA(): pass

    label("Function_0_1BA")

    Return()

    # Function_0_1BA end

    def Function_1_1BB(): pass

    label("Function_1_1BB")

    Return()

    # Function_1_1BB end

    def Function_2_1BC(): pass

    label("Function_2_1BC")

    Call(0, 4)
    Return()

    # Function_2_1BC end

    def Function_3_1C1(): pass

    label("Function_3_1C1")

    Call(0, 5)
    Return()

    # Function_3_1C1 end

    def Function_4_1C6(): pass

    label("Function_4_1C6")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_207")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 2)), scpexpr(EXPR_END)), "loc_207")
    Call(6, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F6")
    OP_A9(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_1F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_207")
    TalkEnd(0x8)
    Return()

    label("loc_207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_978")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 3)), scpexpr(EXPR_END)), "loc_3AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_278")

    ChrTalk(    #0
        0x8,
        (
            "Good luck with the patrol. If anything comes\x01",
            "up, I'll contact the guild right away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A7")

    label("loc_278")


    ChrTalk(    #1
        0x8,
        (
            "Seems like the old man's pretty\x01",
            "interested in those new orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "He's been spending a lot of time\x01",
            "alone lately, tuning them and such.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "If you have any questions about\x01",
            "orbments, he'd be the one with the\x01",
            "answers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "I know it not easy work by any means,\x01",
            "but good luck with the patrol.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_3A7")

    Jump("loc_978")

    label("loc_3AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E0")
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)

    ChrTalk(    #5
        0x8,
        "Yo, Estelle and Scherazard!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "It's been a while.\x01",
            "Good to see you're both well.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 2)), scpexpr(EXPR_END)), "loc_4AF")

    ChrTalk(    #7
        0x101,
        (
            "#1006FYeah, you too, Freddy.\x02\x03",

            "Seems like your training in\x01",
            "Zeiss went okay, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "It did. Was a good chance to study.\x02",
    )

    CloseMessageWindow()
    Jump("loc_64B")

    label("loc_4AF")


    ChrTalk(    #9
        0x101,
        "#1000FGood evening, Freddy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x103,
        "#027FYou seem in good spirits.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #11
        0x8,
        (
            "Yeah, I just got back from\x01",
            "Zeiss a bit ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "I went to the central factory for a\x01",
            "little training on the new orbments\x01",
            "that were released recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#1004FAww, you were in Zeiss too?\x02\x03",

            "#1015FI can't believe we never crossed paths!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x103,
        "#020FGuess luck just wasn't on our side.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        "Haha, yeah, must've just missed each other.\x02",
    )

    CloseMessageWindow()

    label("loc_64B")

    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #16
        0x8,
        (
            "Anyway, you guys look like you're pretty\x01",
            "busy. Kinda late for work, ain't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "Are you in the middle of a\x01",
            "patrol or something?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188A)
    Jump("loc_74B")

    label("loc_6E0")


    ChrTalk(    #18
        0x8,
        (
            "Hey there! You're up late.\x01",
            "Must be workin' hard. Seems\x01",
            "like a pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "Out patrolling or something?\x02",
    )

    CloseMessageWindow()

    label("loc_74B")


    ChrTalk(    #20
        0x101,
        "#1015FYeah...more or less.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x103,
        (
            "#020FWe're investigating the fog, and\x01",
            "giving the town a once-over while\x01",
            "we're at it.\x02\x03",

            "Has anything happened over here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "Mmm, not that I can think of.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #23
        0x8,
        (
            "...Hey, old man.\x01",
            "Nothing's happened, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)
    OP_4A(0x9, 255)

    ChrTalk(    #24
        0x9,
        "#3PNope. Been pretty quiet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1011FOkay.\x02\x03",

            "#1006FWell, quiet's better than loud!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 400)
    OP_8C(0x9, 90, 400)
    OP_4B(0x9, 255)

    ChrTalk(    #26
        0x103,
        (
            "#026FWe won't keep you gentlemen any longer.\x02\x03",

            "#020FCome on, we should get back to our patrol.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #27
        0x8,
        "Good luck!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "If anything does happen, we'll\x01",
            "contact the guild immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188B)

    label("loc_978")

    TalkEnd(0x8)
    Return()

    # Function_4_1C6 end

    def Function_5_97C(): pass

    label("Function_5_97C")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 4)), scpexpr(EXPR_END)), "loc_9C2")
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9A8")
    OP_A9(0x8)
    Jump("loc_9AA")

    label("loc_9A8")

    OP_A9(0x1)

    label("loc_9AA")

    TalkEnd(0xA)
    Return()

    label("loc_9B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C2")
    TalkEnd(0xA)
    Return()

    label("loc_9C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_1603")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 4)), scpexpr(EXPR_END)), "loc_C7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A59")

    ChrTalk(    #29
        0xA,
        (
            "This fog seems to defy common sense.\x01",
            "Nothing natural about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xA,
        (
            "You be careful on your patrol,\x01",
            "now, you hear?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C07")

    label("loc_A59")


    ChrTalk(    #31
        0xA,
        (
            "Oh, hey there. Out patrolling?\x01",
            "Much obliged. I feel safer already!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xA,
        (
            "Day or night, this fog is the same.\x01",
            "No change whatsoever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "Normally, once night sets in, a wind comes\x01",
            "by and blows it away, and everything's all\x01",
            "clear by morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xA,
        (
            "But this particular fog just seems to defy\x01",
            "common sense. Nothing natural about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xA,
        (
            "You can never be too careful these\x01",
            "days. Anything out of the ordinary\x01",
            "is cause for alarm.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C07")

    Jump("loc_C7B")

    label("loc_C0A")


    ChrTalk(    #36
        0xA,
        (
            "I'm worried about what happened\x01",
            "to Luke and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xA,
        (
            "You be sure you take care out on\x01",
            "patrol, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7B")

    Jump("loc_1603")

    label("loc_C7E")

    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x101, 0)
    Sleep(400)

    ChrTalk(    #38
        0xA,
        "Oh, hey, it's Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xA,
        (
            "Been a while. Haven't seen you since\x01",
            "you went off on that training trip, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1000FHi, Elger. Yeah, it has been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xA,
        "Welcome back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        (
            "If Scherazard's with you, then I'm\x01",
            "assuming you're in the middle of\x01",
            "some guild job again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x103,
        (
            "#026FYes, we're just doing a quick\x01",
            "patrol around the town.\x02\x03",

            "#022FYou might have already heard, but\x01",
            "there are some strange things going\x01",
            "on around here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x103, 400)

    ChrTalk(    #44
        0xA,
        "So they say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        (
            "Definitely worrisome, too. I appreciate\x01",
            "you guys making the rounds.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #46
        0xA,
        (
            "And I gotta say, you really look\x01",
            "like a pro now, you know that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        (
            "Ahhh, it seems like only yesterday you were\x01",
            "complaining about training because you hated\x01",
            "the paper tests! Those were the days...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #48
        0x101,
        "#1008FH-Hey, Elger, ixnay on the eststay...\x02",
    )

    CloseMessageWindow()

    def lambda_FCB():
        TurnDirection(0x0, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_FCB)

    def lambda_FD9():
        TurnDirection(0x1, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_FD9)

    def lambda_FE7():
        TurnDirection(0x2, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_FE7)
    TurnDirection(0x3, 0x101, 400)
    Sleep(400)

    ChrTalk(    #49
        0x103,
        (
            "#021FNow, now, what is there to hide?\x02\x03",

            "It's true that your paper tests were appalling--\x01",
            "more than any bracer before or since--but\x01",
            "you've always gotten top marks in the practicals.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10FA")

    ChrTalk(    #50
        0x106,
        (
            "#051FHaha, thought so.\x02\x03",

            "That's so freakin' you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1235")

    label("loc_10FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_112D")

    ChrTalk(    #51
        0x107,
        (
            "#560FAhaha...\x02\x03",

            "Ohh, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1235")

    label("loc_112D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_119B")

    ChrTalk(    #52
        0x104,
        (
            "#031FHeh. By description alone, I feel as though\x01",
            "I can picture the entire event unfold!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1235")

    label("loc_119B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1235")

    ChrTalk(    #53
        0x108,
        (
            "#070FHaha. Now, don't be embarrassed.\x02\x03",

            "A handful of flaws are to be expected\x01",
            "from anyone, and make up a good part\x01",
            "of a person's charm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1235")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1257")

    ChrTalk(    #54
        0x105,
        "#041FHeehee...\x02",
    )

    CloseMessageWindow()

    label("loc_1257")


    ChrTalk(    #55
        0xA,
        "Ah, sorry, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xA,
        (
            "I suppose yammering on about the past\x01",
            "like this is proof that I'm getting old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        "More to the point...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xA,
        (
            "Did you learn anything about\x01",
            "Joshua's whereabouts?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_131A():
        TurnDirection(0x0, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_131A)

    def lambda_1328():
        TurnDirection(0x1, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1328)

    def lambda_1336():
        TurnDirection(0x2, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1336)
    TurnDirection(0x3, 0xA, 400)
    Sleep(400)

    ChrTalk(    #59
        0x101,
        (
            "#1003FAh...\x02\x03",

            "#1007FI've done a lot of digging, but\x01",
            "I keep coming up empty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xA,
        (
            "I was afraid of that. He won't\x01",
            "be easy to find...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xA,
        (
            "I admit I was worried when I heard about\x01",
            "the incident from Cassius, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xA,
        (
            "From the looks of it, Estelle,\x01",
            "you seem to be hanging in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        (
            "If things ever get too hard to deal with,\x01",
            "though, do feel free to come by any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xA,
        (
            "Stella and I would be glad to lend you an\x01",
            "ear if you need it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1025FElger...\x02\x03",

            "#1000FThanks. I may take you up on that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        "You're more than welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xA,
        "But for now, I wish you luck on your patrol!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        (
            "If anything out of the ordinary happens\x01",
            "here, we'll contact you immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x103,
        "#020FYes, please do.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x188C)
    OP_A2(0x1)

    label("loc_1603")

    TalkEnd(0xA)
    Return()

    # Function_5_97C end

    def Function_6_1607(): pass

    label("Function_6_1607")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_22AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 6)), scpexpr(EXPR_END)), "loc_1AF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 7)), scpexpr(EXPR_END)), "loc_16E3")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #70
        0xFE,
        (
            "I'm worried about all those who\x01",
            "have taken ill, but you have to take\x01",
            "care of yourself as well, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "Understand? You mustn't push yourself\x01",
            "too hard, or you'll simply break!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AF4")

    label("loc_16E3")

    TurnDirection(0xFE, 0x101, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1766")

    ChrTalk(    #72
        0xFE,
        "Come to think of it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "Why are you up so late, Estelle? Do you\x01",
            "still have some manner of errand to run?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BE")

    label("loc_1766")


    ChrTalk(    #74
        0xFE,
        "Well, if it isn't Estelle and Schera!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "What brings you here at this late hour?\x02",
    )

    CloseMessageWindow()

    label("loc_17BE")


    ChrTalk(    #76
        0x101,
        "#1015FWe're just patrolling the town a little.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x103,
        (
            "#020FThe guild's issued a patrol\x01",
            "as a precautionary measure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "I've heard about all the coma victims.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "Poor Luke, and the others too. I shudder\x01",
            "to think that they might not wake up again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "You need to be careful too, Estelle,\x01",
            "is that clear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Understand? You mustn't push yourself\x01",
            "too hard, or you'll simply break!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1013FAwww...\x02\x03",

            "You always treat me like a kid, Stella.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19B1")

    ChrTalk(    #83
        0x107,
        "#061FAhaha... Just like a mom.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A84")

    label("loc_19B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19E6")

    ChrTalk(    #84
        0x105,
        "#045FShe's a very sweet woman.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A84")

    label("loc_19E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A3D")

    ChrTalk(    #85
        0x104,
        (
            "#031FHeh. Like a home away from home,\x01",
            "she's a mom away from Mom!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A84")

    label("loc_1A3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A84")

    ChrTalk(    #86
        0x106,
        "#051FHaha, looks like you ain't got nothing on her.\x02",
    )

    CloseMessageWindow()

    label("loc_1A84")


    ChrTalk(    #87
        0x103,
        (
            "#020FMmm, yes, but she's got the right of it.\x02\x03",

            "We'd best be careful ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#1006FOh, for sure!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x188F)

    label("loc_1AF4")

    Jump("loc_22AD")

    label("loc_1AF7")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #89
        0xFE,
        "Oh...?!\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #90
        0xFE,
        "Oh, my goodness! If it isn't Estelle!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #91
        0xFE,
        "My, my, my! And...is that Schera?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1008FHeya! Been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x103,
        "#021FHHeehee. Indeed, it has.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "It really has! And I've been\x01",
            "rather frustrated, you know.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #95
        0xFE,
        (
            "I kept hearing rumors you were back,\x01",
            "but you never came to pay me a visit!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1016FAhaha, sorry, Stella.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x103,
        (
            "#027FWell, Estelle's been preoccupied with\x01",
            "a few things, as you might imagine.\x02\x03",

            "How about we let bygones be bygones?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "Oh, but of course! I was simply teasing.\x01",
            "Even at my age, the news of the day travels\x01",
            "fast. I've heard all about your travels!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "Though the incident with Joshua is\x01",
            "rather troubling...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "But you seem to be keeping your head\x01",
            "held high, Estelle, and that always\x01",
            "means things will work out in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#1016FY-Yeah...hopefully.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "Let's not dwell any more on such sad\x01",
            "things, though!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "Hmmmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1015FWh-What? Why are you staring at me?\x02\x03",

            "I brushed my teeth and washed my face. I know\x01",
            "I did. I swear! I even got behind the ears!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "#3SJust...look at you!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #106
        0x101,
        "#1004F...Excuse me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "That SKIRT!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "It's perfect on you! It screams spunk\x01",
            "and positivity, yet is still so distinctly\x01",
            "feminine. I simply love it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#1008FAhaha... Y-You do?\x02\x03",

            "Schera bought this for me in the capital.\x02\x03",

            "It was her present to me, in honor of me\x01",
            "becoming a full-on bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "How nice! Schera, you have excellent taste.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x103,
        "#021FI'm glad you like it, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "Clothing is a reflection of the wearer's\x01",
            "attitude, they say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "And from the looks of things, you'll do\x01",
            "just fine as a full-fledged bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "My sloppy, dirty little Estelle's\x01",
            "cleaned up so beautifully!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "Oooh... Th-This old lady is on the\x01",
            "verge of tears, she is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#1008FHa... Haha...\x02\x03",

            "#1013F(I... I didn't think she'd cry over a skirt.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        (
            "#025F(If she saw you dressed up for a wedding,\x01",
            "she'd probably need medical attention.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188E)
    OP_A2(0x2)

    label("loc_22AD")

    TalkEnd(0xB)
    Return()

    # Function_6_1607 end

    def Function_7_22B1(): pass

    label("Function_7_22B1")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_2354")

    ChrTalk(    #118
        0xFE,
        "Hmmhmmhmmmmm... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "Heheh. Hey, I've come all the\x01",
            "way to this city, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "Gotta enjoy some shopping,\x01",
            "at least, or it's a waste!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2497")

    label("loc_2354")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_23F3")

    ChrTalk(    #121
        0xFE,
        (
            "Zosimov said he saw that cat\x01",
            "while he was out on the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "If you want the details, ask him in\x01",
            "person. He's probably still at the dock.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2497")

    label("loc_23F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_2405")
    Call(1, 0)
    Jump("loc_2497")

    label("loc_2405")


    ChrTalk(    #123
        0xFE,
        "Hmmhmmhmmmmm... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "Heheh. Hey, I've come all the\x01",
            "way to this city, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "Gotta enjoy some shopping,\x01",
            "at least, or it's a waste!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2497")

    TalkEnd(0xC)
    Return()

    # Function_7_22B1 end

    SaveToFile()

Try(main)
