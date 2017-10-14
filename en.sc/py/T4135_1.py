from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4135_1 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4135.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T4135_1 ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_378",          # 01, 1
        "Function_2_57F",          # 02, 2
        "Function_3_C2A",          # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(500)
    OP_6D(7120, 4000, -2220, 0)
    OP_67(0, 6860, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(52000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 6870, 4000, -2400, 192)
    SetChrPos(0x105, 6210, 4000, -1560, 181)
    SetChrPos(0x104, 7220, 4000, -1410, 180)
    SetChrPos(0x108, 6750, 4000, -500, 197)
    SetChrPos(0x9, 7000, 4000, -3740, 0)
    SetChrSubChip(0x9, 0)
    OP_0D()

    ChrTalk(    #0
        0x9,
        "Hello there. How can I help you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1000FBetter yet, how can WE help you?\x02\x03",

            "We're with the Bracer Guild, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x9,
        (
            "Oh, excellent! I was hoping\x01",
            "someone would come soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "Let's waste no time getting down\x01",
            "to business.\x02",
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
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27C")
    Call(1, 2)
    Jump("loc_375")

    label("loc_27C")


    ChrTalk(    #4
        0x101,
        (
            "#1016FHmmm, sorry.\x02\x03",

            "We wanted to check in, at least,\x01",
            "but we're actually a little too busy\x01",
            "to start right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        "Really? That's a shame.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x9,
        (
            "Well, thank you for checking in.\x01",
            "I do hope you'll be ready to take\x01",
            "on the job soon, however.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC4, 0x1, 0x8000)

    label("loc_375")

    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_378(): pass

    label("Function_1_378")

    EventBegin(0x0)
    Fade(500)
    OP_6D(7120, 4000, -2220, 0)
    OP_67(0, 6860, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(52000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 6870, 4000, -2400, 192)
    SetChrPos(0x105, 6210, 4000, -1560, 181)
    SetChrPos(0x104, 7220, 4000, -1410, 180)
    SetChrPos(0x108, 6750, 4000, -500, 197)
    SetChrPos(0x9, 7000, 4000, -3740, 0)
    SetChrSubChip(0x9, 0)
    OP_0D()

    ChrTalk(    #7
        0x9,
        (
            "Hello again! Were you able to\x01",
            "clear your schedule for the job?\x02",
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
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AC")
    Call(1, 2)
    Jump("loc_57C")

    label("loc_4AC")


    ChrTalk(    #8
        0x101,
        (
            "#1016FNot yet, sorry.\x02\x03",

            "We've still got a few other things\x01",
            "to take care of first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        "Truly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x9,
        (
            "Well, thank you for checking in again.\x01",
            "I do hope you'll be ready to take on the\x01",
            "job soon, however.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC4, 0x1, 0x8000)

    label("loc_57C")

    EventEnd(0x0)
    Return()

    # Function_1_378 end

    def Function_2_57F(): pass

    label("Function_2_57F")


    ChrTalk(    #11
        0x101,
        (
            "#1000FYeah, sure.\x02\x03",

            "#1002FSo what was stolen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x9,
        "About that...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)

    ChrTalk(    #13
        0x9,
        "Do you notice anything off here?\x02",
    )

    CloseMessageWindow()

    def lambda_5F7():
        OP_8C(0x101, 135, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5F7)
    Sleep(100)

    def lambda_60A():
        OP_8C(0x105, 135, 400)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_60A)
    Sleep(100)

    def lambda_61D():
        OP_8C(0x104, 135, 400)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_61D)
    Sleep(50)

    def lambda_630():
        OP_8C(0x108, 135, 400)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_630)
    WaitChrThread(0x108, 0x2)

    ChrTalk(    #14
        0x101,
        (
            "#1015FOff...?\x02\x03",

            "This is the airship gallery, right?\x02\x03",

            "Hey, now that you mention it,\x01",
            "something seems to be missing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x105,
        (
            "#042FYou're right, Estelle.\x02\x03",

            "There was a portrait of the Arseille\x01",
            "on this wall, as I recall.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #16
        0x101,
        (
            "#1004FNow that you mention it, Kloe,\x01",
            "I DO remember something like\x01",
            "that being here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x104,
        (
            "#030FHow could I forget? I saw the\x01",
            "portrait myself while touring the\x01",
            "capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x108,
        (
            "#072FGuess we know why you called\x01",
            "us now. The portrait of the Arseille\x01",
            "was stolen, wasn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(    #19
        0x9,
        "Precisely that.\x02",
    )

    CloseMessageWindow()

    def lambda_863():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_863)
    Sleep(100)

    def lambda_876():
        OP_8C(0x105, 180, 400)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_876)
    Sleep(100)

    def lambda_889():
        OP_8C(0x104, 180, 400)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_889)
    Sleep(50)

    def lambda_89C():
        OP_8C(0x108, 180, 400)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_89C)
    WaitChrThread(0x108, 0x2)

    ChrTalk(    #20
        0x9,
        (
            "It was there this morning, but around\x01",
            "noon or so, I'd noticed that it was gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        "This card was on the wall in its place.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #22
        (
            "\x07\x05'O beauteous princess and her loyal companions,\x01",
            "the image of the proud white falcon has fallen into\x01",
            "my hands.\x02\x03",

            "Should you seek it, then answer my challenge.\x02\x03",

            "The first key is in the residence of the aged\x01",
            "general. Search the [Onlooker of Time].'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #23
        0x101,
        "#1007F*sigh* Him. Again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x105,
        "#045FHaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x104,
        "#035FOur rivalry burns brighter still.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x108,
        (
            "#073FYeah, sounds like Phantom Thief\x01",
            "Bleublanc, all right.\x02\x03",

            "#072FYou guys told me about him,\x01",
            "but I thought you were exaggerating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x9,
        "You already know who the criminal is?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "Now that's what I call reassuring!\x01",
            "I have every confidence that you'll\x01",
            "crack this case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#1000FWe won't let you down!\x02\x03",

            "We'll be back before you know it.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC4, 0x4, 0x4)
    OP_28(0xC4, 0x4, 0x8)
    OP_28(0xC4, 0x1, 0x1)
    OP_28(0xC4, 0x1, 0x2)
    Return()

    # Function_2_57F end

    def Function_3_C2A(): pass

    label("Function_3_C2A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(7120, 4000, 4420, 0)
    OP_67(0, 6860, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(52000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 6870, 4000, -2400, 192)
    SetChrPos(0x105, 6210, 4000, -1560, 181)
    SetChrPos(0x104, 7220, 4000, -1410, 180)
    SetChrPos(0x108, 6750, 4000, -500, 197)
    SetChrPos(0x9, 7000, 4000, -3740, 0)
    SetChrSubChip(0x9, 0)
    OP_4A(0x9, 255)
    OP_72(0x1, 0x4)
    FadeToBright(1000, 0)
    OP_6D(7120, 4000, -2220, 4000)

    ChrTalk(    #30
        0x9,
        "I can't thank you enough, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        (
            "Still, why would that 'Phantom Thief'\x01",
            "fellow steal a portrait of the Arseille?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "It certainly is lovely, but it's really\x01",
            "nothing more than a simple portrait.\x01",
            "It holds little monetary value.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1015FWell, he doesn't really care about value\x01",
            "so much as he cares about pulling off a\x01",
            "good prank or two.\x02\x03",

            "#1013FAnd it's probably our fault that the\x01",
            "museum got wrapped up in his latest one.\x01",
            "Sorry for putting you through all this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "Haha, no need to apologize.\x01",
            "It wasn't your doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x9,
        (
            "And if anything, I'm very pleased with\x01",
            "how you handled this. Excellent work.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #36
        "Quest #2C[The Missing Exhibit] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0xC4, 0x4, 0x10)
    OP_28(0xC4, 0x1, 0x200)
    OP_A2(0x3)
    OP_4B(0x9, 255)
    SetChrPos(0x9, 7000, 4000, -3740, 90)
    EventEnd(0x0)
    Return()

    # Function_3_C2A end

    SaveToFile()

Try(main)
