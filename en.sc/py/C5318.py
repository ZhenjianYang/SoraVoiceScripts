from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5318   ._SN',
        MapName             = 'Other',
        Location            = 'C5318.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60056",
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
        'Professor Weissmann',                  # 9
        'Greed',                                # 10
        'コア用ターゲットキャラ',               # 11
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_10A",          # 00, 0
        "Function_1_119",          # 01, 1
        "Function_2_149",          # 02, 2
        "Function_3_193",          # 03, 3
        "Function_4_C05",          # 04, 4
        "Function_5_105D",         # 05, 5
        "Function_6_1695",         # 06, 6
        "Function_7_1704",         # 07, 7
        "Function_8_1726",         # 08, 8
        "Function_9_1736",         # 09, 9
        "Function_10_17BC",        # 0A, 10
    )


    def Function_0_10A(): pass

    label("Function_0_10A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_118")
    OP_A3(0x10F0)
    Event(0, 2)

    label("loc_118")

    Return()

    # Function_0_10A end

    def Function_1_119(): pass

    label("Function_1_119")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x451), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x38), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x452), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_143")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x39), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_143")

    OP_71(0x2, 0x4)
    Return()

    # Function_1_119 end

    def Function_2_149(): pass

    label("Function_2_149")

    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x103), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x0)
    OP_C4(0x0, 0x10)
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C4(0x1, 0x10)
    OP_A3(0x0)
    Call(0, 3)
    Call(0, 4)
    Call(0, 5)
    Return()

    # Function_2_149 end

    def Function_3_193(): pass

    label("Function_3_193")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AA")
    Call(0, 9)
    Call(0, 10)

    label("loc_1AA")

    OP_D2(0x270110, 0x270120, 0x0)
    OP_D2(0x270130, 0x270140, 0x1)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_1EF"),
        (5, "loc_1FC"),
        (3, "loc_209"),
        (4, "loc_216"),
        (6, "loc_223"),
        (7, "loc_230"),
        (8, "loc_23D"),
        (10, "loc_24A"),
        (14, "loc_257"),
        (15, "loc_264"),
        (SWITCH_DEFAULT, "loc_271"),
    )


    label("loc_1EF")

    OP_D2(0x701D0, 0x701DC, 0x2)
    Jump("loc_271")

    label("loc_1FC")

    OP_D2(0x70218, 0x70224, 0x2)
    Jump("loc_271")

    label("loc_209")

    OP_D2(0x701E8, 0x701F4, 0x2)
    Jump("loc_271")

    label("loc_216")

    OP_D2(0x27036E, 0x27037B, 0x2)
    Jump("loc_271")

    label("loc_223")

    OP_D2(0x70230, 0x7023C, 0x2)
    Jump("loc_271")

    label("loc_230")

    OP_D2(0x70248, 0x70254, 0x2)
    Jump("loc_271")

    label("loc_23D")

    OP_D2(0x270176, 0x270183, 0x2)
    Jump("loc_271")

    label("loc_24A")

    OP_D2(0x702B4, 0x702BB, 0x2)
    Jump("loc_271")

    label("loc_257")

    OP_D2(0x2702D6, 0x2702E0, 0x2)
    Jump("loc_271")

    label("loc_264")

    OP_D2(0x2702C2, 0x2702CC, 0x2)
    Jump("loc_271")

    label("loc_271")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_2A2"),
        (5, "loc_2AF"),
        (3, "loc_2BC"),
        (4, "loc_2C9"),
        (6, "loc_2D6"),
        (7, "loc_2E3"),
        (8, "loc_2F0"),
        (10, "loc_2FD"),
        (14, "loc_30A"),
        (15, "loc_317"),
        (SWITCH_DEFAULT, "loc_324"),
    )


    label("loc_2A2")

    OP_D2(0x701D0, 0x701DC, 0x3)
    Jump("loc_324")

    label("loc_2AF")

    OP_D2(0x70218, 0x70224, 0x3)
    Jump("loc_324")

    label("loc_2BC")

    OP_D2(0x701E8, 0x701F4, 0x3)
    Jump("loc_324")

    label("loc_2C9")

    OP_D2(0x27036E, 0x27037B, 0x3)
    Jump("loc_324")

    label("loc_2D6")

    OP_D2(0x70230, 0x7023C, 0x3)
    Jump("loc_324")

    label("loc_2E3")

    OP_D2(0x70248, 0x70254, 0x3)
    Jump("loc_324")

    label("loc_2F0")

    OP_D2(0x270176, 0x270183, 0x3)
    Jump("loc_324")

    label("loc_2FD")

    OP_D2(0x702B4, 0x702BB, 0x3)
    Jump("loc_324")

    label("loc_30A")

    OP_D2(0x2702D6, 0x2702E0, 0x3)
    Jump("loc_324")

    label("loc_317")

    OP_D2(0x2702C2, 0x2702CC, 0x3)
    Jump("loc_324")

    label("loc_324")

    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x101, -1200, 0, -500, 0)
    SetChrPos(0x102, 600, 0, -500, 0)
    SetChrPos(0xF8, -900, 0, -1500, 0)
    SetChrPos(0xF9, 1000, 0, -1500, 0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 1)
    SetChrChipByIndex(0xF8, 2)
    SetChrChipByIndex(0xF9, 3)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 0, 0, 9500, 180)
    OP_A1(0x8, 0x2)
    OP_72(0x2, 0x4)
    OP_71(0x0, 0x4)
    OP_6F(0x2, 11)
    OP_70(0x2, 0x32)
    OP_6D(-730, 2890, 2610, 0)
    OP_67(0, 2230, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(25000, 0)
    OP_6E(583, 0)
    OP_E8(0xDC, 0x5, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    OP_6B(1800, 3000)
    OP_0D()
    SetMessageWindowPos(100, 190, -1, -1)
    SetChrName("Weissmann's Voice")

    AnonymousTalk(    #0
        (
            "\x07\x05Your tenacity is both impressive and frustrating.\x02\x03",

            "Frustrating, you see, for it is pointless.\x02\x03",

            "BEHOLD NOW! The INFINITE POWER of the Aur--\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    Fade(500)
    OP_6D(0, 0, 18610, 0)
    OP_67(0, 3380, -10000, 0)
    OP_6B(3900, 0)
    OP_6C(0, 0)
    OP_6E(410, 0)
    OP_0D()

    def lambda_522():
        OP_6B(3450, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_522)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 51)
    OP_70(0x2, 0x5A)
    OP_22(0x148, 0x0, 0x64)
    OP_73(0x2)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 11)
    OP_70(0x2, 0x32)
    WaitChrThread(0x101, 0x0)
    SetMessageWindowPos(190, 270, -1, -1)
    SetChrName("Weissmann's Voice")

    AnonymousTalk(    #1
        (
            "\x07\x05What...is...?\x02\x03",

            "The Aureole... It's... Graaaaaaah!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_DB()
    LoadEffect(0x0, "monster\\ms31000.eff")
    LoadEffect(0x1, "map\\mp103_00.eff")
    LoadEffect(0x2, "monster\\ms30900f.eff")
    Fade(500)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 211)
    OP_70(0x2, 0xFA)
    OP_22(0x8F, 0x0, 0x64)
    OP_73(0x2)
    Play3DEffect(0x0, 0x0, 0x2, "Frame95__ball", 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x5DC, 0x0)
    OP_22(0xD7, 0x0, 0x64)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 251)
    OP_70(0x2, 0x122)
    Sleep(2000)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(0, 0, -690, 0)
    OP_67(0, 80810, -10000, 0)
    OP_6B(500, 0)
    OP_6C(1000, 0)
    OP_6E(858, 0)
    SetChrPos(0x101, -550, 0, -500, 0)
    SetChrPos(0x102, 600, 0, -500, 0)
    SetChrPos(0xF8, -1250, 0, -1500, 0)
    SetChrPos(0xF9, 1200, 0, -1500, 0)
    OP_0D()
    Sleep(1000)

    def lambda_706():
        OP_6B(0, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_706)
    Sleep(400)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0x101, 0x3)
    Fade(500)
    OP_6D(0, -30000, -500, 0)
    OP_67(0, 2510, -10000, 0)
    OP_6B(230, 0)
    OP_6C(0, 0)
    OP_6E(600, 0)
    OP_22(0x85, 0x0, 0x64)
    OP_0D()
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x9, 0, -50000, 9500, 180)
    OP_A1(0x9, 0x1)
    OP_72(0x1, 0x4)
    OP_B0(0x1, 0x14)
    OP_6F(0x1, 291)
    OP_70(0x1, 0x14A)
    OP_22(0x156, 0x0, 0x64)
    OP_91(0x9, 0x0, 0x4E20, 0x0, 0xFA0, 0x0)
    Sleep(1000)

    def lambda_7C8():
        OP_6B(1500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7C8)

    def lambda_7D8():
        OP_6E(644, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D8)
    WaitChrThread(0x101, 0x0)
    OP_B0(0x1, 0x1E)

    def lambda_7F1():
        OP_8F(0xFE, 0x0, 0x7530, 0x251C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7F1)
    Sleep(500)

    def lambda_811():
        OP_8F(0xFE, 0x0, 0x7530, 0x251C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_811)
    Sleep(400)

    def lambda_831():
        OP_8F(0xFE, 0x0, 0x7530, 0x251C, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_831)
    Sleep(300)

    def lambda_851():
        OP_8F(0xFE, 0x0, 0x7530, 0x251C, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_851)
    Sleep(200)

    def lambda_871():
        OP_8F(0xFE, 0x0, 0x7530, 0x251C, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_871)
    Sleep(100)

    def lambda_891():
        OP_8F(0xFE, 0x0, 0x7530, 0x251C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_891)
    WaitChrThread(0x9, 0x0)
    Fade(500)
    OP_6D(0, -60400, 12450, 0)
    OP_67(0, 40270, -10000, 0)
    OP_6B(590, 0)
    OP_6C(0, 0)
    OP_6E(733, 0)
    SetChrPos(0x9, 0, -100000, 7500, 180)
    OP_B0(0x1, 0x28)

    def lambda_908():
        OP_6B(0, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_908)
    OP_91(0x9, 0x0, 0x186A0, 0x2710, 0x4E20, 0x0)
    OP_71(0x1, 0x4)
    OP_82(0x0, 0x0)
    OP_71(0x2, 0x4)
    OP_72(0x0, 0x4)
    SetChrPos(0x8, 0, 3000, 9500, 180)
    OP_A1(0x8, 0x0)
    OP_6F(0x0, 11)
    OP_70(0x0, 0x32)
    Play3DEffect(0x0, 0x1, 0x0, "Frame294__ball", 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x5DC, 0x0)
    Fade(500)
    OP_6D(0, 0, 9700, 0)
    OP_67(0, 9620, -10000, 0)
    OP_6B(1910, 0)
    OP_6C(0, 0)
    OP_6E(659, 0)

    def lambda_9D9():
        OP_67(0, 7490, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9D9)

    def lambda_9F1():
        OP_6B(1650, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F1)

    def lambda_A01():
        OP_6E(579, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A01)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 50)
    OP_70(0x0, 0x5A)
    Sleep(1200)
    OP_23(0x85)
    OP_23(0x156)
    OP_22(0x157, 0x0, 0x64)
    OP_73(0x0)
    WaitChrThread(0x101, 0x0)

    def lambda_A3C():
        OP_6D(0, 5170, 7290, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A3C)

    def lambda_A54():
        OP_67(0, 5870, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A54)
    OP_20(0x1388)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 91)
    OP_70(0x0, 0x82)
    OP_22(0x148, 0x0, 0x64)
    SetMessageWindowPos(170, 280, -1, -1)
    SetChrName("Weissmann's Voice")

    AnonymousTalk(    #2 op#5
        "\x07\x05#40W#3SGhh...oooOOOOAAAGGHH!!\x05\x02",
    )

    WaitChrThread(0x101, 0x0)
    OP_56(0x0)
    Sleep(100)
    Fade(500)
    OP_6D(0, 5170, 9100, 0)
    OP_67(0, 5850, -10000, 0)
    OP_6B(840, 0)
    OP_6C(0, 0)
    OP_6E(746, 0)
    OP_0D()
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 170)
    OP_70(0x0, 0xD2)
    OP_22(0x14D, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 251)
    OP_70(0x0, 0x122)
    Sleep(1000)

    def lambda_B5E():
        OP_6D(0, 7000, 12410, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B5E)

    def lambda_B76():
        OP_67(0, -3830, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B76)

    def lambda_B8E():
        OP_6B(1800, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B8E)

    def lambda_B9E():
        OP_6E(900, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B9E)
    Sleep(1000)
    PlayEffect(0x1, 0x2, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x147, 0x0, 0x64)
    OP_1D(0x39)
    WaitChrThread(0x101, 0x0)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    Sleep(2500)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    Return()

    # Function_3_193 end

    def Function_4_C05(): pass

    label("Function_4_C05")

    OP_6F(0x0, 371)
    OP_70(0x0, 0x19A)
    Play3DEffect(0x2, 0xFF, 0x0, "Frame43_hiface", 0x0, 0x0, 0xFFFFFC18, 0x0, 0x0, 0xFF97, 0x3E8, 0x3E8, 0x3E8, 0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_6D(110, 5040, 12390, 0)
    OP_67(0, 1920, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(181000, 0)
    OP_6E(804, 0)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_6D(-50, 5320, 7830, 0)
    OP_67(0, 1360, -10000, 0)
    OP_6B(1580, 0)
    OP_6C(0, 0)
    OP_6E(539, 0)

    def lambda_CF6():
        OP_6D(0, 4000, 1090, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CF6)

    def lambda_D0E():
        OP_67(0, 1330, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D0E)

    def lambda_D26():
        OP_6B(1580, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D26)

    def lambda_D36():
        OP_6E(733, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D36)
    FadeToBright(1000, 16777215)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 331)
    OP_70(0x0, 0x172)
    OP_22(0x148, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 371)
    OP_70(0x0, 0x19A)
    WaitChrThread(0x101, 0x0)

    def lambda_D82():
        OP_6B(1680, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D82)
    OP_DC()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB8")

    ChrTalk(    #3
        0x107,
        "#065FWaaaaaaah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_DDC")

    label("loc_DB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DDC")

    ChrTalk(    #4
        0x110,
        "#273FWhat in...?\x02",
    )

    CloseMessageWindow()

    label("loc_DDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E02")

    ChrTalk(    #5
        0x105,
        "#1163FA-Angel?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E5E")

    label("loc_E02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E39")

    ChrTalk(    #6
        0x10F,
        "#173FAn...angel? What has he...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_E5E")

    label("loc_E39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E5E")

    ChrTalk(    #7
        0x10B,
        "#216FAn...angel?!\x02",
    )

    CloseMessageWindow()

    label("loc_E5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E88")

    ChrTalk(    #8
        0x104,
        "#039FWhat terror...\x02",
    )

    CloseMessageWindow()
    Jump("loc_F48")

    label("loc_E88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EBC")

    ChrTalk(    #9
        0x108,
        "#077FWhat overwhelming power!\x02",
    )

    CloseMessageWindow()
    Jump("loc_F48")

    label("loc_EBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F01")

    ChrTalk(    #10
        0x103,
        (
            "#523FI can feel the power coming\x01",
            "off of it...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F48")

    label("loc_F01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F48")

    ChrTalk(    #11
        0x109,
        (
            "#1070FLike being hit in the FACE\x01",
            "with raw heresy...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F82")

    ChrTalk(    #12
        0x106,
        (
            "#054FChange all you want!\x01",
            "Bring it on!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F82")


    ChrTalk(    #13
        0x101,
        (
            "#1002F#5PLooks like he's really starting\x01",
            "to lose it.\x02\x03",

            "#1005FC'mon, guys! Take him down\x01",
            "and let's get back to Loewe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        "#1046F#2PHere we go!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    Battle(0x452, 0x300017, 0x0, 0x0, 0xFF)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_4_C05 end

    def Function_5_105D(): pass

    label("Function_5_105D")

    OP_A2(0x22B4)
    EventBegin(0x0)
    FadeToDark(0, 16777215, -1)
    OP_D2(0x270110, 0x270120, 0x0)
    OP_D2(0x270130, 0x270140, 0x1)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_10A9"),
        (5, "loc_10B6"),
        (3, "loc_10C3"),
        (4, "loc_10D0"),
        (6, "loc_10DD"),
        (7, "loc_10EA"),
        (8, "loc_10F7"),
        (10, "loc_1104"),
        (SWITCH_DEFAULT, "loc_1111"),
    )


    label("loc_10A9")

    OP_D2(0x701D0, 0x701DC, 0x2)
    Jump("loc_1111")

    label("loc_10B6")

    OP_D2(0x70218, 0x70224, 0x2)
    Jump("loc_1111")

    label("loc_10C3")

    OP_D2(0x701E8, 0x701F4, 0x2)
    Jump("loc_1111")

    label("loc_10D0")

    OP_D2(0x27036E, 0x27037B, 0x2)
    Jump("loc_1111")

    label("loc_10DD")

    OP_D2(0x70230, 0x7023C, 0x2)
    Jump("loc_1111")

    label("loc_10EA")

    OP_D2(0x70248, 0x70254, 0x2)
    Jump("loc_1111")

    label("loc_10F7")

    OP_D2(0x270176, 0x270183, 0x2)
    Jump("loc_1111")

    label("loc_1104")

    OP_D2(0x702B4, 0x702BB, 0x2)
    Jump("loc_1111")

    label("loc_1111")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_113A"),
        (5, "loc_1147"),
        (3, "loc_1154"),
        (4, "loc_1161"),
        (6, "loc_116E"),
        (7, "loc_117B"),
        (8, "loc_1188"),
        (10, "loc_1195"),
        (SWITCH_DEFAULT, "loc_11A2"),
    )


    label("loc_113A")

    OP_D2(0x701D0, 0x701DC, 0x3)
    Jump("loc_11A2")

    label("loc_1147")

    OP_D2(0x70218, 0x70224, 0x3)
    Jump("loc_11A2")

    label("loc_1154")

    OP_D2(0x701E8, 0x701F4, 0x3)
    Jump("loc_11A2")

    label("loc_1161")

    OP_D2(0x27036E, 0x27037B, 0x3)
    Jump("loc_11A2")

    label("loc_116E")

    OP_D2(0x70230, 0x7023C, 0x3)
    Jump("loc_11A2")

    label("loc_117B")

    OP_D2(0x70248, 0x70254, 0x3)
    Jump("loc_11A2")

    label("loc_1188")

    OP_D2(0x270176, 0x270183, 0x3)
    Jump("loc_11A2")

    label("loc_1195")

    OP_D2(0x702B4, 0x702BB, 0x3)
    Jump("loc_11A2")

    label("loc_11A2")

    SetChrPos(0x101, -550, 0, -500, 0)
    SetChrPos(0x102, 600, 0, -500, 0)
    SetChrPos(0xF8, -1250, 0, -1500, 0)
    SetChrPos(0xF9, 1200, 0, -1500, 0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 1)
    SetChrChipByIndex(0xF8, 2)
    SetChrChipByIndex(0xF9, 3)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_72(0x3, 0x4)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 0, 3000, 9500, 180)
    OP_A1(0x8, 0x3)
    OP_72(0x3, 0x20)
    OP_43(0x8, 0x3, 0x0, 0x7)
    OP_43(0x102, 0x3, 0x0, 0x8)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x9, 0, 3000, 9500, 180)
    OP_A1(0x9, 0x4)
    OP_71(0x4, 0x4)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 0, 5300, 7700, 180)
    OP_A1(0xA, 0x5)
    OP_71(0x5, 0x4)
    LoadEffect(0x0, "monster\\ms31000.eff")
    LoadEffect(0x1, "monster\\ms31003a.eff")
    LoadEffect(0x2, "monster\\ms30900f.eff")
    Play3DEffect(0x0, 0x0, 0x3, "Frame147_chest", 0x5DC, 0x0, 0x0, 0x0, 0x5A, 0xB4, 0x708, 0x708, 0x708, 0x0)

    def lambda_130A():

        label("loc_130A")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_130A")

    QueueWorkItem2(0x8, 0, lambda_130A)
    OP_6D(0, 3000, -4850, 0)
    OP_67(0, 190, -10000, 0)
    OP_6B(1400, 0)
    OP_6C(0, 0)
    OP_6E(660, 0)
    OP_22(0x85, 0x0, 0x64)
    FadeToBright(2000, 16777215)

    def lambda_1370():
        OP_6D(0, 4890, 9640, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1370)

    def lambda_1388():
        OP_67(0, 540, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1388)

    def lambda_13A0():
        OP_6B(1400, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13A0)

    def lambda_13B0():
        OP_6E(733, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_13B0)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    Fade(500)
    OP_6B(1200, 0)
    OP_44(0x8, 0x3)
    OP_44(0x102, 0x3)
    OP_71(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_72(0x4, 0x20)
    OP_6F(0x4, 10)
    OP_70(0x4, 0xA)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x14)
    OP_82(0x0, 0x2)
    OP_22(0x14F, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xA, 0, 0, 0, 0, 0, 0, 2300, 2300, 2300, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_1466():
        OP_6D(0, 1750, 3200, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1466)

    def lambda_147E():
        OP_67(0, -15110, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_147E)

    def lambda_1496():
        OP_6B(240, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1496)

    def lambda_14A6():
        OP_6E(700, 5000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14A6)
    PlayEffect(0x0, 0x2, 0xA, 0, -300, 0, 0, 0, 0, 2300, 2300, 2300, 0xFF, 0, 0, 0, 0)

    def lambda_14EB():
        OP_8F(0xFE, 0x0, 0x2134, 0x1E14, 0xFA, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_14EB)
    Sleep(500)

    def lambda_150B():
        OP_8F(0xFE, 0x0, 0x2134, 0x1E14, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_150B)
    Sleep(400)

    def lambda_152B():
        OP_8F(0xFE, 0x0, 0x2134, 0x1E14, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_152B)
    Sleep(300)

    def lambda_154B():
        OP_8F(0xFE, 0x0, 0x2134, 0x1E14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_154B)
    Sleep(900)

    def lambda_156B():
        OP_8F(0xFE, 0x0, 0x2134, 0x1E14, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_156B)
    Sleep(700)

    def lambda_158B():
        OP_8F(0xFE, 0x0, 0x2134, 0x1E14, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_158B)
    Sleep(500)

    def lambda_15AB():
        OP_8F(0xFE, 0x0, 0x2134, 0x1E14, 0xFA, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_15AB)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)

    def lambda_15D5():
        OP_6B(1400, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_15D5)

    def lambda_15E5():
        OP_67(0, -10110, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15E5)
    PlayEffect(0x1, 0x3, 0xA, 0, -100, 0, 0, 45, 0, 1800, 1800, 1800, 0xFF, 0, 0, 0, 0)
    OP_22(0x150, 0x0, 0x64)

    def lambda_1637():

        label("loc_1637")

        OP_7C(0x12C, 0x12C, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1637")

    QueueWorkItem2(0x8, 0, lambda_1637)
    Sleep(4000)
    OP_71(0x5, 0x4)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    Sleep(4000)
    OP_22(0x147, 0x0, 0x64)
    OP_43(0x8, 0x3, 0x0, 0x6)
    OP_20(0xBB8)
    FadeToBright(3000, 16777215)
    OP_0D()
    OP_21()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5317   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_105D end

    def Function_6_1695(): pass

    label("Function_6_1695")

    OP_24(0x85, 0x5A)
    OP_24(0x147, 0x5A)
    Sleep(400)
    OP_24(0x85, 0x50)
    OP_24(0x147, 0x50)
    Sleep(400)
    OP_24(0x85, 0x46)
    OP_24(0x147, 0x46)
    Sleep(400)
    OP_24(0x85, 0x3C)
    OP_24(0x147, 0x3C)
    Sleep(400)
    OP_24(0x85, 0x32)
    OP_24(0x147, 0x32)
    Sleep(400)
    OP_24(0x85, 0x28)
    OP_24(0x147, 0x28)
    Sleep(400)
    OP_24(0x85, 0x1E)
    OP_24(0x147, 0x1E)
    Sleep(400)
    OP_24(0x85, 0x14)
    OP_24(0x147, 0x14)
    Sleep(400)
    OP_23(0x85)
    OP_23(0x147)
    Return()

    # Function_6_1695 end

    def Function_7_1704(): pass

    label("Function_7_1704")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1725")
    OP_6F(0x3, 350)
    OP_70(0x3, 0x17C)
    OP_73(0x3)
    OP_D8(0x3, 0x1F4)
    Jump("Function_7_1704")

    label("loc_1725")

    Return()

    # Function_7_1704 end

    def Function_8_1726(): pass

    label("Function_8_1726")

    OP_22(0x148, 0x0, 0x46)
    Sleep(4000)
    OP_22(0x148, 0x0, 0x46)
    Return()

    # Function_8_1726 end

    def Function_9_1736(): pass

    label("Function_9_1736")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_17AF"),
        (1, "loc_17B5"),
        (SWITCH_DEFAULT, "loc_17BB"),
    )


    label("loc_17AF")

    OP_A2(0x1200)
    Jump("loc_17BB")

    label("loc_17B5")

    OP_A2(0x1201)
    Jump("loc_17BB")

    label("loc_17BB")

    Return()

    # Function_9_1736 end

    def Function_10_17BC(): pass

    label("Function_10_17BC")

    FadeToDark(0, 0, -1)
    OP_6D(-211220, -20490, -48190, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xE, 0xF, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_10_17BC end

    SaveToFile()

Try(main)
