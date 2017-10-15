from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5207   ._SN',
        MapName             = 'Other',
        Location            = 'C5207.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60066",
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
        'Targeting Camera',                     # 9
        'Dummy Joshua',                         # 10
        '地震制御用ダミーキャラ',               # 11
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


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_10A",          # 00, 0
        "Function_1_10F",          # 01, 1
        "Function_2_126",          # 02, 2
        "Function_3_E37",          # 03, 3
        "Function_4_E5A",          # 04, 4
        "Function_5_EAF",          # 05, 5
    )


    def Function_0_10A(): pass

    label("Function_0_10A")

    Event(0, 2)
    Return()

    # Function_0_10A end

    def Function_1_10F(): pass

    label("Function_1_10F")

    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_6F(0x3, 1)
    OP_22(0x1C3, 0x1, 0x46)
    Return()

    # Function_1_10F end

    def Function_2_126(): pass

    label("Function_2_126")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x2601F8, 0x2601FD, 0x0)
    OP_D2(0x26008C, 0x260091, 0x1)
    SetChrPos(0x101, 940, -8000, 46490, 0)
    SetChrPos(0x102, 940, -8000, 46490, 0)
    OP_6D(1120, -7920, 44810, 0)
    OP_67(0, 5990, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(349, 0)
    OP_C4(0x0, 0x2)
    OP_7E(0x44C, 0x44C, 0xFF88, 0xA, 0x1)
    OP_43(0xA, 0x3, 0x0, 0x3)
    OP_22(0x85, 0x1, 0x46)
    FadeToBright(2000, 0)
    OP_0D()
    OP_72(0x0, 0x10)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1E)
    OP_73(0x0)

    def lambda_1EE():
        OP_6D(1070, -8000, 14420, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1EE)

    def lambda_206():
        OP_8E(0xFE, 0x17C, 0xFFFFE0C0, 0x3728, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_206)
    Sleep(300)

    def lambda_226():
        OP_8E(0xFE, 0x78A, 0xFFFFE0C0, 0x3728, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_226)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_22(0x88, 0x0, 0x64)
    OP_7C(0x3E8, 0x0, 0x3E8, 0x1F4)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x101,
        "#1014F#3P#1KWaaah!\x02",
    )


    ChrTalk(    #1
        0x102,
        "#1047F#2P#1KGh!\x02",
    )

    OP_56(0x1)
    OP_59()
    Sleep(100)
    Fade(500)
    OP_44(0x8, 0x1)
    OP_6D(-80, -8000, 4540, 0)
    OP_67(0, 6040, -10000, 0)
    OP_6B(3870, 0)
    OP_6C(315000, 0)
    OP_6E(387, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x257, 0x0, 0x64)
    OP_6F(0x3, 1)
    OP_70(0x3, 0x6)
    OP_73(0x3)
    Sleep(500)

    ChrTalk(    #2
        0x101,
        "#1004F#6PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        "#1046F#6PDamn it...!\x02",
    )

    CloseMessageWindow()

    def lambda_35F():
        OP_8E(0xFE, 0x17C, 0xFFFFE0C0, 0x23C8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35F)
    Sleep(60)

    def lambda_37F():
        OP_8E(0xFE, 0x78A, 0xFFFFE0C0, 0x23C8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_37F)
    Sleep(200)
    OP_22(0x259, 0x0, 0x64)
    Sleep(300)
    OP_6F(0x3, 5)
    OP_70(0x3, 0x190)
    Sleep(1000)
    Fade(500)
    OP_6D(520, -8000, 9150, 0)
    OP_67(0, 6580, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(315000, 0)
    OP_6E(276, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #4
        0x101,
        "#1020F#6PAck!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 600)

    ChrTalk(    #5
        0x102,
        "#1046FLet's go back, Estelle!\x02",
    )

    CloseMessageWindow()

    def lambda_441():
        OP_6D(770, -8000, 13840, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_441)
    OP_8C(0x101, 0, 600)

    def lambda_460():
        OP_8E(0xFE, 0x1AE, 0xFFFFE0C0, 0x3BC4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_460)
    Sleep(50)
    OP_8C(0x102, 0, 600)

    def lambda_487():
        OP_8E(0xFE, 0x848, 0xFFFFE0C0, 0x3BC4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_487)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_22(0x88, 0x0, 0x64)
    OP_7C(0x3E8, 0x0, 0x3E8, 0x1F4)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_6D(-40, -8000, 21740, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(6500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_20(0xBB8)
    OP_22(0x259, 0x0, 0x64)
    OP_6F(0x3, 400)
    OP_70(0x3, 0x24E)
    Sleep(1000)
    OP_73(0x3)
    Fade(500)
    OP_6D(0, -8000, 17970, 0)
    OP_67(0, 4800, -10000, 0)
    OP_6B(3290, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #6
        0x101,
        "#1026F#5P...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x50)
    OP_24(0x85, 0x3C)
    Sleep(100)
    OP_24(0x85, 0x32)
    Sleep(400)

    def lambda_5CF():
        OP_6D(1360, -8000, 19520, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5CF)

    def lambda_5E7():
        OP_67(0, 6370, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5E7)

    def lambda_5FF():
        OP_8F(0xFE, 0x5D2, 0xFFFFE0C0, 0x4510, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5FF)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #7
        0x101,
        (
            "#1003F#5PWell...so much for going back,\x01",
            "I guess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#1043F#5P...Yeah...\x02\x03",

            "#1035FThis column won't support us for long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1025F#5PWhich means...we're...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        (
            "#1043F#5PEstelle... I'm so sorry.\x02\x03",

            "If I hadn't tripped back there...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_717():
        OP_6D(790, -8000, 17650, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_717)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #11
        0x101,
        (
            "#1007F#4PNo, you don't need to say it.\x02\x03",

            "#1006FYou bailed me out when I was about to be\x01",
            "buried under that rubble, anyway.\x01",
            "We're both screw-ups... Heheh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        "#1043F#5PBut...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#1016F#4PAhaha... You know, it's really funny.\x02\x03",

            "Despite how COMPLETELY SCREWED\x01",
            "we are, I'm not actually scared.\x02\x03",

            "#1008FAre you, Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        (
            "#1044F#5PI'm...\x02\x03",

            "#1053FNo, you're right.\x02\x03",

            "#1054FI'm not scared at all.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(7350, -18890, 23200, 0)
    OP_67(0, 6770, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(315000, 0)
    OP_6E(359, 0)
    OP_0D()
    OP_22(0x154, 0x0, 0x64)
    OP_6F(0x3, 590)
    OP_70(0x3, 0x258)
    OP_73(0x3)
    Sleep(1000)

    def lambda_929():
        OP_6D(790, -8000, 17650, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_929)

    def lambda_941():
        OP_67(0, 4800, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_941)

    def lambda_959():
        OP_6B(3290, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_959)

    def lambda_969():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_969)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #15
        0x101,
        (
            "#1013F#4PHey... J-J-Joshua?\x02\x03",

            "Can I ask two favors,\x01",
            "here at the end?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        "#1040F#5PAlways.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1012F#4PSo, first...\x02\x03",

            "#1017FWould you hold on to me?\x01",
            "Like...tightly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        "#1049F#5POf course I will.\x02",
    )

    CloseMessageWindow()

    def lambda_A4D():
        OP_6D(770, -8000, 18200, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A4D)

    def lambda_A65():
        OP_6B(3100, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A65)
    OP_8E(0x102, 0x5DC, 0xFFFFE0C0, 0x42B8, 0x5DC, 0x0)
    WaitChrThread(0x101, 0x1)
    Fade(500)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x102, 0x80)
    OP_99(0x101, 0x0, 0x4, 0x3E8)
    Sleep(1000)

    ChrTalk(    #19
        0x101,
        "#1008F#4PAhh...hahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        (
            "#1040F#6PThere should be a second in there,\x01",
            "somewhere, I think.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x24), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x25), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(500)

    ChrTalk(    #21
        0x101,
        (
            "#1013F#4POh, er, um.\x02\x03",

            "So, um, even at, you know, the end of, er, things,\x01",
            "here, I don't want to be TOO pushy...\x02\x03",

            "I, well... I don't want to have any regrets,\x01",
            "and, crap, how do I put thi--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        (
            "#1035F#6PDon't worry.\x01",
            "I can say the rest.\x02\x03",

            "#1041FEstelle...may I kiss you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1004F#4PAh...!\x02",
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x24), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(500)

    ChrTalk(    #24
        0x101,
        "#1017F#4PYes... Yes!\x02",
    )

    CloseMessageWindow()
    OP_DB()
    OP_20(0x3E8)
    OP_21()
    OP_1D(0x85)
    Sleep(500)
    OP_99(0x101, 0x4, 0x6, 0x3E8)
    Sleep(500)

    def lambda_CC7():
        OP_6B(2900, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CC7)
    OP_99(0x101, 0x6, 0x8, 0x3E8)
    Sleep(2000)

    def lambda_CE5():
        OP_99(0xFE, 0x8, 0xA, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CE5)

    def lambda_CF5():
        OP_67(0, 10670, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CF5)

    def lambda_D0D():
        OP_6E(378, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D0D)
    Sleep(1000)
    OP_22(0x259, 0x0, 0x64)
    OP_B0(0x3, 0x28)
    OP_6F(0x3, 600)
    OP_70(0x3, 0x3E8)

    def lambda_D39():
        OP_67(0, 14670, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D39)

    def lambda_D51():
        OP_6D(770, -20000, 18200, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D51)

    def lambda_D69():
        OP_6B(1000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D69)
    OP_C4(0x1, 0x2)
    ClearChrFlags(0x101, 0x1)
    OP_99(0x101, 0xA, 0xC, 0x4B0)
    OP_43(0x102, 0x3, 0x0, 0x4)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x85, 0x28)
    Sleep(200)
    OP_24(0x85, 0x1E)
    Sleep(200)
    OP_24(0x85, 0x14)
    Sleep(200)
    OP_24(0x85, 0xA)
    Sleep(200)
    OP_23(0x85)
    ClearMapFlags(0x100000)
    OP_C4(0x0, 0x10)
    OP_48()
    FadeToBright(1, 0)
    PlayMovie(0x0, "ED6_DT46.dat", 0x0, 0x1)

    label("loc_DED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E07")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_E04")
    Jump("loc_E07")

    label("loc_E04")

    Jump("loc_DED")

    label("loc_E07")

    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    Sleep(500)
    OP_C4(0x1, 0x10)
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/E0110   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_2_126 end

    def Function_3_E37(): pass

    label("Function_3_E37")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E59")
    OP_7C(0x1E, 0x1E, 0x3E8, 0x384)
    Sleep(1000)
    Jump("Function_3_E37")

    label("loc_E59")

    Return()

    # Function_3_E37 end

    def Function_4_E5A(): pass

    label("Function_4_E5A")

    SetChrPos(0x101, 1500, -8500, 17200, 0)
    SetChrFlags(0x101, 0x20)

    def lambda_E76():
        OP_91(0xFE, 0x0, 0xFFFF3CB0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E76)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    def lambda_EA1():

        label("loc_EA1")

        OP_99(0x101, 0xE, 0x1D, 0x5DC)
        OP_48()
        Jump("loc_EA1")

    QueueWorkItem2(0x102, 2, lambda_EA1)
    Return()

    # Function_4_E5A end

    def Function_5_EAF(): pass

    label("Function_5_EAF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EFB")
    OP_51(0x8, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_5_EAF")

    label("loc_EFB")

    Return()

    # Function_5_EAF end

    SaveToFile()

Try(main)
