from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7499   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7499.x',
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
        'Anima Mundi',                          # 9
        'Stigma',                               # 10
        'Dummy Camera',                         # 11
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
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
        NpcIndex            = 0x1C4,
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
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_10A",          # 00, 0
        "Function_1_11E",          # 01, 1
        "Function_2_11F",          # 02, 2
        "Function_3_9D2",          # 03, 3
        "Function_4_A2B",          # 04, 4
        "Function_5_A42",          # 05, 5
        "Function_6_A5E",          # 06, 6
        "Function_7_A7A",          # 07, 7
        "Function_8_A91",          # 08, 8
        "Function_9_AA8",          # 09, 9
    )


    def Function_0_10A(): pass

    label("Function_0_10A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_11D")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_11D")

    Return()

    # Function_0_10A end

    def Function_1_11E(): pass

    label("Function_1_11E")

    Return()

    # Function_1_11E end

    def Function_2_11F(): pass

    label("Function_2_11F")

    EventBegin(0x0)
    FadeToDark(0, 16777215, -1)
    OP_20(0x0)
    LoadEffect(0x0, "map\\mp282_05.eff")
    LoadEffect(0x1, "map\\mp282_07.eff")
    LoadEffect(0x2, "map\\mp282_08.eff")
    LoadEffect(0x3, "map\\mp282_09.eff")
    LoadEffect(0x4, "map\\mp121_00.eff")
    LoadEffect(0x5, "map\\mp252_05.eff")
    OP_E0(250, 0x40, 0x2)
    OP_E0(250, 0x41, 0x3)
    OP_E0(251, 0x42, 0x2)
    OP_E0(251, 0x43, 0x3)
    OP_E0(252, 0x44, 0x2)
    OP_E0(252, 0x45, 0x3)
    OP_E0(253, 0x46, 0x2)
    OP_E0(253, 0x47, 0x3)
    SetChrPos(0xFA, -790, 0, 860, 0)
    SetChrPos(0xFB, 660, 0, 800, 0)
    SetChrPos(0xFC, -1420, 0, -890, 0)
    SetChrPos(0xFD, 1370, 0, -1080, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_A1(0x10, 0x0)
    SetChrPos(0x10, 0, 6000, 13000, 180)
    OP_72(0x400, 0x0)
    ExitThread()
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_B0(0x0, 0x14)
    OP_6F(0x0, 172)
    OP_70(0x0, 0xD2)
    OP_A1(0x11, 0x1)
    SetChrPos(0x11, 0, 8000, 16000, 180)
    OP_72(0x401, 0x0)
    ExitThread()
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_B0(0x1, 0x14)
    OP_6F(0x1, 30)
    OP_70(0x1, 0x1E)
    PlayEffect(0x0, 0x0, 0x10, 0, 2000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_43(0x10, 0x3, 0x0, 0x4)
    OP_22(0x32E, 0x1, 0x64)
    OP_22(0x2F2, 0x1, 0x64)
    OP_22(0x137, 0x1, 0x64)
    OP_22(0x85, 0x0, 0x64)

    def lambda_2E5():

        label("loc_2E5")

        OP_7C(0x96, 0x96, 0xBB8, 0x64)
        OP_48()
        Jump("loc_2E5")

    QueueWorkItem2(0x11, 3, lambda_2E5)
    OP_6D(4090, 5000, 9950, 0)
    OP_67(0, -4000, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(315000, 0)
    OP_6E(670, 0)
    FadeToBright(2000, 16777215)

    def lambda_346():
        OP_6D(3090, 10000, 9950, 3500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_346)

    def lambda_35E():
        OP_67(0, 1880, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_35E)

    def lambda_376():
        OP_6B(1600, 3500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_376)

    def lambda_386():
        OP_6C(329000, 3500)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_386)

    def lambda_396():
        OP_6E(630, 3500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_396)
    OP_43(0x10, 0x2, 0x0, 0x7)
    Sleep(1500)
    OP_43(0x10, 0x2, 0x0, 0x8)
    Sleep(1000)
    OP_43(0x10, 0x3, 0x0, 0x5)
    Sleep(500)
    Fade(500)
    OP_44(0x12, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x2)
    OP_44(0x12, 0x3)
    OP_44(0x12, 0x0)
    OP_6D(1110, 10150, 16510, 0)
    OP_67(0, -2600, -10000, 0)
    OP_6B(1500, 0)
    OP_6C(33000, 0)
    OP_6E(700, 0)

    def lambda_420():
        OP_6B(1700, 3000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_420)

    def lambda_430():
        OP_6E(950, 3000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_430)
    Sleep(500)
    PlayEffect(0x1, 0x1, 0x10, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x10, 0x2, 0x0, 0x8)
    Sleep(2000)
    OP_43(0x10, 0x3, 0x0, 0x6)
    Fade(500)
    OP_44(0x12, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x2)
    OP_44(0x12, 0x3)
    OP_6D(0, 5500, 3930, 0)
    OP_67(0, -3490, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(0, 0)
    OP_6E(800, 0)

    def lambda_4DF():
        OP_6D(0, 7000, 3930, 6000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_4DF)

    def lambda_4F7():
        OP_67(0, -2000, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4F7)

    def lambda_50F():
        OP_6B(1000, 6000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_50F)

    def lambda_51F():
        OP_6E(450, 6000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_51F)
    OP_22(0x27C, 0x0, 0x64)
    Sleep(2300)
    Sleep(2000)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_D8(0x0, 0x5DC)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 461)
    OP_70(0x0, 0x1E0)
    OP_44(0x10, 0x3)
    OP_44(0x10, 0x2)
    Sleep(300)
    PlayEffect(0x2, 0x2, 0x10, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0x10, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x10, 0, -1000, 0, 0, 45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x10, 0, 0, 0, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x374, 0x0, 0x64)
    OP_22(0x36F, 0x0, 0x64)
    OP_22(0x309, 0x0, 0x64)
    OP_82(0x0, 0x2)
    OP_44(0x10, 0x3)
    OP_44(0x10, 0x2)
    OP_23(0x32E)
    OP_23(0x2F2)
    OP_23(0x137)
    OP_22(0x14F, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_676():
        OP_6D(0, 8700, 3930, 4000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_676)

    def lambda_68E():
        OP_67(0, 500, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_68E)

    def lambda_6A6():
        OP_6B(3200, 4000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_6A6)

    def lambda_6B6():
        OP_6E(600, 4000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_6B6)
    Sleep(200)
    OP_22(0x27B, 0x0, 0x64)
    OP_22(0x278, 0x0, 0x64)
    Sleep(700)
    Fade(2000)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_23(0x85)
    OP_44(0x11, 0x3)
    OP_0D()

    def lambda_6ED():
        OP_6B(3400, 6000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_6ED)

    def lambda_6FD():
        OP_6E(590, 6000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_6FD)
    Sleep(5000)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x12, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x2)
    OP_44(0x12, 0x3)
    OP_6D(0, 4500, 3930, 0)
    OP_67(0, 2770, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(0, 0)
    OP_6E(557, 0)
    SetChrPos(0x11, 0, 5000, 16000, 180)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_0D()
    Sleep(1000)
    OP_22(0xD7, 0x0, 0x64)
    Fade(1000)
    OP_E5(0x0, 0x1, 0x0, 262144)
    OP_E5(0x0, 0x1, 0x1, 262144)
    OP_E5(0x0, 0x1, 0x2, 262144)
    OP_E5(0x0, 0x1, 0x3, 262144)
    OP_E5(0x0, 0x1, 0x4, 262144)
    OP_E5(0x0, 0x1, 0x5, 262144)
    OP_E5(0x0, 0x1, 0x6, 262144)
    OP_E5(0x2, 0x1, 0x0, 1000)
    OP_E5(0x2, 0x1, 0x1, 1000)
    OP_E5(0x2, 0x1, 0x2, 1000)
    OP_E5(0x2, 0x1, 0x3, 1000)
    OP_E5(0x2, 0x1, 0x4, 1000)
    OP_E5(0x2, 0x1, 0x5, 1000)
    OP_E5(0x2, 0x1, 0x6, 1000)
    OP_0D()
    Sleep(2000)
    OP_22(0x1BF, 0x0, 0x64)
    Fade(2000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_82B():
        OP_6D(0, 5000, 3930, 1000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_82B)

    def lambda_843():
        OP_67(0, 2300, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_843)

    def lambda_85B():
        OP_6B(2800, 1000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_85B)
    PlayEffect(0x4, 0x0, 0x11, 0, -1000, 0, 0, 0, 0, 1900, 1900, 1900, 0xFF, 0, 0, 0, 0)
    OP_71(0x401, 0x0)
    ExitThread()
    OP_0D()
    Sleep(300)

    ChrTalk(    #0
        0x109,
        "#1079F#5POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10F,
        "#1952F#5PIts color changed...\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_8EC():
        OP_6D(0, 6800, 3930, 8000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_8EC)

    def lambda_904():
        OP_67(0, 0, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_904)

    def lambda_91C():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_91C)

    def lambda_92C():
        OP_6E(600, 8000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_92C)
    Sleep(2000)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(4000)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_44(0x12, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x2)
    OP_44(0x12, 0x3)
    OP_C4(0x0, 0x10)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    Sleep(2000)
    OP_43(0x10, 0x3, 0x0, 0x3)
    OP_AD(0x240184, 0x0, 0x0, 0x5DC)
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_A2(0x2506)
    NewScene("ED6_DT21/M5415   ._SN", 100, 20, 0)
    IdleLoop()
    Return()

    # Function_2_11F end

    def Function_3_9D2(): pass

    label("Function_3_9D2")

    OP_24(0x147, 0x5A)
    Sleep(200)
    OP_24(0x147, 0x50)
    Sleep(200)
    OP_24(0x147, 0x46)
    Sleep(200)
    OP_24(0x147, 0x3C)
    Sleep(200)
    OP_24(0x147, 0x32)
    Sleep(200)
    OP_24(0x147, 0x28)
    Sleep(200)
    OP_24(0x147, 0x1E)
    Sleep(200)
    OP_24(0x147, 0x14)
    Sleep(200)
    OP_24(0x147, 0xA)
    Sleep(200)
    OP_24(0x147, 0x0)
    OP_23(0x147)
    Return()

    # Function_3_9D2 end

    def Function_4_A2B(): pass

    label("Function_4_A2B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A41")
    OP_22(0x26D, 0x0, 0x46)
    Sleep(400)
    Jump("Function_4_A2B")

    label("loc_A41")

    Return()

    # Function_4_A2B end

    def Function_5_A42(): pass

    label("Function_5_A42")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A5D")
    OP_22(0x237, 0x0, 0x50)
    OP_22(0x26D, 0x0, 0x50)
    Sleep(300)
    Jump("Function_5_A42")

    label("loc_A5D")

    Return()

    # Function_5_A42 end

    def Function_6_A5E(): pass

    label("Function_6_A5E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A79")
    OP_22(0x237, 0x0, 0x5A)
    OP_22(0x26D, 0x0, 0x5A)
    Sleep(230)
    Jump("Function_6_A5E")

    label("loc_A79")

    Return()

    # Function_6_A5E end

    def Function_7_A7A(): pass

    label("Function_7_A7A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A90")
    OP_22(0x376, 0x0, 0x3C)
    Sleep(500)
    Jump("Function_7_A7A")

    label("loc_A90")

    Return()

    # Function_7_A7A end

    def Function_8_A91(): pass

    label("Function_8_A91")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AA7")
    OP_22(0x376, 0x0, 0x46)
    Sleep(400)
    Jump("Function_8_A91")

    label("loc_AA7")

    Return()

    # Function_8_A91 end

    def Function_9_AA8(): pass

    label("Function_9_AA8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ABE")
    OP_22(0x148, 0x0, 0x64)
    Sleep(2500)
    Jump("Function_9_AA8")

    label("loc_ABE")

    Return()

    # Function_9_AA8 end

    SaveToFile()

Try(main)
