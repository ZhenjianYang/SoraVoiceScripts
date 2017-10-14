from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T3221_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3221_1 ._SN',
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
        "Function_1_C0A",          # 01, 1
        "Function_2_DF0",          # 02, 2
        "Function_3_3306",         # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x8, 2590, 250, 5360, 180)
    SetChrPos(0x101, 2000, 250, 3320, 0)
    SetChrPos(0x107, 3030, 250, 2920, 0)
    SetChrPos(0xF7, 1910, 250, 1820, 0)
    SetChrPos(0xF9, 3060, 250, 1500, 0)
    OP_6D(1350, 250, 4070, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 2)), scpexpr(EXPR_END)), "loc_312")

    ChrTalk(    #0
        0x8,
        (
            "#683FOh, hello!\x02\x03",

            "Now, what's brought you all together\x01",
            "today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1001FWe're here to stay the night, of course!\x02\x03",

            "#1007F...Yeah, I wish. Keep dreamin', Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_248")

    ChrTalk(    #2
        0x106,
        (
            "#050F#1PUnfortunately, we're here for work today,\x01",
            "too.\x02\x03",

            "We saw the board. Seems like you've\x01",
            "got some kinda problem.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C9")

    label("loc_248")


    ChrTalk(    #3
        0x103,
        (
            "#020F#1PUnfortunately, we're here for work today,\x01",
            "too.\x02\x03",

            "We saw the board. It seems like you've\x01",
            "got some kind of problem...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C9")


    ChrTalk(    #4
        0x8,
        (
            "#682FThe board?\x02\x03",

            "Oh, that thing I contacted the guild\x01",
            "about, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A03")

    label("loc_312")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x8)

    ChrTalk(    #5
        0x8,
        "#680FOh, welcome! I see little Tita's with you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x107,
        "#061FHi, Mrs. Mao!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1001F#3PLong time no see, Mrs. Mao.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#681FWhy, hello, Estelle!\x01",
            "It HAS been a while.\x02\x03",

            "You're looking more and more\x01",
            "grown up every time I see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1008F#6PHaha, you think so?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8DB")

    ChrTalk(    #10
        0x104,
        (
            "#035FMadam, thank you for your care\x01",
            "the other day.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 400)

    ChrTalk(    #11
        0x8,
        (
            "#683FOh, I thought I'd recognized you.\x02\x03",

            "If it isn't Olivier!\x01",
            "What brings you back so soon?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_500():
        TurnDirection(0x107, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_500)
    Sleep(100)

    def lambda_513():
        TurnDirection(0x101, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_513)
    Sleep(200)
    TurnDirection(0xF7, 0x104, 400)

    ChrTalk(    #12
        0x107,
        "#064F#2PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x104,
        (
            "#031FI have my reasons.\x02\x03",

            "For now, I've been accompanying\x01",
            "Estelle as a supporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1004F#6PD-Do you two know each other?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #15
        0x8,
        (
            "#680FWe do. He stayed here not\x01",
            "that long ago.\x02\x03",

            "#685FHe's the first customer we've ever\x01",
            "had that played a lute in the baths.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6CA")

    ChrTalk(    #16
        0x106,
        "#551F#1PNew place, same shtick. Typical.\x02",
    )

    CloseMessageWindow()
    Jump("loc_709")

    label("loc_6CA")


    ChrTalk(    #17
        0x103,
        (
            "#025F#1P*sigh* I guess you do the same \x01",
            "thing everywhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_709")


    ChrTalk(    #18
        0x104,
        (
            "#031FBut of course! 'Tis the sacred duty\x01",
            "of all those dedicated to the arts.\x02\x03",

            "Time and location mean nothing to one\x01",
            "who serves the Goddess of beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1007F#6PYeah, but playing your lute in the buff?\x02\x03",

            "#1013F...\x01",
            "...\x01",
            "And now that image is in my head. Ewww.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #20
        0x107,
        "#562F#2PC-C'mon, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#680FWell, always good to see you again.\x02\x03",

            "How about staying for a while?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_89E():
        TurnDirection(0xF7, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_89E)
    Sleep(100)

    def lambda_8B1():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8B1)
    Sleep(150)

    def lambda_8C4():
        TurnDirection(0x104, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8C4)
    Sleep(50)
    TurnDirection(0x107, 0x8, 400)
    Jump("loc_932")

    label("loc_8DB")


    ChrTalk(    #22
        0x8,
        (
            "#680FWell, always good to see you again.\x02\x03",

            "How about staying for a\x01",
            "relaxing night?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_982")

    ChrTalk(    #23
        0x106,
        (
            "#050F#1PWe'd love to, but didn't you put in\x01",
            "a request for a job?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BE")

    label("loc_982")


    ChrTalk(    #24
        0x103,
        (
            "#020F#1PWe'd love to, but don't you have a\x01",
            "job for us?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BE")


    ChrTalk(    #25
        0x8,
        (
            "#680FA job?\x02\x03",

            "Oh, that thing I contacted the guild\x01",
            "about, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1482)

    label("loc_A03")


    ChrTalk(    #26
        0x101,
        (
            "#1002F#6PThat's the one.\x02\x03",

            "Something about a peeping tom\x01",
            "creeping about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#682FYes, that's right.\x02\x03",

            "If you've got a minute, I'd like you\x01",
            "to investigate immediately.\x02\x03",

            "Do you guys have time right now?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B53")

    ChrTalk(    #28
        0x101,
        "#1006F#6PYeah, no problem.\x02",
    )

    CloseMessageWindow()
    OP_28(0x70, 0x4, 0x8)
    OP_28(0x70, 0x1, 0x1)
    OP_28(0x70, 0x1, 0x2)
    Call(1, 2)
    Jump("loc_C09")

    label("loc_B53")


    ChrTalk(    #29
        0x101,
        (
            "#1007F#6PSorry. We can't right this second.\x02\x03",

            "#1002FWe'll be back as soon as we can,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "#680FIs that so?\x02\x03",

            "I don't mind waiting, but come\x01",
            "back soon, all right?\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x70, 0x1, 0x8000)
    EventEnd(0x0)
    Return()

    label("loc_C09")

    Return()

    # Function_0_AA end

    def Function_1_C0A(): pass

    label("Function_1_C0A")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x8, 2590, 250, 5360, 180)
    SetChrPos(0x101, 2000, 250, 3320, 0)
    SetChrPos(0x107, 3030, 250, 2920, 0)
    SetChrPos(0xF7, 1910, 250, 1820, 0)
    SetChrPos(0xF9, 3060, 250, 1500, 0)
    OP_6D(1350, 250, 4070, 0)
    OP_0D()

    ChrTalk(    #31
        0x8,
        (
            "#683FWelcome back!\x02\x03",

            "Ready to start the job, then?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D30")

    ChrTalk(    #32
        0x101,
        "#1006F#6PYeah, no problem. Fire away.\x02",
    )

    CloseMessageWindow()
    OP_28(0x70, 0x4, 0x8)
    Call(1, 2)
    Jump("loc_DEF")

    label("loc_D30")


    ChrTalk(    #33
        0x101,
        (
            "#1007F#6PSorry, Mrs. Mao. I don't think\x01",
            "we can do it quite yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "#685FThat's all right, I'm sure you're\x01",
            "very busy.\x02\x03",

            "#680FI don't mind waiting, but come\x01",
            "back soon, all right?\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x70, 0x1, 0x8000)
    EventEnd(0x0)

    label("loc_DEF")

    Return()

    # Function_1_C0A end

    def Function_2_DF0(): pass

    label("Function_2_DF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_E1E")

    ChrTalk(    #35
        0x106,
        "#050F#1PLet's get right to it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E5E")

    label("loc_E1E")


    ChrTalk(    #36
        0x103,
        (
            "#020F#1PWould you mind if we got\x01",
            "right to the explanation?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5E")


    ChrTalk(    #37
        0x8,
        (
            "#682FApparently, someone's been\x01",
            "peeping on my guests!\x02\x03",

            "It's a recent thing, but I've heard tell\x01",
            "from a number of my female guests\x01",
            "in particular.\x02\x03",

            "I won't stand for it, so I contacted the guild.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #38
        0x101,
        (
            "#1009F#6PUgh, peeping toms. Totally gross.\x02\x03",

            "When I find him, I'm gonna rearrange\x01",
            "his face with my staff.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1022")

    ChrTalk(    #39
        0x106,
        (
            "#050F#1PWhat kind of specifics have you\x01",
            "gotten from your guests?\x02\x03",

            "Did any of them see the criminal?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109F")

    label("loc_1022")


    ChrTalk(    #40
        0x103,
        (
            "#022F#1PHave you been able to get any\x01",
            "specific details from your guests?\x02\x03",

            "It'd be helpful if they've seen the criminal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109F")


    ChrTalk(    #41
        0x8,
        (
            "#682FNo, no, nothing that clear.\x02\x03",

            "They've been reporting things like\x01",
            "the feeling that someone's watching\x01",
            "them or strange sounds.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1172")

    ChrTalk(    #42
        0x104,
        (
            "#032FMight it only be a misunderstanding\x01",
            "of some sort?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CD")

    label("loc_1172")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11CD")

    ChrTalk(    #43
        0x105,
        (
            "#042FBut nothing concrete, right?\x02\x03",

            "Could it just be a misunderstanding?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CD")


    ChrTalk(    #44
        0x8,
        (
            "#682FMmmm, I thought so too, at first.\x02\x03",

            "But like I said before, I keep\x01",
            "getting those same reports again\x01",
            "and again.\x02\x03",

            "At this point, I can't just toss it\x01",
            "aside sayin' it's a coincidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1015F#6PThat's certainly true, but...\x01",
            "it's kind of a problem.\x02\x03",

            "It's not even clear that this is a case,\x01",
            "really. There's no way we can investigate\x01",
            "properly with any specifics.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_13DD")

    ChrTalk(    #46
        0x106,
        (
            "#053F#1PIf it ain't clear, then we just\x01",
            "gotta put it to the test.\x02\x03",

            "Not like we could make an\x01",
            "arrest unless we caught them\x01",
            "in the act, anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_148C")

    label("loc_13DD")


    ChrTalk(    #47
        0x103,
        (
            "#026F#1PWell, if it isn't clear, then we just\x01",
            "have to put it to the test.\x02\x03",

            "It'd be hard to make an arrest\x01",
            "unless we were to catch the perpetrator\x01",
            "red-handed, so why not?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_148C")


    def lambda_1492():
        TurnDirection(0x107, 0xF7, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1492)
    Sleep(50)

    def lambda_14A5():
        TurnDirection(0x101, 0xF7, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14A5)
    Sleep(100)
    TurnDirection(0xF9, 0xF7, 400)

    ChrTalk(    #48
        0x107,
        (
            "#064F#2PTest?\x02\x03",

            "Put what to the test, exactly?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x107, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_153C")

    ChrTalk(    #49
        0x106,
        (
            "#050F#1PThat should be obvious.\x02\x03",

            "We're gonna take a bath.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1579")

    label("loc_153C")


    ChrTalk(    #50
        0x103,
        (
            "#021F#1PIsn't it obvious?\x02\x03",

            "We'll take a bath ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1579")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1BCE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_186D")
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #51
        0x101,
        (
            "#1004F#4PYou want us to be bait to lure\x01",
            "out the criminal?!\x02\x03",

            "#1015FI-I don't really mind, I guess,\x01",
            "but...\x02\x03",

            "I feel like for a certain portion of us,\x01",
            "this might be a SLIGHT problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x105,
        "#540F#5P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x105, 400)

    ChrTalk(    #53
        0x106,
        (
            "#050F#1PI'm not gonna force anyone.\x02\x03",

            "#053FHowever, I'd appreciate the help.\x02\x03",

            "The more bait we have, the more\x01",
            "effective, I'm sure.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #54
        0x105,
        (
            "#540F#5POh, don't mind me.\x02\x03",

            "#047FI'd like to help in any way I can.\x02\x03",

            "#045FI'm your support, so I'd hate to\x01",
            "not be of assistance just when\x01",
            "I'm needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x106,
        (
            "#053F#1PSorry, and thanks.\x02\x03",

            "#552FStill not sure if we've got enough\x01",
            "bait, but I guess this'll have to work.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #56
        0x101,
        (
            "#1007F#4PYeah, well, excuse me for not being\x01",
            "sexy enough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FC")

    label("loc_186D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19FC")

    ChrTalk(    #57
        0x101,
        (
            "#1004F#4PYou want me to be bait to lure\x01",
            "out the criminal?!\x02\x03",

            "#1015FI-I don't really mind, I guess,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x106,
        (
            "#552F#1PDunno if you'll be much bait,\x01",
            "but you're all we got.\x02\x03",

            "#053FDo the best you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1007F#4PYeah, well, excuse me for not being\x01",
            "sexy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x104,
        (
            "#031F#5PDo not be disheartened, fair Estelle.\x01",
            "What you lack in seductiveness, you more\x01",
            "than make up for in raw nubility!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19FC")


    ChrTalk(    #61
        0x107,
        "#061F#2PHeehee!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #62
        0x101,
        (
            "#1009F#6PAwww, gimme a break.\x01",
            "Even Tita's laughing at me!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #63
        0x107,
        (
            "#064F#2PN-No, I wasn't laughing at you!\x02\x03",

            "#560FI was just...kinda happy.\x02\x03",

            "It's been a while since the two of\x01",
            "us took a bath together.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #64
        0x101,
        (
            "#1016F#6PSounds sweet enough, sure...\x02\x03",

            "But, um, you do know this is a\x01",
            "totally exploitative bait plan, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x8, 400)
    Sleep(400)

    ChrTalk(    #65
        0x106,
        (
            "#051F#1PAnyway, would you mind lending\x01",
            "us your outdoor bath, ma'am?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2593")

    label("loc_1BCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_211E")
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #66
        0x101,
        (
            "#1004F#4PYou want us to be bait to lure\x01",
            "out the criminal?!\x02\x03",

            "#1015FI-I don't really mind, I guess,\x01",
            "but...\x02\x03",

            "I feel like for a certain portion of us,\x01",
            "this might be a SLIGHT problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x105,
        "#540F#5P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x105, 400)

    ChrTalk(    #68
        0x103,
        (
            "#026F#1PI'm not gonna force anyone.\x02\x03",

            "#027FHowever, I'd appreciate the help.\x02\x03",

            "The more enticing a scene we have,\x01",
            "the more effective, I'm sure.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #69
        0x105,
        (
            "#540F#5POh, don't mind me.\x02\x03",

            "#047FI'd like to help in any way I can.\x02\x03",

            "#045FI'm your support, so I'd hate to\x01",
            "not be of assistance just when\x01",
            "I'm needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x103,
        (
            "#021F#1PHeehee! And needed, you are!\x01",
            "Thank you for your cooperation.\x02\x03",

            "#525FWith a lure like this, I'm sure\x01",
            "we'll catch ourselves a big fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x107,
        "#061F#2PHeehee!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #72
        0x101,
        "#1011F#6PYou sure seem happy, Tita.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #73
        0x107,
        (
            "#560F#2PYeah, I'm kinda excited.\x02\x03",

            "We haven't had a bath together\x01",
            "in a long time, and last time was\x01",
            "really fun.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #74
        0x101,
        (
            "#1016F#6PIt was fun last time, sure...\x02\x03",

            "But, um, you do know this is a\x01",
            "totally exploitative bait plan, right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1FF4():
        TurnDirection(0xF9, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1FF4)
    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #75
        0x103,
        (
            "#020F#1PI think Tita's on the right track.\x01",
            "Forgetting we're working a case\x01",
            "would make it a bit more natural, no?\x02\x03",

            "It's just us women, so let's take\x01",
            "the chance to let down our hair.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x8, 400)
    Sleep(400)

    ChrTalk(    #76
        0x103,
        (
            "#020F#1PAll right. You wouldn't mind\x01",
            "lending us your bath, would you,\x01",
            "ma'am?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2593")

    label("loc_211E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2593")
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #77
        0x101,
        (
            "#1004F#4PYou want us to be bait to lure\x01",
            "out the criminal?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x103,
        (
            "#020F#1PWell, it's better than just waiting\x01",
            "for the peeping tom to appear.\x02\x03",

            "#525FYou alone would be, you know,\x01",
            "but with me and Tita around, no man\x01",
            "could possibly resist taking a peek.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1007F#4PYeah, well, excuse me for not being\x01",
            "sexy enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x104,
        (
            "#031F#5PDo not be disheartened, fair Estelle.\x01",
            "What you lack in seductiveness, you more\x01",
            "than make up for in raw nubility!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x107,
        "#061F#2PHeehee!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #82
        0x101,
        (
            "#1009F#6PAwww, gimme a break.\x01",
            "Even Tita's laughing at me!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #83
        0x107,
        (
            "#064F#2PN-No, I wasn't laughing at you!\x02\x03",

            "#560FI was just...kinda happy.\x02\x03",

            "It's been a while since the two of\x01",
            "us took a bath together.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #84
        0x101,
        (
            "#1016F#6PSounds sweet enough, sure...\x02\x03",

            "But, um, you do know this is a\x01",
            "totally exploitative bait plan, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x103,
        (
            "#020F#1PI think Tita's on the right track.\x01",
            "Forgetting we're working a case\x01",
            "would make it a bit more natural, no?\x02\x03",

            "Let's just think of it as a short\x01",
            "vacation and let our hair down.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x8, 400)
    Sleep(400)

    ChrTalk(    #86
        0x103,
        (
            "#020F#1PAll right. You wouldn't mind\x01",
            "lending us your bath, would you,\x01",
            "ma'am?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2593")


    ChrTalk(    #87
        0x8,
        (
            "#681FYeah, use it as you like.\x02\x03",

            "I'll reserve it entirely for you for a bit,\x01",
            "so you four go warm yourselves up.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_260D():
        TurnDirection(0x107, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_260D)
    Sleep(250)

    def lambda_2620():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2620)
    Sleep(150)
    TurnDirection(0xF9, 0x8, 400)

    ChrTalk(    #88
        0x107,
        "#061FThanks, Mrs. Mao.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#1015F#6PPhew! I guess we're really doing this.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2CDB")

    ChrTalk(    #90
        0x106,
        (
            "#051F#1PYep, sure are.\x02\x03",

            "Have a good time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        "#1004F#6PHey, wait a sec.\x02",
    )

    CloseMessageWindow()

    def lambda_26E0():
        TurnDirection(0x107, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_26E0)

    def lambda_26EE():
        TurnDirection(0xF9, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_26EE)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #92
        0x101,
        (
            "#1004F#4PA good time?\x02\x03",

            "You're not coming\x01",
            "to the bath?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x106,
        (
            "#055F#1PThe hell are you on?\x02\x03",

            "Why do I have to go\x01",
            "into the bath?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "#682FThe better question is,\x01",
            "why wouldn't you?\x02\x03",

            "You've come this far, and yet\x01",
            "you're not gonna bathe? Well,\x01",
            "I won't stand for it!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_285B")

    ChrTalk(    #95
        0x104,
        (
            "#031F#5PShe has a point.\x02\x03",

            "Come, now, there's no\x01",
            "need to be shy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28DB")

    label("loc_285B")


    ChrTalk(    #96
        0x101,
        (
            "#1012F#4PYeah! You're the one who came\x01",
            "up with the plan in the first place.\x02\x03",

            "#1002F...Wait, are you seriously embarrassed?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28DB")

    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #97
        0x106,
        (
            "#552F#1PSh-Shut up, I'm not embarrassed.\x02\x03",

            "Work comes first, and I ain't\x01",
            "exactly what we need for this\x01",
            "job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        (
            "#685FAhhh, what nonsense!\x02\x03",

            "#682FYou've got nothing to worry about\x01",
            "if you're a man, so man up and\x01",
            "get your butt in the bath!\x02\x03",

            "To come to a hot springs and\x01",
            "not take a bath? Pfft. I've never\x01",
            "heard anything more ridiculous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        "#1015F#4P...What she said?\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x106)

    ChrTalk(    #100
        0x106,
        (
            "#551F#1PGeez, that's enough!\x02\x03",

            "I get it. I get it. I'll go in,\x01",
            "okay?\x02\x03",

            "#057FJust don't forget that this\x01",
            "is a job, you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#1006F#4PYep, no problem on that point.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #102
        0x101,
        "#1006F#6PRight, Tita?\x02",
    )

    CloseMessageWindow()

    def lambda_2B56():
        TurnDirection(0xF9, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2B56)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #103
        0x107,
        "#560F#2PY-Yeah, no problem.\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(    #104
        0x107,
        (
            "#064F...Ah, oh, no!\x02\x03",

            "Mrs. Mao, could you lend me\x01",
            "a towel set?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        "#683FOh, did you forget yours, Tita?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x107,
        (
            "#063FYeah, I didn't think I'd be taking\x01",
            "a bath.\x02\x03",

            "#064FOh, and some shampoo, too,\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#1016F#6P(W-Wow. She doesn't mess\x01",
            "around, does she?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x106,
        "#551F#1P(Not a care in the world...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_32EE")

    label("loc_2CDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3175")

    ChrTalk(    #109
        0x104,
        "#035FIs everyone ready?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #110
        0x101,
        "#1019F#4PWait, who the heck put you in charge?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #111
        0x104,
        (
            "#031FIn charge? You flatter me, but\x01",
            "I'm merely eager to be back in\x01",
            "the spring's fevered embrace.\x02\x03",

            "My last visit is still quite fresh in\x01",
            "my mind, so it's only natural that I,\x01",
            "expert as I am, should guide you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#1007F#4PThat's what your mouth says,\x01",
            "but...\x02\x03",

            "You totally intended to casually\x01",
            "follow us into the changing room,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #113
        0x104,
        (
            "#033FGhkt...?!\x02\x03",

            "#031FWh-Whatever could you mean?\x01",
            "Ah ha...haha...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        (
            "#1019F#4PIf you think you can keep pulling\x01",
            "the same old tricks, you've got\x01",
            "another thing coming, mister.\x02\x03",

            "#1007FGirls, you go on ahead.\x02\x03",

            "I have a little escort job to the men's\x01",
            "changing rooms to take care of first.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 400)

    ChrTalk(    #115
        0x103,
        (
            "#021F#1PThank you.\x02\x03",

            "Sorry, Olivier, but we'll be\x01",
            "going ahead. ㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x104, 400)

    ChrTalk(    #116
        0x107,
        "#560F#2PSee you at the outdoor bath.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x104,
        (
            "#035FHeh, heheh... Well, fine.\x02\x03",

            "I'll return this favor at the bath when--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1019F#4P...If you do return the favor,\x01",
            "my staff is going somewhere\x01",
            "sensitive.\x02\x03",

            "And I will hand you over to the\x01",
            "guild as the peeping tom.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #119
        0x104,
        "#034FY-Yes, ma'am. Understood.\x02",
    )

    CloseMessageWindow()
    Jump("loc_32EE")

    label("loc_3175")


    ChrTalk(    #120
        0x103,
        "#020F#1PWell, then, if you'll pardon us.\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(    #121
        0x107,
        (
            "#064F...Ah, oh, no!\x02\x03",

            "Mrs. Mao, could you lend me\x01",
            "a towel set?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_320F():
        TurnDirection(0xF7, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_320F)

    def lambda_321D():
        TurnDirection(0xF9, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_321D)
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #122
        0x8,
        "#683FOh, did you forget yours, Tita?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x107,
        (
            "#063FYeah, I didn't think I'd be taking\x01",
            "a bath.\x02\x03",

            "#064FOh, and some shampoo, too,\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        (
            "#1016F#6P(W-Wow. She doesn't mess\x01",
            "around, does she?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32EE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T3200   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_2_DF0 end

    def Function_3_3306(): pass

    label("Function_3_3306")

    EventBegin(0x0)
    SetChrPos(0x8, 2590, 250, 5360, 180)
    SetChrPos(0x101, 2000, 250, 3320, 0)
    SetChrPos(0x107, 3030, 250, 2920, 0)
    SetChrPos(0xF7, 1910, 250, 1820, 0)
    SetChrPos(0xF9, 3060, 250, 1500, 0)
    OP_6D(1350, 250, 4070, 0)
    OP_4A(0x8, 255)
    OP_0D()

    ChrTalk(    #125
        0x8,
        (
            "#683F#4P...My, my.\x02\x03",

            "So the peeping tom turned out\x01",
            "to be monsters.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3452")

    ChrTalk(    #126
        0x106,
        (
            "#050FWe can't be absolutely sure,\x01",
            "but it's very likely.\x02\x03",

            "We taught 'em a hard lesson, though,\x01",
            "so I don't think they'll bother you again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34CB")

    label("loc_3452")


    ChrTalk(    #127
        0x103,
        (
            "#020FWe can't be absolutely sure,\x01",
            "but it's very likely.\x02\x03",

            "We taught them a lesson,\x01",
            "so I don't think they'll be back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34CB")


    ChrTalk(    #128
        0x101,
        (
            "#1015F#6POne or two of those guys,\x01",
            "I understand.\x02\x03",

            "#1002FBut don't you think it's a little\x01",
            "weird that so many were coming?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x8,
        (
            "#682F#4PMmmm, it's very odd, indeed.\x01",
            "This is the first time we've had\x01",
            "such a thing.\x02\x03",

            "Something must have happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x107,
        (
            "#063FMaybe it has something to do\x01",
            "with the earthquakes?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3605():
        TurnDirection(0x101, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3605)
    Sleep(150)

    def lambda_3618():
        TurnDirection(0xF7, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3618)
    Sleep(100)
    TurnDirection(0xF9, 0x107, 400)

    ChrTalk(    #131
        0x101,
        "#1004F#6PEarthquakes?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #132
        0x107,
        (
            "#063F#2PUm, well, I mean, sometimes\x01",
            "monsters go a bit wild because\x01",
            "of earthquakes.\x02\x03",

            "Maybe their habitat got messed\x01",
            "up after a bad quake, or something\x01",
            "like that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3735")

    ChrTalk(    #133
        0x105,
        "#042FI see... That's certainly believable.\x02",
    )

    CloseMessageWindow()
    Jump("loc_376F")

    label("loc_3735")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_376F")

    ChrTalk(    #134
        0x104,
        "#030FHmm... It's certainly believable.\x02",
    )

    CloseMessageWindow()

    label("loc_376F")


    ChrTalk(    #135
        0x8,
        (
            "#680F#4PBelievable as it is, there's\x01",
            "not much we can do about a\x01",
            "natural disaster.\x02\x03",

            "If they show up again, I'll just\x01",
            "have to give the guild a ring.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_380D():
        OP_8C(0xF7, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_380D)
    Sleep(150)

    def lambda_3820():
        OP_8C(0x101, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3820)
    Sleep(100)

    def lambda_3833():
        OP_8C(0xF9, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3833)
    Sleep(50)
    OP_8C(0x107, 0, 400)

    ChrTalk(    #136
        0x101,
        (
            "#1006F#6PYeah, go for it!\x02\x03",

            "#1001FI'm always up for a chance to\x01",
            "relax in your bath again.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3901")

    ChrTalk(    #137
        0x106,
        (
            "#551FWell, if we were gonna come for\x01",
            "a soak, I'd rather do it off the clock.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_395B")

    label("loc_3901")


    ChrTalk(    #138
        0x103,
        (
            "#021FWell, if we were going to come\x01",
            "for a bath, I'd prefer to do it on our\x01",
            "downtime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_395B")


    ChrTalk(    #139
        0x8,
        (
            "#681FAhaha, you guys are welcome in\x01",
            "the baths any time, on the job or no.\x02\x03",

            "I owe you for today. If anything\x01",
            "comes up, you'll be the first I call.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        "#1006F#6PYeah, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x107,
        "#061FBye, Mrs. Mao!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_28(0x70, 0x4, 0x10)
    OP_28(0x70, 0x1, 0x4)
    OP_28(0x70, 0x1, 0x8)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #142
        "Quest #2C[Eliminate the Peeping Tom] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4B(0x8, 255)
    ClearMapFlags(0x10000000)
    EventEnd(0x0)
    Return()

    # Function_3_3306 end

    SaveToFile()

Try(main)
