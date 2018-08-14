from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5407   ._SN',
        MapName             = 'Other',
        Location            = 'C5407.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_209",          # 03, 3
        "Function_4_265",          # 04, 4
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
    OP_6D(1570, 0, 1270, 0)
    OP_67(0, 6720, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x124, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x124, 0x1, 0x0, 0x3)
    WaitChrThread(0x124, 0x1)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x5A)
    Sleep(1000)
    SetMessageWindowPos(360, 60, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #0
        (
            "\x07\x05去圣堂及机关部的\x01",
            "移动被限制了。\x02",
        )
    )

    Jump("loc_14E")

    label("loc_14E")

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("声音")

    AnonymousTalk(    #1
        "\x07\x05请接受认证检查。\x02",
    )

    Jump("loc_172")

    label("loc_172")

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #2
        0x124,
        (
            "#120F#6P是执行者Ｎｏ．Ⅱ――\x01",
            "『剑帝』莱恩哈特。\x02\x03",

            "――正向『圣堂』前去。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    SetChrName("声音")

    AnonymousTalk(    #3
        "──认证完毕。\x02",
    )

    Jump("loc_1EE")

    label("loc_1EE")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    NewScene("ED6_DT21/C5400   ._SN", 125, 0, 0)
    IdleLoop()
    Return()

    # Function_2_AC end

    def Function_3_209(): pass

    label("Function_3_209")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 340, 0, -1480, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_230():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_230)
    OP_8E(0xFE, 0x208, 0x0, 0xFFFFFFBA, 0x7D0, 0x0)
    OP_8E(0xFE, 0x672, 0x0, 0xFFFFFFBA, 0x7D0, 0x0)
    Return()

    # Function_3_209 end

    def Function_4_265(): pass

    label("Function_4_265")

    EventBegin(0x0)
    OP_6D(990, 0, 1420, 0)
    OP_67(0, 8620, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 1590, 0, -160, 90)
    SetChrPos(0x1, 830, 0, 1050, 90)
    SetChrPos(0x2, -790, 0, 1400, 90)
    SetChrPos(0x3, -580, 0, -150, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Return()

    # Function_4_265 end

    SaveToFile()

Try(main)
