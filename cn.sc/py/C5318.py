from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '怀斯曼教授',                           # 9
        '格里德',                               # 10
        '核心用目标角色',                       # 11
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
        "Function_3_18F",          # 03, 3
        "Function_4_F2D",          # 04, 4
        "Function_5_1565",         # 05, 5
        "Function_6_15D4",         # 06, 6
        "Function_7_15F6",         # 07, 7
        "Function_8_1606",         # 08, 8
        "Function_9_168D",         # 09, 9
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

    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x112), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x0)
    OP_C4(0x0, 0x10)
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C4(0x1, 0x10)
    OP_A3(0x0)
    Call(0, 3)
    Call(0, 4)
    Return()

    # Function_2_149 end

    def Function_3_18F(): pass

    label("Function_3_18F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A6")
    Call(0, 8)
    Call(0, 9)

    label("loc_1A6")

    OP_D2(0x270110, 0x270120, 0x0)
    OP_D2(0x270130, 0x270140, 0x1)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_1E3"),
        (5, "loc_1F0"),
        (3, "loc_1FD"),
        (4, "loc_20A"),
        (6, "loc_217"),
        (7, "loc_224"),
        (8, "loc_231"),
        (10, "loc_23E"),
        (SWITCH_DEFAULT, "loc_24B"),
    )


    label("loc_1E3")

    OP_D2(0x701D0, 0x701DC, 0x2)
    Jump("loc_24B")

    label("loc_1F0")

    OP_D2(0x70218, 0x70224, 0x2)
    Jump("loc_24B")

    label("loc_1FD")

    OP_D2(0x701E8, 0x701F4, 0x2)
    Jump("loc_24B")

    label("loc_20A")

    OP_D2(0x27036E, 0x27037B, 0x2)
    Jump("loc_24B")

    label("loc_217")

    OP_D2(0x70230, 0x7023C, 0x2)
    Jump("loc_24B")

    label("loc_224")

    OP_D2(0x70248, 0x70254, 0x2)
    Jump("loc_24B")

    label("loc_231")

    OP_D2(0x270176, 0x270183, 0x2)
    Jump("loc_24B")

    label("loc_23E")

    OP_D2(0x702B4, 0x702BB, 0x2)
    Jump("loc_24B")

    label("loc_24B")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_274"),
        (5, "loc_281"),
        (3, "loc_28E"),
        (4, "loc_29B"),
        (6, "loc_2A8"),
        (7, "loc_2B5"),
        (8, "loc_2C2"),
        (10, "loc_2CF"),
        (SWITCH_DEFAULT, "loc_2DC"),
    )


    label("loc_274")

    OP_D2(0x701D0, 0x701DC, 0x3)
    Jump("loc_2DC")

    label("loc_281")

    OP_D2(0x70218, 0x70224, 0x3)
    Jump("loc_2DC")

    label("loc_28E")

    OP_D2(0x701E8, 0x701F4, 0x3)
    Jump("loc_2DC")

    label("loc_29B")

    OP_D2(0x27036E, 0x27037B, 0x3)
    Jump("loc_2DC")

    label("loc_2A8")

    OP_D2(0x70230, 0x7023C, 0x3)
    Jump("loc_2DC")

    label("loc_2B5")

    OP_D2(0x70248, 0x70254, 0x3)
    Jump("loc_2DC")

    label("loc_2C2")

    OP_D2(0x270176, 0x270183, 0x3)
    Jump("loc_2DC")

    label("loc_2CF")

    OP_D2(0x702B4, 0x702BB, 0x3)
    Jump("loc_2DC")

    label("loc_2DC")

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
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    OP_6B(1800, 3000)
    OP_0D()
    SetMessageWindowPos(100, 190, -1, -1)
    SetChrName("怀斯曼的声音")

    AnonymousTalk(    #0
        (
            "\x07\x05竟然能纠缠到这种地步……\x02\x03",

            "但终究……\x01",
            "也只是徒劳的挣扎而已。\x02\x03",

            "在隐藏了无限力量的『环』面前──\x02",
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

    def lambda_48F():
        OP_6B(3450, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_48F)
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
    SetChrName("怀斯曼的声音")

    AnonymousTalk(    #1
        (
            "\x07\x05怎、怎么……\x02\x03",

            "『环』……\x01",
            "……我体内的『环』……！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
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

    def lambda_66D():
        OP_6B(0, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_66D)
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

    def lambda_72F():
        OP_6B(1500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_72F)

    def lambda_73F():
        OP_6E(644, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_73F)
    WaitChrThread(0x101, 0x0)
    OP_B0(0x1, 0x1E)

    def lambda_758():
        OP_8F(0xFE, 0x0, 0x7530, 0x251C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_758)
    Sleep(500)

    def lambda_778():
        OP_8F(0xFE, 0x0, 0x7530, 0x251C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_778)
    Sleep(400)

    def lambda_798():
        OP_8F(0xFE, 0x0, 0x7530, 0x251C, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_798)
    Sleep(300)

    def lambda_7B8():
        OP_8F(0xFE, 0x0, 0x7530, 0x251C, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7B8)
    Sleep(200)

    def lambda_7D8():
        OP_8F(0xFE, 0x0, 0x7530, 0x251C, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7D8)
    Sleep(100)

    def lambda_7F8():
        OP_8F(0xFE, 0x0, 0x7530, 0x251C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7F8)
    WaitChrThread(0x9, 0x0)
    Fade(500)
    OP_6D(0, -60400, 12450, 0)
    OP_67(0, 40270, -10000, 0)
    OP_6B(590, 0)
    OP_6C(0, 0)
    OP_6E(733, 0)
    SetChrPos(0x9, 0, -100000, 7500, 180)
    OP_B0(0x1, 0x28)

    def lambda_86F():
        OP_6B(0, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_86F)
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

    def lambda_940():
        OP_67(0, 7490, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_940)

    def lambda_958():
        OP_6B(1650, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_958)

    def lambda_968():
        OP_6E(579, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_968)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 50)
    OP_70(0x0, 0x5A)
    Sleep(1200)
    OP_23(0x85)
    OP_23(0x156)
    OP_22(0x157, 0x0, 0x64)
    OP_73(0x0)
    WaitChrThread(0x101, 0x0)

    def lambda_9A3():
        OP_6D(0, 5170, 7290, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9A3)

    def lambda_9BB():
        OP_67(0, 5870, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9BB)
    OP_20(0x1388)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 91)
    OP_70(0x0, 0x82)
    OP_22(0x148, 0x0, 0x64)
    SetMessageWindowPos(170, 280, -1, -1)
    SetChrName("怀斯曼的声音")

    AnonymousTalk(    #2 op#5
        (
            "\x07\x05#40W#3S呜……\x01",
            "……啊啊啊啊啊啊啊啊……！\x05\x02",
        )
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

    def lambda_ACB():
        OP_6D(0, 7000, 12410, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_ACB)

    def lambda_AE3():
        OP_67(0, -3830, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE3)

    def lambda_AFB():
        OP_6B(1800, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AFB)

    def lambda_B0B():
        OP_6E(900, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B0B)
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
    OP_6F(0x0, 371)
    OP_70(0x0, 0x19A)
    Play3DEffect(0x2, 0xFF, 0x0, "Frame43_hiface", 0x0, 0x0, 0xFFFFFC18, 0x0, 0x0, 0xFF97, 0x3E8, 0x3E8, 0x3E8, 0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0xF8, 0x80)
    ClearChrFlags(0xF9, 0x80)
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

    def lambda_C62():
        OP_6D(0, 4000, 1090, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C62)

    def lambda_C7A():
        OP_67(0, 1330, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C7A)

    def lambda_C92():
        OP_6B(1580, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C92)

    def lambda_CA2():
        OP_6E(733, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_CA2)
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

    def lambda_CEE():
        OP_6B(1680, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CEE)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D27")

    ChrTalk(    #3
        0x107,
        "#065F#5P哎呀呀呀……！\x02",
    )

    CloseMessageWindow()

    label("loc_D27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D57")

    ChrTalk(    #4
        0x105,
        "#1163F#5P天、天使……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_D83")

    label("loc_D57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D83")

    ChrTalk(    #5
        0x10B,
        "#216F#5P天、天使……！？\x02",
    )

    CloseMessageWindow()

    label("loc_D83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DBB")

    ChrTalk(    #6
        0x104,
        (
            "#039F#5P唔……\x01",
            "好强大的灵压啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E61")

    label("loc_DBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF1")

    ChrTalk(    #7
        0x108,
        (
            "#077F#5P唔……\x01",
            "好强的灵压啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E61")

    label("loc_DF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E2A")

    ChrTalk(    #8
        0x103,
        "#523F#5P唔……这是什么灵压啊……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_E61")

    label("loc_E2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E61")

    ChrTalk(    #9
        0x109,
        "#1070F#5P唔……好惊人的灵压啊……！\x02",
    )

    CloseMessageWindow()

    label("loc_E61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E8F")

    ChrTalk(    #10
        0x106,
        "#054F#5P嘿……这样才对！！\x02",
    )

    CloseMessageWindow()

    label("loc_E8F")


    ChrTalk(    #11
        0x101,
        (
            "#1002F#5P看来这是最后的\x01",
            "捶死挣扎了……\x02\x03",

            "#1005F赶快打倒它，\x01",
            "然后回到莱维身边！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        "#1046F#5P嗯……！\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    Battle(0x452, 0x300017, 0x0, 0x0, 0xFF)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_3_18F end

    def Function_4_F2D(): pass

    label("Function_4_F2D")

    OP_A2(0x22B4)
    EventBegin(0x0)
    FadeToDark(0, 16777215, -1)
    OP_D2(0x270110, 0x270120, 0x0)
    OP_D2(0x270130, 0x270140, 0x1)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_F79"),
        (5, "loc_F86"),
        (3, "loc_F93"),
        (4, "loc_FA0"),
        (6, "loc_FAD"),
        (7, "loc_FBA"),
        (8, "loc_FC7"),
        (10, "loc_FD4"),
        (SWITCH_DEFAULT, "loc_FE1"),
    )


    label("loc_F79")

    OP_D2(0x701D0, 0x701DC, 0x2)
    Jump("loc_FE1")

    label("loc_F86")

    OP_D2(0x70218, 0x70224, 0x2)
    Jump("loc_FE1")

    label("loc_F93")

    OP_D2(0x701E8, 0x701F4, 0x2)
    Jump("loc_FE1")

    label("loc_FA0")

    OP_D2(0x27036E, 0x27037B, 0x2)
    Jump("loc_FE1")

    label("loc_FAD")

    OP_D2(0x70230, 0x7023C, 0x2)
    Jump("loc_FE1")

    label("loc_FBA")

    OP_D2(0x70248, 0x70254, 0x2)
    Jump("loc_FE1")

    label("loc_FC7")

    OP_D2(0x270176, 0x270183, 0x2)
    Jump("loc_FE1")

    label("loc_FD4")

    OP_D2(0x702B4, 0x702BB, 0x2)
    Jump("loc_FE1")

    label("loc_FE1")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_100A"),
        (5, "loc_1017"),
        (3, "loc_1024"),
        (4, "loc_1031"),
        (6, "loc_103E"),
        (7, "loc_104B"),
        (8, "loc_1058"),
        (10, "loc_1065"),
        (SWITCH_DEFAULT, "loc_1072"),
    )


    label("loc_100A")

    OP_D2(0x701D0, 0x701DC, 0x3)
    Jump("loc_1072")

    label("loc_1017")

    OP_D2(0x70218, 0x70224, 0x3)
    Jump("loc_1072")

    label("loc_1024")

    OP_D2(0x701E8, 0x701F4, 0x3)
    Jump("loc_1072")

    label("loc_1031")

    OP_D2(0x27036E, 0x27037B, 0x3)
    Jump("loc_1072")

    label("loc_103E")

    OP_D2(0x70230, 0x7023C, 0x3)
    Jump("loc_1072")

    label("loc_104B")

    OP_D2(0x70248, 0x70254, 0x3)
    Jump("loc_1072")

    label("loc_1058")

    OP_D2(0x270176, 0x270183, 0x3)
    Jump("loc_1072")

    label("loc_1065")

    OP_D2(0x702B4, 0x702BB, 0x3)
    Jump("loc_1072")

    label("loc_1072")

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
    OP_43(0x8, 0x3, 0x0, 0x6)
    OP_43(0x102, 0x3, 0x0, 0x7)
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

    def lambda_11DA():

        label("loc_11DA")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_11DA")

    QueueWorkItem2(0x8, 0, lambda_11DA)
    OP_6D(0, 3000, -4850, 0)
    OP_67(0, 190, -10000, 0)
    OP_6B(1400, 0)
    OP_6C(0, 0)
    OP_6E(660, 0)
    OP_22(0x85, 0x0, 0x64)
    FadeToBright(2000, 16777215)

    def lambda_1240():
        OP_6D(0, 4890, 9640, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1240)

    def lambda_1258():
        OP_67(0, 540, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1258)

    def lambda_1270():
        OP_6B(1400, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1270)

    def lambda_1280():
        OP_6E(733, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1280)
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

    def lambda_1336():
        OP_6D(0, 1750, 3200, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1336)

    def lambda_134E():
        OP_67(0, -15110, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_134E)

    def lambda_1366():
        OP_6B(240, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1366)

    def lambda_1376():
        OP_6E(700, 5000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1376)
    PlayEffect(0x0, 0x2, 0xA, 0, -300, 0, 0, 0, 0, 2300, 2300, 2300, 0xFF, 0, 0, 0, 0)

    def lambda_13BB():
        OP_8F(0xFE, 0x0, 0x2134, 0x1E14, 0xFA, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_13BB)
    Sleep(500)

    def lambda_13DB():
        OP_8F(0xFE, 0x0, 0x2134, 0x1E14, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_13DB)
    Sleep(400)

    def lambda_13FB():
        OP_8F(0xFE, 0x0, 0x2134, 0x1E14, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_13FB)
    Sleep(300)

    def lambda_141B():
        OP_8F(0xFE, 0x0, 0x2134, 0x1E14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_141B)
    Sleep(900)

    def lambda_143B():
        OP_8F(0xFE, 0x0, 0x2134, 0x1E14, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_143B)
    Sleep(700)

    def lambda_145B():
        OP_8F(0xFE, 0x0, 0x2134, 0x1E14, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_145B)
    Sleep(500)

    def lambda_147B():
        OP_8F(0xFE, 0x0, 0x2134, 0x1E14, 0xFA, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_147B)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)

    def lambda_14A5():
        OP_6B(1400, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14A5)

    def lambda_14B5():
        OP_67(0, -10110, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14B5)
    PlayEffect(0x1, 0x3, 0xA, 0, -100, 0, 0, 45, 0, 1800, 1800, 1800, 0xFF, 0, 0, 0, 0)
    OP_22(0x150, 0x0, 0x64)

    def lambda_1507():

        label("loc_1507")

        OP_7C(0x12C, 0x12C, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1507")

    QueueWorkItem2(0x8, 0, lambda_1507)
    Sleep(4000)
    OP_71(0x5, 0x4)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    Sleep(4000)
    OP_22(0x147, 0x0, 0x64)
    OP_43(0x8, 0x3, 0x0, 0x5)
    OP_20(0xBB8)
    FadeToBright(3000, 16777215)
    OP_0D()
    OP_21()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5317   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_F2D end

    def Function_5_1565(): pass

    label("Function_5_1565")

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

    # Function_5_1565 end

    def Function_6_15D4(): pass

    label("Function_6_15D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15F5")
    OP_6F(0x3, 350)
    OP_70(0x3, 0x17C)
    OP_73(0x3)
    OP_D8(0x3, 0x1F4)
    Jump("Function_6_15D4")

    label("loc_15F5")

    Return()

    # Function_6_15D4 end

    def Function_7_15F6(): pass

    label("Function_7_15F6")

    OP_22(0x148, 0x0, 0x46)
    Sleep(4000)
    OP_22(0x148, 0x0, 0x46)
    Return()

    # Function_7_15F6 end

    def Function_8_1606(): pass

    label("Function_8_1606")

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
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1680"),
        (1, "loc_1686"),
        (SWITCH_DEFAULT, "loc_168C"),
    )


    label("loc_1680")

    OP_A2(0x1200)
    Jump("loc_168C")

    label("loc_1686")

    OP_A2(0x1201)
    Jump("loc_168C")

    label("loc_168C")

    Return()

    # Function_8_1606 end

    def Function_9_168D(): pass

    label("Function_9_168D")

    FadeToDark(0, 0, -1)
    OP_6D(-211220, -20490, -48190, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_9_168D end

    SaveToFile()

Try(main)
