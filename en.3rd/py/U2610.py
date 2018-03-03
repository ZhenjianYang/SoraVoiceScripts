from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U2610   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U2610.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60231",
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
        'Butler Phillip',                       # 9
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
        'ED6_DT07/CH02470 ._CH',             # 00
        'ED6_DT26/CH20714 ._CH',             # 01
        'ED6_DT27/CH04410 ._CH',             # 02
        'ED6_DT27/CH04411 ._CH',             # 03
        'ED6_DT27/CH04414 ._CH',             # 04
        'ED6_DT27/CH04419 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02470P._CP',             # 00
        'ED6_DT26/CH20714P._CP',             # 01
        'ED6_DT27/CH04410P._CP',             # 02
        'ED6_DT27/CH04411P._CP',             # 03
        'ED6_DT27/CH04414P._CP',             # 04
        'ED6_DT27/CH04419P._CP',             # 05
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


    DeclActor(
        TriggerX            = -80200,
        TriggerZ            = 300,
        TriggerY            = 32200,
        TriggerRange        = 1000,
        ActorX              = -80200,
        ActorZ              = 1300,
        ActorY              = 32200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_11E",          # 00, 0
        "Function_1_150",          # 01, 1
        "Function_2_16A",          # 02, 2
        "Function_3_301",          # 03, 3
        "Function_4_30A",          # 04, 4
        "Function_5_1980",         # 05, 5
        "Function_6_2148",         # 06, 6
        "Function_7_2207",         # 07, 7
    )


    def Function_0_11E(): pass

    label("Function_0_11E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_136")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    Event(0, 7)
    Jump("loc_14F")

    label("loc_136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_14F")

    Return()

    # Function_0_11E end

    def Function_1_150(): pass

    label("Function_1_150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_162")
    OP_6F(0xB, 0)
    Jump("loc_169")

    label("loc_162")

    OP_6F(0xB, 60)

    label("loc_169")

    Return()

    # Function_1_150 end

    def Function_2_16A(): pass

    label("Function_2_16A")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x1E)
    OP_73(0xB)
    OP_6F(0xB, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0xC8)
    AddSepith(0x1, 0xC8)
    AddSepith(0x2, 0xC8)
    AddSepith(0x3, 0xC8)
    AddSepith(0x4, 0xC8)
    AddSepith(0x5, 0xC8)
    AddSepith(0x6, 0xC8)

    AnonymousTalk(    #0
        (
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x200\x01",
            "#57IWater Sepith x200\x01",
            "#58IFire Sepith x200\x01",
            "#59IWind Sepith x200\x01",
            "#62ITime Sepith x200\x01",
            "#60ISpace Sepith x200\x01",
            "#61IMirage Sepith x200.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BAB)
    Jump("loc_2EA")

    label("loc_27A")


    AnonymousTalk(    #1
        (
            "\x07\x05The words 'Renne,' 'Rend,' and 'End' combine to make...what, exactly?\x01",
            "Be sure to keep this hint in mind.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2EA")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xF4, 0x0)
    Return()

    # Function_2_16A end

    def Function_3_301(): pass

    label("Function_3_301")

    Call(0, 4)
    Call(0, 5)
    Return()

    # Function_3_301 end

    def Function_4_30A(): pass

    label("Function_4_30A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x7D0)
    OP_E0(238, 0x46, 0x2)
    OP_E0(238, 0x47, 0x3)
    OP_E0(239, 0x48, 0x2)
    OP_E0(239, 0x49, 0x3)
    OP_E0(240, 0x4A, 0x2)
    OP_E0(240, 0x4B, 0x3)
    OP_E0(241, 0x4C, 0x2)
    OP_E0(241, 0x4D, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 2000, 24770, 180)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x109, -970, 0, 3040, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C2")
    SetChrPos(0xEF, 570, 0, 2840, 0)
    SetChrPos(0xF0, -1170, 0, 1320, 0)
    SetChrPos(0xF1, 590, 0, 1090, 0)
    Jump("loc_447")

    label("loc_3C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_406")
    SetChrPos(0xF0, 570, 0, 2840, 0)
    SetChrPos(0xEF, -1170, 0, 1320, 0)
    SetChrPos(0xF1, 590, 0, 1090, 0)
    Jump("loc_447")

    label("loc_406")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_447")
    SetChrPos(0xF1, 570, 0, 2840, 0)
    SetChrPos(0xEF, -1170, 0, 1320, 0)
    SetChrPos(0xF0, 590, 0, 1090, 0)

    label("loc_447")

    OP_6D(920, 0, 3200, 0)
    OP_67(0, 6880, -10000, 0)
    OP_6B(2340, 0)
    OP_6C(45000, 0)
    OP_6E(304, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #2
        0x10,
        "Man's Voice",
        "#4PI have been anticipating your arrival.\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50D")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_574")

    label("loc_50D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_535")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_574")

    label("loc_535")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55D")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_574")

    label("loc_55D")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_574")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A1")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_608")

    label("loc_5A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C9")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_608")

    label("loc_5C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F1")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_608")

    label("loc_5F1")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_608")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_635")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_69C")

    label("loc_635")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65D")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_69C")

    label("loc_65D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_685")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_69C")

    label("loc_685")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_69C")

    Sleep(1000)

    def lambda_6A7():
        OP_6D(860, 2000, 25480, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6A7)

    def lambda_6BF():
        OP_67(0, 5630, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6BF)

    def lambda_6D7():
        OP_6B(2770, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6D7)

    def lambda_6E7():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6E7)

    def lambda_6F7():
        OP_6E(256, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_6F7)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #3
        0x109,
        "#1064F#1PWhat the...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x105,
        "#1164F#1PPh-Phillip?!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(1910, 50, 21210, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(2470, 0)
    OP_6C(45000, 0)
    OP_6E(395, 0)
    SetChrPos(0x109, -1210, 0, 8970, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D9")
    SetChrPos(0xEF, 550, 0, 8340, 0)
    SetChrPos(0xF0, -1530, 0, 7100, 0)
    SetChrPos(0xF1, 620, 0, 6370, 0)
    Jump("loc_85E")

    label("loc_7D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81D")
    SetChrPos(0xF0, 550, 0, 8340, 0)
    SetChrPos(0xEF, -1530, 0, 7100, 0)
    SetChrPos(0xF1, 620, 0, 6370, 0)
    Jump("loc_85E")

    label("loc_81D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85E")
    SetChrPos(0xF1, 550, 0, 8340, 0)
    SetChrPos(0xEF, -1530, 0, 7100, 0)
    SetChrPos(0xF0, 620, 0, 6370, 0)

    label("loc_85E")


    def lambda_864():
        OP_8F(0xFE, 0xFFFFFD3A, 0x0, 0x4092, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_864)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EA")

    def lambda_892():
        OP_8F(0xFE, 0x2BC, 0x0, 0x4074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_892)
    Sleep(100)

    def lambda_8B2():
        OP_8F(0xFE, 0xFFFFFB28, 0x0, 0x39F8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_8B2)
    Sleep(100)

    def lambda_8D2():
        OP_8F(0xFE, 0x3CA, 0x0, 0x3AE8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_8D2)
    Jump("loc_9BF")

    label("loc_8EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_956")

    def lambda_8FE():
        OP_8F(0xFE, 0x2BC, 0x0, 0x4074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_8FE)
    Sleep(100)

    def lambda_91E():
        OP_8F(0xFE, 0xFFFFFB28, 0x0, 0x39F8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_91E)
    Sleep(100)

    def lambda_93E():
        OP_8F(0xFE, 0x3CA, 0x0, 0x3AE8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_93E)
    Jump("loc_9BF")

    label("loc_956")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BF")

    def lambda_96A():
        OP_8F(0xFE, 0x2BC, 0x0, 0x4074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_96A)
    Sleep(100)

    def lambda_98A():
        OP_8F(0xFE, 0xFFFFFB28, 0x0, 0x39F8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_98A)
    Sleep(100)

    def lambda_9AA():
        OP_8F(0xFE, 0x3CA, 0x0, 0x3AE8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_9AA)

    label("loc_9BF")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(500)

    ChrTalk(    #5
        0x10,
        (
            "#720FCongratulations on your victory outside.\x02\x03",

            "And now that you have done so, I will be\x01",
            "serving as your next opponent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        (
            "#1063F#6PI'm assuming you're a copy of the real Phillip,\x01",
            "too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "#722FIndeed, I am.\x02\x03",

            "And because of that, I've no choice but to point\x01",
            "my blade at even you, Your Highness, knowing\x01",
            "full well how unforgivable that act is.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)

    def lambda_B46():
        OP_6D(1500, 500, 22210, 300)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_B46)

    def lambda_B5E():
        OP_67(0, 5890, -10000, 300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_B5E)

    def lambda_B76():
        OP_6B(2200, 300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_B76)

    def lambda_B86():
        OP_6E(395, 300)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_B86)
    WaitChrThread(0xEE, 0x0)
    OP_22(0x1F5, 0x0, 0x64)
    OP_99(0x10, 0x1, 0x7, 0x4B0)
    OP_22(0x1F8, 0x0, 0x64)
    OP_99(0x10, 0x7, 0x8, 0x4B0)
    Sleep(500)
    Fade(500)
    OP_6D(0, 1800, 22110, 0)
    OP_67(0, 2160, -10000, 0)
    OP_6B(6150, 0)
    OP_6C(0, 0)
    OP_6E(158, 0)
    ClearChrFlags(0x10, 0x2)
    ClearChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x109, -630, 0, 17050, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C61")
    SetChrPos(0x105, 650, 0, 16900, 0)
    SetChrPos(0xF0, -1230, 0, 14540, 0)
    SetChrPos(0xF1, 1270, 0, 14310, 0)
    Jump("loc_CE6")

    label("loc_C61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA5")
    SetChrPos(0x105, 650, 0, 16900, 0)
    SetChrPos(0xEF, -1230, 0, 14540, 0)
    SetChrPos(0xF1, 1270, 0, 14310, 0)
    Jump("loc_CE6")

    label("loc_CA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE6")
    SetChrPos(0x105, 650, 0, 16900, 0)
    SetChrPos(0xEF, -1230, 0, 14540, 0)
    SetChrPos(0xF0, 1270, 0, 14310, 0)

    label("loc_CE6")

    OP_0D()
    OP_1D(0x99)
    Sleep(500)

    ChrTalk(    #8
        0x10,
        (
            "#721F#5PAs the first guardian...\x02\x03",

            "...I, Phillip Runall, the Sword Fox and former\x01",
            "captain of the Royal Guard, challenge you to\x01",
            "battle!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEE, 6)
    SetChrSubChip(0xEE, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 8)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 10)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 12)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF4")

    ChrTalk(    #9
        0x107,
        "#065F#5PO-Oh, no!\x02",
    )

    CloseMessageWindow()

    label("loc_DF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E5A")

    ChrTalk(    #10
        0x10B,
        (
            "#216F#5PI don't think I've met someone so polite who\x01",
            "was so intimidating before...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EA2")

    ChrTalk(    #11
        0x10A,
        "#1317F#5PI can't see a single opening in his stance!\x02",
    )

    CloseMessageWindow()

    label("loc_EA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1067")

    ChrTalk(    #12
        0x101,
        (
            "#1002F#5PI-I never thought I'd see the day we'd have\x01",
            "to fight against Phillip...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#722F#5PI prayed this day would never come... After all \x01",
            "you've done for Duke Dunan, it brings me great\x01",
            "pain to be forced into this position.\x02\x03",

            "#721FStill, this is apparently how fate would have it...\x01",
            "I beg that you don't hold back on my account.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1006F#5PWouldn't dream of it!\x02\x03",

            "If it's something we gotta do anyway,\x01",
            "then I'm gonna go all out!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1067")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1190")

    ChrTalk(    #15
        0x10E,
        (
            "#178F#5PI wasn't expecting to ever have to put my skills to\x01",
            "the test against the famed Demon Commander...\x02\x03",

            "#177F...but now that I have this chance, I gladly won't\x01",
            "hold back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "#720FHaha... I cast off that name long ago.\x02\x03",

            "Still, I hope to give you a fight worthy\x01",
            "of the name.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1190")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12CA")

    ChrTalk(    #17
        0x102,
        (
            "#1505F#5PWell, you WERE able to hold your own against\x01",
            "four Enforcers at once, so your skill must be\x01",
            "something worth boasting...\x02\x03",

            "#1502F...and that's why I won't be holding back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "#720FHaha... I think you overestimate my abilities.\x02\x03",

            "Still, I'll do what I can do be a worthy opponent\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1428")

    ChrTalk(    #19
        0x10C,
        (
            "#115F#5PI was aware of your history from my time leading\x01",
            "the Intelligence Division...\x02\x03",

            "#118F...but it's clear that you're every bit the fearsome\x01",
            "opponent your file suggested from your stance\x01",
            "alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        (
            "#720FI could say the same to you.\x02\x03",

            "I look forward to witnessing the skills you have\x01",
            "inherited from the Divine Blade first hand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1428")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E3")

    ChrTalk(    #21
        0x110,
        (
            "#1306F#5PHeehee. It's been quite a while since we last\x01",
            "saw each other, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        "#721FSo it has... I remember you well, fair lady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x110,
        (
            "#1305F#5POh, I bet you do. The way you fought was\x01",
            "veeery impressive.\x02\x03",

            "#266FBut you spent all your time fighting Walter\x01",
            "and Bleublanc! You didn't spare any playtime\x01",
            "for me at all.\x02\x03",

            "#1306FI hope you're going to make up for that this\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        "#722FI can only hope that I don't disappoint.\x02",
    )

    CloseMessageWindow()

    label("loc_15E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1631")

    ChrTalk(    #25
        0x10F,
        "#1446F#5PAnd yet again, we have no choice but to fight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17AB")

    label("loc_1631")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_167E")

    ChrTalk(    #26
        0x108,
        "#074F#5PAnd yet again, we have no choice but to fight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17AB")

    label("loc_167E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16F9")

    ChrTalk(    #27
        0x106,
        (
            "#053F#5PSure would be great if we didn't HAVE to fight\x01",
            "every time, but no use bitchin' about it now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17AB")

    label("loc_16F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1754")

    ChrTalk(    #28
        0x103,
        (
            "#1526F#5PLooks like we've got no choice but to fight\x01",
            "this time, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17AB")

    label("loc_1754")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17AB")

    ChrTalk(    #29
        0x10D,
        (
            "#272F#5PLooks like we've got no choice but to fight\x01",
            "this time, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17F6")

    ChrTalk(    #30
        0x104,
        "#1541F#5PAnd yet again, we have no choice but to fight.\x02",
    )

    CloseMessageWindow()

    label("loc_17F6")


    ChrTalk(    #31
        0x105,
        (
            "#1162F#5P...Very well. If this is how it must be, I won't\x01",
            "hesitate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x109,
        "#1069F#5PWe accept your challenge!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_187B():
        OP_6D(0, 250, 22010, 300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_187B)

    def lambda_1893():
        OP_67(0, 3380, -10000, 300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1893)

    def lambda_18AB():
        OP_6B(2700, 300)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_18AB)

    def lambda_18BB():
        OP_6E(280, 300)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_18BB)
    SetChrChipByIndex(0x10, 5)
    SetChrSubChip(0x10, 7)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_18DA():
        OP_96(0xFE, 0x0, 0xFFFFFFCE, 0x4CF4, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_18DA)

    def lambda_18F8():
        OP_91(0xFE, 0x0, 0x0, 0x1F40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_18F8)

    def lambda_1913():
        OP_91(0xFE, 0x0, 0x0, 0x1F40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1913)

    def lambda_192E():
        OP_91(0xFE, 0x0, 0x0, 0x1F40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_192E)

    def lambda_1949():
        OP_91(0xFE, 0x0, 0x0, 0x1F40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1949)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x29F, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_4_30A end

    def Function_5_1980(): pass

    label("Function_5_1980")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x10, 0x0)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 20340, 180)
    SetChrChipByIndex(0x10, 4)
    SetChrSubChip(0x10, 3)
    SetChrFlags(0x10, 0x800)
    OP_43(0x10, 0x3, 0x0, 0x6)
    LoadEffect(0x0, "map\\mp259_02.eff")
    LoadEffect(0x1, "map\\mp256_00.eff")
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x0, 0x0, 0x10, 0, 600, 100, 0, 0, 0, 2200, 2300, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, -830, -50, 17700, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8A")
    SetChrPos(0xEF, 470, 0, 17700, 0)
    SetChrPos(0xF0, -1190, 0, 16200, 0)
    SetChrPos(0xF1, 690, 0, 16200, 0)
    Jump("loc_1B0F")

    label("loc_1A8A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ACE")
    SetChrPos(0xF0, 470, 0, 17980, 0)
    SetChrPos(0xEF, -1190, 0, 16379, 0)
    SetChrPos(0xF1, 690, 0, 16620, 0)
    Jump("loc_1B0F")

    label("loc_1ACE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B0F")
    SetChrPos(0xF1, 470, 0, 17980, 0)
    SetChrPos(0xEF, -1190, 0, 16379, 0)
    SetChrPos(0xF0, 690, 0, 16620, 0)

    label("loc_1B0F")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(2029, -900, 20500, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(45000, 0)
    OP_6E(316, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #33
        0x10,
        (
            "#724F#5PPerhaps this was inevitable... I'm simply not\x01",
            "young enough to pose a challenge to you any\x01",
            "more, I fear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        (
            "#1068F#6PY-You've gotta be kidding me...\x02\x03",

            "I can only hope age is that kind to me...\x01",
            "Your strength is nuts.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CA5")

    ChrTalk(    #35
        0x101,
        "#1007F#6PY-Yeah. That was unbelievable...\x02",
    )

    CloseMessageWindow()

    label("loc_1CA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D5C")

    ChrTalk(    #36
        0x10E,
        (
            "#176F#6PThe fabled rumors about you were in no way\x01",
            "exaggerated.\x02\x03",

            "#175FAs a fellow officer in the Royal Guard, I can't\x01",
            "help but feel quite inadequate in comparison.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DC2")

    ChrTalk(    #37
        0x10C,
        (
            "#111F#6PI fear I might have underestimated you. \x01",
            "You were an exceptional opponent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E29")

    ChrTalk(    #38
        0x102,
        (
            "#1514F#6PIt's no surprise those Enforcers struggled\x01",
            "against you, that's for sure...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E7D")

    ChrTalk(    #39
        0x110,
        (
            "#261F#6PWell! I'd say that qualifies as making up for\x01",
            "last time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E7D")


    ChrTalk(    #40
        0x10,
        "#724F#5PHaha... There's no need to try and flatter me.\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #41
        0x10,
        (
            "#721F#5PRegardless, while I may not have been able to\x01",
            "pose a challenge to you, I am sure the other\x01",
            "guardians will.\x02\x03",

            "Be sure not to let your guard down against them\x01",
            "even for a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x105,
        "#1382F#6PWe'll bear that in mind, Phillip. Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "#724F#5PNow, if you will all excuse me, I think it's time\x01",
            "for me to depart...\x02\x03",

            "Once I disappear, the next path should open.\x02\x03",

            "It is my hope that you will all overcome the\x01",
            "remaining trials and return from this place\x01",
            "safe and well.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_23(0x146)
    OP_22(0x138, 0x0, 0x64)

    def lambda_20B2():
        OP_6B(3000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_20B2)
    PlayEffect(0x1, 0x1, 0x10, -100, -700, 0, 0, 0, 0, 1800, 1800, 1800, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)

    def lambda_210A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_210A)
    Sleep(800)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M4111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1980 end

    def Function_6_2148(): pass

    label("Function_6_2148")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2169")
    Sleep(100)
    Jump("loc_21E4")

    label("loc_2169")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_217E")
    Sleep(200)
    Jump("loc_21E4")

    label("loc_217E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2193")
    Sleep(300)
    Jump("loc_21E4")

    label("loc_2193")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21A8")
    Sleep(400)
    Jump("loc_21E4")

    label("loc_21A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21BD")
    Sleep(500)
    Jump("loc_21E4")

    label("loc_21BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21D2")
    Sleep(600)
    Jump("loc_21E4")

    label("loc_21D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21E4")
    Sleep(700)

    label("loc_21E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2206")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_21E4")

    label("loc_2206")

    Return()

    # Function_6_2148 end

    def Function_7_2207(): pass

    label("Function_7_2207")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -830, -50, 18010, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2268")
    SetChrPos(0xEF, 570, 0, 17980, 0)
    SetChrPos(0xF0, -1190, 0, 16379, 0)
    SetChrPos(0xF1, 690, 0, 16620, 0)
    Jump("loc_22ED")

    label("loc_2268")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22AC")
    SetChrPos(0xF0, 570, 0, 17980, 0)
    SetChrPos(0xEF, -1190, 0, 16379, 0)
    SetChrPos(0xF1, 690, 0, 16620, 0)
    Jump("loc_22ED")

    label("loc_22AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22ED")
    SetChrPos(0xF1, 570, 0, 17980, 0)
    SetChrPos(0xEF, -1190, 0, 16379, 0)
    SetChrPos(0xF0, 690, 0, 16620, 0)

    label("loc_22ED")

    OP_6D(990, -50, 18490, 0)
    OP_67(0, 6450, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(45000, 0)
    OP_6E(303, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #44
        0x109,
        "#1840F#6PHe's one hell of a tough butler.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x105,
        "#1165F#11PIndeed...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23BF")

    def lambda_2395():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2395)
    Sleep(100)

    def lambda_23A8():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_23A8)
    Sleep(100)
    OP_8C(0x109, 90, 400)
    Jump("loc_2438")

    label("loc_23BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23FD")

    def lambda_23D3():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_23D3)
    Sleep(100)

    def lambda_23E6():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_23E6)
    Sleep(100)
    OP_8C(0x109, 90, 400)
    Jump("loc_2438")

    label("loc_23FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2438")

    def lambda_2411():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2411)
    Sleep(100)

    def lambda_2424():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2424)
    Sleep(100)
    OP_8C(0x109, 90, 400)

    label("loc_2438")

    Sleep(500)

    ChrTalk(    #46
        0x105,
        (
            "#1160F#5PIs everyone ready to move on to the next area?\x02\x03",

            "I'm guessing we'll be able to access that from\x01",
            "the scenic route like we did this one. Let's go\x01",
            "see which of the other monuments has activated.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2537")

    ChrTalk(    #47
        0x10F,
        "#1448FAll right, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2743")

    label("loc_2537")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_255B")

    ChrTalk(    #48
        0x101,
        "#1006FGot it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2743")

    label("loc_255B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_257E")

    ChrTalk(    #49
        0x102,
        "#1500FRight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2743")

    label("loc_257E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25A1")

    ChrTalk(    #50
        0x10B,
        "#210FGot it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2743")

    label("loc_25A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25D5")

    ChrTalk(    #51
        0x110,
        "#260FThat sounds like a plan.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2743")

    label("loc_25D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25F7")

    ChrTalk(    #52
        0x107,
        "#560FRight!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2743")

    label("loc_25F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2619")

    ChrTalk(    #53
        0x10A,
        "#816FRight!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2743")

    label("loc_2619")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_264E")

    ChrTalk(    #54
        0x103,
        "#1536FThat sounds like a plan.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2743")

    label("loc_264E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2671")

    ChrTalk(    #55
        0x106,
        "#051FGot it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2743")

    label("loc_2671")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2693")

    ChrTalk(    #56
        0x108,
        "#070FRight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2743")

    label("loc_2693")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26BA")

    ChrTalk(    #57
        0x10E,
        "#170FUnderstood.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2743")

    label("loc_26BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26EC")

    ChrTalk(    #58
        0x104,
        "#1545FAnd away we go, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2743")

    label("loc_26EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2719")

    ChrTalk(    #59
        0x10D,
        "#277FThat sounds wise.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2743")

    label("loc_2719")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2743")

    ChrTalk(    #60
        0x10C,
        "#111FThat sounds wise.\x02",
    )

    CloseMessageWindow()

    label("loc_2743")

    OP_A2(0x2B08)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2757")
    OP_A2(0x263E)

    label("loc_2757")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2768")
    OP_A2(0x263F)

    label("loc_2768")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2779")
    OP_A2(0x2640)

    label("loc_2779")

    OP_28(0x38, 0x4, 0x4)
    OP_28(0x38, 0x4, 0x8)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_7_2207 end

    SaveToFile()

Try(main)
