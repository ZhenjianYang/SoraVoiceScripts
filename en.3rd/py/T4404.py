from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4404   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4404.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        'Strange Man',                          # 9
        'Gilbert',                              # 10
        'G-Apache',                             # 11
        'Rifle',                                # 12
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


    AddCharChip(
        'ED6_DT07/CH02420 ._CH',             # 00
        'ED6_DT27/CH03750 ._CH',             # 01
        'ED6_DT27/CH04750 ._CH',             # 02
        'ED6_DT27/CH04751 ._CH',             # 03
        'ED6_DT27/CH04753 ._CH',             # 04
        'ED6_DT26/CH20632 ._CH',             # 05
        'ED6_DT26/CH20501 ._CH',             # 06
        'ED6_DT27/CH04150 ._CH',             # 07
        'ED6_DT27/CH04151 ._CH',             # 08
        'ED6_DT27/CH04152 ._CH',             # 09
        'ED6_DT27/CH04153 ._CH',             # 0A
        'ED6_DT27/CH04154 ._CH',             # 0B
        'ED6_DT26/CH20611 ._CH',             # 0C
        'ED6_DT26/CH20451 ._CH',             # 0D
        'ED6_DT29/CH14970 ._CH',             # 0E
        'ED6_DT27/CH04080 ._CH',             # 0F
        'ED6_DT26/CH20622 ._CH',             # 10
        'ED6_DT27/CH03440 ._CH',             # 11
        'ED6_DT26/CH20617 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH02420P._CP',             # 00
        'ED6_DT27/CH03750P._CP',             # 01
        'ED6_DT27/CH04750P._CP',             # 02
        'ED6_DT27/CH04751P._CP',             # 03
        'ED6_DT27/CH04753P._CP',             # 04
        'ED6_DT26/CH20632P._CP',             # 05
        'ED6_DT26/CH20501P._CP',             # 06
        'ED6_DT27/CH04150P._CP',             # 07
        'ED6_DT27/CH04151P._CP',             # 08
        'ED6_DT27/CH04152P._CP',             # 09
        'ED6_DT27/CH04153P._CP',             # 0A
        'ED6_DT27/CH04154P._CP',             # 0B
        'ED6_DT26/CH20611P._CP',             # 0C
        'ED6_DT26/CH20451P._CP',             # 0D
        'ED6_DT29/CH14970P._CP',             # 0E
        'ED6_DT27/CH04080P._CP',             # 0F
        'ED6_DT26/CH20622P._CP',             # 10
        'ED6_DT27/CH03440P._CP',             # 11
        'ED6_DT26/CH20617P._CP',             # 12
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1C2",          # 00, 0
        "Function_1_1FE",          # 01, 1
        "Function_2_204",          # 02, 2
        "Function_3_1A9E",         # 03, 3
        "Function_4_1D32",         # 04, 4
        "Function_5_1D81",         # 05, 5
        "Function_6_1E16",         # 06, 6
        "Function_7_1E5C",         # 07, 7
        "Function_8_1E99",         # 08, 8
        "Function_9_2F9B",         # 09, 9
        "Function_10_2FF4",        # 0A, 10
    )


    def Function_0_1C2(): pass

    label("Function_0_1C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_1E1")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)
    Jump("loc_1FD")

    label("loc_1E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1FD")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_1FD")

    Return()

    # Function_0_1C2 end

    def Function_1_1FE(): pass

    label("Function_1_1FE")

    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_1FE end

    def Function_2_204(): pass

    label("Function_2_204")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "battle\\damage0.eff")
    LoadEffect(0x1, "map\\mpsibuk.eff")
    LoadEffect(0x2, "map\\mp255_00.eff")
    SetChrPos(0x109, 3620, 0, 66530, 0)
    SetChrPos(0x10F, 3620, 0, 66530, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-78990, 1750, 13960, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(332000, 0)
    OP_6D(1820, 0, -960, 0)
    OP_67(0, 10300, -10000, 0)
    OP_6B(3580, 0)
    OP_6C(45000, 0)
    OP_6E(506, 0)

    def lambda_2F9():
        OP_6D(430, 0, 28700, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2F9)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10F, 0x0)
    Fade(500)
    OP_6D(300, 0, 25910, 0)
    OP_67(0, 8340, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(371, 0)
    OP_0D()
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -90, 0, 13540, 0)

    def lambda_379():
        OP_8E(0xFE, 0xFFFFFE84, 0x0, 0x6234, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_379)
    WaitChrThread(0x11, 0x0)
    Sleep(200)
    OP_8C(0x11, 270, 600)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_8C(0x11, 0, 800)
    OP_8C(0x11, 90, 800)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3E1():
        OP_8E(0xFE, 0x3912, 0x0, 0x62F2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_3E1)
    WaitChrThread(0x11, 0x0)
    Fade(1000)
    SetChrPos(0x11, 6940, 0, 73790, 90)

    def lambda_417():
        OP_8E(0xFE, 0x53B6, 0x0, 0x124A8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_417)
    OP_6D(20900, 0, 74140, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(2750, 0)
    OP_6B(3380, 0)
    OP_6C(224000, 0)
    OP_6E(298, 0)

    def lambda_478():
        OP_6B(2750, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_478)
    WaitChrThread(0x11, 0x0)
    Sleep(200)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x11, 135, 600)
    Sleep(500)
    OP_8C(0x11, 45, 600)
    Sleep(300)
    OP_8C(0x11, 90, 600)
    Sleep(500)

    ChrTalk(    #0
        0x11,
        (
            "#674F#5PUgh... Where did they go?!\x02\x03",

            "I saw them enter this area. I'm sure of it!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x109, 9080, 0, 74240, 90)
    SetChrPos(0x10F, 8830, 0, 75680, 90)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #1
        0x109,
        "Kevin's Voice",
        "#3PIt was you, huh?\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0x11,
        "#672F#5PWha...?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 600)

    def lambda_5B4():
        OP_6D(18500, 0, 73760, 3000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_5B4)

    def lambda_5CC():
        OP_67(0, 5180, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5CC)

    def lambda_5E4():
        OP_6B(2930, 3000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5E4)

    def lambda_5F4():
        OP_6C(224000, 3000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_5F4)

    def lambda_604():
        OP_6E(295, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_604)

    def lambda_614():
        OP_8E(0xFE, 0x4038, 0x0, 0x12200, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_614)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    Sleep(500)

    def lambda_63F():
        OP_8E(0xFE, 0x3F6F, 0x0, 0x127A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_63F)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_67C():
        OP_8F(0xFE, 0x5960, 0x0, 0x12480, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_67C)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x13, 0x0)

    ChrTalk(    #3
        0x11,
        (
            "#676FH-How?!\x02\x03",

            "How did you discover me? My stealth abilities\x01",
            "are the height of perfection!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1840F#5PHaha... You're just like I remember you.\x01",
            "Still way too sure of yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        "#1443FWho might he be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        (
            "#1075F#5PWell, he's technically part of Ouroboros.\x02\x03",

            "#1060FHe's about as low-ranking a member as\x01",
            "you can get, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10F,
        "#1446FAhh, I see. He does look the part.\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #8
        0x11,
        (
            "#674FH-How dare you? I'll have you know,\x01",
            "I'm very much on the up!\x02\x03",

            "And as for YOU!\x02\x03",

            "What do you mean, 'He does look the part'?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10F,
        (
            "#1805F#40W...#20W\x02\x03",

            "#1447FYou couldn't look more like a nobody if you tried.\x02\x03",

            "You're the kind of person who constantly throws\x01",
            "himself into things too big to handle and ends up\x01",
            "sabotaging himself without anyone lifting a finger.\x02\x03",

            "#1448FAnd you refuse to learn from any of your failures,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #10
        0x11,
        "#676FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x109,
        (
            "#1066F#5PYou haven't lost your touch.\x02\x03",

            "I'm impressed how accurately you were able\x01",
            "to judge his character after talking to him for,\x01",
            "like, a second.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10F,
        (
            "#1446FI didn't even need to talk to him.\x02\x03",

            "He oozes irrelevance from his every pore.\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x11, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #13
        0x11,
        (
            "#674FY-You...\x02\x03",

            "#673F...Cocky, aren't you?\x02\x03",

            "#675FHeheheh. Well, let's see how long\x01",
            "that cockiness lasts!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(20700, 0, 73950, 0)
    OP_67(0, 5850, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(135000, 0)
    OP_6E(305, 0)
    OP_0D()
    OP_22(0xCB, 0x0, 0x64)
    OP_8C(0x11, 90, 2000)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    OP_8C(0x11, 0, 2000)
    OP_8C(0x11, 270, 2000)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(300)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #14
        0x109,
        "#1063FBah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15 op#A op#5
        0x10F,
        "#1441F#6P#8A...\x05\x02",
    )

    Fade(250)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(800)

    def lambda_C6A():
        OP_6D(22470, 0, 73750, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C6A)

    def lambda_C82():
        OP_6B(2400, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_C82)
    OP_43(0x10F, 0x0, 0x0, 0x3)
    Sleep(2000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x10F, 0x0)

    def lambda_CBF():
        OP_6D(20800, 0, 73500, 1500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_CBF)

    def lambda_CD7():
        OP_67(0, 4950, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_CD7)

    def lambda_CEF():
        OP_6B(2910, 1500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_CEF)

    def lambda_CFF():
        OP_6C(135000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_CFF)

    def lambda_D0F():
        OP_6E(298, 1500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_D0F)
    WaitChrThread(0x13, 0x0)
    Sleep(300)

    ChrTalk(    #16
        0x109,
        (
            "#1065F#4PA templar sword?\x02\x03",

            "#1067F...So that's what you picked, huh?\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(300)

    def lambda_D8C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_D8C)
    Sleep(700)

    ChrTalk(    #17
        0x10F,
        (
            "#1445F#5PJust like you chose a bowgun as your weapon\x01",
            "of choice, I chose a templar sword for mine.\x02\x03",

            "#1806FThat's all there is to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x109,
        (
            "#1840F#4P...Got'cha.\x02\x03",

            "#1065F...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_E52():
        OP_6D(24720, 0, 73600, 3000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_E52)

    def lambda_E6A():
        OP_67(0, 5560, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E6A)

    def lambda_E82():
        OP_6B(2680, 3000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_E82)

    def lambda_E92():
        OP_6C(135000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_E92)

    def lambda_EA2():
        OP_6E(307, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_EA2)

    def lambda_EB2():
        OP_8E(0xFE, 0x58C0, 0x0, 0x12110, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_EB2)
    Sleep(1000)
    OP_8C(0x10F, 90, 400)
    WaitChrThread(0x10, 0x0)
    OP_44(0x11, 0x1)
    Sleep(500)
    Fade(250)
    SetChrFlags(0x11, 0x1)
    SetChrChipByIndex(0x11, 5)
    SetChrSubChip(0x11, 0)
    SetChrPos(0x11, 25400, 0, 74910, 270)
    OP_0D()
    OP_9E(0x11, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #19
        0x11,
        "#1224F#5PI-Impossible...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrSubChip(0x11, 1)
    Sleep(500)

    ChrTalk(    #20
        0x11,
        (
            "#1224F#5PWh-What did you just do?! I don't even know\x01",
            "how I got hit!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x109,
        (
            "#1075F#4PIt's a weapon used by the Gralsritter called\x01",
            "a templar sword.\x02\x03",

            "The blade's made up of multiple pieces held\x01",
            "together by wires that let the user extend it\x01",
            "at will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        "#1222F#5PMmmrgr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x109,
        (
            "#1065F#4PAnyway, it's time those lips started flapping.\x02\x03",

            "#1063FWhat's a wanted criminal like you doing here\x01",
            "in Grancel?\x02\x03",

            "How much of our business do you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        "#1220F#5PHmph! Why should I have to answer your--\x02",
    )

    CloseMessageWindow()

    def lambda_113E():
        OP_8E(0xFE, 0x57E4, 0x0, 0x124F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_113E)

    def lambda_1159():
        OP_6D(25720, 0, 73600, 900)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1159)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x10, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(300)
    OP_9E(0x11, 0xF, 0x0, 0x12C, 0xBB8)

    ChrTalk(    #25
        0x11,
        "#1224F#5PYeeek!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10F,
        (
            "#1801F#6PYou don't know when to give up.\x02\x03",

            "Start talking. Now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        (
            "#1066F#4PFYI, she's NOT in a good mood.\x02\x03",

            "And, uh...you don't want to make her any madder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x11,
        (
            "#1224F#5PUgh... Uuurgh...\x02\x03",

            "#1225FIt looks like I've got only one option.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)

    def lambda_12B7():
        OP_6D(25800, 0, 73600, 300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_12B7)

    def lambda_12CF():
        OP_6B(2500, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_12CF)

    def lambda_12DF():
        OP_96(0xFE, 0x6662, 0x0, 0x124D0, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_12DF)
    SetChrChipByIndex(0x11, 13)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x11, 0x800)
    OP_22(0xA4, 0x0, 0x64)
    OP_0D()
    Sleep(500)
    OP_43(0x11, 0x0, 0x0, 0x6)

    ChrTalk(    #29
        0x11,
        (
            "#1227F#5PI'm so sorry! Forgive me!\x02\x03",

            "I'm only here because I crashlanded! I didn't\x01",
            "even WANT to come here!\x02\x03",

            "And after I did, I happened to see you two,\x01",
            "so I decided to follow you! I swear!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x11, 0x0)
    OP_43(0x11, 0x0, 0x0, 0x7)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #30
        0x10F,
        (
            "#1446F#6PMaybe I misjudged him.\x02\x03",

            "#1440FThere might be more to him than meets the eye.\x01",
            "...In a sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x109,
        (
            "#1068F#4PThat's a nice way of putting it...\x02\x03",

            "#1063FSo go on. Keep talking.\x02\x03",

            "You said you crashlanded here? That means\x01",
            "there's an Ouroboros airship somewhere near\x01",
            "here that you came on, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x11, 0x0)
    Sleep(300)
    Fade(250)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #32
        0x11,
        (
            "#1224F#5PN-No! There isn't!\x02\x03",

            "I did crashland, but it wasn't on board an\x01",
            "airship...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    PlayEffect(0x2, 0x0, 0xFF, 32130, -2000, 74350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xE3, 0x0, 0x64)
    OP_22(0x10B, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)
    OP_20(0x7D0)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    SetChrPos(0x109, 20630, 0, 74330, 90)
    SetChrPos(0x10F, 20030, 0, 75290, 90)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    ClearChrFlags(0x11, 0x2)
    ClearChrFlags(0x11, 0x800)

    def lambda_16B4():
        OP_96(0xFE, 0x6590, 0x0, 0x12430, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_16B4)
    OP_22(0xA3, 0x0, 0x64)
    OP_6D(26900, 0, 74700, 0)
    OP_67(0, 3600, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(90000, 0)
    OP_6E(350, 0)

    def lambda_1714():
        OP_6B(2620, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1714)
    OP_0D()

    ChrTalk(    #33 op#A op#5
        0x11,
        "#1221F#20A#3S#5PIt was on board THIS!\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(1500)
    Fade(500)
    OP_1D(0x97)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_177B():
        OP_6D(24630, 1000, 74700, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_177B)

    def lambda_1793():
        OP_67(0, 2860, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1793)

    def lambda_17AB():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_17AB)
    OP_23(0xE3)
    OP_23(0x10B)
    OP_22(0xDC, 0x0, 0x64)
    OP_22(0x5C, 0x0, 0x64)
    OP_22(0x77, 0x0, 0x64)
    OP_22(0x135, 0x1, 0x64)
    PlayEffect(0x1, 0x1, 0xFF, 33130, -2000, 74500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x2)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 32130, -5000, 74700, 270)

    def lambda_1823():

        label("loc_1823")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1823")

    QueueWorkItem2(0x12, 3, lambda_1823)

    def lambda_1836():
        OP_8F(0xFE, 0x7D82, 0x578, 0x123CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1836)

    def lambda_1851():
        OP_7C(0xC8, 0xC8, 0xBB8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1851)
    Sleep(1000)
    OP_82(0x1, 0x2)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 0)

    def lambda_1880():
        OP_96(0xFE, 0x4704, 0x0, 0x126EC, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1880)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x109, 15)
    SetChrSubChip(0x109, 0)

    def lambda_18B2():
        OP_96(0xFE, 0x4ABA, 0x0, 0x12110, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_18B2)
    WaitChrThread(0x10F, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    WaitChrThread(0x109, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    WaitChrThread(0x12, 0x0)

    ChrTalk(    #34
        0x109,
        "#1069F#12PWh-What the...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10F,
        "#1449F#6PHe has an archaism?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 225, 600)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_1938():
        OP_96(0xFE, 0x5C6C, 0x0, 0x11D50, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1938)
    SetChrChipByIndex(0x11, 5)
    SetChrSubChip(0x11, 0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x11, 0x0)

    def lambda_196A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_196A)
    Sleep(300)
    SetChrFlags(0x13, 0x80)
    OP_8C(0x11, 270, 0)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x11, 4)
    SetChrSubChip(0x11, 0)

    def lambda_199C():
        OP_96(0xFE, 0x65EA, 0x0, 0x123CC, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_199C)
    WaitChrThread(0x11, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    Sleep(300)

    ChrTalk(    #36
        0x11,
        "#1221F#5P#3SHahaha! Not so irrelevant now, am I?\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #37
        0x11,
        "#1226F#5PShow them what you can do, G-Apache!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #38
        0x11,
        "#1225F#5P#3SMow them down!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(100)
    Battle(0x74, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 8)
    Return()

    # Function_2_204 end

    def Function_3_1A9E(): pass

    label("Function_3_1A9E")

    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    SetChrFlags(0xFE, 0x1000)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_1AB6():
        OP_8E(0xFE, 0x4A10, 0x0, 0x12660, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1AB6)
    Sleep(50)
    SetChrChipByIndex(0xFE, 8)
    SetChrSubChip(0xFE, 2)
    WaitChrThread(0xFE, 0x1)

    def lambda_1AE5():
        OP_96(0xFE, 0x51C2, 0x0, 0x124D0, 0x4B0, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1AE5)
    Sleep(100)
    OP_51(0x10F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0xC5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x4F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 9)
    SetChrSubChip(0xFE, 0)

    def lambda_1BC2():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1BC2)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(100)

    def lambda_1BE1():
        OP_7C(0x64, 0x0, 0x1388, 0xC8)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1BE1)
    PlayEffect(0x0, 0xFF, 0x11, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x11, 0x0, 0x0, 0x5)
    Sleep(100)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xFE, 0x2)
    OP_51(0x10F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 11)
    SetChrSubChip(0xFE, 3)
    Sleep(500)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x1000)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_3_1A9E end

    def Function_4_1D32(): pass

    label("Function_4_1D32")

    SetChrFlags(0x13, 0x800)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 22880, 0, 74880, 0)
    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x9B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1D5E():
        OP_96(0xFE, 0x5CD0, 0x0, 0x11AE4, 0xBB8, 0x1770)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1D5E)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA, 0x0, 0x64)
    Return()

    # Function_4_1D32 end

    def Function_5_1D81(): pass

    label("Function_5_1D81")


    ChrTalk(    #39 op#A op#5
        0x11,
        "#1227F#5P#10AGaah!\x05\x02",
    )

    OP_43(0x13, 0x0, 0x0, 0x4)
    OP_22(0x50, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 4)
    SetChrSubChip(0xFE, 0)

    def lambda_1DB5():
        OP_96(0xFE, 0x5F0A, 0x0, 0x124B2, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1DB5)
    WaitChrThread(0xFE, 0x1)
    OP_22(0x20C, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 6)
    SetChrSubChip(0xFE, 0)

    def lambda_1DEC():
        OP_96(0xFE, 0x61A8, 0x0, 0x1249E, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1DEC)
    WaitChrThread(0xFE, 0x1)
    Sleep(1000)
    OP_43(0xFE, 0x1, 0x0, 0x7)
    Return()

    # Function_5_1D81 end

    def Function_6_1E16(): pass

    label("Function_6_1E16")

    OP_22(0x218, 0x0, 0x64)
    OP_99(0x11, 0x0, 0x6, 0x5DC)
    Sleep(1000)

    label("loc_1E29")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E5B")
    OP_99(0x11, 0x6, 0x2, 0x5DC)
    OP_22(0x218, 0x0, 0x64)
    OP_99(0x11, 0x2, 0x6, 0x5DC)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E58")
    Jump("loc_1E5B")

    label("loc_1E58")

    Jump("loc_1E29")

    label("loc_1E5B")

    Return()

    # Function_6_1E16 end

    def Function_7_1E5C(): pass

    label("Function_7_1E5C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E98")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_7_1E5C")

    label("loc_1E98")

    Return()

    # Function_7_1E5C end

    def Function_8_1E99(): pass

    label("Function_8_1E99")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    ClearChrFlags(0x109, 0x80)
    SetChrPos(0x109, 20950, 0, 74370, 90)
    SetChrChipByIndex(0x109, 15)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x10F, 0x80)
    SetChrPos(0x10F, 20920, 0, 76000, 90)
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 25400, 0, 74870, 270)
    SetChrChipByIndex(0x11, 5)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x40)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 25000, -300, 74870, 270)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 32130, 1500, 74350, 270)

    def lambda_1F5A():

        label("loc_1F5A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1F5A")

    QueueWorkItem2(0x12, 3, lambda_1F5A)

    def lambda_1F6D():

        label("loc_1F6D")

        OP_9E(0xFE, 0xA, 0xA, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_1F6D")

    QueueWorkItem2(0x12, 2, lambda_1F6D)
    OP_6D(30350, 1150, 74660, 0)
    OP_67(0, 5330, -10000, 0)
    OP_6B(2260, 0)
    OP_6C(122000, 0)
    OP_6E(445, 0)
    LoadEffect(0x1, "map\\mpsibuk.eff")
    LoadEffect(0x2, "monster\\ms30109a.eff")
    LoadEffect(0x3, "map\\mpsmk0.eff")
    LoadEffect(0x4, "map\\mp252_01.eff")
    LoadEffect(0x5, "map\\mp252_05.eff")
    OP_22(0x143, 0x0, 0x64)
    PlayEffect(0x2, 0x0, 0x12, 0, 0, 0, 0, 0, 0, 1800, 1800, 1800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x1, 0x12, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToBright(2000, 0)
    Sleep(500)
    OP_23(0x143)

    def lambda_20A7():
        OP_6B(1600, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_20A7)

    def lambda_20B7():
        OP_8F(0xFE, 0x7D82, 0xFFFFC568, 0x1226E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_20B7)
    Sleep(1500)
    OP_22(0xDC, 0x0, 0x64)

    def lambda_20DC():
        OP_7C(0xC8, 0xC8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_20DC)
    PlayEffect(0x1, 0x2, 0xFF, 32130, -1500, 74750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x2)
    Sleep(1000)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)

    ChrTalk(    #40
        0x11,
        "#1224F#5P#3SNooooooooo!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 0x2)
    Sleep(300)

    def lambda_215E():
        OP_6D(24460, 0, 73600, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_215E)

    def lambda_2176():
        OP_67(0, 4910, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2176)

    def lambda_218E():
        OP_6B(2150, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_218E)

    def lambda_219E():
        OP_6C(122000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_219E)

    def lambda_21AE():
        OP_6E(421, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_21AE)
    Sleep(1000)
    SetChrSubChip(0x11, 1)
    Sleep(300)
    WaitChrThread(0x109, 0x0)
    SetChrFlags(0x12, 0x80)

    ChrTalk(    #41
        0x11,
        (
            "#1225F#5PC-Curse you! Do you have any idea how much\x01",
            "I had to go through to earn that?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x109,
        "#1065FYou really are full of surprises, aren't you?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #43
        0x109,
        (
            "#1060F#11PI'm impressed, Ries. You sure know how to\x01",
            "get the best out of that thing.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x10F, 180, 400)
    Sleep(300)

    ChrTalk(    #44
        0x10F,
        (
            "#1446F#6PNot at all. I've still got a lot to learn.\x02\x03",

            "#1445FEspecially if I want to be half as good\x01",
            "as my sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x109,
        (
            "#1840F#11P...Heh.\x02\x03",

            "#1075FStill, I'm no different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10F,
        (
            "#1802F#6P...\x02\x03",

            "#1445FKevin, I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x109,
        "#1067F#11PAnyway...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    def lambda_2412():
        OP_8E(0xFE, 0x59BA, 0x0, 0x124A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2412)
    Sleep(300)
    Fade(500)
    OP_6D(22650, 0, 73560, 0)
    OP_67(0, 4910, -10000, 0)
    OP_6B(2150, 0)
    OP_6C(224000, 0)
    OP_6E(421, 0)
    OP_8C(0x10F, 90, 400)
    OP_0D()
    Sleep(500)

    ChrTalk(    #48
        0x109,
        (
            "#1060F#5PI'd wager you're out of tricks now, sooo...\x01",
            "you ready to give up and come quietly?\x02\x03",

            "If you don't try and cause any more trouble, \x01",
            "I'll hand you over to the soldiers here and\x01",
            "leave it at that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10F,
        "#1802F#2P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #50
        0x11,
        (
            "#1222F#6PY-You're planning to hand me over to the\x01",
            "Royal Army?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x109,
        (
            "#1075F#5PThat's your best option. If you really want us to\x01",
            "take you back to Arteria instead, that's cool by\x01",
            "me...\x02\x03",

            "#1073F...but if you go with that one, I can't guarantee\x01",
            "your safety. I'll leave that one to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x11, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(300)

    ChrTalk(    #52
        0x11,
        "#1224F#6PEeek...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_20(0x7D0)
    OP_22(0x15F, 0x0, 0x64)
    OP_C4(0x0, 0x400)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #53
        0x109,
        "#1063F#5PUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10F,
        "#1443F#2PA-Again?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_C4(0x1, 0x400)
    OP_0D()
    Sleep(500)
    OP_62(0x13, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #55
        0x11,
        "#1224F#6PWh-What was that?\x02",
    )

    CloseMessageWindow()
    Sleep(250)
    Fade(500)
    SetChrChipByIndex(0x109, 16)
    SetChrSubChip(0x109, 1)
    Sleep(800)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)
    PlayEffect(0x4, 0x0, 0x109, 270, 1250, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC9, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1500)

    ChrTalk(    #56
        0x109,
        (
            "#1067F#5PThis thing again? It starts glowing so\x01",
            "randomly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10F,
        "#1802F#2PMaybe it's reacting to something?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x0)

    ChrTalk(    #58
        0x11,
        (
            "#1224F#6PWh-What is that thing?! What are you planning\x01",
            "on doing?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x109,
        (
            "#1068F#5PNothing to you, don't worry. Shut up for a sec.\x02\x03",

            "#1067FWhat is UP with this thing?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(    #60
        "\x07\x05Haha... So the time to begin is finally upon us.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0xB0)
    Sleep(300)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x2)
    SetChrPos(0x10, 17660, 6700, 68260, 0)
    SetChrChipByIndex(0x10, 18)
    SetChrSubChip(0x10, 10)

    def lambda_29FD():
        OP_6D(19500, 6050, 66800, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_29FD)

    def lambda_2A15():
        OP_67(0, 4850, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2A15)

    def lambda_2A2D():
        OP_6B(3020, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2A2D)

    def lambda_2A3D():
        OP_6C(143000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2A3D)

    def lambda_2A4D():
        OP_6E(300, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2A4D)
    Sleep(2000)
    OP_99(0x10, 0xA, 0xC, 0x5DC)
    SetChrSubChip(0x10, 6)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x20)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)

    ChrTalk(    #61
        0x11,
        "#1224F#2PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x109,
        "#1069F#2PWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10F,
        "#1441F#2PWhen did you...?\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #64
        0x10,
        (
            "\x07\x05#1591F#5PIt's a pleasure to see you again, Kevin Graham.\x02\x03",

            "Traverser of the pathless darkness, repenting\x01",
            "of his transgressions with the sin of a Stigma\x01",
            "forever on his back.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x109,
        (
            "#1079F#2P...?!\x02\x03",

            "#1063FWh-Who the hell are you?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrPos(0x109, 22930, 0, 74580, 0)
    SetChrPos(0x10F, 21140, 0, 75820, 180)
    SetChrPos(0x11, 26360, 0, 75020, 180)
    SetChrPos(0x13, 26360, -200, 74420, 270)
    PlayEffect(0x4, 0x0, 0x109, 270, 1250, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_8C(0x109, 180, 0)
    Fade(500)
    OP_6D(21190, 4180, 72060, 0)
    OP_67(0, 6950, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(327000, 0)
    OP_6E(344, 0)
    OP_0D()
    SetChrFlags(0x10, 0x2)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(250)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(250)

    def lambda_2CAD():
        OP_6D(21820, 0, 75340, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2CAD)
    WaitChrThread(0xEE, 0x0)
    PlayEffect(0x4, 0x0, 0x109, 270, 1250, 100, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0x147, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10F, 135, 400)
    Sleep(300)
    PlayEffect(0x5, 0x2, 0xFF, 22490, 1000, 74230, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToDark(14000, 16777215, -1)

    def lambda_2DA8():
        OP_6B(4500, 16000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2DA8)
    OP_43(0x11, 0x0, 0x0, 0xA)
    Sleep(1000)

    ChrTalk(    #66 op#A op#5
        0x11,
        "#1227F#5P#22AW-Waaaaaah!\x05\x02",
    )

    Sleep(2200)

    ChrTalk(    #67 op#A op#5
        0x109,
        "#1070F#5P#10AUgh!\x05\x02",
    )

    Sleep(1300)

    ChrTalk(    #68 op#A op#5
        0x10F,
        "#1449F#5P#10AKevin!\x05\x02",
    )

    Sleep(1800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Strange Man")

    AnonymousTalk(    #69 op#A
        (
            "\x07\x05#1591F#4P#40AThus my lord was revived, and the door\x01",
            "to Gehenna opened...\x02",
        )
    )

    Sleep(4700)
    OP_56(0x0)
    Sleep(500)
    OP_44(0x11, 0x0)
    SetChrName("Strange Man")

    AnonymousTalk(    #70 op#A
        "\x07\x05#1591F#4P#40ACome forth, offerings! Come forth, lost lambs!\x02",
    )

    Sleep(4400)
    OP_56(0x0)
    Sleep(500)
    SetChrName("Strange Man")

    AnonymousTalk(    #71 op#A
        "\x07\x05#1591F#4P#40ABurn to ashes in the ever-blazing flames!\x07\x00\x02",
    )

    Sleep(4700)
    OP_56(0x0)
    OP_43(0x10F, 0x0, 0x0, 0x9)
    OP_0D()
    OP_44(0x109, 0x2)
    Sleep(1000)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    OP_6D(0, -100000, 0, 0)
    OP_20(0x1388)
    FadeToBright(3000, 16777215)
    OP_0D()
    OP_21()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U7004   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_8_1E99 end

    def Function_9_2F9B(): pass

    label("Function_9_2F9B")

    OP_24(0xC9, 0x5A)
    Sleep(250)
    OP_24(0xC9, 0x50)
    Sleep(250)
    OP_24(0xC9, 0x46)
    Sleep(250)
    OP_24(0xC9, 0x3C)
    Sleep(250)
    OP_24(0xC9, 0x32)
    Sleep(250)
    OP_24(0xC9, 0x28)
    Sleep(250)
    OP_24(0xC9, 0x1E)
    Sleep(250)
    OP_24(0xC9, 0x14)
    Sleep(250)
    OP_24(0xC9, 0xA)
    Sleep(250)
    OP_24(0xC9, 0x0)
    OP_23(0xC9)
    Return()

    # Function_9_2F9B end

    def Function_10_2FF4(): pass

    label("Function_10_2FF4")

    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1500)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    Return()

    # Function_10_2FF4 end

    SaveToFile()

Try(main)
