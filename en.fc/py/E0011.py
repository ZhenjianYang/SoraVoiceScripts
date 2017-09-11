from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0011   ._SN',
        MapName             = 'event',
        Location            = 'E0011.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        'General Morgan',                       # 9
        'Royal Army Soldier A',                 # 10
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
        'ED6_DT07/CH02080 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH02080P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
    )

    DeclNpc(
        X                   = -7752,
        Z                   = -2000,
        Y                   = 4527,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -7116,
        Z                   = -2000,
        Y                   = -197,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_FA",           # 00, 0
        "Function_1_146",          # 01, 1
        "Function_2_147",          # 02, 2
        "Function_3_15D",          # 03, 3
        "Function_4_FF8",          # 04, 4
        "Function_5_163D",         # 05, 5
    )


    def Function_0_FA(): pass

    label("Function_0_FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_115")
    OP_A2(0x328)
    Event(0, 3)

    label("loc_115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_123")
    OP_A3(0x3FA)
    Event(0, 5)

    label("loc_123")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_12F"),
        (SWITCH_DEFAULT, "loc_145"),
    )


    label("loc_12F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_142")
    OP_A2(0x329)
    Event(0, 4)

    label("loc_142")

    Jump("loc_145")

    label("loc_145")

    Return()

    # Function_0_FA end

    def Function_1_146(): pass

    label("Function_1_146")

    Return()

    # Function_1_146 end

    def Function_2_147(): pass

    label("Function_2_147")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_147")

    label("loc_15C")

    Return()

    # Function_2_147 end

    def Function_3_15D(): pass

    label("Function_3_15D")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(1000, 5000, -3500, 0)
    SetChrPos(0x101, 1000, 5000, -3590, 225)
    SetChrPos(0x102, -360, 5000, -3840, 135)
    SetChrPos(0x103, 730, 5000, -4940, 315)

    ChrTalk(    #0
        0x101,
        (
            "#002FWe checked it over, but it looks\x01",
            "like there's nobody inside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#012FThere's a high possibility the\x01",
            "passengers were transferred\x01",
            "to the sky bandits' airship.\x02\x03",

            "And then to wherever their\x01",
            "hideout is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#002FAgreed.\x02\x03",

            "But this sucks... Right when\x01",
            "I thought we had some clues,\x01",
            "we're back to zero.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x103,
        (
            "#020FCome on, cheer up already.\x02\x03",

            "It's not like every clue has\x01",
            "completely vanished.\x02\x03",

            "Why do you think the sky bandits\x01",
            "hid the airliner in a place like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#002FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x103,
        (
            "#020FAs far as I can tell, the orbal energy in the ship\x01",
            "has completely stopped.\x02\x03",

            "Which means that the orbal engine was stripped\x01",
            "from the aircraft.\x02\x03",

            "Furthermore, the sky bandits made multiple trips\x01",
            "to carry off a large amount of cargo.\x02\x03",

            "Considering the time and risk involved, don't you\x01",
            "think it would have been more effective just to\x01",
            "take the entire airliner to their hideout?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#000FYeah, that does seem a little\x01",
            "odd that they didn't...\x02\x03",

            "So, why'd they hide the airliner\x01",
            "here then?\x02\x03",

            "Umm, all I can think of is that\x01",
            "they did it in order to...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Sort the cargo.]\x01",                                                 # 0
            "[Move the hostages aboard their own aircraft.]\x01",                    # 1
            "[Steal the orbal engine.]\x01",                                         # 2
            "[Keep clear of the Royal Army's search party.]\x01",                    # 3
            "[Ditch the Linde, because their hideout is somewhere weird.]\x01",      # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6DC"),
        (1, "loc_79C"),
        (2, "loc_852"),
        (3, "loc_90E"),
        (4, "loc_A06"),
        (SWITCH_DEFAULT, "loc_A2E"),
    )


    label("loc_6DC")


    ChrTalk(    #7
        0x103,
        (
            "#026FIt's true this may have been a\x01",
            "good place to sort the cargo\x01",
            "because of the space...\x02\x03",

            "However, it doesn't account for\x01",
            "the fact that they didn't take\x01",
            "the airliner to their hideout.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2E")

    label("loc_79C")


    ChrTalk(    #8
        0x103,
        (
            "#026FIt's true they would have needed to\x01",
            "land in order to move the hostages...\x02\x03",

            "However, it doesn't account for\x01",
            "the fact that they didn't take\x01",
            "the airliner to their hideout.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2E")

    label("loc_852")


    ChrTalk(    #9
        0x103,
        (
            "#026FIt's true they would have needed\x01",
            "to land in order to remove the\x01",
            "orbal engine...\x02\x03",

            "However, it doesn't account for\x01",
            "the fact that they didn't take\x01",
            "the airliner to their hideout.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2E")

    label("loc_90E")


    ChrTalk(    #10
        0x103,
        (
            "#026FIt's true the airliner is rather\x01",
            "large and easily seen...\x02\x03",

            "And in that sense, it would seem highly\x01",
            "likely that they would leave it in a\x01",
            "different place than their hideout.\x02\x03",

            "However, that alone couldn't be\x01",
            "considered a decisive reason.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2E")

    label("loc_A06")


    ChrTalk(    #11
        0x103,
        "#020FYes, that's exactly right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2E")

    label("loc_A2E")


    ChrTalk(    #12
        0x103,
        (
            "#020FFrom my guess, I would imagine\x01",
            "that their hideout is in a slightly\x01",
            "peculiar place.\x02\x03",

            "Maybe 10 to 15 arge in size...\x02\x03",

            "In short, a peculiar place on which\x01",
            "only a small aircraft like the sky\x01",
            "bandits' airship could land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#000FInteresting...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        (
            "#012FHow about terrain covered with\x01",
            "extreme differences in height,\x01",
            "like mountains and ravines...?\x02\x03",

            "That seems like a likely place\x01",
            "for the sky bandits' hideout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x103,
        (
            "#020FYes, that's what I've been\x01",
            "thinking, too.\x02\x03",

            "However, if that's the case...then we\x01",
            "may be unable to do anything else.\x02\x03",

            "There's the possibility that their\x01",
            "hideout may be in a place we can't\x01",
            "reach by foot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#002FTh-Then what CAN we do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        (
            "#022FWell...\x02\x03",

            "I hate to say it, but we may have\x01",
            "to share our conclusions with the\x01",
            "army and ask for their cooperation.\x02\x03",

            "Because they're the ones with\x01",
            "the patrol ships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#004FWhat...? Now you're trying to tell\x01",
            "us we should go crawling back to\x01",
            "the army and ask them for help?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#012FEither way, we still have to report\x01",
            "to them about the airliner.\x02\x03",

            "Personally speaking, I still think\x01",
            "we should cooperate with the army,\x01",
            "whatever their attitude may be.\x02\x03",

            "Especially if that means bringing\x01",
            "the hostages back safe and sound.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#002FI guess you're right...\x02\x03",

            "This isn't the time or place to be\x01",
            "letting my personal feelings get\x01",
            "the best of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x103,
        (
            "#020FFor the time being, let's get back\x01",
            "to the guild and report our findings\x01",
            "to Lugran.\x02\x03",

            "We should be able to contact\x01",
            "the Haken Gate if we use the\x01",
            "orbal telephone.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_3_15D end

    def Function_4_FF8(): pass

    label("Function_4_FF8")

    EventBegin(0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)

    ChrTalk(    #22
        0x101,
        (
            "#004FHuh?!\x02\x03",

            "Wh-What the heck?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#017FGreat... Now this was something\x01",
            "I did not expect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x103,
        (
            "#025FI wonder if we should be glad,\x01",
            "since they've saved us the trouble of\x01",
            "having to contact them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        (
            "We have found a suspicious\x01",
            "armed group!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x9,
        "Put your hands in the air! All of you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x9,
        (
            "What is this world coming to? A woman\x01",
            "and two kids are the sky bandits...?\x01",
            "Though the girl DOES look shifty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#009FH-Hey! I do not! And who are\x01",
            "you calling sky bandits?!\x02\x03",

            "Can't you see this shiny emblem\x01",
            "on my chest?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #29
        0x8,
        "Man's Voice",
        "Hmph! The bracer emblem, huh...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #30
        0x8,
        "Man's Voice",
        (
            "I hope you don't think for a moment\x01",
            "something like that proves your\x01",
            "innocence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#004FG-General Morgan?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x102,
        "#014FWhy are you here...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "#160FAfter looking over the reports of my men, I\x01",
            "found this place to have been insufficiently\x01",
            "investigated, so I came to see for myself...\x02\x03",

            "Who would have thought the lot of you\x01",
            "were conspiring with the sky bandits?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x103,
        (
            "#022FMight I get you to stop with the\x01",
            "accusations, General?\x02\x03",

            "We happened to find this place\x01",
            "one step ahead of your men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "#160FIf that's the truth, then why don't\x01",
            "you tell me where the sky bandits\x01",
            "are?\x02\x03",

            "Are the hostages inside that\x01",
            "airliner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#012FWe almost had the sky bandits,\x01",
            "but they managed to escape...\x02\x03",

            "And there are no hostages to be\x01",
            "found here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#160FHmph! It looks like the truth\x01",
            "has come out...\x02\x03",

            "Most likely, you notified the sky\x01",
            "bandits to let them know we were\x01",
            "coming!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#005FW-Wait a minute here!\x01",
            "How about you cut with the crap!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#162FMy thoughts exactly!\x02\x03",

            "All right, men!\x01",
            "Take them into custody!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T1410   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_FF8 end

    def Function_5_163D(): pass

    label("Function_5_163D")

    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-2670, 5000, -10370, 0)
    OP_6C(315000, 0)
    OP_6B(2400, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x104, 0, 5000, -10200, 180)
    SetChrPos(0x103, 0, 5000, -1650, 180)
    FadeToBright(2000, 0)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Man's Voice")

    AnonymousTalk(    #40
        (
            "\x07\x00And that's about the gist of\x01",
            "the sky bandit incident that\x01",
            "occurred in northern Liberl...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #41
        "\x07\x00...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #42
        (
            "\x07\x00And to think that the bankrupt\x01",
            "Capua family drifted all the way\x01",
            "down here.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #43
        (
            "\x07\x00You might be contacted by Liberl\x01",
            "regarding the incident, so deal\x01",
            "with it as you see fit.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #44
        "\x07\x00...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #45
        (
            "\x07\x00Yeah, it turns out I wasn't able to\x01",
            "meet him in the end. It seems like\x01",
            "something else must have come up.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #46
        (
            "\x07\x00Also, the connection with the sky bandit\x01",
            "incident is still unknown, but it's clear\x01",
            "that another power is at work here.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #47
        "\x07\x00...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #48
        (
            "\x07\x00No, it's not like that at all.\x01",
            "I've also become acquainted\x01",
            "with an interesting bunch.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #49
        (
            "\x07\x00The food's great, and there are babes\x01",
            "everywhere. This is unquestionably\x01",
            "my kind of country.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #50
        (
            "\x07\x00Maybe I'll just take up permanent\x01",
            "residence here while I'm at it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #51
        "\x07\x00...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #52
        (
            "\x07\x00All right, all right.\x01",
            "There's no need to throw a fit.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #53
        (
            "\x07\x00Anyway, see what else you can find out.\x01",
            "Just don't get caught looking into things\x01",
            "by the chancellor.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #54
        "\x07\x00I'll contact you again...my dear friend.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_77(0xFF, 0xFF, 0xFF, 0x7D000, 0x0)
    Sleep(1000)

    ChrTalk(    #55
        0x104,
        (
            "#030FHa ha. I love messing with that guy.\x02\x03",

            "He's just so stuffy and uptight\x01",
            "that I can't help myself...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #56
        0x103,
        "Woman's Voice",
        "A portable phone, huh...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #57
        0x103,
        "Woman's Voice",
        (
            "Well, aren't you carrying around\x01",
            "quite the nifty gadget?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x104, 0x103, 500)

    def lambda_1BE2():
        OP_6B(3000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BE2)
    OP_6D(-190, 5000, -6110, 1000)
    Sleep(1000)

    ChrTalk(    #58
        0x104,
        "#030FSch-Schera...\x02",
    )

    CloseMessageWindow()

    def lambda_1C20():
        OP_6D(100, 5000, -9000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C20)
    OP_8E(0x103, 0x0, 0x1388, 0xFFFFE142, 0x7D0, 0x0)

    ChrTalk(    #59
        0x103,
        (
            "#020FAnd the fact that you're carrying around\x01",
            "an orbment that even the Zeiss Central\x01",
            "Factory couldn't create, well...\x02\x03",

            "How about you tell me who you\x01",
            "really are?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x104,
        (
            "#030FCome on, Schera. Don't treat me\x01",
            "like I'm some kind of stranger.\x02\x03",

            "I'm Olivier Lenheim, the wandering bard\x01",
            "and gifted musician you've come to adore.\x02\x03",

            "But if you'd like to get to know me better,\x01",
            "I'm sure we could arrange something...\x01",
            "A little pillow talk, perhaps...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x103,
        (
            "#020FHow about we skip the foreplay and go\x01",
            "straight to the climax. Your cheap\x01",
            "antics don't fool me, Olivier.\x02\x03",

            "Or should I call you\x01",
            "'Mr. Erebonian Operative'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x104,
        (
            "#030F...\x02\x03",

            "Heh. It looks like the title 'Silver Streak'\x01",
            "isn't just for show.\x02\x03",

            "So I guess you were pretending\x01",
            "that you didn't notice in front\x01",
            "of Estelle and Joshua, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x103,
        (
            "#020FI don't want to worry those two\x01",
            "any more than they already are.\x02\x03",

            "So back to the subject at hand,\x01",
            "why don't you start talking?\x02\x03",

            "Who are you, and what are you\x01",
            "doing in Liberl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x104,
        (
            "#030FBefore that...I'm going to have to\x01",
            "correct you on two points.\x02\x03",

            "First off, these 'cheap antics', as\x01",
            "you call them, are totally natural.\x02\x03",

            "I'm not playacting or anything.\x01",
            "That's just who I am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x103,
        (
            "#020FOh, I'm sure.\x02\x03",

            "So do you mean to tell me that you\x01",
            "drank that wine without paying just\x01",
            "because you felt like it?\x02\x03",

            "And after that, being taken to the Haken\x01",
            "Gate so you could gather information was\x01",
            "all a part of the plan?\x02\x03",

            "And you even set yourself up to\x01",
            "run into us? I don't think so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x104,
        (
            "#030FHeh... I'll leave that part\x01",
            "up to your imagination.\x02\x03",

            "The other thing I must correct you on\x01",
            "is that this device is not an orbment.\x02\x03",

            "It is an artifact which was unearthed\x01",
            "in the Empire.\x02\x03",

            "It can piggyback off any orbal communications\x01",
            "system and its transmissions can be encrypted,\x01",
            "so there's no worry about them being intercepted.\x02\x03",

            "It comes in handy for a busy man such as myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x103,
        (
            "#020FAn artifact...like one of the sacred relics\x01",
            "the Septian Church has stewardship over?\x02\x03",

            "Now I'm all the more curious to know\x01",
            "what you're after.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x104,
        (
            "#030FOh no, no, no, Schera.\x02\x03",

            "You should never try to pry into\x01",
            "the secrets of a mysterious beauty\x01",
            "all at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x103,
        (
            "#020F...\x02\x03",

            "How would you like to get to know a\x01",
            "real woman? I'd be more than willing\x01",
            "to show you with my whip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x104,
        (
            "#030F...\x01",
            "Schera...I don't see any humor\x01",
            "in those eyes...\x02\x03",

            "Well, jokes aside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x103,
        (
            "#020FYou really should have just been\x01",
            "straightforward from the beginning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x104,
        (
            "#030FAs you have already figured out,\x01",
            "my position is like that of an\x01",
            "operative in the Empire.\x02\x03",

            "But I have no intention of sabotaging\x01",
            "anything or stealing classified\x01",
            "information.\x02\x03",

            "I merely came here to meet a certain\x01",
            "someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x103,
        "#020FA certain someone...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x104,
        (
            "#030FYes, someone you know all too well.\x02\x03",

            "The one lauded as the supreme swordsman\x01",
            "and master strategist by the Royal Army.\x02\x03",

            "The bracer with the special title belonging\x01",
            "to but four people throughout the whole of\x01",
            "the entire continent.\x02\x03",

            "The Divine Blade--Cassius Bright\x01",
            "is the one I seek.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_163D end

    SaveToFile()

Try(main)
