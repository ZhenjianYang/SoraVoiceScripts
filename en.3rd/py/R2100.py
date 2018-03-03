from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R2100   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2100.x',
        MapIndex            = 100,
        MapDefaultBGM       = "ed60029",
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
        'Manoria Village',                      # 9
        'Krone Trail',                          # 10
        'Target Camera',                        # 11
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
        X                   = -18570,
        Z                   = -2000,
        Y                   = -37710,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 100500,
        Z                   = -2070,
        Y                   = 132300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 7120,
        Y                   = -2920,
        Z                   = 70760,
        Range               = 20700,
        Unknown_10          = 0xF50,
        Unknown_14          = 0x10748,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    ScpFunction(
        "Function_0_12A",          # 00, 0
        "Function_1_12B",          # 01, 1
        "Function_2_1C0",          # 02, 2
        "Function_3_61A",          # 03, 3
        "Function_4_686",          # 04, 4
        "Function_5_692",          # 05, 5
    )


    def Function_0_12A(): pass

    label("Function_0_12A")

    Return()

    # Function_0_12A end

    def Function_1_12B(): pass

    label("Function_1_12B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14E")
    OP_16(0x2, 0xFA0, 0xFFFE7578, 0xFFFEE6C0, 0x23002B)

    label("loc_14E")

    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1C4, 0x1, 0x64)
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BF")
    OP_71(0x0, 0x0)
    ExitThread()
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x200, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_18B")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_18B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 4)), scpexpr(EXPR_END)), "loc_1AC")
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9")
    OP_1B(0x0, 0x0, 0x4)
    OP_1B(0x1, 0x0, 0x4)

    label("loc_1A9")

    Jump("loc_1B1")

    label("loc_1AC")

    OP_1B(0x0, 0x0, 0x5)

    label("loc_1B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1BF")
    OP_A3(0x2504)
    Event(0, 3)

    label("loc_1BF")

    Return()

    # Function_1_12B end

    def Function_2_1C0(): pass

    label("Function_2_1C0")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C4(0x0, 0x20000000)
    EventBegin(0x0)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(18080, -2000, 83980, 0)
    OP_67(0, 5000, -10000, 0)
    OP_6B(3260, 0)
    OP_6C(52000, 0)
    OP_6E(272, 0)
    SetChrPos(0x14E, 17400, -2000, 83580, 0)

    def lambda_232():
        OP_6B(3060, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_232)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_8C(0x14E, 180, 400)
    OP_0D()
    OP_8C(0x14E, 270, 400)
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #0
        0x14E,
        "#3S#1717F#11PPolly! Come on out!#2S\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_8C(0x14E, 90, 500)
    Sleep(300)

    ChrTalk(    #1
        0x14E,
        "#1717F#4S#6PPolly!#2S\x02",
    )

    OP_7C(0x64, 0x64, 0xBB8, 0x12C)
    CloseMessageWindow()
    Sleep(1500)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xFA, 0x2)
    Sleep(3000)
    OP_63(0x14E)
    OP_8C(0x14E, 60, 400)
    Sleep(500)

    def lambda_2F5():
        OP_6D(21770, -2000, 85910, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_2F5)

    def lambda_30D():
        OP_67(0, 5000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_30D)

    def lambda_325():
        OP_6B(2610, 3000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_325)

    def lambda_335():
        OP_6C(97000, 3000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_335)

    def lambda_345():
        OP_8E(0xFE, 0x514A, 0xFFFFF830, 0x15086, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_345)
    WaitChrThread(0x14E, 0x1)
    WaitChrThread(0x12, 0x0)
    Sleep(300)

    ChrTalk(    #2
        0x14E,
        (
            "#1716F(I can't find her anywhere...)\x02\x03",

            "#1713F(This is all my fault for being so careless...)\x02\x03",

            "(I shouldn't have taken my eyes off her...\x01",
            "I never do this, either! So why did I do it\x01",
            "this time?!)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_8C(0x14E, 120, 400)
    Sleep(500)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #3
        0x14E,
        "#1714FW-Wait a second...\x02",
    )

    CloseMessageWindow()
    Fade(3000)

    def lambda_488():
        OP_6D(20840, -2000, 85570, 4000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_488)

    def lambda_4A0():
        OP_67(0, 7840, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4A0)

    def lambda_4B8():
        OP_6B(2540, 4000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_4B8)

    def lambda_4C8():
        OP_6C(183000, 4000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_4C8)

    def lambda_4D8():
        OP_6E(221, 4000)
        ExitThread()

    QueueWorkItem(0x14E, 0, lambda_4D8)
    Sleep(3000)
    OP_8C(0x14E, 160, 500)
    Sleep(500)
    OP_8C(0x14E, 0, 500)
    Sleep(900)
    OP_8C(0x14E, 180, 500)
    Sleep(500)
    OP_8C(0x14E, 45, 500)
    WaitChrThread(0x12, 0x3)

    ChrTalk(    #4
        0x14E,
        "#1714F(...Is this the right way?)\x02",
    )

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)
    OP_8C(0x14E, 135, 500)
    Sleep(500)
    OP_8C(0x14E, 45, 500)
    Sleep(1000)
    OP_8C(0x14E, 225, 400)
    Sleep(500)

    ChrTalk(    #5
        0x14E,
        "#1900F(Wh-Which way did I come from again?)\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_5BD():
        OP_6D(19460, -2000, 84430, 5000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_5BD)

    def lambda_5D5():
        OP_8E(0xFE, 0x31BA, 0xFFFFF876, 0x12CF0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_5D5)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x14E, 0x1)
    OP_44(0x14E, 0x0)
    OP_A2(0x2F24)
    OP_20(0x7D0)
    OP_21()
    Sleep(1000)
    NewScene("ED6_DT21/C1500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1C0 end

    def Function_3_61A(): pass

    label("Function_3_61A")

    EventBegin(0x2)
    FadeToDark(0, 0, -1)
    OP_6D(20810, -2000, 86150, 0)
    OP_67(0, 9100, -10000, 0)
    OP_6B(2260, 0)
    OP_6C(232000, 0)
    OP_6E(190, 0)
    SetChrPos(0x14E, 20810, -2000, 86150, 90)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x2)
    Return()

    # Function_3_61A end

    def Function_4_686(): pass

    label("Function_4_686")

    EventBegin(0x1)
    NewScene("ED6_DT21/C1500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_686 end

    def Function_5_692(): pass

    label("Function_5_692")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_702")

    ChrTalk(    #6
        0x14E,
        (
            "#1715F...Huh? How did I end up coming all the way out\x01",
            "here? I've got to head back to Manoria! \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76F")

    label("loc_702")


    ChrTalk(    #7
        0x14E,
        (
            "#1714F...Huh? How did I end up coming all the way out\x01",
            "here?\x02\x03",

            "#1712FI've got to head back to Manoria!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_76F")

    OP_59()
    Fade(1000)
    SetChrPos(0x14E, 88160, -2009, 132000, 270)
    SetChrPos(0x14F, 88160, -2009, 132000, 270)
    OP_6D(87080, -2009, 132000, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_5_692 end

    SaveToFile()

Try(main)
