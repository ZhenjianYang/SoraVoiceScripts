from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0131_2 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0131.x',
        MapIndex            = 7,
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
        "Function_1_452F",         # 01, 1
        "Function_2_456D",         # 02, 2
        "Function_3_45B0",         # 03, 3
        "Function_4_45F3",         # 04, 4
        "Function_5_4636",         # 05, 5
        "Function_6_4694",         # 06, 6
        "Function_7_46C4",         # 07, 7
        "Function_8_46E5",         # 08, 8
        "Function_9_4715",         # 09, 9
        "Function_10_4745",        # 0A, 10
        "Function_11_4787",        # 0B, 11
        "Function_12_4E6E",        # 0C, 12
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    SoundLoad(209)
    SoundLoad(349)
    SoundLoad(524)
    SetChrPos(0x101, 37030, 0, 75500, 135)
    SetChrPos(0xF8, 37530, 0, 73700, 0)
    SetChrPos(0xF9, 36660, 0, 73320, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117")
    SetChrPos(0xF9, 37530, 0, 73700, 0)
    SetChrPos(0xF8, 36660, 0, 73320, 0)

    label("loc_117")

    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x103, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_139")
    SetChrFlags(0x104, 0x80)

    label("loc_139")

    OP_6D(43180, 0, 66690, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(315000, 0)
    OP_6E(250, 0)

    def lambda_17C():
        OP_6D(36390, 0, 75300, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_17C)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #0
        0x101,
        (
            "#1007F#4P*sigh* I came by because I was curious,\x01",
            "but...\x02\x03",

            "#1002FSeems like Schera and Aina aren't here yet.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_256")

    ChrTalk(    #1
        0x107,
        "#063FI wonder if she couldn't convince her.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Jump("loc_350")

    label("loc_256")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A5")

    ChrTalk(    #2
        0x105,
        "#040FThey might have gotten tied up at the guild.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)
    Jump("loc_350")

    label("loc_2A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F0")

    ChrTalk(    #3
        0x108,
        "#070FSomething may have come up at the guild.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)
    Jump("loc_350")

    label("loc_2F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_350")

    ChrTalk(    #4
        0x106,
        (
            "#551FGuild work might've come up.\x02\x03",

            "Aina's got a lot on her plate too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    label("loc_350")


    ChrTalk(    #5
        0x101,
        "#1015F#4PWell, let's take a seat and wait for a bit.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x103, 48000, -500, 70290, 270)
    SetChrPos(0x26, 48000, -500, 68920, 270)
    SetChrPos(0x25, 48000, -500, 71150, 270)
    SetChrPos(0x27, 48000, -500, 69890, 270)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x27, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42D")
    OP_8C(0x106, 135, 400)

    ChrTalk(    #6
        0x106,
        (
            "#050FNah...\x02\x03",

            "Doesn't look like we'll need to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_519")

    label("loc_42D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_478")
    OP_8C(0x108, 135, 400)

    ChrTalk(    #7
        0x108,
        (
            "#070FNo...\x02\x03",

            "Looks like we won't need to wait.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_519")

    label("loc_478")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CC")
    OP_8C(0x105, 135, 400)

    ChrTalk(    #8
        0x105,
        (
            "#040FNo, Estelle...\x02\x03",

            "It seems that won't be necessary.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_519")

    label("loc_4CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_519")
    OP_8C(0x107, 135, 400)

    ChrTalk(    #9
        0x107,
        (
            "#064FAh, but...\x02\x03",

            "I don't think we'll have to wait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_519")


    ChrTalk(    #10
        0x101,
        "#1011F#4PWh...\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_538():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_538)
    Sleep(200)

    def lambda_54B():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_54B)

    def lambda_559():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_559)

    def lambda_567():
        OP_6D(42950, 0, 70140, 2000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_567)

    def lambda_57F():
        OP_6C(326000, 2000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_57F)

    def lambda_58F():
        OP_6E(250, 2000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_58F)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x13, 0x2)
    OP_43(0x103, 0x0, 0x2, 0x1)
    OP_43(0x26, 0x0, 0x2, 0x2)
    OP_43(0x25, 0x0, 0x2, 0x3)
    OP_43(0x27, 0x0, 0x2, 0x4)
    WaitChrThread(0x27, 0x0)

    ChrTalk(    #11
        0x103,
        (
            "#020F#6PSorry to drag you all the way out here, Aina.\x02\x03",

            "Will the guildhouse be okay?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x103, 400)

    ChrTalk(    #12
        0x26,
        (
            "#742F#6PYes, I'm having Ridge mind the front of\x01",
            "house for now.\x02\x03",

            "An important part of the receptionist's work\x01",
            "is to talk with clients, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x25, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #13
        0x25,
        (
            "Forgive me for making you come out\x01",
            "here when you're so busy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x25, 400)

    ChrTalk(    #14
        0x26,
        (
            "#740FNo, don't let it bother you.\x02\x03",

            "Now, what was it you wanted to\x01",
            "talk about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x27,
        "#031FHeh, then let us begin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x25,
        "Y-Yes, please.\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(36390, 0, 75300, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(300000, 0)
    OP_6E(250, 0)
    OP_0D()

    ChrTalk(    #17
        0x101,
        "#1020F#4PSh-She really brought her.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_864")

    ChrTalk(    #18
        0x108,
        (
            "#070FIt seems she used talking\x01",
            "to a client as an excuse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95F")

    label("loc_864")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C3")

    ChrTalk(    #19
        0x106,
        (
            "#050FIt seems she's using the consultation\x01",
            "with the client as an excuse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95F")

    label("loc_8C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_920")

    ChrTalk(    #20
        0x105,
        (
            "#542FIt looks like she's using the client\x01",
            "consultation as an excuse...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95F")

    label("loc_920")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_95F")

    ChrTalk(    #21
        0x107,
        "#067FApparently she made it a consultation.\x02",
    )

    CloseMessageWindow()

    label("loc_95F")


    ChrTalk(    #22
        0x101,
        (
            "#1015F#4PWell, it is KIND of a consultation,\x01",
            "but...\x02\x03",

            "#1007FI wonder if Aina will get mad.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D85")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A10")

    ChrTalk(    #23
        0x107,
        "#561FS-Still, though, why is Olivier there...\x02",
    )

    CloseMessageWindow()
    Jump("loc_AED")

    label("loc_A10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A57")

    ChrTalk(    #24
        0x105,
        "#045FB-Besides that, when did Olivier get there?\x02",
    )

    CloseMessageWindow()
    Jump("loc_AED")

    label("loc_A57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A9D")

    ChrTalk(    #25
        0x106,
        "#552FThat aside, why the heck is Blondie there?\x02",
    )

    CloseMessageWindow()
    Jump("loc_AED")

    label("loc_A9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AED")

    ChrTalk(    #26
        0x108,
        (
            "#073FPutting that aside, when did\x01",
            "Olivier get involved here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AED")

    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #27
        0x101,
        (
            "#1019F#4PN-Now that you mention it...\x02\x03",

            "He was supposed to be on standby\x01",
            "at the guild, wasn't he?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFB")

    ChrTalk(    #28
        0x108,
        (
            "#075FMost likely he was eavesdropping.\x02\x03",

            "He has an almost preternatural sense\x01",
            "for sniffing out these kinds of matters.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D85")

    label("loc_BFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C5D")

    ChrTalk(    #29
        0x106,
        (
            "#551FHe was probably listening in.\x02\x03",

            "The guy has a nose for stuff like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D85")

    label("loc_C5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD6")

    ChrTalk(    #30
        0x107,
        (
            "#067FHe probably overheard the story\x01",
            "at the guild and joined.\x02\x03",

            "#562FIt's very, um, Olivier-like...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D85")

    label("loc_CD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D85")

    ChrTalk(    #31
        0x105,
        (
            "#045FHe probably overheard what was going on\x01",
            "at the guild and joined at the last second.\x02\x03",

            "I'm sure Olivier would find something\x01",
            "like...this hard to resist.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D85")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_72(0x1, 0x4)
    SetChrPos(0x101, 38060, 0, 75490, 180)
    SetChrChipByIndex(0x103, 21)
    SetChrSubChip(0x103, 0)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 41700, 200, 67710, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EDF")
    SetChrChipByIndex(0x101, 35)
    SetChrSubChip(0x101, 1)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 41440, 1580, 77300, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E70")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E16")
    SetChrChipByIndex(0xF9, 22)
    Jump("loc_E52")

    label("loc_E16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E2B")
    SetChrChipByIndex(0xF9, 23)
    Jump("loc_E52")

    label("loc_E2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E40")
    SetChrChipByIndex(0xF9, 24)
    Jump("loc_E52")

    label("loc_E40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E52")
    SetChrChipByIndex(0xF9, 25)

    label("loc_E52")

    SetChrSubChip(0xF9, 2)
    SetChrFlags(0xF9, 0x4)
    SetChrPos(0xF9, 39580, 1620, 77050, 110)
    Jump("loc_EDC")

    label("loc_E70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E85")
    SetChrChipByIndex(0xF8, 22)
    Jump("loc_EC1")

    label("loc_E85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9A")
    SetChrChipByIndex(0xF8, 23)
    Jump("loc_EC1")

    label("loc_E9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EAF")
    SetChrChipByIndex(0xF8, 24)
    Jump("loc_EC1")

    label("loc_EAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC1")
    SetChrChipByIndex(0xF8, 25)

    label("loc_EC1")

    SetChrSubChip(0xF8, 2)
    SetChrFlags(0xF8, 0x4)
    SetChrPos(0xF8, 39580, 1620, 77050, 110)

    label("loc_EDC")

    Jump("loc_FDC")

    label("loc_EDF")

    OP_72(0x2, 0x4)
    SetChrChipByIndex(0x101, 35)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 40320, 1620, 78700, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F19")
    SetChrChipByIndex(0xF8, 22)
    Jump("loc_F55")

    label("loc_F19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2E")
    SetChrChipByIndex(0xF8, 23)
    Jump("loc_F55")

    label("loc_F2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F43")
    SetChrChipByIndex(0xF8, 24)
    Jump("loc_F55")

    label("loc_F43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F55")
    SetChrChipByIndex(0xF8, 25)

    label("loc_F55")

    SetChrSubChip(0xF8, 2)
    SetChrFlags(0xF8, 0x4)
    SetChrPos(0xF8, 39580, 1620, 77050, 110)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F85")
    SetChrChipByIndex(0xF9, 22)
    Jump("loc_FC1")

    label("loc_F85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9A")
    SetChrChipByIndex(0xF9, 23)
    Jump("loc_FC1")

    label("loc_F9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAF")
    SetChrChipByIndex(0xF9, 24)
    Jump("loc_FC1")

    label("loc_FAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC1")
    SetChrChipByIndex(0xF9, 25)

    label("loc_FC1")

    SetChrSubChip(0xF9, 1)
    SetChrFlags(0xF9, 0x4)
    SetChrPos(0xF9, 41440, 1580, 77300, 270)

    label("loc_FDC")

    OP_8C(0xC, 180, 0)
    OP_4A(0xC, 255)
    SetChrFlags(0x26, 0x4)
    SetChrFlags(0x26, 0x40)
    SetChrPos(0x26, 38290, -50, 67720, 114)
    SetChrChipByIndex(0x27, 17)
    SetChrSubChip(0x27, 0)
    SetChrFlags(0x27, 0x4)
    SetChrFlags(0x27, 0x40)
    SetChrPos(0x27, 39710, 80, 68530, 180)
    SetChrChipByIndex(0x25, 14)
    SetChrSubChip(0x25, 0)
    SetChrFlags(0x25, 0x4)
    SetChrFlags(0x25, 0x40)
    SetChrPos(0x25, 39690, 40, 66460, 0)
    ClearChrFlags(0x28, 0x80)
    SetChrSubChip(0x28, 28)
    ClearChrFlags(0x33, 0x80)
    SetChrSubChip(0x33, 5)
    ClearChrFlags(0x34, 0x80)
    SetChrSubChip(0x34, 5)
    ClearChrFlags(0x35, 0x80)
    SetChrSubChip(0x35, 5)
    ClearChrFlags(0x36, 0x80)
    SetChrSubChip(0x36, 5)
    OP_6D(38400, 0, 68270, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    OP_20(0x3E8)
    OP_21()
    OP_1D(0x19)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #32
        0x27,
        (
            "#030F...Well, then, first a toast!\x02\x03",

            "To this wonderful meeting of minds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x103,
        "#021FHeehee. Yes, let's.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x26,
        (
            "#743F#6PSure, I don't mind, but...\x02\x03",

            "Umm, are you okay, Anton?\x02\x03",

            "Drinking before a consultation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x25,
        "I-It's okay! Bring it on!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x25,
        (
            "I may look like this, but my tolerance for\x01",
            "alcohol is pretty a-amazing! Hahaha!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x26,
        (
            "#740F#6POh, is that so?\x01",
            "I guess you really can't tell by looking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x27,
        "#031FHeh, well, then, cheers!\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(36700, 0, 77610, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12FF")

    ChrTalk(    #39
        0x105,
        "#045FTh-They're already drinking...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1421")

    label("loc_12FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1365")

    ChrTalk(    #40
        0x107,
        (
            "#065FI-I thought they'd just started, but...\x02\x03",

            "#561F...They're already drinking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1421")

    label("loc_1365")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A7")

    ChrTalk(    #41
        0x108,
        "#070FOhh, they've already started drinking.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1421")

    label("loc_13A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1421")

    ChrTalk(    #42
        0x106,
        (
            "#050FHey, hey.\x01",
            "Just what part of that is a consultation?\x02\x03",

            "Barely a hello before the booze\x01",
            "comes out...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1421")


    ChrTalk(    #43
        0x101,
        (
            "#1002FBut, if Olivier's participating too, then...\x02\x03",

            "#1015F...Did he have some of that medicine?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14F8")

    ChrTalk(    #44
        0x106,
        (
            "#050FYeah. Probably.\x02\x03",

            "No way he'd be able to smile like that\x01",
            "in front of Aina if he hadn't.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1625")

    label("loc_14F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1560")

    ChrTalk(    #45
        0x108,
        (
            "#070FYeah, you're probably right.\x02\x03",

            "I doubt he would look so relaxed if he hadn't.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1625")

    label("loc_1560")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15D7")

    ChrTalk(    #46
        0x107,
        (
            "#062FY-Yeah... I think he took some.\x02\x03",

            "#067FOtherwise, he wouldn't look that confident,\x01",
            "right...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1625")

    label("loc_15D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1625")

    ChrTalk(    #47
        0x105,
        (
            "#040FY-Yes... Most likely.\x02\x03",

            "He seems very confident, so...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1625")

    OP_6D(36700, 0, 74470, 1500)

    ChrTalk(    #48
        0x27,
        (
            "#031F#2PHa. Ha. Ha.\x02\x03",

            "Ahhhh, really. What a joke, Aina.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1007F#6PYup...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(38400, 0, 68270, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    OP_0D()

    ChrTalk(    #50
        0x26,
        (
            "#744F#6PNow, then, let's get to the main topic.\x02\x03",

            "#740FMay I inquire as to the nature of\x01",
            "your request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x25,
        "Y-Yes... So about that...\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x25, 13)
    ClearChrFlags(0x25, 0x4)
    OP_96(0x25, 0x983A, 0x0, 0x102E8, 0x190, 0x1388)

    ChrTalk(    #52
        0x25,
        "U-Umm... Aina!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x26, 165, 0)

    ChrTalk(    #53
        0x26,
        "#740F#4PYes...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x25,
        "P-Please go...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x25,
        "#4SPlease go out with me!!!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x26, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_63(0x26)

    ChrTalk(    #56
        0x26,
        (
            "#743F#4P...\x02\x03",

            "Go out... You mean...like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x25,
        "Y-Yes! Please!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x25,
        "I-I cannot bear to live without you anymore!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x26,
        (
            "#745F#4PW-Well...\x02\x03",

            "That's rather sudden.\x01",
            "I'm not sure how to respond.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x27, 2)

    ChrTalk(    #60
        0x27,
        (
            "#030FHeh, I can understand Aina's confusion.\x02\x03",

            "The bonds of man and woman are not\x01",
            "such that rationality might know...\x02\x03",

            "They are not a problem that one\x01",
            "might solve through thinking.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x25, 30, 400)

    ChrTalk(    #61
        0x25,
        (
            "B-But, I need to have some\x01",
            "kind of solution!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x25,
        (
            "Am I just supposed to just live, crushed\x01",
            "under the weight of these feelings?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x27, 0)

    ChrTalk(    #63
        0x27,
        (
            "#030FHeh, fear not, young man.\x01",
            "I have an excellent plan.\x02\x03",

            "Shall we settle things with a contest?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x26, 114, 400)

    ChrTalk(    #64
        0x26,
        "#743F#6PContest...?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 2)

    ChrTalk(    #65
        0x103,
        "#023FMeaning?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x27,
        (
            "#035FThe battle stage, a bar...\x02\x03",

            "Having said that, the 'weapons' at\x01",
            "your disposal should be clear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x25,
        "I-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x26,
        "#742F#6PA drinking contest, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x103,
        "#027FWell, now that's an interesting suggestion.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x27, 2)

    ChrTalk(    #70
        0x27,
        (
            "#035FStill, it would be unjust to cast poor Anton\x01",
            "into this ring as such.\x02\x03",

            "Let us attach a handicap to Aina.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x26,
        "#742F#6PAll right, but...what kind of handicap?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x27,
        (
            "#037FI shall take the field with Anton.\x02\x03",

            "In other words, you contest the two of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x26,
        (
            "#744F#6P...\x02\x03",

            "#742FAll right. I accept your challenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x103,
        (
            "#525FNow we're talkin'!\x02\x03",

            "I will serve as referee, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x26,
        "#742F#6PHowever, I have my own condition.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x25, 0x26, 400)

    ChrTalk(    #76
        0x25,
        "Wh-What condition would that be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x26,
        (
            "#742F#6PWe'll use the strongest liquor they have here.\x02\x03",

            "I apologize, but I can't waste too much\x01",
            "time on this.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x27, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x25, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #78
        0x27,
        (
            "#034FU-Understood...\x01",
            "(A-As expected from Aina.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x25, 14)
    SetChrSubChip(0x25, 0)
    SetChrFlags(0x25, 0x4)
    SetChrPos(0x25, 39690, 50, 66460, 0)
    ClearChrFlags(0x2A, 0x80)
    SetChrSubChip(0x2A, 29)
    ClearChrFlags(0x2B, 0x80)
    SetChrSubChip(0x2B, 29)
    ClearChrFlags(0x2C, 0x80)
    SetChrSubChip(0x2C, 29)
    SetChrSubChip(0x28, 29)
    SetChrPos(0xC, 37670, 0, 66970, 62)
    SetChrSubChip(0x33, 1)
    SetChrSubChip(0x34, 1)
    SetChrSubChip(0x35, 1)
    SetChrSubChip(0x27, 0)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #79
        0xC,
        "Th-That should be enough for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xC,
        (
            "This is enough to make a Rhinocider\x01",
            "go cross-eyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x26,
        "#740F#4PThank you, Faulkner.\x02",
    )

    CloseMessageWindow()
    OP_43(0xC, 0x0, 0x2, 0x5)
    Sleep(1000)

    ChrTalk(    #82
        0x103,
        (
            "#027FNow...\x02\x03",

            "Shall we begin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x27,
        "#035FHeh, I am ready.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x26,
        "#742F#6PYes, let's.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x25,
        "A-All right! I'll do my best!\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(36700, 0, 77610, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    OP_0D()

    ChrTalk(    #86
        0x101,
        "#1002F...And they're off.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2088")

    ChrTalk(    #87
        0x106,
        (
            "#050FYeah...\x02\x03",

            "Let's see how far they can go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215E")

    label("loc_2088")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20CF")

    ChrTalk(    #88
        0x107,
        (
            "#063FY-Yeah.\x02\x03",

            "I sure hope that medicine works...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215E")

    label("loc_20CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2117")

    ChrTalk(    #89
        0x108,
        (
            "#070FYeah...\x02\x03",

            "Let's see if those two can make it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215E")

    label("loc_2117")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_215E")

    ChrTalk(    #90
        0x105,
        (
            "#043FYes.\x02\x03",

            "Hopefully that medicine has an effect...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_215E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(38400, 0, 68270, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    SetChrSubChip(0x103, 2)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #91
        0x25,
        "Ahhhhhhhh, that's five!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x25,
        "Ghhh, really hits ya right in the gut!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x27,
        (
            "#030FHeh. I have cleared five myself,\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x103,
        (
            "#020FThat would be ten between the two of you, then.\x02\x03",

            "A pretty good pace, I'd say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x26,
        (
            "#740F#6PYes, really... Perhaps too good, though.\x02\x03",

            "If you blow through it too fast, the liquor\x01",
            "will hit you all at once, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x25,
        "No, no. I wouldn't get drunk this over THIS.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x27,
        (
            "#031FIndeed, and my liver feels especially strong\x01",
            "today as well.\x02\x03",

            "Now, let us keep up the pace.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(36700, 0, 77610, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    OP_0D()

    ChrTalk(    #98
        0x101,
        (
            "#1002FHmm... Both of them look pretty good.\x02\x03",

            "#1015FI wonder if this is the effect of the medicine.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24AF")

    ChrTalk(    #99
        0x105,
        (
            "#042FOn the other hand, Aina's expression\x01",
            "hasn't change at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25B2")

    label("loc_24AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_251A")

    ChrTalk(    #100
        0x107,
        (
            "#561FBut, Aina's expression hasn't changed at all.\x02\x03",

            "And she hasn't had any medicine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25B2")

    label("loc_251A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_256F")

    ChrTalk(    #101
        0x106,
        (
            "#052FAina looks the same as always.\x01",
            "Not a hint of flush there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25B2")

    label("loc_256F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25B2")

    ChrTalk(    #102
        0x108,
        "#070FStill, Aina's color hasn't changed at all.\x02",
    )

    CloseMessageWindow()

    label("loc_25B2")


    ChrTalk(    #103
        0x101,
        (
            "#1016FW-Well, she IS Aina.\x02\x03",

            "But, this might be a better\x01",
            "match than I'd thought.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x2D, 0x80)
    SetChrSubChip(0x2D, 29)
    ClearChrFlags(0x2E, 0x80)
    SetChrSubChip(0x2E, 29)
    SetChrPos(0x2D, 41440, 0, 66610, 15)
    SetChrPos(0x2E, 41090, 0, 66050, 30)
    OP_6D(38400, 0, 68270, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #104
        0x26,
        (
            "#744F#6PPhew! Twenty.\x02\x03",

            "#740F...And? How are you two?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x25,
        "I-I've finished t-t-ten...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x27,
        "#037FThat was my tenth as well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x103,
        (
            "#027FWell, then, they are also at twenty...\x02\x03",

            "You're evenly matched.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x26,
        (
            "#743F#6PMy, what a surprise.\x02\x03",

            "Your pace hasn't slowed at all\x01",
            "since we started drinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x25,
        (
            "Heh heh. J-Just like I said at the start,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x25,
        "But, I gotta admit my throat's burning a bit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x27,
        (
            "#034FY-Yes... It feels like it's been scorched.\x02\x03",

            "#036FYou don't feel it at all, Aina?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x27, 2)

    ChrTalk(    #112
        0x26,
        (
            "#741F#6POh, is something wrong with your throat?\x02\x03",

            "Do you have a cold?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x25, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x27, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #113
        0x27,
        (
            "#034FI-I was asking the wrong person,\x01",
            "it seems...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x26,
        (
            "#740F#6PIf you're not feeling well,\x01",
            "don't force yourself.\x02\x03",

            "I don't want to cause trouble for the store,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x25,
        "Y-Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x27,
        "#035FHmph. Let us continue our match.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x2F, 0x80)
    SetChrSubChip(0x2F, 29)
    ClearChrFlags(0x30, 0x80)
    SetChrSubChip(0x30, 29)
    SetChrSubChip(0x27, 0)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #117
        0x27,
        (
            "#037FFif... fifteen...\x02\x03",

            "*cough* *cough*\x01",
            "Ahhh, even my stomach burns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x25,
        "...\x02",
    )

    CloseMessageWindow()
    OP_62(0x27, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    SetChrSubChip(0x103, 0)

    ChrTalk(    #119
        0x27,
        "#033FHmm...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x103,
        "#023FAnton?\x02",
    )

    CloseMessageWindow()
    OP_62(0x25, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #121
        0x25,
        "Ah...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x25,
        "Wh-What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x26,
        (
            "#743F#6PAre you feeling okay?\x02\x03",

            "It seemed like you spaced out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x25,
        "N-No... I'm okay, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x27,
        (
            "#530F(Anton! Keep it together!)\x02\x03",

            "(The medicine's effect hasn't faded yet!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x25,
        "(Y-Yes!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x27,
        (
            "#035F(Aina's already drunk quite a lot herself...)\x02\x03",

            "(No matter how strong a drinker she is,\x01",
            "her limit should be close.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x25,
        "(B-But, Olivier...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x25,
        (
            "(She doesn't seem bothered at all!\x01",
            "Just look at her. She's not even the\x01",
            "slightest bit red!)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x27, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrSubChip(0x27, 2)
    Sleep(400)

    ChrTalk(    #130
        0x27,
        "#032F(*gulp*...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x26,
        (
            "#740F#6PMmm?\x02\x03",

            "What is it, you two?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x27, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x27, 0)
    Sleep(400)

    ChrTalk(    #132
        0x27,
        (
            "#039F(Tch, if you're a man, then be not\x01",
            "troubled by such trivial things!)\x02\x03",

            "(Beyond here it is a battle of wills. Now,\x01",
            "overcome it with your love and courage!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x25,
        "(G-Got it!!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x26,
        (
            "#743F#6PAre you sure you're okay?\x02\x03",

            "If you're not feeling well, then you\x01",
            "should give up sooner rather than later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x27,
        (
            "#035FHeh, thank you for your thoughtfulness,\x01",
            "but we have no intention of surrendering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x103,
        (
            "#520FYes, yes, this is where things REALLY\x01",
            "get started.\x02\x03",

            "Now, let us continue the match.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(38400, 0, 68270, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    ClearChrFlags(0x31, 0x80)
    SetChrSubChip(0x31, 29)
    ClearChrFlags(0x32, 0x80)
    SetChrSubChip(0x32, 29)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    SetChrFlags(0x25, 0x4)
    SetChrFlags(0x25, 0x40)
    SetChrPos(0x25, 39690, 40, 66460, 0)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #137
        0x26,
        "#745F#6P...Number thirty-six!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x25,
        "N-Nummmber eight...teen!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x27,
        "#037FM-Me too! Eighteen!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x26,
        (
            "#740F#6PGentlemen, you're not looking very good.\x02\x03",

            "Do you intend to keep going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x27,
        "#037FHa. Ha. Ha. What a thing to ask now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x25,
        "Haha, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x25,
        (
            "If I backed down now, I couldn't\x01",
            "really be called a maaaa...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x25,
        "...Eh?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0)

    ChrTalk(    #145
        0x103,
        "#023FAnton?!\x02",
    )

    CloseMessageWindow()

    def lambda_3111():
        OP_6D(40270, 0, 67330, 1000)
        ExitThread()

    QueueWorkItem(0x26, 0, lambda_3111)

    def lambda_3129():
        OP_6C(315000, 1000)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_3129)
    OP_9E(0x25, 0x14, 0x0, 0x1F4, 0xFA0)
    ClearChrFlags(0x25, 0x100)
    SetChrChipByIndex(0x25, 13)
    SetChrPos(0x25, 40480, 0, 66130, 0)
    SetChrChipByIndex(0x25, 13)
    OP_D1(37, 20000, 0, 0, 0)

    def lambda_317F():
        OP_D1(37, 60000, -15000, -90000, 200)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_317F)
    OP_51(0x25, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_22(0xD1, 0x0, 0x64)
    ClearChrFlags(0x2D, 0x100)
    ClearChrFlags(0x2E, 0x100)
    OP_51(0x2D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_31E4():
        OP_96(0x2D, 0xA3FC, 0x0, 0x10586, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_31E4)

    def lambda_3202():
        OP_D1(45, 30000, -15000, -80000, 200)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_3202)

    def lambda_321C():
        OP_D1(46, 60000, -15000, -135000, 200)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_321C)
    OP_22(0x15D, 0x0, 0x64)
    WaitChrThread(0x2D, 0x2)
    OP_51(0x2D, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2D, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2D, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x2E, 0x2)
    OP_51(0x2E, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2E, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2E, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x27, 1)
    SetChrSubChip(0x103, 1)
    OP_0D()
    OP_62(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x26, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x27, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #146
        0x27,
        "#036F#4PA-Anton?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x26,
        "#743F#6PUh oh.\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_3308():
        OP_6D(41230, 0, 67950, 1000)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_3308)

    def lambda_3320():
        OP_6C(315000, 1000)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_3320)
    OP_43(0x26, 0x1, 0x2, 0xC)
    SetChrChipByIndex(0x103, 65535)
    SetChrFlags(0x103, 0x40)
    ClearChrFlags(0x103, 0x4)
    OP_96(0x103, 0xA1E0, 0x0, 0x10662, 0xC8, 0x1388)
    OP_8C(0x103, 180, 0)
    ClearChrFlags(0x27, 0x4)
    SetChrChipByIndex(0x27, 16)
    OP_96(0x27, 0x9E3E, 0x0, 0x10C98, 0x190, 0x1388)
    SetChrChipByIndex(0x27, 36)
    OP_8E(0x27, 0x9F60, 0x0, 0x10C98, 0xFA0, 0x1)
    SetChrSubChip(0x27, 3)
    WaitChrThread(0x25, 0x1)

    ChrTalk(    #148
        0x27,
        "#038F#6P...Hmm?!\x02",
    )

    OP_9E(0x27, 0x14, 0x0, 0x1F4, 0xFA0)
    CloseMessageWindow()
    OP_59()
    SetChrSubChip(0x27, 0)
    SetChrFlags(0x27, 0x4)
    OP_96(0x27, 0xA3AC, 0xF0, 0x10B94, 0x190, 0xFA0)
    SetChrChipByIndex(0x27, 18)
    OP_51(0x27, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x20C, 0x0, 0x64)
    OP_96(0x27, 0xA4A6, 0xF0, 0x10B94, 0x190, 0xFA0)
    OP_8C(0x103, 0, 400)

    ChrTalk(    #149
        0x103,
        "#025F#6PAhhh, and there goes Olivier...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x26,
        "#742F#6PHang in there, you two!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x80)
    SetChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34C9")
    ClearChrFlags(0xF8, 0x80)
    SetChrFlags(0xF8, 0x40)
    ClearChrFlags(0xF8, 0x4)
    SetChrChipByIndex(0xF8, 65535)
    SetChrPos(0xF8, 42530, 1500, 78540, 180)

    label("loc_34C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34FB")
    ClearChrFlags(0xF9, 0x80)
    SetChrFlags(0xF9, 0x40)
    ClearChrFlags(0xF9, 0x4)
    SetChrChipByIndex(0xF9, 65535)
    SetChrPos(0xF9, 42960, 1500, 78910, 180)

    label("loc_34FB")

    SetChrChipByIndex(0x101, 65535)
    SetChrPos(0x101, 42860, 1500, 77720, 180)

    def lambda_3517():
        OP_6D(41380, 0, 69390, 3000)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_3517)
    OP_43(0x101, 0x0, 0x2, 0x6)
    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_354C")
    OP_43(0xF9, 0x0, 0x2, 0x8)
    Jump("loc_3576")

    label("loc_354C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3563")
    OP_43(0xF8, 0x0, 0x2, 0x8)
    Jump("loc_3576")

    label("loc_3563")

    OP_43(0xF8, 0x0, 0x2, 0x8)
    Sleep(600)
    OP_43(0xF9, 0x0, 0x2, 0x9)

    label("loc_3576")

    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)

    ChrTalk(    #151
        0x101,
        "#1020F#4PO-Olivier...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x27,
        "#038F#2PHhnnn...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3632")

    ChrTalk(    #153
        0x106,
        (
            "#551FHis eyes are totally rolled back in his head...\x02\x03",

            "Looks like their little trump card has expired.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3744")

    label("loc_3632")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3692")

    ChrTalk(    #154
        0x108,
        (
            "#075FThey are...completely intoxicated.\x02\x03",

            "Seems the medicine has worn off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3744")

    label("loc_3692")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36EB")

    ChrTalk(    #155
        0x105,
        (
            "#043FTh-They're completely wasted.\x02\x03",

            "Maybe the medicine wore off...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3744")

    label("loc_36EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3744")

    ChrTalk(    #156
        0x107,
        (
            "#561FTh-They're completely drunk.\x02\x03",

            "I wonder if the medicine wore off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3744")


    ChrTalk(    #157
        0x103,
        (
            "#025F#6PReally, that's too bad...\x02\x03",

            "Today I thought I'd see Aina get sunk\x01",
            "in her cups.\x02\x03",

            "*sigh* I guess that medicine was\x01",
            "only a veneer of strength in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x26,
        "#743F#1PMedicine...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        "#1015F#4PEr... So actually...\x02",
    )

    CloseMessageWindow()

    def lambda_382A():
        OP_6D(40560, 0, 66540, 2000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_382A)
    WaitChrThread(0x13, 0x0)
    SetChrPos(0x24, 39760, -500, 61000, 0)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x24, 0x80)

    def lambda_3868():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_3868)
    OP_8E(0x24, 0x9B50, 0x0, 0xFBB8, 0x7D0, 0x0)
    OP_8C(0x24, 50, 400)

    ChrTalk(    #160
        0x24,
        "Mmmm, this is bad...\x02",
    )

    CloseMessageWindow()

    def lambda_38AF():
        TurnDirection(0xFE, 0x24, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_38AF)

    def lambda_38BD():
        TurnDirection(0xFE, 0x24, 400)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_38BD)

    def lambda_38CB():
        TurnDirection(0xFE, 0x24, 400)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_38CB)

    def lambda_38D9():
        TurnDirection(0xFE, 0x24, 400)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_38D9)
    TurnDirection(0x26, 0x24, 400)

    ChrTalk(    #161
        0x103,
        "#023F#4POh, Father.\x02",
    )

    CloseMessageWindow()

    def lambda_3907():
        OP_6D(41450, 0, 68050, 2500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_3907)

    def lambda_391F():

        label("loc_391F")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_391F")

    QueueWorkItem2(0x101, 3, lambda_391F)

    def lambda_3930():

        label("loc_3930")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3930")

    QueueWorkItem2(0x103, 3, lambda_3930)

    def lambda_3941():

        label("loc_3941")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3941")

    QueueWorkItem2(0xF8, 3, lambda_3941)

    def lambda_3952():

        label("loc_3952")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3952")

    QueueWorkItem2(0xF9, 3, lambda_3952)

    def lambda_3963():

        label("loc_3963")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3963")

    QueueWorkItem2(0x26, 3, lambda_3963)
    OP_8E(0x24, 0xA316, 0x0, 0xFD51, 0x7D0, 0x0)
    OP_8E(0x24, 0xA64A, 0x0, 0x10036, 0x7D0, 0x0)
    OP_8C(0x24, 315, 400)
    WaitChrThread(0x13, 0x0)
    OP_44(0x101, 0x3)
    OP_44(0x103, 0x3)
    OP_44(0xF8, 0x3)
    OP_44(0xF9, 0x3)
    OP_44(0x26, 0x3)

    ChrTalk(    #162
        0x26,
        "#743F#6PUm, what brings you here?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x26, 400)

    ChrTalk(    #163
        0x24,
        (
            "#2PI heard two youths were having\x01",
            "a drinking contest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x24,
        "#2PI had a suspicion and...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x24,
        "#2PIt seems I was correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        (
            "#1007FYep, they're totally trashed.\x02\x03",

            "Seems like the medicine wore off,\x01",
            "so...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x101, 400)

    ChrTalk(    #167
        0x24,
        (
            "#5PNo, normally that medicine should\x01",
            "last for an entire evening. However...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x24,
        (
            "#5PMost likely the two of them shared\x01",
            "it between themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x24,
        (
            "#5PWithout the intended quantities, the\x01",
            "effect won't be what is expected...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #170
        0x101,
        "#1008FAh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BFD")

    ChrTalk(    #171
        0x107,
        "#561FAhaha... So that's why.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CAD")

    label("loc_3BFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C35")

    ChrTalk(    #172
        0x106,
        "#053FHeh. That's why it wore off.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CAD")

    label("loc_3C35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C74")

    ChrTalk(    #173
        0x108,
        "#070FHaha. So they earned what they got.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CAD")

    label("loc_3C74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CAD")

    ChrTalk(    #174
        0x105,
        "#047FAh, so that's how this happened.\x02",
    )

    CloseMessageWindow()

    label("loc_3CAD")


    ChrTalk(    #175
        0x24,
        (
            "#5PEveryone, make sure you obey usage\x01",
            "instructions when taking medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x26,
        (
            "#745F#6P*sigh* I think I see what's going on.\x02\x03",

            "I thought it was odd for Olivier\x01",
            "to suddenly invite me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#1016FAhahaha...\x02\x03",

            "I guess that's just going to\x01",
            "strengthen his trauma, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x24,
        (
            "#5PAnyway, I will take responsibility\x01",
            "for taking care of these two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x24,
        (
            "#5PIt seems they've imbibed quite an\x01",
            "unhealthy amount of liquor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x26,
        (
            "#740F#6PYes, please.\x02\x03",

            "I need to be getting back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x26, 400)

    ChrTalk(    #181
        0x24,
        "#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x26,
        "#743F#6PWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x24,
        (
            "#2PAina...\x01",
            "You smell strongly of alcohol yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x24,
        (
            "#2PYou've had quite a bit yourself,\x01",
            "it seems, but are you not drunk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x26,
        (
            "#741F#6PMe? No. This was hardly anything.\x02\x03",

            "I drank, sure, but that was just\x01",
            "barely enough to be social.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FCB")
    OP_62(0xF6, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4009")

    label("loc_3FCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FF2")
    OP_62(0xF6, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4009")

    label("loc_3FF2")

    OP_62(0xF6, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4009")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4030")
    OP_62(0xF7, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_406E")

    label("loc_4030")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4057")
    OP_62(0xF7, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_406E")

    label("loc_4057")

    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_406E")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40E5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40A7")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_40E5")

    label("loc_40A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40CE")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_40E5")

    label("loc_40CE")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_40E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4157")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4119")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4157")

    label("loc_4119")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4140")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4157")

    label("loc_4140")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4157")


    def lambda_415D():
        OP_8C(0x0, 180, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_415D)

    def lambda_416B():
        OP_8C(0x1, 180, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_416B)

    def lambda_4179():
        OP_8C(0x2, 180, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4179)

    def lambda_4187():
        OP_8C(0x3, 180, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4187)
    Sleep(1000)

    ChrTalk(    #186
        0x101,
        "#1020FWhaaat?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41D7")

    ChrTalk(    #187
        0x108,
        "#073FHmmm, impressive...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4281")

    label("loc_41D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_420B")

    ChrTalk(    #188
        0x106,
        "#055FYou gotta be kidding me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4281")

    label("loc_420B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_425D")

    ChrTalk(    #189
        0x105,
        (
            "#045FI-I feel like we've heard quite\x01",
            "the amazing statement.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4281")

    label("loc_425D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4281")

    ChrTalk(    #190
        0x107,
        "#065FN-No way...\x02",
    )

    CloseMessageWindow()

    label("loc_4281")


    ChrTalk(    #191
        0x103,
        "#025F#4PSeriously, you're a bottomless pit...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x24,
        "#2P...I see. Well, then that's fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x24,
        (
            "#2PIt's true you do smell of liquor,\x01",
            "but you don't seem to be drunk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x26,
        "#740F#6PThen, if you'll pardon me...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x103, 400)
    TurnDirection(0x103, 0x26, 400)

    ChrTalk(    #195
        0x26,
        (
            "#741F#6PWell, Scherazard.\x01",
            "Take care of the rest, thanks.\x02\x03",

            "Oh, yes, and you can put it on Olivier's tab.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_43D3():

        label("loc_43D3")

        TurnDirection(0xFE, 0x26, 400)
        OP_48()
        Jump("loc_43D3")

    QueueWorkItem2(0x101, 0, lambda_43D3)

    def lambda_43E4():

        label("loc_43E4")

        TurnDirection(0xFE, 0x26, 400)
        OP_48()
        Jump("loc_43E4")

    QueueWorkItem2(0x103, 0, lambda_43E4)

    def lambda_43F5():

        label("loc_43F5")

        TurnDirection(0xFE, 0x26, 400)
        OP_48()
        Jump("loc_43F5")

    QueueWorkItem2(0xF8, 0, lambda_43F5)

    def lambda_4406():

        label("loc_4406")

        TurnDirection(0xFE, 0x26, 400)
        OP_48()
        Jump("loc_4406")

    QueueWorkItem2(0xF9, 0, lambda_4406)

    def lambda_4417():

        label("loc_4417")

        TurnDirection(0xFE, 0x26, 400)
        OP_48()
        Jump("loc_4417")

    QueueWorkItem2(0x24, 0, lambda_4417)

    def lambda_4428():
        OP_69(0x27, 0x5DC)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_4428)
    OP_43(0x26, 0x0, 0x2, 0xA)
    WaitChrThread(0x26, 0x2)

    ChrTalk(    #196
        0x27,
        (
            "#038F#2PH-Heh... Aina.\x02\x03",

            "That part of you that never misses\x01",
            "anything is what I...lo... *blorf*\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x26, 0x80)
    OP_28(0x76, 0x1, 0x8)
    OP_28(0x76, 0x1, 0x10)
    OP_28(0x76, 0x1, 0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_44D1")
    OP_28(0x76, 0x1, 0x4000)

    label("loc_44D1")

    OP_28(0x76, 0x4, 0x10)
    OP_EA(0x1, 0x4, 0x0, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #197
        "Quest #2C[Diaset's Secret] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T0121   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_0_AA end

    def Function_1_452F(): pass

    label("Function_1_452F")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_4545():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4545)
    OP_8E(0xFE, 0xA410, 0x0, 0x11292, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_1_452F end

    def Function_2_456D(): pass

    label("Function_2_456D")

    Sleep(1000)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_4588():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4588)
    OP_8E(0xFE, 0xA7F8, 0x0, 0x10D38, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_2_456D end

    def Function_3_45B0(): pass

    label("Function_3_45B0")

    Sleep(1400)
    OP_9F(0x25, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x25, 0x80)

    def lambda_45CB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x25, 3, lambda_45CB)
    OP_8E(0x25, 0xA7F8, 0x0, 0x115EE, 0x7D0, 0x0)
    OP_8C(0x25, 180, 400)
    Return()

    # Function_3_45B0 end

    def Function_4_45F3(): pass

    label("Function_4_45F3")

    Sleep(2000)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_460E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_460E)
    OP_8E(0xFE, 0xAC44, 0x0, 0x11102, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_4_45F3 end

    def Function_5_4636(): pass

    label("Function_5_4636")

    SetChrFlags(0xFE, 0x40)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x823C, 0x0, 0x10F54, 0x1388, 0x0)
    OP_8E(0xFE, 0x823C, 0x0, 0x11850, 0x1388, 0x0)
    OP_8E(0xFE, 0x82C8, 0x654, 0x125D4, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x8)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_5_4636 end

    def Function_6_4694(): pass

    label("Function_6_4694")

    OP_8E(0xFE, 0xA76C, 0x0, 0x12110, 0x1388, 0x0)
    OP_8E(0xFE, 0xA4A6, 0x0, 0x110D0, 0x1388, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_6_4694 end

    def Function_7_46C4(): pass

    label("Function_7_46C4")

    ClearChrFlags(0xFE, 0x1000)
    OP_8E(0xFE, 0xA564, 0x0, 0x101B2, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_7_46C4 end

    def Function_8_46E5(): pass

    label("Function_8_46E5")

    OP_8E(0xFE, 0xA622, 0x0, 0x12110, 0x1388, 0x0)
    OP_8E(0xFE, 0xA8A2, 0x0, 0x11044, 0x1388, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_8_46E5 end

    def Function_9_4715(): pass

    label("Function_9_4715")

    OP_8E(0xFE, 0xA7D0, 0x0, 0x12110, 0x1388, 0x0)
    OP_8E(0xFE, 0xA14A, 0x0, 0x1103A, 0x1388, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_9_4715 end

    def Function_10_4745(): pass

    label("Function_10_4745")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x9EE8, 0x0, 0xF456, 0x7D0, 0x0)

    def lambda_4766():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4766)
    OP_8E(0xFE, 0x9EE8, 0xFFFFFE0C, 0xDAC0, 0x7D0, 0x0)
    Return()

    # Function_10_4745 end

    def Function_11_4787(): pass

    label("Function_11_4787")

    EventBegin(0x0)
    OP_6D(38400, 0, 68270, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(315000, 0)
    OP_6E(230, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x103, 0x80)
    ClearChrFlags(0x103, 0x8)
    SetChrFlags(0x26, 0x4)
    SetChrFlags(0x26, 0x40)
    SetChrPos(0x26, 38290, -100, 67720, 114)
    SetChrChipByIndex(0x27, 17)
    SetChrSubChip(0x27, 0)
    SetChrFlags(0x27, 0x4)
    SetChrFlags(0x27, 0x40)
    SetChrPos(0x27, 39710, 80, 68530, 180)
    SetChrChipByIndex(0x25, 14)
    SetChrSubChip(0x25, 0)
    SetChrFlags(0x25, 0x4)
    SetChrFlags(0x25, 0x40)
    SetChrPos(0x25, 39690, 40, 66460, 0)
    OP_72(0x1, 0x4)
    SetChrChipByIndex(0x103, 21)
    SetChrSubChip(0x103, 0)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 41700, 200, 67710, 225)
    ClearChrFlags(0x2D, 0x80)
    SetChrSubChip(0x2D, 29)
    ClearChrFlags(0x2E, 0x80)
    SetChrSubChip(0x2E, 29)
    SetChrPos(0x2D, 41440, 0, 66610, 15)
    SetChrPos(0x2E, 41090, 0, 66050, 30)

    ChrTalk(    #198
        0x25,
        "……あ、あれ？\x02",
    )

    CloseMessageWindow()
    OP_9E(0x25, 0x14, 0x0, 0x1F4, 0xFA0)
    ClearChrFlags(0x25, 0x100)
    SetChrChipByIndex(0x25, 13)
    SetChrPos(0x25, 40480, 0, 66130, 0)
    SetChrChipByIndex(0x25, 13)
    OP_D1(37, 20000, 0, 0, 0)

    def lambda_48FF():
        OP_D1(37, 60000, -15000, -90000, 200)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_48FF)
    OP_51(0x25, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    ClearChrFlags(0x2D, 0x100)
    ClearChrFlags(0x2E, 0x100)
    OP_51(0x2D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_495F():
        OP_96(0x2D, 0xA3FC, 0x0, 0x10586, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_495F)

    def lambda_497D():
        OP_D1(45, 30000, -15000, -80000, 200)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_497D)

    def lambda_4997():
        OP_D1(46, 60000, -15000, -135000, 200)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_4997)
    WaitChrThread(0x2D, 0x2)
    OP_51(0x2D, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2D, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2D, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x2E, 0x2)
    OP_51(0x2E, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2E, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2E, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x27, 1)
    SetChrSubChip(0x103, 1)
    OP_0D()
    OP_62(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x26, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x27, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #199
        0x27,
        "#036Fア、アントン君！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x26,
        "#743F#1Pまあ、大変！\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_4A8A():
        OP_6D(41230, 0, 67950, 1000)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_4A8A)

    def lambda_4AA2():
        OP_6C(315000, 1000)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_4AA2)
    OP_43(0x26, 0x1, 0x2, 0xC)
    SetChrChipByIndex(0x103, 65535)
    SetChrFlags(0x103, 0x40)
    ClearChrFlags(0x103, 0x4)
    OP_96(0x103, 0xA1E0, 0x0, 0x10662, 0xC8, 0x1388)
    OP_8C(0x103, 180, 0)
    ClearChrFlags(0x27, 0x4)
    SetChrChipByIndex(0x27, 16)
    OP_96(0x27, 0x9E3E, 0x0, 0x10C98, 0x190, 0x1388)
    SetChrChipByIndex(0x27, 36)
    OP_8E(0x27, 0x9F60, 0x0, 0x10C98, 0xFA0, 0x1)
    SetChrSubChip(0x27, 3)
    WaitChrThread(0x25, 0x1)

    ChrTalk(    #201
        0x27,
        "#038F#2P……お、おや……！？\x02",
    )

    OP_9E(0x27, 0x14, 0x0, 0x1F4, 0xFA0)
    CloseMessageWindow()
    OP_59()
    SetChrSubChip(0x27, 0)
    SetChrFlags(0x27, 0x4)
    OP_96(0x27, 0xA3AC, 0xF0, 0x10B94, 0x190, 0xFA0)
    SetChrChipByIndex(0x27, 18)
    OP_51(0x27, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_96(0x27, 0xA4A6, 0xF0, 0x10B94, 0x190, 0xFA0)
    OP_8C(0x103, 0, 400)

    ChrTalk(    #202
        0x103,
        "#025F#1Pあちゃ～、オリビエまで……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x26,
        "#743F#1P２人ともしっかり！？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x80)
    SetChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C4A")
    ClearChrFlags(0xF8, 0x80)
    SetChrFlags(0xF8, 0x40)
    ClearChrFlags(0xF8, 0x4)
    SetChrChipByIndex(0xF8, 65535)
    SetChrPos(0xF8, 42530, 1500, 78540, 180)

    label("loc_4C4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C7C")
    ClearChrFlags(0xF9, 0x80)
    SetChrFlags(0xF9, 0x40)
    ClearChrFlags(0xF9, 0x4)
    SetChrChipByIndex(0xF9, 65535)
    SetChrPos(0xF9, 42960, 1500, 78910, 180)

    label("loc_4C7C")

    SetChrChipByIndex(0x101, 65535)
    SetChrPos(0x101, 42860, 1500, 77720, 180)

    def lambda_4C98():
        OP_6D(41380, 0, 69390, 3000)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_4C98)
    OP_43(0x101, 0x0, 0x2, 0x6)
    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CCD")
    OP_43(0xF9, 0x0, 0x2, 0x8)
    Jump("loc_4CF7")

    label("loc_4CCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CE4")
    OP_43(0xF8, 0x0, 0x2, 0x8)
    Jump("loc_4CF7")

    label("loc_4CE4")

    OP_43(0xF8, 0x0, 0x2, 0x8)
    Sleep(600)
    OP_43(0xF9, 0x0, 0x2, 0x9)

    label("loc_4CF7")

    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)

    ChrTalk(    #204
        0x101,
        "#1020F#2Pオ、オリビエ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x27,
        "#038F#4Pう、う～～ん……\x02",
    )

    CloseMessageWindow()

    def lambda_4D49():
        OP_6D(40560, 0, 66540, 2000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_4D49)
    WaitChrThread(0x13, 0x0)
    SetChrPos(0x24, 39760, -500, 61000, 0)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x24, 0x80)

    def lambda_4D87():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_4D87)
    OP_8E(0x24, 0x9B50, 0x0, 0xFBB8, 0x7D0, 0x0)
    OP_8C(0x24, 50, 400)

    ChrTalk(    #206
        0x24,
        "むむ、これはいけない……\x02",
    )

    CloseMessageWindow()

    def lambda_4DD2():
        OP_6D(41450, 0, 68050, 2500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_4DD2)

    def lambda_4DEA():

        label("loc_4DEA")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_4DEA")

    QueueWorkItem2(0x101, 3, lambda_4DEA)

    def lambda_4DFB():

        label("loc_4DFB")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_4DFB")

    QueueWorkItem2(0x103, 3, lambda_4DFB)

    def lambda_4E0C():

        label("loc_4E0C")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_4E0C")

    QueueWorkItem2(0xF8, 3, lambda_4E0C)

    def lambda_4E1D():

        label("loc_4E1D")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_4E1D")

    QueueWorkItem2(0xF9, 3, lambda_4E1D)

    def lambda_4E2E():

        label("loc_4E2E")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_4E2E")

    QueueWorkItem2(0x26, 3, lambda_4E2E)
    OP_8E(0x24, 0xA316, 0x0, 0xFD51, 0x7D0, 0x0)
    OP_8E(0x24, 0xA64A, 0x0, 0x10036, 0x7D0, 0x0)
    OP_8C(0x24, 315, 400)
    WaitChrThread(0x13, 0x0)
    Return()

    # Function_11_4787 end

    def Function_12_4E6E(): pass

    label("Function_12_4E6E")

    ClearChrFlags(0x26, 0x4)
    OP_96(0x26, 0x9380, 0x0, 0x10720, 0x190, 0x1388)
    OP_62(0x26, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x26, 0x9646, 0x0, 0x100CC, 0xBB8, 0x0)
    OP_8E(0x26, 0x9D94, 0x0, 0xFDA2, 0xBB8, 0x0)
    OP_8E(0x26, 0x9EE8, 0x0, 0x10004, 0xBB8, 0x0)
    OP_8C(0x26, 0, 400)
    Return()

    # Function_12_4E6E end

    SaveToFile()

Try(main)
