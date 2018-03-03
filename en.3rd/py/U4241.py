from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4241   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4241.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60230",
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
        'Elevator',                             # 9
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 100,
        TriggerY            = -60610,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 900,
        ActorY              = -60610,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_EE",           # 00, 0
        "Function_1_120",          # 01, 1
        "Function_2_133",          # 02, 2
        "Function_3_B25",          # 03, 3
        "Function_4_B4C",          # 04, 4
        "Function_5_B78",          # 05, 5
        "Function_6_BA4",          # 06, 6
        "Function_7_BD0",          # 07, 7
        "Function_8_BE3",          # 08, 8
        "Function_9_FC5",          # 09, 9
        "Function_10_13A9",        # 0A, 10
        "Function_11_16B9",        # 0B, 11
    )


    def Function_0_EE(): pass

    label("Function_0_EE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_10F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F")
    Event(0, 10)

    label("loc_11F")

    Return()

    # Function_0_EE end

    def Function_1_120(): pass

    label("Function_1_120")

    OP_B1("U4241_1")
    OP_10(0x1, 0x0)
    OP_71(0x201, 0x0)
    ExitThread()
    Return()

    # Function_1_120 end

    def Function_2_133(): pass

    label("Function_2_133")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -780, 0, -77630, 0)
    SetChrPos(0x10F, 460, 0, -77990, 0)
    SetChrPos(0xF0, -780, 0, -77630, 0)
    SetChrPos(0xF1, 460, 0, -77990, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(160, 1350, -61500, 0)
    OP_67(0, 7990, -10000, 0)
    OP_6B(3020, 0)
    OP_6C(45000, 0)
    OP_6E(297, 0)

    def lambda_1F2():
        OP_6D(1100, 0, -67410, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1F2)

    def lambda_20A():
        OP_67(0, 5830, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_20A)

    def lambda_222():
        OP_6B(2950, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_222)

    def lambda_232():
        OP_6E(280, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_232)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x109, 0x0, 0x0, 0x3)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    OP_43(0xF0, 0x0, 0x0, 0x5)
    OP_43(0xF1, 0x0, 0x0, 0x6)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #0
        0x10F,
        "#1444F#5PIs this some form of elevator?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10E,
        (
            "#173F#6PYes. It connects the castle and a ruin\x01",
            "500 arge below it, but...\x02\x03",

            "#178F...this doesn't make any sense...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        "#1067F#5PYou're tellin' me. What's going on here?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_462")

    ChrTalk(    #3
        0x10D,
        "#270F#6PWhat exactly do you find strange?\x02",
    )

    CloseMessageWindow()

    def lambda_39D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_39D)
    Sleep(100)
    OP_8C(0x10F, 225, 400)
    Sleep(300)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #4
        0x109,
        (
            "#1063F#5PWell, when I first came to Liberl, Julia led me\x01",
            "through this room and into the area below...\x02\x03",

            "...but this isn't how this room was. It was way\x01",
            "tidier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BD")

    label("loc_462")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_494")

    ChrTalk(    #5
        0x102,
        "#1504F#6PI'm not following.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F5")

    label("loc_494")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C4")

    ChrTalk(    #6
        0x107,
        "#064F#6PWhat do you mean?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F5")

    label("loc_4C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F5")

    ChrTalk(    #7
        0x10B,
        "#213F#6PWhat's bothering you?\x02",
    )

    CloseMessageWindow()

    label("loc_4F5")


    def lambda_4FB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4FB)
    Sleep(100)
    OP_8C(0x10F, 225, 400)
    Sleep(300)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #8
        0x109,
        (
            "#1063F#5PWell, when I first came to Liberl, Julia led me\x01",
            "through this room and into the area below...\x02\x03",

            "...but this isn't how this room was. It was way\x01",
            "tidier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_80E")

    ChrTalk(    #9
        0x10E,
        (
            "#176F#6PIndeed. To my knowledge, the room was put\x01",
            "in order and then locked, and I was under\x01",
            "the impression it was to remain that way.\x02\x03",

            "#178FI have seen it this way once before, though...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_71C")

    ChrTalk(    #10
        0x102,
        (
            "#1503F#6PYeah. So have I.\x02\x03",

            "#1502FIt's exactly how I remember it being when\x01",
            "we came here during the coup d'etat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D7")

    label("loc_71C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D7")
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #11
        0x107,
        (
            "#065F#6PM-My memories of it are getting kinda hazy, but...\x02\x03",

            "...wasn't this the way it was when we all gathered\x01",
            "here during the coup d'etat?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D7")


    ChrTalk(    #12
        0x10E,
        "#176F#6PThat's what I was thinking of as well.\x02",
    )

    CloseMessageWindow()
    Jump("loc_92E")

    label("loc_80E")


    ChrTalk(    #13
        0x10E,
        (
            "#176F#6PIndeed. To my knowledge, the room was put\x01",
            "in order and then locked, and I was under the\x01",
            "impression it was to remain that way...\x02\x03",

            "#178FIt's almost as if it's returned to the same way it\x01",
            "was back during the coup d'etat.\x02\x03",

            "That's the last time I remember it being in this\x01",
            "state.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92E")


    ChrTalk(    #14
        0x10F,
        (
            "#1802F#5PAre you trying to suggest that we may have gone\x01",
            "back in time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10E,
        (
            "#175F#6PI find it impossible to believe that may have been\x01",
            "the case...but how else could I explain this?\x02\x03",

            "Of course, I could be mistaken. And yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x109,
        (
            "#1063F#5P...\x02\x03",

            "#1065FWell, if we're going to follow what that ghost\x01",
            "seems to want us to do, then we'll keep it up\x01",
            "and hope for more answers along the way.\x02\x03",

            "#1060FTime to climb on board and see what's waiting\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10E,
        "#172F#6PRight!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x271C)
    OP_28(0x2D, 0x1, 0x100)
    OP_28(0x2E, 0x4, 0x4)
    OP_28(0x2E, 0x4, 0x8)
    OP_28(0x2E, 0x1, 0x1)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_133 end

    def Function_3_B25(): pass

    label("Function_3_B25")


    def lambda_B2B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B2B)
    OP_8E(0xFE, 0xFFFFFC9A, 0x0, 0xFFFEF656, 0x7D0, 0x0)
    Return()

    # Function_3_B25 end

    def Function_4_B4C(): pass

    label("Function_4_B4C")

    Sleep(100)

    def lambda_B57():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B57)
    OP_8E(0xFE, 0x280, 0x0, 0xFFFEF624, 0x7D0, 0x0)
    Return()

    # Function_4_B4C end

    def Function_5_B78(): pass

    label("Function_5_B78")

    Sleep(900)

    def lambda_B83():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B83)
    OP_8E(0xFE, 0xFFFFFB78, 0x0, 0xFFFEEF80, 0x7D0, 0x0)
    Return()

    # Function_5_B78 end

    def Function_6_BA4(): pass

    label("Function_6_BA4")

    Sleep(900)

    def lambda_BAF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BAF)
    OP_8E(0xFE, 0x78, 0x0, 0xFFFEEF26, 0x7D0, 0x0)
    Return()

    # Function_6_BA4 end

    def Function_7_BD0(): pass

    label("Function_7_BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 5)), scpexpr(EXPR_END)), "loc_BDE")
    Call(0, 9)
    Jump("loc_BE2")

    label("loc_BDE")

    Call(0, 8)

    label("loc_BE2")

    Return()

    # Function_7_BD0 end

    def Function_8_BE3(): pass

    label("Function_8_BE3")

    EventBegin(0x0)
    Fade(500)
    SetChrBattleFlags(0x109, 0x20)
    SetChrBattleFlags(0x10F, 0x20)
    SetChrBattleFlags(0xF0, 0x20)
    SetChrBattleFlags(0xF1, 0x20)
    OP_89(0x109, -90, 100, -61250, 0)
    OP_89(0x10F, 750, 100, -62230, 0)
    OP_89(0xF0, -1230, 100, -62300, 0)
    OP_89(0xF1, -280, 100, -63320, 0)
    OP_6D(400, 100, -61120, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #18
        "\x07\x05Activate the Elevator?\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC2")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D0C"),
        (SWITCH_DEFAULT, "loc_FB2"),
    )


    label("loc_D0C")

    OP_22(0x9C, 0x0, 0x64)
    OP_71(0x401, 0x0)
    ExitThread()
    Sleep(1000)
    OP_A1(0x10, 0x0)
    SetChrPos(0x10, 0, 0, -62000, 0)
    OP_48()

    def lambda_D39():
        OP_67(0, 6000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D39)

    def lambda_D51():
        OP_6B(2700, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D51)
    OP_22(0xF7, 0x0, 0x64)
    OP_22(0x68, 0x1, 0x64)

    def lambda_D6B():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_D6B)
    Sleep(300)

    def lambda_D8B():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_D8B)
    Sleep(500)

    def lambda_DAB():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_DAB)
    Sleep(800)

    def lambda_DCB():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_DCB)
    Sleep(1000)

    def lambda_DEB():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_DEB)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x10, 0xFF)
    OP_A1(0x10, 0x2)
    SetChrPos(0x10, 0, 170000, 0, 0)
    OP_11(0x0, 0x0, 0x0, 0x7530, 0x9C40, 0x0)
    SetMapFlags(0x10)
    OP_48()
    OP_6A(0x10)
    OP_67(0, 7410, -10000, 0)
    OP_6B(1980, 0)
    OP_6C(36000, 0)
    OP_6E(450, 0)
    OP_89(0x109, -290, 190100, 470, 0)
    OP_89(0x10F, 510, 190100, -670, 0)
    OP_89(0xF0, -1180, 190100, -570, 0)
    OP_89(0xF1, -370, 190100, -1410, 0)
    Sleep(500)

    def lambda_EC1():
        OP_67(0, 11400, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_EC1)

    def lambda_ED9():
        OP_6B(1310, 10000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ED9)

    def lambda_EE9():
        OP_6C(55000, 10000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_EE9)

    def lambda_EF9():
        OP_6E(776, 10000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_EF9)

    def lambda_F09():
        OP_8F(0xFE, 0x0, 0xEA60, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_F09)
    Sleep(300)
    FadeToBright(2000, 0)
    WaitChrThread(0x10, 0x0)
    FadeToDark(2000, 0, -1)

    def lambda_F41():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_F41)
    OP_24(0x68, 0x5A)
    Sleep(400)
    OP_24(0x68, 0x55)
    Sleep(400)
    OP_24(0x68, 0x50)
    Sleep(400)
    OP_24(0x68, 0x4B)
    Sleep(400)
    OP_24(0x68, 0x46)
    Sleep(400)
    OP_24(0x68, 0x41)
    Sleep(400)
    OP_24(0x68, 0x3C)
    Sleep(400)
    OP_23(0x68)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M4300   ._SN", 101, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FBF")

    label("loc_FB2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FBF")

    label("loc_FBF")

    Jump("loc_CC7")

    label("loc_FC2")

    EventEnd(0x0)
    Return()

    # Function_8_BE3 end

    def Function_9_FC5(): pass

    label("Function_9_FC5")

    EventBegin(0x0)
    Fade(500)
    SetChrBattleFlags(0x0, 0x20)
    SetChrBattleFlags(0x1, 0x20)
    SetChrBattleFlags(0x2, 0x20)
    SetChrBattleFlags(0x3, 0x20)
    OP_89(0x0, -90, 100, -61250, 0)
    OP_89(0x1, 750, 100, -62230, 0)
    OP_89(0x2, -1230, 100, -62300, 0)
    OP_89(0x3, -280, 100, -63320, 0)
    OP_6D(400, 100, -61120, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #19
        "\x07\x05Activate the Elevator?\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A6")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes \x01",      # 0
            "No\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_10EF"),
        (SWITCH_DEFAULT, "loc_1396"),
    )


    label("loc_10EF")

    OP_22(0x9C, 0x0, 0x64)
    OP_71(0x401, 0x0)
    ExitThread()
    Sleep(1000)
    OP_A1(0x10, 0x0)
    SetChrPos(0x10, 0, 0, -62000, 0)
    OP_48()

    def lambda_111C():
        OP_67(0, 6000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_111C)

    def lambda_1134():
        OP_6B(2700, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1134)
    OP_22(0xF7, 0x0, 0x64)
    OP_22(0x68, 0x1, 0x64)

    def lambda_114E():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_114E)
    Sleep(300)

    def lambda_116E():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_116E)
    Sleep(500)

    def lambda_118E():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_118E)
    Sleep(800)

    def lambda_11AE():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_11AE)
    Sleep(1000)

    def lambda_11CE():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_11CE)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x0, 0x0)
    OP_44(0x0, 0x1)
    OP_44(0x10, 0xFF)
    OP_A1(0x10, 0x2)
    SetChrPos(0x10, 0, 170000, 0, 0)
    OP_11(0x0, 0x0, 0x0, 0x7530, 0x9C40, 0x0)
    SetMapFlags(0x10)
    OP_48()
    OP_6A(0x10)
    OP_67(0, 7410, -10000, 0)
    OP_6B(1980, 0)
    OP_6C(36000, 0)
    OP_6E(450, 0)
    OP_89(0x0, -290, 190100, 470, 0)
    OP_89(0x1, 510, 190100, -670, 0)
    OP_89(0x2, -1180, 190100, -570, 0)
    OP_89(0x3, -370, 190100, -1410, 0)
    Sleep(500)

    def lambda_12A4():
        OP_67(0, 11400, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_12A4)

    def lambda_12BC():
        OP_6B(1310, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_12BC)

    def lambda_12CC():
        OP_6C(55000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_12CC)

    def lambda_12DC():
        OP_6E(776, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_12DC)

    def lambda_12EC():
        OP_8F(0xFE, 0x0, 0xEA60, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_12EC)
    Sleep(300)
    FadeToBright(2000, 0)
    Sleep(5000)
    FadeToDark(2000, 0, -1)

    def lambda_1324():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1324)
    OP_24(0x68, 0x5A)
    Sleep(400)
    OP_24(0x68, 0x55)
    Sleep(400)
    OP_24(0x68, 0x50)
    Sleep(400)
    OP_24(0x68, 0x4B)
    Sleep(400)
    OP_24(0x68, 0x46)
    Sleep(400)
    OP_24(0x68, 0x41)
    Sleep(400)
    OP_24(0x68, 0x3C)
    Sleep(400)
    OP_23(0x68)
    OP_0D()
    OP_44(0x10, 0x0)
    NewScene("ED6_DT21/M4300   ._SN", 101, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13A3")

    label("loc_1396")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13A3")

    label("loc_13A3")

    Jump("loc_10A9")

    label("loc_13A6")

    EventEnd(0x0)
    Return()

    # Function_9_FC5 end

    def Function_10_13A9(): pass

    label("Function_10_13A9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x401, 0x0)
    ExitThread()
    OP_A1(0x10, 0x2)
    SetChrPos(0x10, 0, 70000, 0, 0)
    OP_11(0x0, 0x0, 0x0, 0x7530, 0x9C40, 0x0)
    SetMapFlags(0x10)
    OP_48()
    OP_6A(0x10)
    OP_67(0, 11400, -10000, 0)
    OP_6B(1310, 0)
    OP_6C(55000, 0)
    OP_6E(776, 0)
    SetChrBattleFlags(0x0, 0x20)
    SetChrBattleFlags(0x1, 0x20)
    SetChrBattleFlags(0x2, 0x20)
    SetChrBattleFlags(0x3, 0x20)
    OP_89(0x0, -290, 90100, 470, 0)
    OP_89(0x1, 510, 90100, -670, 0)
    OP_89(0x2, -1180, 90100, -570, 0)
    OP_89(0x3, -370, 90100, -1410, 0)
    Sleep(500)

    def lambda_1479():
        OP_67(0, 7410, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1479)

    def lambda_1491():
        OP_6B(1980, 10000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1491)

    def lambda_14A1():
        OP_6C(36000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_14A1)

    def lambda_14B1():
        OP_6E(450, 10000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_14B1)
    OP_43(0x10, 0x3, 0x0, 0xB)

    def lambda_14C8():
        OP_8F(0xFE, 0x0, 0x27100, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_14C8)
    Sleep(300)
    FadeToBright(2000, 0)
    Sleep(5000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x0)
    OP_6A(0xFF)
    OP_44(0x0, 0x0)
    OP_44(0x0, 0x1)
    OP_44(0x0, 0x2)
    OP_44(0x0, 0x3)
    ClearMapFlags(0x10)
    Sleep(300)
    OP_A1(0x10, 0x0)
    SetChrPos(0x10, 0, -10000, -62000, 0)
    OP_48()
    Sleep(100)
    SetChrBattleFlags(0x0, 0x20)
    SetChrBattleFlags(0x1, 0x20)
    SetChrBattleFlags(0x2, 0x20)
    SetChrBattleFlags(0x3, 0x20)
    OP_89(0x0, -90, -5100, -61450, 0)
    OP_89(0x1, 750, -5100, -62430, 0)
    OP_89(0x2, -1230, -5100, -62500, 0)
    OP_89(0x3, -280, -5100, -63520, 0)
    OP_6D(400, 100, -61120, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)

    def lambda_15D8():
        OP_67(0, 8000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_15D8)

    def lambda_15F0():
        OP_6B(2800, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_15F0)
    FadeToBright(1000, 0)

    def lambda_1609():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF0DD0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1609)
    Sleep(1000)

    def lambda_1629():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF0DD0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1629)
    Sleep(800)

    def lambda_1649():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF0DD0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1649)
    Sleep(600)

    def lambda_1669():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF0DD0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1669)
    Sleep(300)

    def lambda_1689():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF0DD0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1689)
    WaitChrThread(0x10, 0x1)
    OP_22(0xF7, 0x0, 0x64)
    OP_23(0x68)
    OP_72(0x401, 0x0)
    ExitThread()
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_10_13A9 end

    def Function_11_16B9(): pass

    label("Function_11_16B9")

    OP_22(0x68, 0x1, 0x0)
    Sleep(100)
    OP_24(0x68, 0xA)
    Sleep(100)
    OP_24(0x68, 0x14)
    Sleep(100)
    OP_24(0x68, 0x1E)
    Sleep(100)
    OP_24(0x68, 0x28)
    Sleep(100)
    OP_24(0x68, 0x32)
    Sleep(100)
    OP_24(0x68, 0x3C)
    Sleep(100)
    OP_24(0x68, 0x46)
    Sleep(100)
    OP_24(0x68, 0x50)
    Sleep(100)
    OP_24(0x68, 0x5A)
    Sleep(100)
    OP_24(0x68, 0x64)
    Return()

    # Function_11_16B9 end

    SaveToFile()

Try(main)
