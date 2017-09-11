from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4134   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4134.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Sister Ellen',                         # 9
        '1st Lieutenant Schwarz',               # 10
        "Man's Voice",                          # 11
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
        'ED6_DT07/CH01410 ._CH',             # 00
        'ED6_DT06/CH20112 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01410P._CP',             # 00
        'ED6_DT06/CH20112P._CP',             # 01
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_12E",          # 01, 1
        "Function_2_12F",          # 02, 2
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_12D")
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_12D")

    Return()

    # Function_0_11A end

    def Function_1_12E(): pass

    label("Function_1_12E")

    Return()

    # Function_1_12E end

    def Function_2_12F(): pass

    label("Function_2_12F")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(80, 0, -470, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -30, 1000, 17550, 180)
    SetChrPos(0x9, -30, 1000, 17550, 0)
    SetChrPos(0x102, 10, 0, 450, 0)
    SetChrPos(0x101, -360, -250, -3700, 0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(500, 0)
    OP_8E(0x101, 0xFFFFFDF8, 0x0, 0xFFFFFACE, 0x7D0, 0x0)
    Sleep(500)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #0
        0x102,
        (
            "#012F...I'm sorry, Estelle.\x02\x03",

            "I guess I misunderstood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #2
        0x8,
        "Woman's Voice",
        "#3P...Ha ha. You came after all.\x02",
    )

    CloseMessageWindow()

    def lambda_295():
        OP_6D(-290, 1000, 16930, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_295)
    WaitChrThread(0x101, 0x2)
    Fade(1000)
    OP_6D(10, 8100, 16470, 0)
    OP_6C(0, 0)
    OP_6E(582, 0)
    OP_67(0, 3500, -10000, 0)
    OP_6B(1490, 0)
    SetChrPos(0x101, -510, 0, 9550, 0)
    SetChrPos(0x102, 500, 0, 9640, 0)
    OP_6D(0, 500, 16500, 3000)

    ChrTalk(    #3
        0x102,
        "#012FYou...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#004FHey...aren't you the nun from\x01",
            "before? The one who was\x01",
            "attacked on the scenic route?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "Thank you for what you\x01",
            "did back there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        "I assume you got my message?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#505FThat letter was yours...\x02\x03",

            "But why would you do something\x01",
            "so secretive-like just to say thanks...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#015FAhh... Now I get it.\x02\x03",

            "#010FIt was her all along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "Ha ha...\x01",
            "You're very observant, Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "Pardon me, then. Allow me to\x01",
            "get more...comfortable.\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)

    def lambda_50B():
        OP_6D(10, 500, 19000, 1000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_50B)
    OP_8C(0x8, 90, 400)
    OP_8C(0x8, 0, 400)
    OP_22(0xCB, 0x0, 0x64)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_8C(0x9, 270, 400)
    OP_8C(0x9, 180, 400)
    OP_0D()
    Sleep(500)

    ChrTalk(    #12
        0x101,
        "#004F#5SWhat?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_579():
        OP_8E(0xFE, 0xFFFFFFEC, 0x0, 0x3232, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_579)

    def lambda_594():
        OP_67(0, 5010, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_594)
    OP_6D(-10, 0, 12730, 3000)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #13
        0x9,
        (
            "#460FLieutenant Julia Schwarz, commander\x01",
            "of the Royal Guardsmen, at your\x01",
            "service.\x02\x03",

            "It's been a long time, you two.\x02\x03",

            "I knew you'd come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        (
            "#010FIt's nice to see you again, Lieutenant.\x02\x03",

            "Last time was...back in Ruan,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        (
            "#461FYes, it was.\x02\x03",

            "It hasn't been that long,\x01",
            "but it feels like ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#509FH-Hey, hold on a second...\x02\x03",

            "Why are you in that getup?\x02\x03",

            "And why'd you call us here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x9,
        (
            "#460FI'll answer your questions one\x01",
            "at a time.\x02\x03",

            "First, the clothes... The Septian\x01",
            "Church has long and deep ties\x01",
            "with the royal family.\x02\x03",

            "Colonel Richard's little conspiracy\x01",
            "has us on the run, and they've helped\x01",
            "us stay hidden within the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#007FOh, okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        (
            "#460FThe answer to your other question...\x01",
            "why I called you here...\x02\x03",

            "If you win the final match tomorrow,\x01",
            "you'll get invited to that dinner\x01",
            "party at the castle, right?\x02\x03",

            "What I need you to do is to get\x01",
            "in touch with Her Majesty, once\x01",
            "you get inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#004F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        "#014F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        (
            "#464FI realize that it's a selfish request.\x02\x03",

            "But since we're basically fugitives,\x01",
            "there's no way for us to make contact.\x02\x03",

            "You're the only hope we have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#506FWell, then...\x01",
            "This is kind of unexpected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        (
            "#010FActually, we're participating in\x01",
            "the competition specifically in\x01",
            "hopes of seeing the queen, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        "#463FWhat...?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #26
        (
            "\x07\x05Joshua explained the request that Professor Russell gave them during the\x01",
            "Leiston Fortress incident.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #27
        0x9,
        (
            "#463FReally, now...\x02\x03",

            "#465FAlmighty Aidios... Thank you\x01",
            "for your gift most sacred...\x02\x03",

            "In that case, I have only one\x01",
            "favor to ask of you.\x02\x03",

            "#460FWhen you speak to Her Majesty,\x01",
            "heed her counsel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#006FOf course. That was the plan\x01",
            "from the get-go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#010FThat non-involvement rule still applies,\x01",
            "even in a situation like this.\x02\x03",

            "But we'll do everything we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x9,
        (
            "#461FI'm grateful...\x02\x03",

            "Please, take this with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x9, 0xFFFFFF7E, 0x0, 0x2972, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #31
        "\x07\x00Received \x07\x02Julia's Letter\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x36C, 1)
    OP_8F(0x9, 0xFFFFFFD8, 0x0, 0x2EA4, 0x7D0, 0x0)

    ChrTalk(    #32
        0x101,
        "#505FWhat's this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x9,
        (
            "#460FGive this to the head maid,\x01",
            "Hilda, and she'll know that\x01",
            "you've spoken to me.\x02\x03",

            "#465FHer Majesty is probably under\x01",
            "very heavy guard by the Special\x01",
            "Ops men...\x02\x03",

            "...but you can trust Hilda. With\x01",
            "her help, you may be able to speak\x01",
            "with Her Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#501FHuh... She sounds like a\x01",
            "heck of a lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        "#010FGot it. We'll talk to her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "#460FThank you very much.\x02\x03",

            "#465FHa ha...\x01",
            "Pathetic, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#004FEh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "#464FI was deceived, and thereby\x01",
            "failed the one I was supposed\x01",
            "to protect at all costs.\x02\x03",

            "And this happened not long after I\x01",
            "swore that I would give my life to\x01",
            "safeguard Her Majesty from harm...\x02\x03",

            "You can't imagine how helpless I\x01",
            "feel having to depend entirely\x01",
            "on another's help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#505FYou really shouldn't be so hard\x01",
            "on yourself...\x02\x03",

            "#007FI hate to say this, but there\x01",
            "is the chance that we'll lose\x01",
            "tomorrow's match...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "#461FHa ha... I'm certain that you'll\x01",
            "do just fine.\x02\x03",

            "That Calvardian martial artist\x01",
            "is extremely skilled...\x02\x03",

            "...and you are both the children\x01",
            "of Colonel Cassius Bright.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #41
        0x101,
        (
            "#004FYou mean you knew\x01",
            "our dad, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        (
            "#465FIt's not without reason that he\x01",
            "was known as the finest swordsman in all\x01",
            "the Royal Army--the 'Divine Blade,' at that.\x02\x03",

            "#460FBefore he retired from service, I had a chance\x01",
            "to be trained by him when he was a martial arts\x01",
            "instructor at the military academy.\x02\x03",

            "If not for him, I would not be\x01",
            "nearly as skilled as I am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#505FI-I can't believe that... Dad's never\x01",
            "used anything except a bo staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        (
            "#465FI guess he must have given up\x01",
            "the sword when he decided to\x01",
            "become a bracer.\x02\x03",

            "His goal wasn't to kill his enemies...\x01",
            "He wanted to improve himself and help\x01",
            "those weaker than he...\x02\x03",

            "#460FThat's why he chose the bo staff\x01",
            "as his weapon...or so I imagine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#007FReally...?\x02\x03",

            "I didn't know that my use of a staff\x01",
            "had that kind of significance...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #46
        0x102,
        (
            "#010FI'm sure he hoped that you'd inherit\x01",
            "that same kind of mindset.\x02\x03",

            "I think he'd be proud of you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #47
        0x101,
        "#008FJoshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "#460FColonel Cassius trained both of you.\x02\x03",

            "I have all the faith in the world\x01",
            "that you'll win tomorrow's match.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15CF():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15CF)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #49
        0x101,
        (
            "#506FHeh heh... Hearing you say that almost\x01",
            "makes me think you're right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x102,
        (
            "#010FWe'll put everything we\x01",
            "have into it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xA, 0, 0, 1870, 0)
    OP_22(0x72, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_16C7():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16C7)

    def lambda_16D5():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16D5)

    def lambda_16E3():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_16E3)
    OP_6D(0, 0, 9920, 1000)

    NpcTalk(    #51
        0xA,
        "Man's Voice",
        (
            "#5PPardon us...\x01",
            "This is the Grancel City Guard.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #52
        0xA,
        "Man's Voice",
        (
            "#5PDue to the terrorist threat,\x01",
            "we will now be patrolling the\x01",
            "main facilities.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #53
        0xA,
        "Man's Voice",
        (
            "#5PI apologize for the lateness of the hour,\x01",
            "but do you mind if we have a look inside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#005F(Crap...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "#461FQuite all right. Thank you.\x02\x03",

            "Just a moment, please, and\x01",
            "I'll open the door.\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)

    def lambda_187A():
        OP_6D(-10, 0, 12730, 1000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_187A)

    def lambda_1892():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1892)
    TurnDirection(0x101, 0x9, 400)
    OP_8C(0x9, 90, 600)
    OP_8C(0x9, 0, 600)
    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0x9, 0)
    OP_8C(0x9, 270, 600)
    OP_8C(0x9, 180, 600)
    OP_0D()
    Sleep(500)

    ChrTalk(    #56
        0x9,
        (
            "#5P(There's another door at the\x01",
            "back of the altar room.)\x02\x03",

            "(You can get outside from there.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#006F(Okay!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        "#012F(Please be careful.)\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_197E")
    Jump("loc_19B9")

    label("loc_197E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x2000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1999")
    OP_2B(0x45, 0x1)
    Jump("loc_19B9")

    label("loc_1999")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x1000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x800)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19B4")
    OP_2B(0x45, 0x3)
    Jump("loc_19B9")

    label("loc_19B4")

    OP_2B(0x45, 0x5)

    label("loc_19B9")

    OP_A2(0x3FD)
    NewScene("ED6_DT01/T4151   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_12F end

    SaveToFile()

Try(main)
