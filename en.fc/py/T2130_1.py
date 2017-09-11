from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T2130_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2130.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
    )

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_2503",         # 01, 1
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x335)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D")
    Call(1, 1)
    Jump("loc_2502")

    label("loc_7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_1DA")
    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_101")

    ChrTalk(    #0
        0xFE,
        (
            "If you find anything,\x01",
            "let me know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I'm counting on you! Any treasure\x01",
            "we find, we split equally!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x11)
    Jump("loc_1D7")

    label("loc_101")


    ChrTalk(    #2
        0xFE,
        "Oh, you're back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "So...any treasure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#505FSorry, but we haven't found\x01",
            "anything yet.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #5
        0xFE,
        (
            "If you find anything,\x01",
            "let me know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I'm counting on you! Any treasure\x01",
            "we find, we split equally!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x11)

    label("loc_1D7")

    Jump("loc_2502")

    label("loc_1DA")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrFlags(0x11, 0x10)
    Fade(1000)
    SetChrPos(0x101, 54200, 0, 49000, 270)
    SetChrPos(0x102, 54200, 0, 47500, 270)
    SetChrPos(0x105, 56000, 0, 48500, 270)
    TalkBegin(0x11)
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x12, 0x3E8)
    ClearChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_3CF")
    OP_2B(0x1E, 0x2)
    OP_2C(0x1E, 0x3E8)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #7
        0xFE,
        "...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "I saw you guys the other day...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        "#010FNice to see you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#508FOh, hi! You're the guy we met\x01",
            "on the beach, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #11
        0xFE,
        "You can call me Jimmy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "You really saved my skin before,\x01",
            "so let me thank you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "So...have you checked out the\x01",
            "bulletin board today?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_436")

    label("loc_3CF")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #14
        0xFE,
        "...Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "Hey, are you bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Then you must have seen the\x01",
            "bulletin board, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_436")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_654")
    OP_28(0x1E, 0x4, 0x4)
    OP_28(0x1E, 0x4, 0x8)
    OP_28(0x1E, 0x1, 0x1)
    OP_28(0x1E, 0x1, 0x2)
    OP_28(0x1E, 0x1, 0x4)
    OP_28(0x1E, 0x1, 0x8)
    OP_A2(0x0)

    ChrTalk(    #17
        0x101,
        (
            "#000FWell, yes...\x02\x03",

            "...but why in Liberl did you pick\x01",
            "HERE to meet, of all places?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Well, I kinda stand out here,\x01",
            "don't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I mean, it costs a lot to put up one of those\x01",
            "requests, and I figure people'll see me here,\x01",
            "and ask, 'Hey, why are you in the chapel?'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "And then I'll be like, 'So that YOU can\x01",
            "help me find some awesome treasure!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#006FWell, then how about we get\x01",
            "down to business?\x02\x03",

            "That request of yours certainly\x01",
            "sounds intriguing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "Heh heh...glad you agree!\x02",
    )

    CloseMessageWindow()
    Jump("loc_874")

    label("loc_654")

    OP_28(0x1E, 0x4, 0x8)
    OP_28(0x1E, 0x4, 0x4)
    OP_28(0x1E, 0x4, 0x2)
    OP_28(0x1E, 0x1, 0x1)
    OP_28(0x1E, 0x1, 0x2)
    OP_28(0x1E, 0x1, 0x4)
    OP_28(0x1E, 0x1, 0x8)
    OP_A2(0x0)

    ChrTalk(    #23
        0x101,
        "#004FOh, did you post a request?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "What, you haven't seen it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "I figured that's why you were here!\x01",
            "To rendezvous with me!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(    #26
        0x102,
        (
            "#014FRendezvous?\x01",
            "In the chapel...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #27
        0xFE,
        (
            "Well, I kinda stand out here,\x01",
            "don't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "I mean, it costs a lot to put up one of those\x01",
            "requests, and I figure people'll see me here,\x01",
            "and ask, 'Hey, why are you in the chapel?'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "And then I'll be like, 'So that YOU can\x01",
            "help me find some awesome treasure!'\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #30
        0x101,
        "#006FSo, uh...it's a treasure hunt?\x02",
    )

    CloseMessageWindow()

    label("loc_874")

    OP_8C(0xFE, 90, 0)

    ChrTalk(    #31
        0xFE,
        (
            "Yep! I actually just acquired\x01",
            "an ancient map a short while\x01",
            "ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "And you wouldn't believe it\x01",
            "if I told you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#002FWouldn't believe...what, now?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #34
        0xFE,
        (
            "It leads to the treasure of the\x01",
            "great pirate, Schirmer!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #35
        0x101,
        (
            "#004FWhat?! No way!\x02\x03",

            "#000FBut, um...I don't really know\x01",
            "who that is.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #36
        0xFE,
        "Y-You've never heard of Schirmer?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Aren't you from Ruan? ...Or wait, are\x01",
            "you from somewhere else? Ehh, either way,\x01",
            "SCHIRMER! How can you not know?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#509FDon't go making assumptions.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x105,
        "#040FIf memory serves me correctly...\x02",
    )

    CloseMessageWindow()

    def lambda_AD6():
        TurnDirection(0x101, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD6)

    def lambda_AE4():
        TurnDirection(0x102, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AE4)

    def lambda_AF2():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF2)

    ChrTalk(    #40
        0x105,
        (
            "#040FSchirmer was a pirate that used to,\x01",
            "umm, work in the waters around Ruan\x01",
            "around a hundred years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "Precisely! Nicely done!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Leave it to the royal academy to\x01",
            "teach the right things! Shame\x01",
            "about the uniform, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#004FWow, you know a lot, Kloe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x105,
        (
            "#045FCome on, Estelle... It's not THAT\x01",
            "impressive!\x02\x03",

            "It's just...a story I heard, that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "I'd like to ask you to look for\x01",
            "Schirmer's treasure.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CAD():
        TurnDirection(0x101, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CAD)

    def lambda_CBB():
        TurnDirection(0x102, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CBB)

    ChrTalk(    #46
        0xFE,
        (
            "The location is marked on\x01",
            "the map...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_E9F")

    ChrTalk(    #47
        0xFE,
        (
            "Do you remember where I\x01",
            "was when we met before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "It was a pit in a sandy beach.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        "#010FThe Gull Seaside Way, right?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #50
        0xFE,
        "Exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "The map has that pit marked.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#000FIs that why you were there?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #53
        0xFE,
        (
            "That's right. I was conducting a\x01",
            "field survey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "And since I found the place,\x01",
            "monsters have started showing\x01",
            "up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "So, I figured that I should get some\x01",
            "professionals to take over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FBC")

    label("loc_E9F")


    ChrTalk(    #56
        0xFE,
        (
            "There's a place that matches that\x01",
            "description along the Gull Seaside\x01",
            "Way, but it's surrounded by cliffs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "The map has that pit marked.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "But every time I've gone to check\x01",
            "it out lately, monsters attack!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "So, I figured that I should get some\x01",
            "professionals to take over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FBC")


    ChrTalk(    #60
        0x101,
        "#000FSo, what's next after the pit?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #61
        0xFE,
        (
            "The map shows an X to the\x01",
            "southeast of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "I figure that's got to be the\x01",
            "location of the treasure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#002FY-You might be right.\x02\x03",

            "#004F...Oh, yeah! I need to make a\x01",
            "note of this.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    ChrTalk(    #64
        0x102,
        (
            "#010FWell, let's take a minute to work\x01",
            "out a plan...\x02\x03",

            "We go to the beach in Ruan,\x01",
            "find the pit, and go directly\x01",
            "southeast from there.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x335)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_206E")
    OP_28(0x1E, 0x1, 0x20)
    OP_63(0x101)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #65
        0x101,
        (
            "#505FSounds right...\x02\x03",

            "#004FAh, I just remembered. I found\x01",
            "something neat earlier, on the\x01",
            "beach.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #66
        0xFE,
        "Wh-What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "Wh-Wh-What did you find?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #68
        0x102,
        (
            "#010FA barrel drifted ashore...\x02\x03",

            "That's where you found those daggers\x01",
            "and that torn-up map, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#000FNow, where did I put those...?\x02",
    )

    CloseMessageWindow()
    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(400)
    OP_63(0xFE)

    ChrTalk(    #70
        0xFE,
        (
            "The sea chart! This could be a\x01",
            "major discovery!\x02",
        )
    )

    CloseMessageWindow()
    OP_94(0x1, 0xFE, 0x0, 0x2BC, 0xBB8, 0x0)
    TurnDirection(0x101, 0xFE, 400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)

    ChrTalk(    #71
        0xFE,
        "Please, let me see it!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#008FH-Hey, c-calm down. I don't want you\x01",
            "to die of excitement or anything...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #73
        "\x07\x00Handed over \x07\x02Torn Map\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x335, 1)
    OP_28(0x1E, 0x1, 0x40)
    OP_28(0x1E, 0x4, 0x10)
    OP_8E(0xFE, 0xCF08, 0x0, 0xBBE4, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(800)
    OP_63(0xFE)
    Sleep(400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #74
        0xFE,
        (
            "Whoa... Is this what I think it\x01",
            "is...?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "Oh, wow! This is incredible!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #76
        0xFE,
        (
            "This is one of Schirmer's treasure\x01",
            "maps!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #77
        0x101,
        "#004F#3P#1KWhat?!\x02",
    )


    ChrTalk(    #78
        0x105,
        "#044F#4P#1K...Hmm.\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()

    ChrTalk(    #79
        0x101,
        (
            "#509FNow hold on a second, mister.\x02\x03",

            "You just said a minute ago that you\x01",
            "had the treasure map already.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 400)

    ChrTalk(    #80
        0xFE,
        (
            "That had to have been a\x01",
            "'Treasure Map Map'!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "My map shows the location of THIS\x01",
            "map, which shows where the actual\x01",
            "treasure is!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #82
        0x105,
        "#045FThis is getting confusing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#007F...But I found the chart inside \x01",
            "a barrel...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #84
        0x102,
        (
            "#010FLet's not worry about that. Sometimes\x01",
            "we have to just suspend our disbelief\x01",
            "to get through the day.\x02\x03",

            "It may seem a little strange that\x01",
            "we'd find a sea chart like that...\x02\x03",

            "But the sea chart WAS found where\x01",
            "the old map has the X marked.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(    #85
        0x105,
        "#040FHa ha... That is true.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #86
        0x101,
        (
            "#505FWell, as long as our client is\x01",
            "happy...we're happy! Even if\x01",
            "we're also very confused...\x02\x03",

            "#004FOh, yeah...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    def lambda_199A():
        TurnDirection(0x102, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_199A)

    def lambda_19A8():
        TurnDirection(0x105, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_19A8)

    ChrTalk(    #87
        0x101,
        (
            "#000FHey, Jimmy? What about the daggers\x01",
            "we found with the chart?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #88
        0xFE,
        "You guys can keep those.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "I don't have much in the way of mira,\x01",
            "so it's the only payment I can offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "Please! Take them! Share in the\x01",
            "mystery with me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        "#000FOkay, thanks.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #92
        0xFE,
        (
            "Wow...this is really amazing. This sea\x01",
            "chart is just a spectacular find.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "Ha ha ha... Looks like I'll be busy\x01",
            "again, real soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "I've gotta take this to O'Neil to\x01",
            "get it deciphered. He's gonna flip!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x105,
        "#044FO'Neil?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        "Later! Thanks for your help!\x02",
    )

    CloseMessageWindow()

    def lambda_1BCF():

        label("loc_1BCF")

        TurnDirection(0x101, 0x11, 0)
        OP_48()
        Jump("loc_1BCF")

    QueueWorkItem2(0x101, 1, lambda_1BCF)

    def lambda_1BE0():

        label("loc_1BE0")

        TurnDirection(0x102, 0x11, 0)
        OP_48()
        Jump("loc_1BE0")

    QueueWorkItem2(0x102, 1, lambda_1BE0)

    def lambda_1BF1():

        label("loc_1BF1")

        TurnDirection(0x105, 0x11, 0)
        OP_48()
        Jump("loc_1BF1")

    QueueWorkItem2(0x105, 1, lambda_1BF1)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xD160, 0x0, 0xB5A4, 0x1770, 0x0)
    OP_8C(0xFE, 135, 0)
    OP_96(0xFE, 0xD6D8, 0x0, 0xAFC8, 0x5DC, 0x1B58)
    OP_8E(0xFE, 0xE1A0, 0x0, 0xAFFA, 0x1388, 0x0)
    OP_8E(0xFE, 0xE678, 0x0, 0x91B4, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x105, 0x1)
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x12, 0x320)

    ChrTalk(    #97
        0x105,
        (
            "#043FO'Neil...\x02\x03",

            "I guess he WOULD be the one\x01",
            "to talk to!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1CF5():
        TurnDirection(0x101, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CF5)

    def lambda_1D03():
        TurnDirection(0x102, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D03)

    ChrTalk(    #98
        0x101,
        "#501F#6PSo, who is he?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #99
        0x105,
        (
            "#040FHe's an older gentleman who runs\x01",
            "a general store...\x02\x03",

            "He tells lots of interesting stories,\x01",
            "but he tends to blow them out of\x01",
            "proportion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#506F#6PYeah, I get what you mean.\x02\x03",

            "So I guess that Jimmy's been taken\x01",
            "in by the old man's tall tales?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x105,
        "#045FYes, so it would appear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#007F#6P*sigh* I knew it sounded too good\x01",
            "to be true.\x02\x03",

            "#000FBut...\x02\x03",

            "If it IS true, maybe that chart really\x01",
            "is the one from his fish tales.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #103
        0x102,
        "#010FThat's possible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x105,
        (
            "#040FHa ha... I guess it is a little\x01",
            "mysterious.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #105
        0x101,
        (
            "#505FHey, if we believe in it, I wonder\x01",
            "if maybe it would pay off.\x02\x03",

            "Honestly, though, I think Jimmy\x01",
            "believes a little too, uh,\x01",
            "fervently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x102,
        (
            "#010FStill, chasing your dreams isn't\x01",
            "a bad way to live.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #107
        "\x07\x00Quest \x07\x02[Secret of the Old Map] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_24F6")

    label("loc_206E")

    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #108
        0xFE,
        "Well, that's that, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        "You've done a great job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x102,
        "#015FThank you.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #111
        0x101,
        (
            "#505FHmmm...but will we ever find it?\x02\x03",

            "All we know is to look southeast\x01",
            "from the pit.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 0)

    ChrTalk(    #112
        0x105,
        "#043FYes, and considering how wide the beach is,that still leaves a large area to search...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(    #113
        0x102,
        (
            "#013FYeah...we just don't have enough\x01",
            "information.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #114
        0xFE,
        (
            "Hey, come on guys, don't be getting all\x01",
            "negative on me now!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xFE, 0)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #115
        0xFE,
        (
            "If you comb every inch of the beach on the Gull\x01",
            "Seaside Way, I'm sure you'll find it somewhere!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 0)

    ChrTalk(    #116
        0x101,
        (
            "#007FSo in other words, treat it like\x01",
            "a test of endurance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        "#010FSounds right up your alley, Estelle.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #118
        0x101,
        (
            "#505FWell, I suppose you're right...\x02\x03",

            "But still, it wouldn't hurt to just have a TINY\x01",
            "bit more to go on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x102,
        (
            "#010FIt's not the most efficient way to go about it,\x01",
            "but what other choice is there?\x02\x03",

            "We'll just have to search the beach from top\x01",
            "to bottom and hope we find something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        "#007F*sigh* I guess you're right.\x02",
    )

    CloseMessageWindow()

    def lambda_2453():
        TurnDirection(0x101, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2453)

    def lambda_2461():
        TurnDirection(0x102, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2461)

    ChrTalk(    #121
        0x102,
        (
            "#010FOkay. If we find anything, we'll\x01",
            "be sure to let you know.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #122
        0xFE,
        (
            "I'm counting on you! Any treasure\x01",
            "we find, we split equally!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F6")

    EventEnd(0x0)
    TalkEnd(0x11)
    OP_8C(0x11, 90, 0)

    label("loc_2502")

    Return()

    # Function_0_66 end

    def Function_1_2503(): pass

    label("Function_1_2503")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrFlags(0x11, 0x10)
    Fade(1000)
    SetChrPos(0x101, 54200, 0, 49000, 270)
    SetChrPos(0x102, 54200, 0, 47500, 270)
    SetChrPos(0x105, 56000, 0, 48500, 270)
    TalkBegin(0x11)
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x12, 0x3E8)
    ClearChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_2613")

    ChrTalk(    #123
        0x101,
        "#501FHey, Jimmy...sorry we're so late...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #124
        0xFE,
        "Oh, you're finally back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "A-Any sign of the treasure?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2667")

    label("loc_2613")


    ChrTalk(    #126
        0x101,
        "#001FHey, Jimmy!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #127
        0xFE,
        "Oh, you're back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "A-Any sign of the treasure?\x02",
    )

    CloseMessageWindow()

    label("loc_2667")


    ChrTalk(    #129
        0x101,
        (
            "#505FUmm...well, we haven't found\x01",
            "anything substantial yet...\x02\x03",

            "#508FBut we did find a couple old\x01",
            "daggers and a beat-up map...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(400)
    OP_63(0xFE)

    ChrTalk(    #130
        0xFE,
        (
            "A-A sea chart! Whoa!\x01",
            "This is big stuff!\x02",
        )
    )

    CloseMessageWindow()
    OP_94(0x1, 0xFE, 0x0, 0x2BC, 0xBB8, 0x0)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)

    ChrTalk(    #131
        0xFE,
        "Please, let me see it!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#008FH-Hey, c-calm down. I don't want you\x01",
            "to die of excitement or anything...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #133
        "\x07\x00Handed over \x07\x02Torn Map\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x335, 1)
    OP_28(0x1E, 0x1, 0x40)
    OP_28(0x1E, 0x4, 0x10)
    OP_8E(0xFE, 0xCF08, 0x0, 0xBBE4, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Sleep(400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #134
        0xFE,
        (
            "Whoa... Is this what I think it\x01",
            "is...?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "Oh, wow! This is incredible!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #136
        0xFE,
        (
            "This is one of Schirmer's treasure\x01",
            "maps!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #137
        0x101,
        "#004F#3P#1KWhat?!\x02",
    )


    ChrTalk(    #138
        0x105,
        "#044F#4P#1K...Hmm.\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()

    ChrTalk(    #139
        0x101,
        (
            "#509FNow hold on a second, mister.\x02\x03",

            "You just said a minute ago that you\x01",
            "had the treasure map already.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 400)

    ChrTalk(    #140
        0xFE,
        (
            "That had to have been a\x01",
            "'Treasure Map Map'!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "My map shows the location of THIS\x01",
            "map, which shows where the actual\x01",
            "treasure is!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #142
        0x105,
        "#045FThis is getting confusing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#007F...But I found the chart inside \x01",
            "a barrel...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F5B")

    ChrTalk(    #144
        0x102,
        (
            "#010FWell, that's not the issue.\x02\x03",

            "Right now, we just don't have time\x01",
            "to spare for this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#004FOh...yeah, you're right.\x02\x03",

            "#002FI'm sorry, Jimmy. We're in a hurry,\x01",
            "so we really have to go.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #146
        0xFE,
        (
            "Don't worry about it.\x01",
            "Thanks for your help today.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(    #147
        0xFE,
        "Oh! I have things to do myself!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "I've gotta take this to O'Neil to\x01",
            "get it deciphered. He's gonna flip!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "See you later!\x01",
            "And thanks!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2DB7():

        label("loc_2DB7")

        TurnDirection(0x101, 0x11, 0)
        OP_48()
        Jump("loc_2DB7")

    QueueWorkItem2(0x101, 1, lambda_2DB7)

    def lambda_2DC8():

        label("loc_2DC8")

        TurnDirection(0x102, 0x11, 0)
        OP_48()
        Jump("loc_2DC8")

    QueueWorkItem2(0x102, 1, lambda_2DC8)

    def lambda_2DD9():

        label("loc_2DD9")

        TurnDirection(0x105, 0x11, 0)
        OP_48()
        Jump("loc_2DD9")

    QueueWorkItem2(0x105, 1, lambda_2DD9)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xD160, 0x0, 0xB5A4, 0x1770, 0x0)
    OP_8C(0xFE, 135, 0)
    OP_96(0xFE, 0xD6D8, 0x0, 0xAFC8, 0x5DC, 0x1B58)
    OP_8E(0xFE, 0xE1A0, 0x0, 0xAFFA, 0x1388, 0x0)
    OP_8E(0xFE, 0xE678, 0x0, 0x91B4, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x105, 0x1)
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x12, 0x320)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #150
        0x102,
        "#012FOkay, we should get going, too.\x02",
    )

    CloseMessageWindow()

    def lambda_2ED1():
        TurnDirection(0x101, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2ED1)

    def lambda_2EDF():
        TurnDirection(0x105, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2EDF)

    ChrTalk(    #151
        0x101,
        "#002FRight!\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #152
        "\x07\x00Quest \x07\x02[Secret of the Old Map] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_383E")

    label("loc_2F5B")


    ChrTalk(    #153
        0x102,
        (
            "#010FLet's not worry about that. Sometimes\x01",
            "we have to just suspend our disbelief\x01",
            "to get through the day.\x02\x03",

            "#010FIt may seem a little strange that\x01",
            "we'd find a sea chart like that...\x02\x03",

            "But I kind of want to believe that\x01",
            "there's something to all of this.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(    #154
        0x105,
        "#040FHa ha...as do I.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #155
        0x101,
        (
            "#505FHmm...well, it is something to\x01",
            "think about.\x02\x03",

            "Well, as long as our client is\x01",
            "happy...we're happy! Even if\x01",
            "we're also very confused...\x02\x03",

            "#004FOh, that's right...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    def lambda_3139():
        TurnDirection(0x102, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3139)

    def lambda_3147():
        TurnDirection(0x105, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3147)

    ChrTalk(    #156
        0x101,
        (
            "#000FHey, Jimmy? What about the daggers\x01",
            "we found with the chart?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #157
        0xFE,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "You guys can keep those.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "I don't have much in the way of mira,\x01",
            "so it's the only payment I can offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "Please! Take them! Share in the\x01",
            "mystery with me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#000FOkay, thanks.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #162
        0xFE,
        (
            "Wow...this is really amazing. This sea\x01",
            "chart is just a spectacular find.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "Ha ha ha... Looks like I'll be busy\x01",
            "again, real soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        "Whoa, I can't stick around here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "I've gotta take this to O'Neil to\x01",
            "get it deciphered. He's gonna flip!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x105,
        "#044FWho's O'Neil?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        "Later! Thanks for your help!\x02",
    )

    CloseMessageWindow()

    def lambda_33A7():

        label("loc_33A7")

        TurnDirection(0x101, 0x11, 0)
        OP_48()
        Jump("loc_33A7")

    QueueWorkItem2(0x101, 1, lambda_33A7)

    def lambda_33B8():

        label("loc_33B8")

        TurnDirection(0x102, 0x11, 0)
        OP_48()
        Jump("loc_33B8")

    QueueWorkItem2(0x102, 1, lambda_33B8)

    def lambda_33C9():

        label("loc_33C9")

        TurnDirection(0x105, 0x11, 0)
        OP_48()
        Jump("loc_33C9")

    QueueWorkItem2(0x105, 1, lambda_33C9)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xD160, 0x0, 0xB5A4, 0x1770, 0x0)
    OP_8C(0xFE, 135, 0)
    ClearChrFlags(0xFE, 0x1)
    OP_96(0xFE, 0xD6D8, 0x0, 0xAFC8, 0x5DC, 0x1B58)
    OP_8E(0xFE, 0xE1A0, 0x0, 0xAFFA, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x1)
    OP_8E(0xFE, 0xE678, 0x0, 0x91B4, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x105, 0x1)
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x12, 0x320)

    ChrTalk(    #168
        0x105,
        (
            "#043FO'Neil...\x02\x03",

            "Oh, okay...now I get it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34C8():
        TurnDirection(0x101, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34C8)

    def lambda_34D6():
        TurnDirection(0x102, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_34D6)

    ChrTalk(    #169
        0x101,
        "#501F#6PSo, who is he?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #170
        0x105,
        (
            "#040FHe's an older gentleman who runs\x01",
            "a general store...\x02\x03",

            "He tells lots of interesting stories,\x01",
            "but he tends to blow them out of\x01",
            "proportion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        (
            "#506F#6PYeah, I get what you mean.\x02\x03",

            "So I guess that Jimmy's been taken\x01",
            "in by the old man's tall tales?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x105,
        "#045FYes, so it would appear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        (
            "#007F#6P*sigh* I knew it sounded too good\x01",
            "to be true.\x02\x03",

            "#000FBut...\x02\x03",

            "If it IS true, maybe that chart really\x01",
            "is the one from his fish tales.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #174
        0x102,
        "#010FThat's possible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x105,
        (
            "#040FHa ha... I guess it is a little\x01",
            "mysterious.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #176
        0x101,
        (
            "#505FHey, if we believe in it, I wonder\x01",
            "if maybe it would pay off.\x02\x03",

            "Honestly, though, I think Jimmy\x01",
            "believes a little too, uh,\x01",
            "fervently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x102,
        (
            "#010FStill, chasing your dreams isn't\x01",
            "a bad way to live.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #178
        "\x07\x00Quest \x07\x02[Secret of the Old Map] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_383E")

    EventEnd(0x0)
    TalkEnd(0x11)
    Return()

    # Function_1_2503 end

    SaveToFile()

Try(main)
