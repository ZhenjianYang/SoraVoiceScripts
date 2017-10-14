from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R0302   ._SN',
        MapName             = 'rolent',
        Location            = 'R0302.x',
        MapIndex            = 21,
        MapDefaultBGM       = "ed60022",
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
        'Fog',                                  # 9
        'Rolent',                               # 10
        'Malga Mine',                           # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
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
        'ED6_DT09/CH11050 ._CH',             # 00
        'ED6_DT09/CH11051 ._CH',             # 01
        'ED6_DT09/CH10100 ._CH',             # 02
        'ED6_DT09/CH10101 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT09/CH11050P._CP',             # 00
        'ED6_DT09/CH11051P._CP',             # 01
        'ED6_DT09/CH10100P._CP',             # 02
        'ED6_DT09/CH10101P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x189,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -146110,
        Z                   = 10,
        Y                   = -9950,
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
        X                   = -163040,
        Z                   = 3920,
        Y                   = 102800,
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


    DeclMonster(
        X                   = -156000,
        Z                   = 2000,
        Y                   = 18000,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -146000,
        Z                   = 2100,
        Y                   = 27000,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x68,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -130000,
        Z                   = 4100,
        Y                   = 26000,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x64,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -117000,
        Z                   = 4100,
        Y                   = 31000,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x67,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -154000,
        Z                   = 2000,
        Y                   = 47000,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x69,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -156000,
        Z                   = 4000,
        Y                   = 68000,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x65,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -109910,
        TriggerZ            = 5850,
        TriggerY            = 62020,
        TriggerRange        = 1000,
        ActorX              = -109910,
        ActorZ              = 7350,
        ActorY              = 62020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1F6",          # 00, 0
        "Function_1_227",          # 01, 1
        "Function_2_30B",          # 02, 2
        "Function_3_3A1",          # 03, 3
        "Function_4_4E7",          # 04, 4
        "Function_5_C45",          # 05, 5
        "Function_6_1150",         # 06, 6
        "Function_7_173C",         # 07, 7
        "Function_8_17D7",         # 08, 8
    )


    def Function_0_1F6(): pass

    label("Function_0_1F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_226")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_210")
    Event(0, 6)
    Jump("loc_226")

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_222")
    Event(0, 5)
    Jump("loc_226")

    label("loc_222")

    Event(0, 4)

    label("loc_226")

    Return()

    # Function_0_1F6 end

    def Function_1_227(): pass

    label("Function_1_227")

    OP_16(0x2, 0xFA0, 0xFFFBF0F0, 0xFFFEB010, 0x230010)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x326, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B")
    OP_6F(0x0, 0)
    Jump("loc_252")

    label("loc_24B")

    OP_6F(0x0, 60)

    label("loc_252")

    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_289")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    OP_C4(0x0, 0x4)
    Jump("loc_30A")

    label("loc_289")

    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_30A")

    Return()

    # Function_1_227 end

    def Function_2_30B(): pass

    label("Function_2_30B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A0")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x37), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_33E")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_353")

    label("loc_33E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x37), scpexpr(EXPR_PUSH_LONG, 0x7D00), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_353")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x7D00), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_353")

    OP_4F(0x38, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_IMUL), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x38), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_383")
    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_398")

    label("loc_383")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x38), scpexpr(EXPR_PUSH_LONG, 0x222E0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_398")
    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x222E0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_398")

    Sleep(10)
    Jump("Function_2_30B")

    label("loc_3A0")

    Return()

    # Function_2_30B end

    def Function_3_3A1(): pass

    label("Function_3_3A1")

    OP_EA(0x2, 0xC9, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x326, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_479")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_412")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1932)
    Jump("loc_476")

    label("loc_412")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_476")

    Jump("loc_4D9")

    label("loc_479")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05I hate to tell you this, but you've already cleaned\x01",
            "this one out.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4D9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3A1 end

    def Function_4_4E7(): pass

    label("Function_4_4E7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_511")
    Call(0, 7)
    FadeToBright(0, 0)
    Call(0, 8)

    label("loc_511")

    OP_6D(-145490, -10, 2670, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(134000, 0)
    OP_6E(243, 0)
    SetChrPos(0x101, -145500, -10, -3730, 0)
    SetChrPos(0x103, -146500, -10, -3730, 0)
    SetChrPos(0xF8, -145250, -10, -4730, 0)
    SetChrPos(0xF9, -146750, -10, -4730, 0)

    def lambda_598():
        OP_90(0xFE, 0x0, 0x0, 0x1B58, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_598)
    Sleep(100)

    def lambda_5B8():
        OP_90(0xFE, 0x0, 0x0, 0x1B58, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B8)
    Sleep(200)

    def lambda_5D8():
        OP_90(0xFE, 0x0, 0x0, 0x1B58, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5D8)
    Sleep(100)

    def lambda_5F8():
        OP_90(0xFE, 0x0, 0x0, 0x1B58, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5F8)
    FadeToBright(1000, 0)
    WaitChrThread(0xF9, 0x1)
    OP_0D()

    ChrTalk(    #3
        0x101,
        "#1004F#6PHey!\x02",
    )

    CloseMessageWindow()

    def lambda_635():
        OP_8E(0xFE, 0xFFFDC7A4, 0x3C, 0x204E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_635)
    Sleep(100)

    def lambda_655():
        OP_8E(0xFE, 0xFFFDC2EA, 0x1E, 0x1FFD, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_655)
    Sleep(200)

    def lambda_675():
        OP_8E(0xFE, 0xFFFDC86C, 0x3C, 0x1AA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_675)
    Sleep(100)

    def lambda_695():
        OP_8E(0xFE, 0xFFFDC2D6, 0x1E, 0x19FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_695)

    def lambda_6B0():
        OP_6D(-145700, 60, 7100, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6B0)

    def lambda_6C8():
        OP_6B(3540, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6C8)
    OP_8C(0x101, 45, 400)
    Sleep(50)
    OP_8C(0x103, 0, 400)
    Sleep(30)
    OP_8C(0xF8, 0, 400)
    Sleep(50)
    OP_8C(0xF9, 320, 400)
    Sleep(300)
    OP_8C(0x101, 0, 400)
    Sleep(50)
    OP_8C(0x103, 45, 400)
    Sleep(30)
    OP_8C(0xF8, 320, 400)
    Sleep(50)
    OP_8C(0xF9, 0, 400)
    Sleep(300)
    OP_8C(0x101, 320, 400)
    Sleep(50)
    OP_8C(0x103, 320, 400)
    Sleep(30)
    OP_8C(0xF8, 0, 400)
    Sleep(50)
    OP_8C(0xF9, 45, 400)
    Sleep(300)
    OP_8C(0x101, 0, 400)
    Sleep(50)
    OP_8C(0x103, 45, 400)
    Sleep(30)
    OP_8C(0xF8, 45, 400)
    Sleep(50)
    OP_8C(0xF9, 320, 400)
    Sleep(300)
    OP_8C(0x101, 180, 400)
    Sleep(50)
    OP_8C(0x103, 180, 400)
    Sleep(30)
    OP_8C(0xF8, 0, 400)
    Sleep(50)
    OP_8C(0xF9, 0, 400)
    Sleep(300)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_802")

    ChrTalk(    #4
        0x107,
        "#560FWow! It's all bright again!\x02",
    )

    CloseMessageWindow()
    Jump("loc_904")

    label("loc_802")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_840")

    ChrTalk(    #5
        0x106,
        "#051FHuh. Well, that's a lot less foggy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_904")

    label("loc_840")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_887")

    ChrTalk(    #6
        0x104,
        (
            "#030FHm. The sun now shows her\x01",
            "lovely face to us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_904")

    label("loc_887")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CF")

    ChrTalk(    #7
        0x105,
        (
            "#048FHow wonderful.\x01",
            "The fog seems to have cleared.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_904")

    label("loc_8CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_904")

    ChrTalk(    #8
        0x108,
        "#070FHey, it's a lot brighter now.\x02",
    )

    CloseMessageWindow()

    label("loc_904")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_964")

    ChrTalk(    #9
        0x107,
        (
            "#061FI guess this is as far as the fog goes?\x01",
            "It kinda just...ends, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADA")

    label("loc_964")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CC")

    ChrTalk(    #10
        0x106,
        (
            "#051FLooks like this is as far as it goes.\x01",
            "Sorta a quick end to the fog, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADA")

    label("loc_9CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A14")

    ChrTalk(    #11
        0x104,
        (
            "#030FIt seems the fog ends here...\x01",
            "quite abruptly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADA")

    label("loc_A14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A74")

    ChrTalk(    #12
        0x105,
        (
            "#048FThis seems to be as far as the fog goes.\x01",
            "It does end quickly, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADA")

    label("loc_A74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADA")

    ChrTalk(    #13
        0x108,
        (
            "#070FGuess this is as far as the fog cover goes.\x01",
            "Kind of a sharp end to it, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADA")


    ChrTalk(    #14
        0x103,
        (
            "#5P#026FSo along the Malga Trail, the fog goes all the\x01",
            "way to 140 selge out from the city... Hmm.\x02\x03",

            "#022FNot only does the fog extend halfway up the\x01",
            "blasted mountain, but there are monsters\x01",
            "everywhere. This is bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1015F#6PYeah, I don't ever remember it being\x01",
            "this bad.\x02\x03",

            "Let's hurry and check the other roads\x01",
            "so we can report to Aina.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1810)
    OP_28(0x8F, 0x2, 0x40)
    OP_28(0x8F, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_4_4E7 end

    def Function_5_C45(): pass

    label("Function_5_C45")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C6F")
    Call(0, 7)
    FadeToBright(0, 0)
    Call(0, 8)

    label("loc_C6F")

    OP_6D(-145490, -10, 2670, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(134000, 0)
    OP_6E(243, 0)
    SetChrPos(0x101, -145500, -10, -730, 0)
    SetChrPos(0x103, -146500, -10, -730, 0)
    SetChrPos(0xF8, -145250, -10, -1730, 0)
    SetChrPos(0xF9, -146750, -10, -1730, 0)

    def lambda_CF6():
        OP_8E(0xFE, 0xFFFDC7A4, 0x3C, 0x204E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CF6)
    Sleep(100)

    def lambda_D16():
        OP_8E(0xFE, 0xFFFDC2EA, 0x1E, 0x1FFD, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D16)
    Sleep(200)

    def lambda_D36():
        OP_8E(0xFE, 0xFFFDC86C, 0x3C, 0x1AA4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_D36)
    Sleep(100)

    def lambda_D56():
        OP_8E(0xFE, 0xFFFDC2D6, 0x1E, 0x19FA, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_D56)

    def lambda_D71():
        OP_6D(-145700, 60, 7100, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D71)

    def lambda_D89():
        OP_6B(3540, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D89)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0xF9, 0x1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDC")

    ChrTalk(    #16
        0x107,
        "#061FYay, the fog's cleared! ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_EAE")

    label("loc_DDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E0F")

    ChrTalk(    #17
        0x106,
        "#051FAnd we're outta the fog.\x02",
    )

    CloseMessageWindow()
    Jump("loc_EAE")

    label("loc_E0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E4A")

    ChrTalk(    #18
        0x104,
        "#030FAh, the fog ends here, it seems.\x02",
    )

    CloseMessageWindow()
    Jump("loc_EAE")

    label("loc_E4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E79")

    ChrTalk(    #19
        0x105,
        "#048FThe fog has cleared.\x02",
    )

    CloseMessageWindow()
    Jump("loc_EAE")

    label("loc_E79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EAE")

    ChrTalk(    #20
        0x108,
        "#070FLooks like the fog's cleared.\x02",
    )

    CloseMessageWindow()

    label("loc_EAE")


    ChrTalk(    #21
        0x103,
        (
            "#5P#026FSo along the Malga Trail, the fog goes all the\x01",
            "way to 140 selge out from the city... Hmm.\x02\x03",

            "#022FNot only does the fog extend halfway up the\x01",
            "blasted mountain, but there are monsters\x01",
            "everywhere. This is bad.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_103A")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as investigated Milch Main Road\x01",      # 0
            "Set as investigated Elize Highway\x01",        # 1
            "No change\x01",                                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1028"),
        (1, "loc_1031"),
        (SWITCH_DEFAULT, "loc_103A"),
    )


    label("loc_1028")

    OP_A3(0x180E)
    OP_A2(0x180F)
    Jump("loc_103A")

    label("loc_1031")

    OP_A2(0x180E)
    OP_A3(0x180F)
    Jump("loc_103A")

    label("loc_103A")

    TurnDirection(0x101, 0x103, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_END)), "loc_10C3")

    ChrTalk(    #22
        0x101,
        (
            "#1006F#6PYeah, let's make sure to let Aina\x01",
            "know how bad it is.\x02\x03",

            "All that's left now is to check the Elize\x01",
            "Highway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_113E")

    label("loc_10C3")


    ChrTalk(    #23
        0x101,
        (
            "#1006F#6PYeah, let's make sure and let Aina know\x01",
            "how bad it is.\x02\x03",

            "All that's left now is to check the Milch\x01",
            "Main Road!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_113E")

    OP_A2(0x1810)
    OP_28(0x8F, 0x2, 0x40)
    OP_28(0x8F, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_5_C45 end

    def Function_6_1150(): pass

    label("Function_6_1150")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_117A")
    Call(0, 7)
    FadeToBright(0, 0)
    Call(0, 8)

    label("loc_117A")

    OP_6D(-145490, -10, 2670, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(134000, 0)
    OP_6E(243, 0)
    SetChrPos(0x101, -145500, -10, -730, 0)
    SetChrPos(0x103, -146500, -10, -730, 0)
    SetChrPos(0xF8, -145250, -10, -1730, 0)
    SetChrPos(0xF9, -146750, -10, -1730, 0)

    def lambda_1201():
        OP_8E(0xFE, 0xFFFDC7A4, 0x3C, 0x204E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1201)
    Sleep(100)

    def lambda_1221():
        OP_8E(0xFE, 0xFFFDC2EA, 0x1E, 0x1FFD, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1221)
    Sleep(200)

    def lambda_1241():
        OP_8E(0xFE, 0xFFFDC86C, 0x3C, 0x1AA4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1241)
    Sleep(100)

    def lambda_1261():
        OP_8E(0xFE, 0xFFFDC2D6, 0x1E, 0x19FA, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1261)

    def lambda_127C():
        OP_6D(-145700, 60, 7100, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_127C)

    def lambda_1294():
        OP_6B(3540, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1294)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0xF9, 0x1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E7")

    ChrTalk(    #24
        0x107,
        "#061FYay, the fog's cleared! ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_13B9")

    label("loc_12E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131A")

    ChrTalk(    #25
        0x106,
        "#051FAnd we're outta the fog.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13B9")

    label("loc_131A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1355")

    ChrTalk(    #26
        0x104,
        "#030FAh, the fog ends here, it seems.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13B9")

    label("loc_1355")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1384")

    ChrTalk(    #27
        0x105,
        "#048FThe fog has cleared.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13B9")

    label("loc_1384")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B9")

    ChrTalk(    #28
        0x108,
        "#070FLooks like the fog's cleared.\x02",
    )

    CloseMessageWindow()

    label("loc_13B9")


    ChrTalk(    #29
        0x103,
        (
            "#5P#026FSo along the Malga Trail, the fog goes all the\x01",
            "way to 140 selge out from the city... Hmm.\x02\x03",

            "#022FNot only does the fog extend halfway up the\x01",
            "blasted mountain, but there are monsters\x01",
            "everywhere. This is bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1015F#6PYeah, I don't ever remember it being\x01",
            "this bad.\x02\x03",

            "Anyway, we've checked all three roads,\x01",
            "so...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #31
        0x101,
        (
            "#1006F#6PTime to head back and report\x01",
            "to Aina, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E6")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as haven't visited Bright house\x01",      # 0
            "Set as visited Bright house\x01",              # 1
            "No change\x01",                                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_15DA"),
        (1, "loc_15E0"),
        (SWITCH_DEFAULT, "loc_15E6"),
    )


    label("loc_15DA")

    OP_A3(0x180D)
    Jump("loc_15E6")

    label("loc_15E0")

    OP_A2(0x180D)
    Jump("loc_15E6")

    label("loc_15E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16BF")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #32
        0x103,
        (
            "#2P#023FWell, we can, but didn't you want to go\x01",
            "home for a little while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1004F#6POh, yeah! I almost forgot.\x02\x03",

            "#1008FLet's stop by on our way back\x01",
            "to the guildhouse.\x02",
        )
    )

    OP_28(0x8F, 0x2, 0x40)
    OP_28(0x8F, 0x1, 0x80)
    OP_28(0x8F, 0x1, 0x800)
    OP_28(0x8F, 0x1, 0x1000)
    CloseMessageWindow()
    Jump("loc_1736")

    label("loc_16BF")

    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #34
        0x103,
        (
            "#2P#021FUnless you can think of any other\x01",
            "pressing business, I'd say that's\x01",
            "right.\x02",
        )
    )

    OP_28(0x8F, 0x2, 0x40)
    OP_28(0x8F, 0x1, 0x80)
    OP_28(0x8F, 0x1, 0x200)
    OP_28(0x8F, 0x1, 0x400)
    CloseMessageWindow()

    label("loc_1736")

    OP_A2(0x1810)
    EventEnd(0x0)
    Return()

    # Function_6_1150 end

    def Function_7_173C(): pass

    label("Function_7_173C")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_17B8"),
        (1, "loc_17BE"),
        (SWITCH_DEFAULT, "loc_17C4"),
    )


    label("loc_17B8")

    OP_A2(0x1200)
    Jump("loc_17C4")

    label("loc_17BE")

    OP_A2(0x1201)
    Jump("loc_17C4")

    label("loc_17C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_17D2")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_17D6")

    label("loc_17D2")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_17D6")

    Return()

    # Function_7_173C end

    def Function_8_17D7(): pass

    label("Function_8_17D7")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_8_17D7 end

    SaveToFile()

Try(main)
