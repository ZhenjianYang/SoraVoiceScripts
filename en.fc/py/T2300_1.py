from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T2300_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2300.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        "Function_1_DD5",          # 01, 1
    )


    def Function_0_66(): pass

    label("Function_0_66")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    Fade(1000)
    OP_6C(338000, 0)
    SetChrPos(0x0, -3200, 8000, 44000, 315)
    SetChrPos(0x1, -2000, 8000, 43900, 315)
    SetChrPos(0x2, -2800, 8000, 42500, 315)
    OP_69(0x0, 0x7D0)
    TalkBegin(0xE)
    OP_4A(0xFE, 255)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #0
        0xFE,
        "...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Umm, are all of you with the\x01",
            "Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_344")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_170")

    ChrTalk(    #2
        0x101,
        (
            "#501F...?\x02\x03",

            "#000FYeah, we are...\x02\x03",

            "I guess you must be Miss Amelia?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_230")

    label("loc_170")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AE")

    ChrTalk(    #3
        0x102,
        (
            "#014FYes, we are...\x02\x03",

            "Are you Miss Amelia?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_230")

    label("loc_1AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_230")

    ChrTalk(    #4
        0x105,
        (
            "#044FYes.\x02\x03",

            "Ah, well, I'm not, but these two\x01",
            "are.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #5
        0x101,
        (
            "#000FOh... I wonder...\x02\x03",

            "Are you Miss Amelia?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    label("loc_230")


    ChrTalk(    #6
        0xFE,
        (
            "That's right. I've been waiting\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(    #7
        0x102,
        (
            "#010FThe assignment said something about\x01",
            "an escort mission?\x02\x03",

            "Guarding someone who's headed into\x01",
            "the mountains?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #8
        0xFE,
        (
            "Yes, that's right. I want you to\x01",
            "protect my uncle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "He's going through the Krone Trail.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D7")

    label("loc_344")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A8")

    ChrTalk(    #10
        0x101,
        (
            "#004F...?\x02\x03",

            "Yeah, that's right...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(    #11
        0x102,
        "#010FWhat would you like us to do?\x02",
    )

    CloseMessageWindow()
    Jump("loc_464")

    label("loc_3A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F9")

    ChrTalk(    #12
        0x102,
        (
            "#014FYes, that's true...\x02\x03",

            "#010FWhat would you like us to do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_464")

    label("loc_3F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_464")

    ChrTalk(    #13
        0x105,
        (
            "#044FYes.\x02\x03",

            "Ah, well, I'm not, but these two\x01",
            "are.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(    #14
        0x102,
        "#010FDid you need something?\x02",
    )

    CloseMessageWindow()

    label("loc_464")

    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #15
        0xFE,
        (
            "Yes, actually... I have an escort\x01",
            "request for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "My uncle is planning to go to\x01",
            "the Krone Trail.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D7")

    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #17
        0x101,
        (
            "#000FHmm...\x02\x03",

            "#508FOh, he's traveling to Bose, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #18
        0xFE,
        "No, not exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "He wants specifically to go\x01",
            "TO the Krone Trail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#004FHuh? How come?\x02\x03",

            "Why would anyone want to just\x01",
            "go there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "He said something about looking\x01",
            "for some rare plants up there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I'm sorry. I don't really know what\x01",
            "he's talking about.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #23
        0x101,
        "#007FAh... Okay, then...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(    #24
        0x102,
        (
            "#010FWell, I think we should ask him\x01",
            "directly, then.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #25
        0xFE,
        "Indeed.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(    #26
        0xFE,
        (
            "Please wait a moment. I've already\x01",
            "called him.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xFE, 0xFFFFEA20, 0x2134, 0xB798, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    SetChrFlags(0xFE, 0x40)
    OP_94(0x1, 0xFE, 0x0, 0x9C4, 0xBB8, 0x0)
    OP_72(0x0, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x0, 30)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    SetChrFlags(0xFE, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_7EE")
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #27
        0x101,
        (
            "#003FThis sounded a lot simpler when\x01",
            "we saw it on the bulletin board...\x02\x03",

            "I have a feeling this isn't going\x01",
            "to go well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83B")

    label("loc_7EE")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #28
        0x101,
        (
            "#505FUmm... I don't really understand\x01",
            "what you're talking about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83B")

    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #29
        0x105,
        (
            "#043FKrone Trail is an exceedingly\x01",
            "dangerous place.\x02\x03",

            "I can't imagine anyone specifically\x01",
            "wanting to go there.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(    #30
        0x102,
        (
            "#010FNo kidding.\x02\x03",

            "We'll never know if we don't ask\x01",
            "the man, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_8C(0x101, 315, 400)

    ChrTalk(    #31
        0x101,
        "#000FOh, looks like he's here.\x02",
    )

    CloseMessageWindow()

    def lambda_948():
        OP_8C(0x102, 315, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_948)

    def lambda_956():
        OP_8C(0x105, 315, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_956)
    ClearChrFlags(0xFE, 0x8)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_8C(0xFE, 90, 0)
    OP_94(0x1, 0xFE, 0x0, 0x9C4, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_72(0x0, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x0, 30)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    OP_8E(0xFE, 0xFFFFEFFC, 0x1F40, 0xB02C, 0xBB8, 0x0)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #32
        0x101,
        "#000FHuh? Where's your uncle?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #33
        0xFE,
        "Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "It looks like he's already set out.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #35
        0x101,
        "#004FWhat?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(    #36
        0x102,
        (
            "#014FSet out...\x02\x03",

            "For the Krone Trail, I assume?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #37
        0xFE,
        "I think so, yes.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)

    ChrTalk(    #38
        0xFE,
        (
            "And I'd asked him to at least\x01",
            "wait until you showed up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "I don't know what made him decide\x01",
            "to just leave on his own like\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#003FHmm... That's not good...\x01",
            "not good at all...\x02\x03",

            "Why would he go there alone?\x01",
            "It's like asking for a monster\x01",
            "to eat you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        (
            "#013FIt'll be even more dangerous\x01",
            "in the dark...\x02\x03",

            "He should really be off the pass\x01",
            "by sundown.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #42
        0xFE,
        "*sigh*... I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "You came all this way for basically\x01",
            "nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#000FOh, don't worry about us.\x01",
            "We're fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "I'm really sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "I'll have a word with my uncle as\x01",
            "soon as he gets back.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x1F, 0x4, 0x4)
    OP_28(0x1F, 0x4, 0x2)
    OP_28(0x1F, 0x1, 0x1)
    OP_28(0x1F, 0x1, 0x2)
    OP_28(0x1F, 0x1, 0x4)
    OP_8E(0xFE, 0xFFFFEA20, 0x2134, 0xB798, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    SetChrFlags(0xFE, 0x40)
    OP_94(0x1, 0xFE, 0x0, 0x9C4, 0xBB8, 0x0)
    OP_72(0x0, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x0, 30)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    SetChrFlags(0xFE, 0x8)
    SetChrFlags(0xFE, 0x80)
    OP_4B(0xFE, 255)
    EventEnd(0x0)
    TalkEnd(0xE)
    Return()

    # Function_0_66 end

    def Function_1_DD5(): pass

    label("Function_1_DD5")

    FadeToBright(2000, 0)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetMapFlags(0x400000)
    OP_6C(270000, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -2780, 8000, 59500, 180)
    SetChrPos(0x101, -1780, 8000, 61500, 180)
    SetChrPos(0x102, -3780, 8000, 62500, 180)
    SetChrPos(0x105, -2780, 8000, 63500, 180)
    OP_6D(-2750, 7990, 58240, 0)

    def lambda_E53():
        OP_6C(315000, 5000)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E53)

    def lambda_E63():
        OP_94(0x1, 0x10, 0x0, 0x1CE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E63)
    Sleep(100)

    def lambda_E7E():
        OP_94(0x1, 0x101, 0x0, 0x2008, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E7E)
    Sleep(50)

    def lambda_E99():
        OP_94(0x1, 0x102, 0x0, 0x2260, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E99)
    Sleep(50)

    def lambda_EB4():
        OP_94(0x1, 0x105, 0x0, 0x21FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EB4)
    OP_0D()
    OP_6D(-2840, 7990, 52900, 4000)
    WaitChrThread(0x10, 0x1)
    TurnDirection(0x10, 0x105, 400)
    Sleep(800)

    ChrTalk(    #47
        0x10,
        "Hmm... This is splendid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        (
            "I am greatly obliged to you for\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_116F")
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #49
        0x10,
        (
            "I do hope that the matter from\x01",
            "earlier can be forgiven and\x01",
            "forgotten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10,
        (
            "It would seem that we are united\x01",
            "by fate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        (
            "When next we meet, I hope we can see\x01",
            "one another as business associates,\x01",
            "rather than mutual nuisances.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_102E():
        TurnDirection(0x105, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_102E)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #52
        0x102,
        (
            "#010FI'm okay with it...\x01",
            "What do you think, Estelle?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #53
        0x101,
        (
            "#505FHmm...\x02\x03",

            "Sounds good to me!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10A9():
        TurnDirection(0x105, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10A9)
    TurnDirection(0x102, 0x10, 400)

    ChrTalk(    #54
        0x102,
        (
            "#019FSo we're all on good terms again...\x02\x03",

            "#010FTo future successes.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(    #55
        0x10,
        "I'm very glad to hear you say that.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x105, 400)

    ChrTalk(    #56
        0x10,
        (
            "Then perhaps we'll meet again\x01",
            "on the next job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11FA")

    label("loc_116F")

    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #57
        0x101,
        "#508FGood luck out there.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10, 400)

    ChrTalk(    #58
        0x102,
        "#010FNow, if you'll excuse us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10,
        (
            "Certainly. Perhaps we'll meet\x01",
            "again on the next job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11FA")

    OP_8C(0x10, 180, 400)
    SetChrFlags(0x10, 0x40)

    def lambda_120C():

        label("loc_120C")

        TurnDirection(0x101, 0x10, 0)
        OP_48()
        Jump("loc_120C")

    QueueWorkItem2(0x101, 1, lambda_120C)

    def lambda_121D():

        label("loc_121D")

        TurnDirection(0x102, 0x10, 0)
        OP_48()
        Jump("loc_121D")

    QueueWorkItem2(0x102, 1, lambda_121D)

    def lambda_122E():

        label("loc_122E")

        TurnDirection(0x105, 0x10, 0)
        OP_48()
        Jump("loc_122E")

    QueueWorkItem2(0x105, 1, lambda_122E)
    OP_94(0x1, 0x10, 0x0, 0x2328, 0xBB8, 0x0)
    SetChrFlags(0x10, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x105, 0x1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #60
        "\x07\x00Quest \x07\x02[Escort Job] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_1_DD5 end

    SaveToFile()

Try(main)
