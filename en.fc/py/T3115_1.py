from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3115_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3115.x',
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
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_3F5",          # 03, 3
        "Function_4_EAE",          # 04, 4
        "Function_5_1815",         # 05, 5
        "Function_6_26B1",         # 06, 6
        "Function_7_2F61",         # 07, 7
        "Function_8_3ADD",         # 08, 8
        "Function_9_3F0B",         # 09, 9
        "Function_10_4609",        # 0A, 10
        "Function_11_4BC8",        # 0B, 11
        "Function_12_5314",        # 0C, 12
        "Function_13_5384",        # 0D, 13
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(2300, 0, 2540, 0)
    SetChrPos(0x101, 1850, 0, 1780, 0)
    SetChrPos(0x102, 3300, 0, 2100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_105")
    SetChrPos(0x107, 2650, 0, 1120, 0)

    label("loc_105")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_124")
    SetChrPos(0x13C, 2530, 0, 3050, 359)

    label("loc_124")

    OP_0D()

    ChrTalk(    #0
        0x8,
        "#800FHmm? What's wrong?\x02",
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #1
        0x13C,
        "Nyaa～～o.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#802FAh, Antoine.\x02\x03",

            "Why are you so fussy?\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #3
        0x13C,
        (
            "Nyaa～～o.\x01",
            "NYAA～～O!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(120)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x107, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #4
        0x101,
        (
            "#509FHmmm...\x01",
            "What's this...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        "#017FLooks like we found the culprit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x107,
        "#561FYeah.\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #7
        0x8,
        (
            "#802F???\x02\x03",

            "What are you talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#002FMr. Murdock, you went to the\x01",
            "clinic today, didn't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #9
        0x8,
        (
            "#802FHuh...?!\x02\x03",

            "#805FN-No... I didn't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        (
            "#012FWe're currently looking for the\x01",
            "cigarettes that were taken from\x01",
            "there.\x02\x03",

            "Would you mind if we searched\x01",
            "this room for a bit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        "#806FS-Sure... Go ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#507FOkay.\x01",
            "We'll start immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x2C, 0x1, 0x200)
    EventEnd(0x0)
    Return()

    # Function_2_AC end

    def Function_3_3F5(): pass

    label("Function_3_3F5")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-102680, 0, 106860, 0)
    SetChrPos(0x101, -103170, 0, 107210, 90)
    SetChrPos(0x102, -102910, 0, 106140, 40)
    SetChrPos(0x107, -104120, 0, 106520, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45F")
    SetChrPos(0x13C, -104780, 0, 107680, 90)

    label("loc_45F")

    OP_0D()
    Sleep(400)

    ChrTalk(    #13
        0x101,
        (
            "#000FExcuse me...\x01",
            "Do you have a moment?\x02\x03",

            "Your name is Prometheus, right?\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x13, 0x10)
    TalkBegin(0x13)
    ClearChrFlags(0x13, 0x10)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_4A(0xFE, 255)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #14
        0xFE,
        "Aye, that's me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "What can I do for you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#006FI just need a few minutes of\x01",
            "your time.\x02\x03",

            "We're actually looking for\x01",
            "a vehicular orbal engine.\x02\x03",

            "We were told that you\x01",
            "were the man to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "Well, let me think...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Sorry, but I haven't the\x01",
            "foggiest notion.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #19
        0x101,
        "#004FHuh? Whaddya mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        (
            "#014FBut we heard that you were\x01",
            "in charge of vehicles.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #21
        0xFE,
        "Aye, but that was years long past.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I did carry out that task,\x01",
            "but I switch duties from\x01",
            "time to time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "So in other words...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "I don't know exactly who you'd need\x01",
            "to talk to...but it's not me. I'm\x01",
            "very sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#007FWell...crap...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Is that all?\x01",
            "I have a lot to get done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        "#010FSorry for taking up your time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "Excuse me, then.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 360, 400)
    OP_4B(0xFE, 255)

    def lambda_7E4():
        OP_6D(-103770, 0, 106670, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7E4)
    OP_8C(0x101, 223, 400)
    OP_8C(0x102, 286, 400)
    WaitChrThread(0xFE, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_9FF")

    ChrTalk(    #29
        0x101,
        (
            "#003FWell, that didn't go the way\x01",
            "I expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x107,
        (
            "#561FI-I'm sorry.\x02\x03",

            "This department is a little...\x01",
            "um, disorganized...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#013FWell, if Prometheus doesn't know...\x02\x03",

            "...then we've only got one last\x01",
            "clue: the information we got\x01",
            "from the Capel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#505FYeah, I made a note about the\x01",
            "factory basement entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x107,
        (
            "#060FOh, you mean the one that leads\x01",
            "out to the Kaldia Tunnel?\x02\x03",

            "A lot of equipment is\x01",
            "stored down there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        "#010FAll right...to the basement, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#006FOkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E97")

    label("loc_9FF")


    ChrTalk(    #36
        0x101,
        (
            "#003FHmmm...\x01",
            "I don't like this.\x02\x03",

            "It was supposed to be a nice,\x01",
            "easy task... A good deed we\x01",
            "could do with almost no trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x107,
        (
            "#561FI-I'm sorry.\x02\x03",

            "I wish I could be more help...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        (
            "#010FHey, it's no big deal.\x02\x03",

            "We'll just have to find some\x01",
            "other means of getting\x01",
            "what we need.\x02\x03",

            "Even if the trail has gone a\x01",
            "little cold...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_D7B")
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #39
        0x101,
        (
            "#505FAnother means...hmm...\x02\x03",

            "...\x02\x03",

            "#004F...Oh, speaking of which.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BBB():
        TurnDirection(0x107, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_BBB)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #40
        0x102,
        "#014FYou have an idea?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #41
        0x101,
        (
            "#002FWell, maybe. What about that...\x01",
            "you know...'Chapel' thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x107,
        "#060FYou mean the Capel?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #43
        0x101,
        (
            "#000FThat's the one.\x02\x03",

            "#505FDidn't that have some information\x01",
            "in it about haulage vehicles?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x107, 400)

    ChrTalk(    #44
        0x102,
        (
            "#014FThat's a good thought...\x02\x03",

            "So if we take another look at the\x01",
            "Capel, we could probably find\x01",
            "some useful info.\x02\x03",

            "#010FLet's go ahead and check it out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #45
        0x101,
        "#508FOkay!\x02",
    )

    CloseMessageWindow()
    OP_28(0x29, 0x1, 0x4)
    Jump("loc_E97")

    label("loc_D7B")


    ChrTalk(    #46
        0x101,
        (
            "#505FAnother means...\x02\x03",

            "That's going to be easier\x01",
            "said than done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        (
            "#010FWell, I'm not exactly thrilled\x01",
            "by the prospect, but we have\x01",
            "no choice.\x02\x03",

            "There may be a hint around\x01",
            "here, somewhere. We'll have\x01",
            "to search the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x107,
        "#060FRight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#006FOkay...\x02\x03",

            "Let's get moving.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E97")

    Sleep(400)
    OP_28(0x29, 0x1, 0x1)
    OP_28(0x29, 0x1, 0x2)
    OP_A2(0xC)
    EventEnd(0x0)
    Return()

    # Function_3_3F5 end

    def Function_4_EAE(): pass

    label("Function_4_EAE")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -102420, 0, 3650, 45)
    SetChrPos(0x102, -101580, 0, 3120, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F33")
    SetChrPos(0x107, -102560, 0, 2630, 45)

    label("loc_F33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F52")
    SetChrPos(0x106, -103730, 0, 3450, 45)

    label("loc_F52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F71")
    SetChrPos(0x13C, -103730, 0, 3450, 45)

    label("loc_F71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F90")
    SetChrPos(0x110, -103380, 0, 2360, 45)

    label("loc_F90")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FAA")

    def lambda_FA2():
        TurnDirection(0x0, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_FA2)

    label("loc_FAA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FC4")

    def lambda_FBC():
        TurnDirection(0x1, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_FBC)

    label("loc_FC4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FDE")

    def lambda_FD6():
        TurnDirection(0x2, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_FD6)

    label("loc_FDE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FF8")

    def lambda_FF0():
        TurnDirection(0x3, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_FF0)

    label("loc_FF8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1012")

    def lambda_100A():
        TurnDirection(0x4, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_100A)

    label("loc_1012")

    TurnDirection(0x10, 0x101, 400)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1293")

    ChrTalk(    #50
        0x101,
        (
            "#000FUm, excuse me?\x02\x03",

            "We saw your request on\x01",
            "the bulletin board.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_10F6")

    ChrTalk(    #51
        0xFE,
        "Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "You're very late. I didn't think\x01",
            "you were going to show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#506FSorry... We got wrapped\x01",
            "up in other business.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1269")

    label("loc_10F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_11A8")

    ChrTalk(    #54
        0xFE,
        "Oh... You're here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "Well, I do know that the Bracer\x01",
            "Guild is short-handed of late,\x01",
            "so what can one do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#506FSorry... We got wrapped up\x01",
            "in other business.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1269")

    label("loc_11A8")


    ChrTalk(    #57
        0xFE,
        "Oh, my. You're here already.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "I only just put in the request\x01",
            "a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#001FHee hee.♪\x02\x03",

            "#006FWell, we had just come in\x01",
            "to change assignments, so\x01",
            "we were ready for work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1269")


    ChrTalk(    #60
        0xFE,
        (
            "Well, shall we get started,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E0")

    label("loc_1293")


    ChrTalk(    #61
        0xFE,
        (
            "Oh, you're here.\x01",
            "Thank you for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "Shall we get started, then?\x02",
    )

    CloseMessageWindow()

    label("loc_12E0")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13F5")

    ChrTalk(    #63
        0x101,
        (
            "#501FUm, sorry... Right now\x01",
            "isn't the best time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "Oh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "Well, please come back\x01",
            "by, once you've finished\x01",
            "whatever business you have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#006FOkay, we will.\x02",
    )

    CloseMessageWindow()
    OP_28(0x2D, 0x1, 0x4000)

    def lambda_13EA():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_13EA)
    EventEnd(0x0)
    Return()

    label("loc_13F5")


    ChrTalk(    #67
        0x101,
        "#006FThat's fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        (
            "#010FThis is about hiring the\x01",
            "temp librarian, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #69
        0xFE,
        "Yes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "It's turned out to be much more\x01",
            "of an ordeal than expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#004FWhat kind of ordeal?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #72
        0xFE,
        "I'll explain that in a moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "Beforehand, though, I've\x01",
            "a matter that I would like\x01",
            "you to help settle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "Consider it a favor, if you will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        (
            "#010FWhat kind of 'matter' are\x01",
            "you referring to?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #76
        0xFE,
        (
            "The Archives loaned out some\x01",
            "books out to various central\x01",
            "factory departments...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "Sometimes they keep them past\x01",
            "the due date and don't pay the\x01",
            "fees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "First, I'd like you to get our\x01",
            "books back.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #79
        0x101,
        (
            "#000FWhat? That's simple.\x01",
            "Where do we need to go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "Let's see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "They should be in the third\x01",
            "floor Design Room, and the\x01",
            "fourth floor Lab and Clinic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#000FThird floor Design Room,\x01",
            "fourth floor Lab and Clinic...\x01",
            "Got it.\x02\x03",

            "...Is that everything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "Please come back once you\x01",
            "have them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        "#001FOkay, we will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x102,
        "#010FWe'll start immediately.\x02",
    )

    CloseMessageWindow()
    OP_28(0x2D, 0x4, 0x4)
    OP_28(0x2D, 0x4, 0x8)
    OP_28(0x2D, 0x1, 0x1)
    OP_28(0x2D, 0x1, 0x2)
    Call(1, 13)

    def lambda_180A():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_180A)
    EventEnd(0x0)
    Return()

    # Function_4_EAE end

    def Function_5_1815(): pass

    label("Function_5_1815")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -102420, 0, 3650, 45)
    SetChrPos(0x102, -101580, 0, 3120, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_189A")
    SetChrPos(0x107, -102560, 0, 2630, 45)

    label("loc_189A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B9")
    SetChrPos(0x106, -103730, 0, 3450, 45)

    label("loc_18B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18D8")
    SetChrPos(0x13C, -103730, 0, 3450, 45)

    label("loc_18D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18F7")
    SetChrPos(0x110, -103380, 0, 2360, 45)

    label("loc_18F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1911")

    def lambda_1909():
        TurnDirection(0x0, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1909)

    label("loc_1911")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_192B")

    def lambda_1923():
        TurnDirection(0x1, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1923)

    label("loc_192B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1945")

    def lambda_193D():
        TurnDirection(0x2, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_193D)

    label("loc_1945")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_195F")

    def lambda_1957():
        TurnDirection(0x3, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1957)

    label("loc_195F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1979")

    def lambda_1971():
        TurnDirection(0x4, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_1971)

    label("loc_1979")

    TurnDirection(0x10, 0x101, 400)
    OP_0D()

    ChrTalk(    #87
        0xFE,
        (
            "Oh...\x01",
            "Are you done?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        (
            "#001FHa ha...♪\x01",
            "We brought them for you.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_END)), "loc_1A33")
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #89
        "\x07\x00Handed over \x07\x02Septium Optic Annals\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x342, 1)

    label("loc_1A33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_END)), "loc_1A97")
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #90
        "\x07\x00Handed over \x07\x02Tomorrow's Cooking\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x341, 1)

    label("loc_1A97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_END)), "loc_1AFF")
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #91
        "\x07\x00Handed over \x07\x02Kitty-Talk for Dummies\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x340, 1)

    label("loc_1AFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_261F")
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #92
        "\x07\x00All of the books have been returned!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #93
        "\x07\x00Quest \x07\x02[Temp Librarian] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(    #94
        0xFE,
        "Good... Now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "We have all of the books again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        "I thank you for your assistance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#502FHa ha...\x01",
            "It was no big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x102,
        "#019FWe didn't have any issues.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "That's good to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "In that case, perhaps I should\x01",
            "go ahead and ask you for help\x01",
            "with my favorite type of work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        (
            "#501FOh, that's right.\x02\x03",

            "You mentioned having some\x01",
            "significant problems,\x01",
            "somewhere along the line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x102,
        "#014FSo, what kind of work is it?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #103
        0xFE,
        (
            "Just like before, we need some\x01",
            "overdue materials returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "The book in question is called,\x01",
            "'The Erbe Woodpecker.'\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #105
        0x102,
        "#015FWe'll make a note of that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#000FRight...\x01",
            "Erbe... Wood...pecker.\x02\x03",

            "#505FSo it's a book on birds, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1EC7")

    ChrTalk(    #107
        0x107,
        (
            "#060FProbably, yeah.\x02\x03",

            "The Erbe Woodpecker is a\x01",
            "pretty famous bird.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F11")

    label("loc_1EC7")


    ChrTalk(    #108
        0x107,
        (
            "#060FYeah, I think so.\x02\x03",

            "The Erbe Woodpecker is a\x01",
            "pretty famous bird.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F11")

    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #109
        0x101,
        "#000FAhhh, I see.\x02",
    )

    CloseMessageWindow()

    label("loc_1F2F")

    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(    #110
        0x102,
        (
            "#010FSo, do you have any clues\x01",
            "for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "Yes, as a matter of fact.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "...Take a look at this.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)
    Sleep(100)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #113
        (
            "\x07\x00'Approach the man of stone standing\x01",
            "in silence within the mountain village\x01",
            "pond, and ye shall receive.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #114
        0x101,
        (
            "#505FOkay, I wrote that down...\x02\x03",

            "...but what the heck is it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #115
        0xFE,
        (
            "It was written on a card that\x01",
            "was taken from the book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "I imagine that it's some kind\x01",
            "of hint as to its whereabouts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#004FA hint of bad poetry maybe...\x02\x03",

            "So...it was only borrowed because someone\x01",
            "with way too much time on their hands\x01",
            "wanted to hide it somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "Evidently so. It's the sort of\x01",
            "trick that researchers used to\x01",
            "play on each other long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "I have no idea what would\x01",
            "possess someone to hide a\x01",
            "book, of all things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "But we certainly have our fair share of unusual\x01",
            "characters. It's not surprising that any of\x01",
            "them might follow such a bizarre custom.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2356")
    OP_62(0x107, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #121
        0x107,
        (
            "#067FHa...ha ha...\x01",
            "Why's everyone looking at me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2356")


    ChrTalk(    #122
        0xFE,
        (
            "Anyway, I leave this matter in\x01",
            "your capable hands. Please,\x01",
            "bring the book back.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #123
        0x101,
        (
            "#004FH-Hey! Hold on a second. Is\x01",
            "this the only lead we have?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "I'm afraid so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "But the guild sent you, so\x01",
            "I have every confidence in\x01",
            "your ability.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #126
        0x101,
        (
            "#007F...\x02\x03",

            "Well, that's just...awesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x102,
        (
            "#010F...Understood.\x02\x03",

            "It will be difficult work, but\x01",
            "we will do all that we can.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #128
        0xFE,
        (
            "You may have to search every\x01",
            "nook and cranny in Zeiss, but\x01",
            "I'm sure you'll find it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "I'll be waiting here. When\x01",
            "you do find it, please bring\x01",
            "it back to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#007F*sigh*... Let's get this show\x01",
            "on the road, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "Ha ha... I look forward\x01",
            "to seeing you again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_266A")

    label("loc_261F")


    ChrTalk(    #132
        0xFE,
        "Good... Now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "I just need the other books.\x02",
    )

    CloseMessageWindow()
    Call(1, 13)

    def lambda_265F():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_265F)
    EventEnd(0x0)
    Return()

    label("loc_266A")

    Call(1, 13)

    def lambda_2674():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2674)
    OP_28(0x2D, 0x4, 0x10)
    OP_28(0x2D, 0x1, 0x20)
    OP_28(0x2E, 0x4, 0x2)
    OP_28(0x2E, 0x4, 0x4)
    OP_28(0x2E, 0x4, 0x8)
    OP_28(0x2E, 0x1, 0x1)
    OP_28(0x2E, 0x1, 0x2)
    OP_28(0x2E, 0x1, 0x4)
    OP_28(0x2E, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_5_1815 end

    def Function_6_26B1(): pass

    label("Function_6_26B1")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -102420, 0, 3650, 45)
    SetChrPos(0x102, -101580, 0, 3120, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2736")
    SetChrPos(0x107, -102560, 0, 2630, 45)

    label("loc_2736")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2755")
    SetChrPos(0x106, -103730, 0, 3450, 45)

    label("loc_2755")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2774")
    SetChrPos(0x13C, -103730, 0, 3450, 45)

    label("loc_2774")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2793")
    SetChrPos(0x110, -103380, 0, 2360, 45)

    label("loc_2793")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27AD")

    def lambda_27A5():
        TurnDirection(0x0, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_27A5)

    label("loc_27AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27C7")

    def lambda_27BF():
        TurnDirection(0x1, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_27BF)

    label("loc_27C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27E1")

    def lambda_27D9():
        TurnDirection(0x2, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_27D9)

    label("loc_27E1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27FB")

    def lambda_27F3():
        TurnDirection(0x3, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_27F3)

    label("loc_27FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2815")

    def lambda_280D():
        TurnDirection(0x4, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_280D)

    label("loc_2815")

    TurnDirection(0x10, 0x101, 400)
    OP_0D()

    ChrTalk(    #134
        0xFE,
        "Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "Have you come to return\x01",
            "the books?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        "#508FYep, they're right here.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_END)), "loc_28DE")
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #137
        "\x07\x00Handed over \x07\x02Septium Optic Annals\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x342, 1)

    label("loc_28DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_END)), "loc_2942")
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #138
        "\x07\x00Handed over \x07\x02Tomorrow's Cooking\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x341, 1)

    label("loc_2942")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_END)), "loc_29AA")
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #139
        "\x07\x00Handed over \x07\x02Kitty-Talk for Dummies\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x340, 1)

    label("loc_29AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C16")
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #140
        "\x07\x00All of the books have been returned!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #141
        "\x07\x00Quest \x07\x02[Temp Librarian] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(    #142
        0xFE,
        "Good... Now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        "We have all of the books again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        "I thank you for your assistance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x102,
        "#010FI'm sorry that it took so long.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #146
        0xFE,
        (
            "For a matter this important,\x01",
            "it's perfectly all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "I truly appreciate you taking\x01",
            "the time out of your busy\x01",
            "schedules to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        "#001FSure thing.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #149
        0xFE,
        "Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        "Good luck on your future journeys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x102,
        "#010FTake care.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        "#000FSee you later.\x02",
    )

    CloseMessageWindow()
    OP_28(0x2D, 0x4, 0x10)
    OP_28(0x2D, 0x1, 0x20)
    Jump("loc_2F41")

    label("loc_2C16")


    ChrTalk(    #153
        0xFE,
        "Indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "All of the remaining books\x01",
            "have been recovered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "I don't have anything more that\x01",
            "I need you to do for the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        (
            "#004FOh...\x01",
            "How come?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "I received word from the guild.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "You're going to be changing\x01",
            "assignments soon, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "Which means that I'll need to\x01",
            "get my requests in order before\x01",
            "your assignment changes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x102,
        (
            "#013FAhh, I see.\x02\x03",

            "We apologize for putting you\x01",
            "in such a position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#003FWe're really sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "Oh, my. Don't concern yourselves\x01",
            "with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "I understand that you have other\x01",
            "important business to attend to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        "#000FThank you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        "Thank you for your help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        "Be well in your travels.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x102,
        "#010FTake care.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        "#508FSee you later.\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #169
        "\x07\x00Quest \x07\x02[Temp Librarian] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2D, 0x4, 0x10)
    OP_28(0x2D, 0x1, 0x40)
    Call(1, 13)

    label("loc_2F41")

    OP_28(0x2D, 0x4, 0x10)
    OP_28(0x2D, 0x1, 0x4000)
    Call(1, 13)

    def lambda_2F56():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2F56)
    EventEnd(0x0)
    Return()

    # Function_6_26B1 end

    def Function_7_2F61(): pass

    label("Function_7_2F61")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -102420, 0, 3650, 45)
    SetChrPos(0x102, -101580, 0, 3120, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FE6")
    SetChrPos(0x107, -102560, 0, 2630, 45)

    label("loc_2FE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3005")
    SetChrPos(0x106, -103730, 0, 3450, 45)

    label("loc_3005")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3024")
    SetChrPos(0x13C, -103730, 0, 3450, 45)

    label("loc_3024")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3043")
    SetChrPos(0x110, -103380, 0, 2360, 45)

    label("loc_3043")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_305D")

    def lambda_3055():
        TurnDirection(0x0, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3055)

    label("loc_305D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3077")

    def lambda_306F():
        TurnDirection(0x1, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_306F)

    label("loc_3077")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3091")

    def lambda_3089():
        TurnDirection(0x2, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3089)

    label("loc_3091")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30AB")

    def lambda_30A3():
        TurnDirection(0x3, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_30A3)

    label("loc_30AB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30C5")

    def lambda_30BD():
        TurnDirection(0x4, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_30BD)

    label("loc_30C5")

    TurnDirection(0x10, 0x101, 400)
    OP_0D()

    ChrTalk(    #170
        0xFE,
        "Oh, have you made some progress?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        (
            "#001FYep! You bet'cha!\x02\x03",

            "#006FWe brought you your book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x102,
        "#010FPlease take a look to be certain.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #173
        "\x07\x00Handed over \x07\x02The Erbe Woodpecker\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #174
        "\x07\x00Quest \x07\x02[Temp Librarian Plus] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x343, 1)
    Sleep(100)

    ChrTalk(    #175
        0xFE,
        "Oh, my.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "This is, indeed, the right book.\x01",
            "Thank you for finding it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#502FHa ha.\x01",
            "Like there was ever any doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "To be honest, I thought it was\x01",
            "going to be a wild goose chase.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "I'm quite impressed that you\x01",
            "actually managed to find it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "Now I know I can leave the rest\x01",
            "of the work in your hands.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #181
        0x101,
        (
            "#004FRight...wait, what?!\x02\x03",

            "...What 'rest of the work'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x102,
        "#014FThere's more?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #183
        0xFE,
        (
            "Traditionally, the researchers would\x01",
            "hide three books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "This leaves us with two still\x01",
            "yet to be found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        "...Did I not tell you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#509FThis is most definitely the\x01",
            "first I've heard of it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #187
        0xFE,
        "Hmm... How odd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "But you're already aboard the\x01",
            "ship, so to speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "So, I hope I can count on your\x01",
            "full support until the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        (
            "#505FWell, I guess so...but...\x02\x03",

            "You mean we have to deal with\x01",
            "another unhinged person's idea\x01",
            "of a game?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_35D2")

    ChrTalk(    #191
        0x102,
        (
            "#017FSpeaking of which, it's\x01",
            "just like back in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35D2")


    ChrTalk(    #192
        0xFE,
        "No need to worry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        "The next book's hint has no words.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x101,
        "#004FErr, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "The proof is in the pudding,\x01",
            "as the saying goes. See for\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #196
        (
            "\x07\x00　● 　 ●　\x01",
            "　　 × 　　\x01",
            "　● 　 ●　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)

    ChrTalk(    #197
        0x101,
        (
            "#509F...\x02\x03",

            "You've gotta be kidding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x102,
        "#014FNo comments or anything...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_379C")

    ChrTalk(    #199
        0x107,
        (
            "#063F...Dots and an X?\x02\x03",

            "Hmm... Maybe the X is supposed\x01",
            "to point where the book is?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37F4")

    label("loc_379C")


    ChrTalk(    #200
        0x107,
        (
            "#063F...Dots and an X?\x02\x03",

            "Hmm... Maybe the X is supposed\x01",
            "to point where the book is?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37F4")


    ChrTalk(    #201
        0xFE,
        (
            "The name of the book in question\x01",
            "is 'Hertz's Adventure II.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        (
            "#000FHertz's...Ad...ven...ture...II.\x01",
            "Got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "Only the first part remains in the library,\x01",
            "so it gets quite frustrating having to listen\x01",
            "to patrons ask about the sequel constantly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "Well, I hope this gets you\x01",
            "fired up to find it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x102,
        (
            "#013FLovely... Another brain-teaser\x01",
            "to figure out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        (
            "#007FI take back what I said about\x01",
            "the stupid poetry. I'd MUCH\x01",
            "rather do that.\x02\x03",

            "Oh, well. Either way, we'd still\x01",
            "be stuck trying to puzzle it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "Well, best of luck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "I'll be waiting here,\x01",
            "as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x102,
        (
            "#010FAll right...\x01",
            "We'll be off, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        (
            "#006FWe'll be back with that book before you\x01",
            "know it.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x2E, 0x4, 0x10)
    OP_28(0x2E, 0x1, 0x20)
    OP_28(0x2F, 0x4, 0x2)
    OP_28(0x2F, 0x4, 0x4)
    OP_28(0x2F, 0x4, 0x8)
    OP_28(0x2F, 0x1, 0x1)
    OP_28(0x2F, 0x1, 0x2)
    OP_28(0x2F, 0x1, 0x4)
    Call(1, 13)

    def lambda_3AD2():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3AD2)
    EventEnd(0x0)
    Return()

    # Function_7_2F61 end

    def Function_8_3ADD(): pass

    label("Function_8_3ADD")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -102420, 0, 3650, 45)
    SetChrPos(0x102, -101580, 0, 3120, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B62")
    SetChrPos(0x107, -102560, 0, 2630, 45)

    label("loc_3B62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B81")
    SetChrPos(0x106, -103730, 0, 3450, 45)

    label("loc_3B81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BA0")
    SetChrPos(0x13C, -103730, 0, 3450, 45)

    label("loc_3BA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BBF")
    SetChrPos(0x110, -103380, 0, 2360, 45)

    label("loc_3BBF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BD9")

    def lambda_3BD1():
        TurnDirection(0x0, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3BD1)

    label("loc_3BD9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BF3")

    def lambda_3BEB():
        TurnDirection(0x1, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3BEB)

    label("loc_3BF3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C0D")

    def lambda_3C05():
        TurnDirection(0x2, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3C05)

    label("loc_3C0D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C27")

    def lambda_3C1F():
        TurnDirection(0x3, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3C1F)

    label("loc_3C27")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C41")

    def lambda_3C39():
        TurnDirection(0x4, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_3C39)

    label("loc_3C41")

    TurnDirection(0x10, 0x101, 400)
    OP_0D()

    ChrTalk(    #211
        0xFE,
        (
            "Oh...\x01",
            "You brought the book?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        "#006FYep.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x102,
        "#010FPlease take a look to be certain.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #214
        "\x07\x00Handed over \x07\x02The Erbe Woodpecker\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #215
        "\x07\x00Quest \x07\x02[Temp Librarian Plus] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x343, 1)
    Sleep(100)

    ChrTalk(    #216
        0xFE,
        "Oh, my.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "This is, indeed, the right book.\x01",
            "Thank you for finding it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x102,
        "#010FI'm sorry that it took so long.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #219
        0xFE,
        (
            "For a matter this important,\x01",
            "it's perfectly all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "I truly appreciate you taking\x01",
            "the time out of your busy\x01",
            "schedules to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x101,
        "#000FSure thing.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #222
        0xFE,
        "See you again some other time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        "Be well in your travels.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x102,
        "#010FTake care.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        "#508FSee you later.\x02",
    )

    CloseMessageWindow()
    OP_28(0x2E, 0x4, 0x10)
    OP_28(0x2E, 0x1, 0x20)
    OP_28(0x2D, 0x1, 0x4000)
    Call(1, 13)

    def lambda_3F00():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3F00)
    EventEnd(0x0)
    Return()

    # Function_8_3ADD end

    def Function_9_3F0B(): pass

    label("Function_9_3F0B")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -102420, 0, 3650, 45)
    SetChrPos(0x102, -101580, 0, 3120, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F90")
    SetChrPos(0x107, -102560, 0, 2630, 45)

    label("loc_3F90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FAF")
    SetChrPos(0x106, -103730, 0, 3450, 45)

    label("loc_3FAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FCE")
    SetChrPos(0x13C, -103730, 0, 3450, 45)

    label("loc_3FCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FED")
    SetChrPos(0x110, -103380, 0, 2360, 45)

    label("loc_3FED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4007")

    def lambda_3FFF():
        TurnDirection(0x0, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3FFF)

    label("loc_4007")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4021")

    def lambda_4019():
        TurnDirection(0x1, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4019)

    label("loc_4021")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_403B")

    def lambda_4033():
        TurnDirection(0x2, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4033)

    label("loc_403B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4055")

    def lambda_404D():
        TurnDirection(0x3, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_404D)

    label("loc_4055")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_406F")

    def lambda_4067():
        TurnDirection(0x4, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_4067)

    label("loc_406F")

    TurnDirection(0x10, 0x101, 400)
    OP_0D()

    ChrTalk(    #226
        0xFE,
        "Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "Did you find the book,\x01",
            "by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x101,
        (
            "#502FHeh heh...\x01",
            "Indeed we have!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x102,
        (
            "#010FAgain, please check it over,\x01",
            "just to be certain.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #230
        "\x07\x00Handed over \x07\x02Hertz's Adventure II\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #231
        "\x07\x00Quest \x07\x02[Temp Librarian Plus 2] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x344, 1)
    Sleep(100)

    ChrTalk(    #232
        0xFE,
        "Yes, this is the genuine article.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "And that leaves us with\x01",
            "just one left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x101,
        (
            "#007F*sigh*... I need a break.\x02\x03",

            "#006FWhat kind of book are we\x01",
            "chasing down this time\x01",
            "anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "Ha ha... I'll spare you the\x01",
            "teasing this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "The last one is entitled,\x01",
            "'31 Cypress Trees.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "And here's its card. It's got\x01",
            "more of that unusual writing\x01",
            "on it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #238
        (
            "\x07\x00'Ah, you (3)1 cypress trees\x01",
            "Nestled atop this Grassy Hill!\x01",
            "afflictions of far-of(F L)ands\x01",
            "draw Nigh Unto me like wine\x01",
            "BARRELs tumbling lightly down a\x01",
            "soft incline as I drift into\x01",
            "Reverie, Enveloped within the\x01",
            "resonance of the tolling Bell!'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(    #239
        0x101,
        (
            "#509FOh, man.\x01",
            "More of this gibberish.\x02\x03",

            "#007FI think I'm actually starting\x01",
            "to get used to these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x102,
        "#010FAnother riddle...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_450B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_44F5")

    ChrTalk(    #241
        0x107,
        "#062FYeah, I guess so.\x02",
    )

    CloseMessageWindow()
    Jump("loc_450B")

    label("loc_44F5")


    ChrTalk(    #242
        0x107,
        "#062FI guess so.\x02",
    )

    CloseMessageWindow()

    label("loc_450B")


    ChrTalk(    #243
        0xFE,
        "Is this your specialty or something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "Well...your task is the same\x01",
            "as before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "May Aidios herself speed you\x01",
            "on your way to success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x101,
        "#508FOkay, we're going.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x102,
        "#010FPardon us.\x02",
    )

    CloseMessageWindow()
    OP_28(0x2F, 0x4, 0x10)
    OP_28(0x2F, 0x1, 0x10)
    OP_28(0x30, 0x4, 0x2)
    OP_28(0x30, 0x4, 0x4)
    OP_28(0x30, 0x4, 0x8)
    OP_28(0x30, 0x1, 0x1)
    OP_28(0x30, 0x1, 0x2)
    Call(1, 13)

    def lambda_45FE():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_45FE)
    EventEnd(0x0)
    Return()

    # Function_9_3F0B end

    def Function_10_4609(): pass

    label("Function_10_4609")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -102420, 0, 3650, 45)
    SetChrPos(0x102, -101580, 0, 3120, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_468E")
    SetChrPos(0x107, -102560, 0, 2630, 45)

    label("loc_468E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46AD")
    SetChrPos(0x106, -103730, 0, 3450, 45)

    label("loc_46AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46CC")
    SetChrPos(0x13C, -103730, 0, 3450, 45)

    label("loc_46CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46EB")
    SetChrPos(0x110, -103380, 0, 2360, 45)

    label("loc_46EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4705")

    def lambda_46FD():
        TurnDirection(0x0, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_46FD)

    label("loc_4705")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_471F")

    def lambda_4717():
        TurnDirection(0x1, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4717)

    label("loc_471F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4739")

    def lambda_4731():
        TurnDirection(0x2, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4731)

    label("loc_4739")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4753")

    def lambda_474B():
        TurnDirection(0x3, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_474B)

    label("loc_4753")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_476D")

    def lambda_4765():
        TurnDirection(0x4, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_4765)

    label("loc_476D")

    TurnDirection(0x10, 0x101, 400)
    OP_0D()

    ChrTalk(    #248
        0xFE,
        "Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        "Did you bring me the book?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x101,
        "#508FYep.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x102,
        "#010FPlease take a look to be certain.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #252
        "\x07\x00Handed over \x07\x02Hertz's Adventure II\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #253
        "\x07\x00Quest \x07\x02[Temp Librarian Plus 2] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x344, 1)
    Sleep(100)

    ChrTalk(    #254
        0xFE,
        "Oh, my.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "This is, indeed, the right book.\x01",
            "Thank you for finding it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "Well, that concludes my requests\x01",
            "for you, at least for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x101,
        (
            "#004FOh... How come?\x02\x03",

            "Aren't there more books missing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        "I received word from the guild.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "You're going to be changing\x01",
            "assignments soon, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        (
            "Which means that I'll need to\x01",
            "get my requests in order before\x01",
            "your assignment changes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x102,
        (
            "#013FAhh, I see.\x02\x03",

            "I'm sorry to put you in such\x01",
            "a position.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #262
        0xFE,
        (
            "For a matter this important,\x01",
            "it's perfectly all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "You've already done so much\x01",
            "for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        (
            "Any other tasks can be left\x01",
            "to the bracers in the Zeiss\x01",
            "branch of the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x101,
        "#006FSure thing.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #266
        0xFE,
        "Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        "Good luck on your future journeys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x102,
        "#010FTake care.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        "#000FSee you later.\x02",
    )

    CloseMessageWindow()
    OP_28(0x2F, 0x4, 0x10)
    OP_28(0x2F, 0x1, 0x10)
    OP_28(0x2F, 0x1, 0x20)
    OP_28(0x2D, 0x1, 0x4000)
    Call(1, 13)

    def lambda_4BBD():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4BBD)
    EventEnd(0x0)
    Return()

    # Function_10_4609 end

    def Function_11_4BC8(): pass

    label("Function_11_4BC8")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -102420, 0, 3650, 45)
    SetChrPos(0x102, -101580, 0, 3120, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C4D")
    SetChrPos(0x107, -102560, 0, 2630, 45)

    label("loc_4C4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C6C")
    SetChrPos(0x106, -103730, 0, 3450, 45)

    label("loc_4C6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C8B")
    SetChrPos(0x13C, -103730, 0, 3450, 45)

    label("loc_4C8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CAA")
    SetChrPos(0x110, -103380, 0, 2360, 45)

    label("loc_4CAA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CC4")

    def lambda_4CBC():
        TurnDirection(0x0, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4CBC)

    label("loc_4CC4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CDE")

    def lambda_4CD6():
        TurnDirection(0x1, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4CD6)

    label("loc_4CDE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CF8")

    def lambda_4CF0():
        TurnDirection(0x2, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4CF0)

    label("loc_4CF8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D12")

    def lambda_4D0A():
        TurnDirection(0x3, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4D0A)

    label("loc_4D12")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D2C")

    def lambda_4D24():
        TurnDirection(0x4, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_4D24)

    label("loc_4D2C")

    TurnDirection(0x10, 0x101, 400)
    OP_0D()

    ChrTalk(    #270
        0xFE,
        "Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        "Perchance, have you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x101,
        "#006FYep. We have the last book.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x102,
        (
            "#010FJust to be sure, please\x01",
            "take a look at it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #274
        "\x07\x00Handed over \x07\x0231 Cypress Trees\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #275
        "\x07\x00Quest \x07\x02[Temp Librarian Plus 3] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x345, 1)
    Sleep(100)

    ChrTalk(    #276
        0xFE,
        "Yes, this is definitely it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "I'm impressed. You actually\x01",
            "found all three books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x101,
        (
            "#001FHeh heh... It just took some\x01",
            "perseverance and patience.\x02\x03",

            "#000FOh, yeah...\x01",
            "That's not all we found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x102,
        (
            "#010FIt was right in the same\x01",
            "spot as the book...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #280
        (
            "\x07\x05Handed over the note and quartz\x01",
            "left behind by the thief.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(    #281
        0xFE,
        (
            "Hmm... Perhaps this is a\x01",
            "clue as to his motivations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "Still, regardless of the reason,\x01",
            "you've done a great deal for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        (
            "You can keep the quartz\x01",
            "for yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "In return for my having taken\x01",
            "up so much of your time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x101,
        "#001FThank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x102,
        (
            "#010FSo, is that all that you need\x01",
            "us to do?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #287
        0xFE,
        "Yes. That's the lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x101,
        (
            "#007FWhew... That's a relief.\x02\x03",

            "I was afraid you were going to\x01",
            "say you still had more work\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51A9")

    ChrTalk(    #289
        0x107,
        "#061FHee hee... No joke.\x02",
    )

    CloseMessageWindow()

    label("loc_51A9")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #290
        0xFE,
        (
            "You've worked so hard that\x01",
            "there's really nothing left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        (
            "Ha ha... I'm very grateful\x01",
            "for your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "Now I can just relax for the\x01",
            "time being...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x101,
        "#501FWhat...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #294
        0xFE,
        "Oh, it's nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "Thank you again. Feel free\x01",
            "to come by any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x101,
        "#001FWe will. Thanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x102,
        "#010FPleased to be of service.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xE)
    OP_28(0x30, 0x4, 0x10)
    OP_28(0x30, 0x1, 0x8)
    Call(1, 13)

    def lambda_5309():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5309)
    EventEnd(0x0)
    Return()

    # Function_11_4BC8 end

    def Function_12_5314(): pass

    label("Function_12_5314")

    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #298
        "\x07\x00Found \x07\x02Septium Optic Annals\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x342, 1)
    SetChrFlags(0x18, 0x80)
    OP_64(0x7, 0x1)
    OP_28(0x2D, 0x1, 0x4)
    TalkEnd(0xFF)
    Return()

    # Function_12_5314 end

    def Function_13_5384(): pass

    label("Function_13_5384")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_5393")
    OP_65(0xD, 0x1)

    label("loc_5393")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_53A2")
    OP_65(0x9, 0x1)

    label("loc_53A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_53B1")
    OP_65(0xE, 0x1)

    label("loc_53B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53C6")
    OP_65(0xA, 0x1)

    label("loc_53C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53DB")
    OP_65(0xB, 0x1)

    label("loc_53DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53F0")
    OP_65(0xC, 0x1)

    label("loc_53F0")

    Return()

    # Function_13_5384 end

    SaveToFile()

Try(main)
