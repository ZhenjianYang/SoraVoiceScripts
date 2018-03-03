from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7407   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7407.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60225",
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


    DeclActor(
        TriggerX            = 6940,
        TriggerZ            = 0,
        TriggerY            = 42960,
        TriggerRange        = 1000,
        ActorX              = 6940,
        ActorZ              = 1000,
        ActorY              = 42960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 0,
        TriggerY            = 82100,
        TriggerRange        = 2000,
        ActorX              = 0,
        ActorZ              = 1500,
        ActorY              = 82100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F2",           # 00, 0
        "Function_1_F3",           # 01, 1
        "Function_2_FA",           # 02, 2
        "Function_3_C2B",          # 03, 3
        "Function_4_1653",         # 04, 4
        "Function_5_1693",         # 05, 5
        "Function_6_16D8",         # 06, 6
        "Function_7_171D",         # 07, 7
        "Function_8_1762",         # 08, 8
    )


    def Function_0_F2(): pass

    label("Function_0_F2")

    Return()

    # Function_0_F2 end

    def Function_1_F3(): pass

    label("Function_1_F3")

    OP_72(0x1000, 0x0)
    ExitThread()
    Return()

    # Function_1_F3 end

    def Function_2_FA(): pass

    label("Function_2_FA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A32")
    OP_A2(0x2C29)
    Fade(1000)
    OP_6D(340, 6750, 76730, 0)
    OP_67(0, 3130, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(404, 0)
    SetChrPos(0xFA, -750, 0, 78490, 0)
    SetChrPos(0xFB, 750, 0, 78380, 0)
    SetChrPos(0xFC, -1250, 0, 76780, 0)
    SetChrPos(0xFD, 1250, 0, 76810, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)

    def lambda_1BB():
        OP_6B(4000, 5000)
        ExitThread()

    QueueWorkItem(0xFA, 0, lambda_1BB)
    OP_0D()
    WaitChrThread(0xFA, 0x0)
    Fade(500)
    OP_6D(1110, 0, 79950, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(2610, 0)
    OP_6C(45000, 0)
    OP_6E(357, 0)
    SetChrPos(0xFA, -1120, 0, 78970, 0)
    SetChrPos(0xFB, 410, 0, 78980, 0)
    SetChrPos(0xFC, -1330, 0, 77010, 0)
    SetChrPos(0xFD, 210, 0, 77060, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28E")

    ChrTalk(    #0
        0x101,
        "#1020F#12PTh-This door's huge...\x02",
    )

    CloseMessageWindow()
    Jump("loc_559")

    label("loc_28E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D9")

    ChrTalk(    #1
        0x102,
        "#1502F#12PThis door's much bigger than the others...\x02",
    )

    CloseMessageWindow()
    Jump("loc_559")

    label("loc_2D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30F")

    ChrTalk(    #2
        0x107,
        "#065F#12PTh-This door's huge...\x02",
    )

    CloseMessageWindow()
    Jump("loc_559")

    label("loc_30F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_345")

    ChrTalk(    #3
        0x10B,
        "#216F#12PTh-This door's huge...\x02",
    )

    CloseMessageWindow()
    Jump("loc_559")

    label("loc_345")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37C")

    ChrTalk(    #4
        0x10A,
        "#1317F#12PTh-This door's huge...\x02",
    )

    CloseMessageWindow()
    Jump("loc_559")

    label("loc_37C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B6")

    ChrTalk(    #5
        0x105,
        "#1162F#12PThis is quite the door...\x02",
    )

    CloseMessageWindow()
    Jump("loc_559")

    label("loc_3B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EF")

    ChrTalk(    #6
        0x103,
        "#1522F#12PThis is one huge door...\x02",
    )

    CloseMessageWindow()
    Jump("loc_559")

    label("loc_3EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_426")

    ChrTalk(    #7
        0x106,
        "#057F#12PDamn. This door's huge.\x02",
    )

    CloseMessageWindow()
    Jump("loc_559")

    label("loc_426")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_465")

    ChrTalk(    #8
        0x108,
        "#072F#12PThis is quite a sizable door...\x02",
    )

    CloseMessageWindow()
    Jump("loc_559")

    label("loc_465")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A4")

    ChrTalk(    #9
        0x10E,
        "#172F#12PThis is quite a sizable door...\x02",
    )

    CloseMessageWindow()
    Jump("loc_559")

    label("loc_4A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DE")

    ChrTalk(    #10
        0x104,
        "#1542F#12PThis is quite a big door.\x02",
    )

    CloseMessageWindow()
    Jump("loc_559")

    label("loc_4DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51D")

    ChrTalk(    #11
        0x10D,
        "#270F#12PThis is quite a sizable door...\x02",
    )

    CloseMessageWindow()
    Jump("loc_559")

    label("loc_51D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_559")

    ChrTalk(    #12
        0x10C,
        "#112F#12PThis is quite a sizable door...\x02",
    )

    CloseMessageWindow()

    label("loc_559")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CA")

    ChrTalk(    #13
        0x110,
        (
            "#1306F#12PHeehee. I'm guessing that means there's\x01",
            "something significant on the other side.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2F")

    label("loc_5CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62A")

    ChrTalk(    #14
        0x10C,
        (
            "#112F#12PThen there must be something significant\x01",
            "on the other side, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2F")

    label("loc_62A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68A")

    ChrTalk(    #15
        0x10D,
        (
            "#276F#12PThen there must be something significant\x01",
            "on the other side, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2F")

    label("loc_68A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F2")

    ChrTalk(    #16
        0x104,
        (
            "#1540F#12PHmm... Then there must be something significant\x01",
            "on the other side, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2F")

    label("loc_6F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_759")

    ChrTalk(    #17
        0x10E,
        (
            "#178F#12PHmm... Then there must be something significant\x01",
            "on the other side, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2F")

    label("loc_759")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C0")

    ChrTalk(    #18
        0x108,
        (
            "#070F#12PHmm... Then there must be something significant\x01",
            "on the other side, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2F")

    label("loc_7C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_805")

    ChrTalk(    #19
        0x106,
        "#051F#12PThey went all out on the design, huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2F")

    label("loc_805")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_847")

    ChrTalk(    #20
        0x103,
        "#1527F#12POh, my... Well, isn't this fancy?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2F")

    label("loc_847")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A8")

    ChrTalk(    #21
        0x105,
        (
            "#1162F#12PThen there must be something significant\x01",
            "on the other side, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2F")

    label("loc_8A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_90B")

    ChrTalk(    #22
        0x10A,
        (
            "#819F#12PTh-This door's gotta have something major\x01",
            "on the other side, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2F")

    label("loc_90B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_96E")

    ChrTalk(    #23
        0x10B,
        (
            "#216F#12PTh-This door's gotta have something major\x01",
            "on the other side, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2F")

    label("loc_96E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D1")

    ChrTalk(    #24
        0x107,
        (
            "#065F#12PTh-This door's gotta have something major\x01",
            "on the other side, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2F")

    label("loc_9D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A2F")

    ChrTalk(    #25
        0x102,
        (
            "#1502F#12PThen there must be something significant\x01",
            "on the other side, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2F")

    Jump("loc_AE6")

    label("loc_A32")

    Fade(500)
    OP_6D(1110, 0, 79950, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(2610, 0)
    OP_6C(45000, 0)
    OP_6E(357, 0)
    SetChrPos(0xFA, -1120, 0, 78970, 0)
    SetChrPos(0xFB, 410, 0, 78980, 0)
    SetChrPos(0xFC, -1330, 0, 77010, 0)
    SetChrPos(0xFD, 210, 0, 77060, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)

    label("loc_AE6")


    ChrTalk(    #26
        0x109,
        "#1063F#6PI think we've reached our destination.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10F,
        "#1936F#12P...Yeah. I can sense Rufina on the other side.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFB, 270, 400)
    Sleep(300)

    ChrTalk(    #28
        0x10F,
        "#1933F#11PWhat should we do, Kevin?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C26)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C28")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Open the Door\x01",      # 0
            "Step Away\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C02"),
        (SWITCH_DEFAULT, "loc_C13"),
    )


    label("loc_C02")

    Call(0, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C25")

    label("loc_C13")

    Fade(1000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C25")

    label("loc_C25")

    Jump("loc_BAE")

    label("loc_C28")

    EventEnd(0x0)
    Return()

    # Function_2_FA end

    def Function_3_C2B(): pass

    label("Function_3_C2B")

    OP_20(0x7D0)

    def lambda_C36():
        OP_6D(1390, 0, 79820, 1500)
        ExitThread()

    QueueWorkItem(0xFA, 0, lambda_C36)

    def lambda_C4E():
        OP_67(0, 5400, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_C4E)

    def lambda_C66():
        OP_6B(2500, 1500)
        ExitThread()

    QueueWorkItem(0xFA, 2, lambda_C66)
    OP_8C(0xFA, 180, 400)
    WaitChrThread(0xFA, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E80")

    ChrTalk(    #29
        0x109,
        (
            "#1840F#5PI can't thank you two enough for sticking with\x01",
            "me up till the very end.\x02\x03",

            "What I'd like to do instead is ask for your help\x01",
            "one more time.\x02\x03",

            "#1065FWe'll be up against the Lord of Phantasma--the\x01",
            "being capable of changing and reconstructing this\x01",
            "entire world according to their whims.\x02\x03",

            "#1063FThis fight is gonna be nasty, and the only way we'll\x01",
            "even stand a chance is if we give it all we've got--\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1023")

    label("loc_E80")


    ChrTalk(    #30
        0x109,
        (
            "#1840F#5PI can't thank you two enough for sticking with\x01",
            "me up till the very end.\x02\x03",

            "But if I could, I'd like to ask for a little more of\x01",
            "your help instead.\x02\x03",

            "#1065FWe're up against the Lord of Phantasma--the being\x01",
            "capable of changing and reconstructing this entire\x01",
            "world according to their whims.\x02\x03",

            "#1063FIt's going to be nasty, and the only way we'll even\x01",
            "stand a chance is if we fight with our everything.\x01",
            "Together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1023")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_104A")

    ChrTalk(    #31
        0x101,
        "#1006F#12PNo sweat!\x02",
    )

    CloseMessageWindow()

    label("loc_104A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1072")

    ChrTalk(    #32
        0x102,
        "#1500F#12POf course!\x02",
    )

    CloseMessageWindow()

    label("loc_1072")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10B4")

    ChrTalk(    #33
        0x10C,
        "#119F#12PThat was my intention from the start!\x02",
    )

    CloseMessageWindow()

    label("loc_10B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10DC")

    ChrTalk(    #34
        0x10E,
        "#170F#12PUnderstood!\x02",
    )

    CloseMessageWindow()

    label("loc_10DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1108")

    ChrTalk(    #35
        0x106,
        "#051F#12PLeave it to me!\x02",
    )

    CloseMessageWindow()

    label("loc_1108")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1139")

    ChrTalk(    #36
        0x108,
        "#070F#12PLet's get this done!\x02",
    )

    CloseMessageWindow()

    label("loc_1139")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_117D")

    ChrTalk(    #37
        0x10D,
        "#275F#12PMy sword won't rest until this is over!\x02",
    )

    CloseMessageWindow()

    label("loc_117D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11AF")

    ChrTalk(    #38
        0x107,
        "#067F#12PI-I'll do what I can!\x02",
    )

    CloseMessageWindow()

    label("loc_11AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11E1")

    ChrTalk(    #39
        0x10A,
        "#816F#12PRight! Let's do this!\x02",
    )

    CloseMessageWindow()

    label("loc_11E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1221")

    ChrTalk(    #40
        0x105,
        "#1168F#12PI'll fight with everything I have!\x02",
    )

    CloseMessageWindow()

    label("loc_1221")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1257")

    ChrTalk(    #41
        0x10B,
        "#210F#12PI'm not turning back now!\x02",
    )

    CloseMessageWindow()

    label("loc_1257")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12A4")

    ChrTalk(    #42
        0x103,
        (
            "#1536F#12PI wouldn't dream of holding back\x01",
            "at this point!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12ED")

    ChrTalk(    #43
        0x104,
        "#1541F#12PThen may the curtain on the final act rise!\x02",
    )

    CloseMessageWindow()

    label("loc_12ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_137D")

    ChrTalk(    #44
        0x110,
        (
            "#263F#12PI don't see why not.\x02\x03",

            "#1306FI've been looking forward to the chance to fight\x01",
            "the Lord of Phantasma for a while now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_137D")


    ChrTalk(    #45
        0x109,
        "#1075F#5P...Thanks.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFA, 90, 400)
    Sleep(300)

    ChrTalk(    #46
        0x109,
        "#1078F#6PAll right. Let's go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10F,
        "#1938F#11PRight!\x02",
    )

    CloseMessageWindow()

    def lambda_13E1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_13E1)
    Sleep(100)
    OP_8C(0xFB, 0, 400)
    OP_1D(0xD4)
    Sleep(500)
    OP_22(0x85, 0x1, 0x3C)

    def lambda_1407():

        label("loc_1407")

        OP_7C(0x5, 0x5, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1407")

    QueueWorkItem2(0xFA, 3, lambda_1407)
    Sleep(300)
    OP_22(0x85, 0x1, 0x50)

    def lambda_142C():

        label("loc_142C")

        OP_7C(0xA, 0xA, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_142C")

    QueueWorkItem2(0xFA, 3, lambda_142C)
    Sleep(300)
    OP_22(0x85, 0x1, 0x64)

    def lambda_1451():

        label("loc_1451")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1451")

    QueueWorkItem2(0xFA, 3, lambda_1451)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x258)
    Sleep(500)
    Fade(1000)
    OP_6D(0, -1000, 81330, 0)
    OP_67(0, 4420, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(0, 0)
    OP_6E(311, 0)
    SetChrPos(0xFA, -850, 0, 78490, 0)
    SetChrPos(0xFB, 680, 0, 78380, 0)
    SetChrPos(0xFC, -1250, 0, 76780, 0)
    SetChrPos(0xFD, 1190, 0, 76810, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)

    def lambda_152D():
        OP_6D(0, 4800, 81080, 7500)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_152D)

    def lambda_1545():
        OP_67(0, 3200, -10000, 7500)
        ExitThread()

    QueueWorkItem(0xFB, 1, lambda_1545)

    def lambda_155D():
        OP_6B(3820, 7500)
        ExitThread()

    QueueWorkItem(0xFC, 1, lambda_155D)

    def lambda_156D():
        OP_6E(431, 7500)
        ExitThread()

    QueueWorkItem(0xFD, 1, lambda_156D)
    WaitChrThread(0xFA, 0x1)
    OP_44(0xFA, 0x3)
    OP_23(0xD2)
    OP_23(0x85)

    def lambda_158C():
        OP_7C(0x28, 0x28, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0xFA, 3, lambda_158C)
    OP_22(0x88, 0x0, 0x64)
    Sleep(2000)

    def lambda_15AE():
        OP_6D(0, 3800, 81080, 10000)
        ExitThread()

    QueueWorkItem(0xFA, 3, lambda_15AE)

    def lambda_15C6():
        OP_67(0, 2500, -10000, 10000)
        ExitThread()

    QueueWorkItem(0xFB, 3, lambda_15C6)

    def lambda_15DE():
        OP_6B(3000, 10000)
        ExitThread()

    QueueWorkItem(0xFC, 3, lambda_15DE)
    OP_43(0xFA, 0x0, 0x0, 0x4)
    Sleep(100)
    OP_43(0xFB, 0x0, 0x0, 0x5)
    Sleep(100)
    OP_43(0xFC, 0x0, 0x0, 0x6)
    Sleep(100)
    OP_43(0xFD, 0x0, 0x0, 0x7)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xFA, 0x0)
    OP_44(0xFB, 0x0)
    OP_44(0xFC, 0x0)
    OP_44(0xFD, 0x0)
    OP_44(0xFA, 0x3)
    OP_44(0xFB, 0x3)
    OP_44(0xFC, 0x3)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7408   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_3_C2B end

    def Function_4_1653(): pass

    label("Function_4_1653")

    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFFCAE, 0x0, 0x14FBE, 0x7D0, 0x0)

    def lambda_1672():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1672)
    OP_8E(0xFE, 0xFFFFFCAE, 0x0, 0x157B6, 0x7D0, 0x0)
    Return()

    # Function_4_1653 end

    def Function_5_1693(): pass

    label("Function_5_1693")

    Sleep(200)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x2BC, 0x0, 0x14FBE, 0x7D0, 0x0)

    def lambda_16B7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16B7)
    OP_8E(0xFE, 0x2BC, 0x0, 0x157B6, 0x7D0, 0x0)
    Return()

    # Function_5_1693 end

    def Function_6_16D8(): pass

    label("Function_6_16D8")

    Sleep(330)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFFBB4, 0x0, 0x14FBE, 0x7D0, 0x0)

    def lambda_16FC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16FC)
    OP_8E(0xFE, 0xFFFFFBB4, 0x0, 0x157B6, 0x7D0, 0x0)
    Return()

    # Function_6_16D8 end

    def Function_7_171D(): pass

    label("Function_7_171D")

    Sleep(360)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x44C, 0x0, 0x14FBE, 0x7D0, 0x0)

    def lambda_1741():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1741)
    OP_8E(0xFE, 0x44C, 0x0, 0x157B6, 0x7D0, 0x0)
    Return()

    # Function_7_171D end

    def Function_8_1762(): pass

    label("Function_8_1762")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #48
        "\x07\x05Strange power is overflowing from the orb.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_17FD"),
        (1, "loc_189B"),
        (SWITCH_DEFAULT, "loc_189B"),
    )


    label("loc_17FD")

    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x82, 0x0)
    OP_1D(0xE1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_189B")

    TalkEnd(0xFF)
    Return()

    # Function_8_1762 end

    SaveToFile()

Try(main)
