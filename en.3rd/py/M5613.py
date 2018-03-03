from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5613   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5613.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60233",
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
        '',                                     # 9
        '',                                     # 10
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
        'ED6_DT29/CH14950 ._CH',             # 00
        'ED6_DT29/CH14951 ._CH',             # 01
        'ED6_DT29/CH14960 ._CH',             # 02
        'ED6_DT29/CH14961 ._CH',             # 03
        'ED6_DT29/CH15160 ._CH',             # 04
        'ED6_DT29/CH15161 ._CH',             # 05
        'ED6_DT29/CH15170 ._CH',             # 06
        'ED6_DT29/CH15171 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT29/CH14950P._CP',             # 00
        'ED6_DT29/CH14951P._CP',             # 01
        'ED6_DT29/CH14960P._CP',             # 02
        'ED6_DT29/CH14961P._CP',             # 03
        'ED6_DT29/CH15160P._CP',             # 04
        'ED6_DT29/CH15161P._CP',             # 05
        'ED6_DT29/CH15170P._CP',             # 06
        'ED6_DT29/CH15171P._CP',             # 07
    )

    DeclMonster(
        X                   = -68620,
        Z                   = 0,
        Y                   = 59500,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x281,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -40790,
        Z                   = 0,
        Y                   = 29390,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x281,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -19050,
        Y                   = 0,
        Z                   = 144000,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = 28990,
        TriggerZ            = 0,
        TriggerY            = 6920,
        TriggerRange        = 1000,
        ActorX              = 28990,
        ActorZ              = 2000,
        ActorY              = 6920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_166",          # 00, 0
        "Function_1_17F",          # 01, 1
        "Function_2_191",          # 02, 2
        "Function_3_4FB",          # 03, 3
        "Function_4_77D",          # 04, 4
    )


    def Function_0_166(): pass

    label("Function_0_166")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E")
    Event(0, 2)

    label("loc_17E")

    Return()

    # Function_0_166 end

    def Function_1_17F(): pass

    label("Function_1_17F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_190")

    Return()

    # Function_1_17F end

    def Function_2_191(): pass

    label("Function_2_191")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x7D0)
    SetChrPos(0x109, 28150, 0, 57470, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F7")
    SetChrPos(0xEF, 29500, 0, 57330, 0)
    SetChrPos(0xF0, 27750, 0, 55850, 0)
    SetChrPos(0xF1, 29640, 0, 55840, 0)
    Jump("loc_27C")

    label("loc_1F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23B")
    SetChrPos(0xF0, 29500, 0, 57330, 0)
    SetChrPos(0xEF, 27750, 0, 55850, 0)
    SetChrPos(0xF1, 29640, 0, 55840, 0)
    Jump("loc_27C")

    label("loc_23B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27C")
    SetChrPos(0xF1, 29500, 0, 57330, 0)
    SetChrPos(0xEF, 27750, 0, 55850, 0)
    SetChrPos(0xF0, 29640, 0, 55840, 0)

    label("loc_27C")

    OP_6D(29690, 0, 57470, 0)
    OP_67(0, 7080, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x109,
        "#1079F#6P...Huh?\x02",
    )

    CloseMessageWindow()

    def lambda_2E4():
        OP_6D(29240, 500, 86160, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2E4)

    def lambda_2FC():
        OP_67(0, 7940, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2FC)

    def lambda_314():
        OP_6B(2600, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_314)

    def lambda_324():
        OP_6C(45000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_324)

    def lambda_334():
        OP_6E(276, 3500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_334)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    ChrTalk(    #1
        0x109,
        (
            "#1063F#1PThat's strange...\x02\x03",

            "I was figuring the next battle would be in this\x01",
            "room, but there's no one here.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(29690, 0, 57470, 0)
    OP_67(0, 7080, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x10A, 270, 400)
    Sleep(300)

    ChrTalk(    #2
        0x10A,
        (
            "#1317F#11PW-Weird...\x02\x03",

            "This is the top floor, though, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #3
        0x109,
        (
            "#1065F#6PNot technically. There's an area for landing\x01",
            "airships on the rooftop.\x02\x03",

            "#1063FWe'd probably better check there, too,\x01",
            "just in case.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B14)
    OP_1D(0xE9)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_191 end

    def Function_3_4FB(): pass

    label("Function_3_4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CA")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(6144)
    Sleep(500)
    Jump("loc_5CD")

    label("loc_5CA")

    TalkBegin(0xFF)

    label("loc_5CD")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #4
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_609")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74C")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_665"),
        (1, "loc_6E0"),
        (2, "loc_70E"),
        (SWITCH_DEFAULT, "loc_73C"),
    )


    label("loc_665")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xE9)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_749")

    label("loc_6E0")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #5
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_749")

    label("loc_70E")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #6
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_749")

    label("loc_73C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_749")

    label("loc_749")

    Jump("loc_609")

    label("loc_74C")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_779")
    OP_A2(0x259B)
    EventEnd(0x1)
    Jump("loc_77C")

    label("loc_779")

    TalkEnd(0xFF)

    label("loc_77C")

    Return()

    # Function_3_4FB end

    def Function_4_77D(): pass

    label("Function_4_77D")

    OP_A3(0x2B64)
    OP_A3(0x2B65)
    OP_A3(0x2B66)
    OP_A3(0x2B67)
    OP_A3(0x2B68)
    OP_A2(0x2B69)
    Return()

    # Function_4_77D end

    SaveToFile()

Try(main)
