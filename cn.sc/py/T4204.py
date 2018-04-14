from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4204   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4204.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '约修亚',                               # 9
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


    AddCharChip(
        'ED6_DT07/CH00010 ._CH',             # 00
        'ED6_DT06/CH20153 ._CH',             # 01
        'ED6_DT06/CH20154 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH00010P._CP',             # 00
        'ED6_DT06/CH20153P._CP',             # 01
        'ED6_DT06/CH20154P._CP',             # 02
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_E2",           # 00, 0
        "Function_1_E7",           # 01, 1
        "Function_2_E8",           # 02, 2
    )


    def Function_0_E2(): pass

    label("Function_0_E2")

    Event(0, 2)
    Return()

    # Function_0_E2 end

    def Function_1_E7(): pass

    label("Function_1_E7")

    Return()

    # Function_1_E7 end

    def Function_2_E8(): pass

    label("Function_2_E8")

    EventBegin(0x0)
    OP_77(0xFF, 0xA0, 0x46, 0x0, 0x0)
    OP_20(0x0)
    OP_6D(-42280, 16000, 81720, 0)
    OP_67(0, 5390, -10000, 0)
    OP_6B(1470, 0)
    OP_6C(45000, 0)
    OP_6E(532, 0)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -42780, 16000, 81000, 90)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x101, -41300, 16000, 81000, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 1)
    SetChrSubChip(0x101, 5)
    FadeToBright(1000, 0)
    Sleep(1250)
    OP_0D()

    ChrTalk(    #0
        0x8,
        (
            "#594F我的艾丝蒂尔……\x01",
            "如太阳般耀眼的你。\x02\x03",

            "和你在一起的时光虽然幸福\x01",
            "同时，却也非常痛苦……\x02\x03",

            "因为就像明亮的光芒会投下浓重的阴影……\x02\x03",

            "与你在一起相处得越久\x01",
            "我，也对自己令人憎恶的本性\x01",
            "认识得更加深刻……\x02\x03",

            "所以，我甚至想过，\x01",
            "要是当初没遇见你该多好啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x7, 0x9, 0x320)
    Sleep(400)

    def lambda_29C():
        OP_6D(-41280, 16000, 81720, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_29C)
    OP_8F(0x8, 0xFFFF5BF0, 0x3E80, 0x13CCC, 0x3E8, 0x0)
    SetChrChipByIndex(0x8, 2)
    SetChrFlags(0x8, 0x2)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_99(0x8, 0x0, 0x2, 0x4B0)
    Sleep(2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x101, 0x2)
    NewScene("ED6_DT21/E0001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_E8 end

    SaveToFile()

Try(main)
